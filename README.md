# integrateazfunctions_with_sqlserver
Integrate Azure Functions with SQL Server  RSG

By default, AZ Functions does not support straight integration with Microsoft SQL Server. As a developer, you can always bring in a module or an external sdk into the context of the AZ Function. Using this technique, I am providing an option to execute straight SQL's in  Python currently. I have another project that you can use if you are looking for a solution in NODEjs. 

https://github.com/RobinGhosh64/integrateazfunctions_with_sqlserver_javascript.git

Another implementation for C# will be provided soon.

Cheers!

Adding my Postman payload here for testing. I do have a version of this project that can stack up multiple requests if your queries are long consuming. In that situation you can come back later and query your response using a jobid.

[{
    "dothread":"N",
    "data": {
      "validationCode": "512d48b6-c7b8-40c8-89fe-f46f9e9622b6",
      "sql" : "select id,trantype,merchant_id from dbo.Transactions",
      "callback_uri" : "https://rsg-webapp-tcc3.azurewebsites.net/asset/add"
    },
    "eventType": "Microsoft.EventGrid.SubscriptionValidationEvent",
    "metadataVersion": "1",
 }]

Also, added screenshots for my postman session

robin.ghosh@microsoft.com   # Robin S Ghosh

(Sr Cloud Solution Architect)

