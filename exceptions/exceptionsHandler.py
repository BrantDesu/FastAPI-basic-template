from exceptionsResolver import *
def CognitoExceptionsHandler(exception):
    match type(exception):        
        case _:
            return unknown_error_exception(exception)