myDevOpsTools={
    "integraionTool": "jenkins",
    "configTool"   : "ansible",
    "dbs" : ["oracledb", "mariadb",]
}

# print(myDevOpsTools["dbs"])
# print(myDevOpsTools.get("dbs","value is not defined"))

# print(list(myDevOpsTools.keys()))
# print(list(myDevOpsTools.values()))
# print(list(myDevOpsTools.items()))

print(myDevOpsTools.get("dbs")[1])

# print("configTool" in myDevOpsTools.keys()) #print("configTool" in myDevOpsTools)
# print("ansible" in myDevOpsTools.values())


# jsonResponse={
#     "tools": [ { "cloud": ["aws", "azure"]}, {"container":['docker',"k8s"]} ],
#     "version": "1.0"
# }

# # toolslist=jsonResponse.get('tools')
# # print(toolslist[0])
# print(jsonResponse['tools'][0].get("cloud")[0])