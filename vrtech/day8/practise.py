devopsToolsDetails={
    "docker": '27.5.1',
    "k8s": "1.32" 
}

keylist = list(devopsToolsDetails.keys())
valuelist = list(devopsToolsDetails.values())         

print(f'Toolname ToolVersion')
print(f'{keylist[0]}    {valuelist[0]}')
print(f'{keylist[1]}    {valuelist[1]}')