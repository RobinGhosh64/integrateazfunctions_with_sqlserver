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
            result1 = service.thread_work(req_body,dothread)
            if result1 is "Success":
                return func.HttpResponse("Successfully queued our work process",status_code=202)
            else:
                return func.HttpResponse("Bad Request", status_code=400)
           
    else:
        return func.HttpResponse(
             "Please pass an attribute called dothread [Y/N]",status_code=400
        )
