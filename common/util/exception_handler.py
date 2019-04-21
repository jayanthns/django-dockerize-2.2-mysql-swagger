from rest_framework.views import exception_handler

from common.util.logger import get_custom_logger

log = get_custom_logger()


def custom_exception_handler(exc, context):
    # Call REST framework's default exception handler first,
    # to get the standard error response.
    response = exception_handler(exc, context)

    # Now add the HTTP status code to the response.
    if response is not None:
        response.data['code'] = response.status_code
        response.data['message'] = response.data['detail']
        response.data['success'] = False
        response.data['data'] = None
        response.data.pop('detail', None)
    return response
