from fastapi import HTTPException, status


class DisciplineNotFoundException(HTTPException):
    def __init__(self):
        super().__init__(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='Дисциплина с указанным id не найдена.'
        )


class DisciplineNameIsNotUniqueException(HTTPException):
    def __init__(self):
        super().__init__(
            status_code=status.HTTP_409_CONFLICT,
            detail='Дисциплина с таким наименованием уже существует.'
        )


class DisciplineShortNameIsNotUniqueException(HTTPException):
    def __init__(self):
        super().__init__(
            status_code=status.HTTP_409_CONFLICT,
            detail='Дисциплина с таким кратким наименованием уже существует.'
        )


class ControlTypeNotFoundException(HTTPException):
    def __init__(self):
        super().__init__(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='Вид контроля дисциплин с указанным id не найден.'
        )


class ControlTypeNameIsNotUniqueException(HTTPException):
    def __init__(self):
        super().__init__(
            status_code=status.HTTP_409_CONFLICT,
            detail='Данный вид контроля дисциплин уже существует.'
        )


class DirectionNotFoundException(HTTPException):
    def __init__(self):
        super().__init__(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='Direction not found.'
        )


class DisciplineBlockNotFoundException(HTTPException):
    def __init__(self):
        super().__init__(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='Discipline block not found.'
        )
