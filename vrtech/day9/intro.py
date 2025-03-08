import os
import sys
import platform
from packaging.version import Version

# print(sys.version)
# pythonVer = sys.version.split()[0]
# print(pythonVer)

# minReqVersion=Version('3.9.21')
# curPyVersion=Version(pythonVer)

# print(curPyVersion>=minReqVersion)
# print(sys.executable)

# print(pythonVer == '3.13.1')
# print(pythonVer >= '3.9.21')

# rePyVl='3.9.1'.split(".")
# cpyv1=pythonVer.split(".")

# print(rePyVl,cpyv1)


# print(sys.version_info.major)
# sys.exit(-2)
# osType=platform.system()
# cmd=input("Enter your command to execute : ")
# if osType == "Windows":  #if condtion/exrpession -> result of condtion/expression alwasy either True/False
#     # cmd="echo %PATH%"
#     os.system(cmd)
# if osType == "Linux":  #if condtion/exrpession -> result of condtion/expression alwasy either True/False
#     # cmd="echo ${PATH}"
#     print("This is a Linux OS")
#     sys.exit(2)


# print("Script Ends Here")

# my_custom_modules_path=r'D:\VRTechnologies\Online_Classes\Python_Scripting\2025_Jan\Day_8'
# sys.path.append(my_custom_modules_path)
# print(sys.path)
# import defaults
# print(defaults.KUBECONFIG)
#
# print(f"Python Script Name: {sys.argv[0]}")
#
# print(sys.argv, len(sys.argv))
# myList=sys.argv[1:]
# print(f'My Command-line args: {myList}')

# if len(sys.argv) != 3:
#     print(f'Help To Run This script: python {sys.argv[0]} <serviceName> <action>')
#     sys.exit(1)
# serviceName = sys.argv[1]
# actionOnService = sys.argv[2]
# print(f'Service Name: {serviceName} and action on it is: {actionOnService}')
import os

# Corrected path with escaped spaces and quotes
# os.makedirs("/Users/tripurakant/Documents/code/My git/Python-Scripting/vrtech/day10", exist_ok=True)
x = platform.system()
print(x)
