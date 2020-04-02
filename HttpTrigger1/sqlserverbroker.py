import logging
import pyodbc
import collections
import json

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
    #cursor.execute(sql)
    cursor.execute("SELECT id,store_id,merchant_id,trantype,refnum FROM dbo.Transactions")
    rows = cursor.fetchall()
    
    # Convert query to row array and pump out json

    objects_list = []
    for row in rows:
        d = collections.OrderedDict()
        d['id'] = row.id
        d['store_id'] = row.store_id
        d['merchant_id'] = row.merchant_id
        d['refnum'] = row.refnum
        d['trantype'] = row.trantype
        objects_list.append(d)

    return json.dumps(objects_list)



    
