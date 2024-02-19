from datetime import datetime

from rest_framework import status
from rest_framework.exceptions import APIException
from rest_framework.views import exception_handler


class BaseCustomException(APIException):
    detail = None
    status_code = None

    def __init__(self, detail, code):
        super().__init__(detail, code)
        self.detail = detail
        self.status_code = code


class InternalServerError(BaseCustomException):
    def __init__(self, detail):
        super().__init__(detail, status.HTTP_500_INTERNAL_SERVER_ERROR)


class DataNotFound(BaseCustomException):
    def __init__(self, detail):
        super().__init__(detail, status.HTTP_404_NOT_FOUND)


class BadRequest(BaseCustomException):
    def __init__(self, detail):
        super().__init__(detail, status.HTTP_400_BAD_REQUEST)


class Forbidden(BaseCustomException):
    def __init__(self, detail):
        super().__init__(detail, status.HTTP_403_FORBIDDEN)


class AlreadyExists(BaseCustomException):
    def __init__(self, detail):
        super().__init__(detail, status.HTTP_409_CONFLICT)


def custom_exception_handler(exc, context):
    response = exception_handler(exc, context)
    if response is not None:
        detail = response.data.get("detail")
        if detail:
            response.data["message"] = detail
            del response.data["detail"]

        response.data["time"] = datetime.now()
    return response
