import logging

import azure.functions as func
from . import sqlserverbroker as service



def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    req_body = req.get_json()
    dothread = req_body[0]['dothread']

    if dothread:
        if dothread == "N" :
            result = service.exec_sql(req_body,dothread)
            if not result:
                return func.HttpResponse("Bad Request",status_code=400)
            else:
                return func.HttpResponse(result, status_code=200)
    else:
        return func.HttpResponse(
             "Please pass an attribute called dothread [Y/N]",status_code=400
        )
