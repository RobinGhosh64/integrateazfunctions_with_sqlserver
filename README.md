# integrateazfunctions_with_sqlserver
Integrate Azure Functions with SQL Server

By default, AZ Functions does not support straight integration with Microsoft SQL Server. As a developer, you can always bring in a module or an an exteranl sdk into the context of the AZ Function. Using this technique, I am providing an option to execute straight SQL's in  Python currently and will later update this project to provide an option using JavaScript as well.

Adding my Postman payload here. Technically the code does not require a payload
[{
    "dothread":"N",
    "data": {
      "validationCode": "512d48b6-c7b8-40c8-89fe-f46f9e9622b6",
      "sql" : "select id,trantype,merchant_id from dbo.Transactions"
    },
    "eventType": "Microsoft.EventGrid.SubscriptionValidationEvent",
    "metadataVersion": "1",
 }]

Also, added screenshots for my response

roghos@microsoft.com   # Robin S Ghosh
Sr Cloud Solution Architect

