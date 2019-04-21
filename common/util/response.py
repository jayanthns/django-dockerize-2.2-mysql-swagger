from rest_framework.response import Response


def return_error_response(msg, code=400):
    return Response(
        {
            "message": msg,
            "code": code,
            "status": code,
            "success": False,
            "data": None
        },
        status=code
    )
