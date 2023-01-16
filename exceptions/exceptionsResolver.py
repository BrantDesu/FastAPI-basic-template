from fastapi import HTTPException
from os import getenv

ENV = getenv("ENV")
BACKEND_DEVELOPER = getenv("BACKEND_DEVELOPER")
      
def unknown_error_exception(exception):
    return HTTPException(status_code=500, 
                         detail={
                                    "customCode": "Cx",
                                    "message": "Error desconocido o no manejado, avisar al backend developer",
                                    "contact": BACKEND_DEVELOPER,
                                    "aditionalInfo": vars(exception) if ENV == "dev" else  ""
                                })

