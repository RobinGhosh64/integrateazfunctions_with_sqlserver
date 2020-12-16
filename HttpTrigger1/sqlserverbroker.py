import logging
import pyodbc
import collections
import json
import threading
import time
import requests


server = 'your-sql-server.database.windows.net'
database = 'your-sql-db'
username = 'your username'
password = 'your password'
driver= '{ODBC Driver 17 for SQL Server}'

  
#
# Execute a hard coded MSSQL query
#    
def exec_sql(req_body,dothread):

    logging.info('Here in exec_sql')

    sql= req_body[0]['data']['sql'] 

    conn = pyodbc.connect('DRIVER='+driver+';SERVER='+server+';PORT=1433;DATABASE='+database+';UID='+username+';PWD='+ password)
    cursor = conn.cursor()
    cursor.execute(sql)
    rows = cursor.fetchall()
    
    # Convert query to row array and pump out json

    objects_list = []
    for row in rows:
        d = collections.OrderedDict()
        d['id'] = row.PONumber
        d['store_id'] = row.name
        d['merchant_id'] = row.addressLine1
        d['refnum'] = row.addressLine2
        d['trantype'] = row.addressLine3
        objects_list.append(d)

    # the print() and logging.info() statement will not produce any output under the context of a thread run
    if dothread == "Y" :
        time.sleep(1)
        callback_uri= req_body[0]['data']['callback_uri'] 
        if(not callback_uri):
            logging.info("The callback_uri is empty")
        else:
            print("No it is not empty, so send a message back to the caller")
            payload = {"id":"5555","product_id":"string","name": "robin ghosh","description": "desc","purpose": "pur","imagelink": "img"}
            headers = {"authorization": "2213"}
            r = requests.post(callback_uri,data=payload, headers=headers)
            s=r.text
            
    print('Dumping the lists')
    return json.dumps(objects_list)



#
# Wrap the actual atomic code as a callable threa
#
def thread_work(req_body,dothread):
# start threads by passing function to Thread constructor
    t = threading.Thread(target=exec_sql, args=(req_body,dothread)) 
    logging.info("Python HTTP trigger function started a worker thread with name of {}".format(threading.current_thread().name))
    t.start() 
    logging.info("Completed the thread..")
    return "Success"




    
