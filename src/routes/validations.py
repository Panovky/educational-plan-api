from fastapi import APIRouter, status
from fastapi.responses import Response
from typing import Any, List, Dict
from pydantic import BaseModel
from enum import Enum

router = APIRouter(
    prefix='/validations',
    tags=['validations']
)


class Discipline(BaseModel):
    id: int
    name: str
    credits: int
    examType: str
    hasCourseWork: bool
    hasPracticalWork: bool
    department: str
    competenceCodes: List[str]
    lectureHours: int
    labHours: int
    practicalHours: int
    sourcePosition: dict | None = None

class Row(BaseModel):
    name: str
    color: str
    data: List[List[Discipline]]

class ValidationSeverity(str, Enum):
    BLOCKING = "blocking"
    WARNING = "warning"

class ValidationResult(BaseModel):
    message: str
    severity: ValidationSeverity
    details: Dict[str, Any] = {}

class ValidationResponse(BaseModel):
    isValid: bool
    results: List[ValidationResult]



def calculate_hours(discipline: Discipline) -> Dict[str, float]:
    total_hours = discipline.credits * 36
    exam_hours = 9 if discipline.examType == "exam" else 0
    individual_hours = sum([
        2 if discipline.examType == "credit" else 0,
        2 if discipline.examType == "diff_credit" else 0,
        2 if discipline.hasCourseWork else 0,
        1 if discipline.hasPracticalWork else 0
    ])
    
    classroom_hours = discipline.lectureHours + discipline.labHours + discipline.practicalHours
    exam_prep_hours = 27 if discipline.examType == "exam" else 0
    contact_hours = individual_hours + exam_hours + classroom_hours
    
    independent_work = total_hours - contact_hours - exam_prep_hours
    
    return {
        "total": total_hours,
        "contact": contact_hours,
        "classroom": classroom_hours,
        "independent": independent_work,
        "exam_prep": exam_prep_hours
    }

@router.post('/validate-up', response_model=ValidationResponse)
def validate_up(request: List[Row]) -> ValidationResponse:
    validation_results = []
    
    # Получаем количество семестров из первой строки
    semesters_count = len(request[0].data)
    
    # Проверяем зачетные единицы по семестрам и курсовые работы
    total_credits = 0
    for semester_idx in range(semesters_count):
        semester_credits = sum(
            row.data[semester_idx][i].credits 
            for row in request 
            for i in range(len(row.data[semester_idx]))
        )
        total_credits += semester_credits
        
        if not 24 <= semester_credits <= 36:
            validation_results.append(ValidationResult(
                message=f"В семестре {semester_idx + 1} количество з.е.: {semester_credits} (должно быть 30 ± 6)",
                severity=ValidationSeverity.BLOCKING
            ))
            
        # Подсчет курсовых работ в семестре
        course_works_count = sum(
            1 
            for row in request 
            for discipline in row.data[semester_idx] 
            if discipline.hasCourseWork
        )
        
        if course_works_count > 2:
            validation_results.append(ValidationResult(
                message=f"В семестре {semester_idx + 1} количество курсовых работ: {course_works_count} (должно быть не больше 2)",
                severity=ValidationSeverity.WARNING
            ))
    
    # Проверяем общее количество зачетных единиц
    expected_credits = 240 if semesters_count == 8 else 120
    if total_credits != expected_credits:
        validation_results.append(ValidationResult(
            message=f"Общее количество з.е.: {total_credits} (должно быть {expected_credits})",
            severity=ValidationSeverity.BLOCKING
        ))

    return ValidationResponse(
        isValid=not any(r.severity == ValidationSeverity.BLOCKING for r in validation_results),
        results=validation_results,
    )
