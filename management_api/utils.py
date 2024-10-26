import json
from rest_framework.views import exception_handler

def custom_exception_handler(exc, context):
    """ Handles serializer errors and returns as json preetify format

    Args:
        exc (_type_): _description_
        context (_type_): _description_

    Returns:
        _type_: application/json
    """
    response = exception_handler(exc, context)
    
    # If there is an error response
    if response is not None and response.data:
        # Pretty-print the errors
        response.data = {"errors": response.data}
    return response
