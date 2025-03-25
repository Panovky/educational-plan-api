from fastapi import HTTPException, status


class DisciplineNotFoundException(HTTPException):
    def __init__(self):
        super().__init__(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='Discipline not found.'
        )