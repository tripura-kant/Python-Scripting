import os
import platform

osType = platform.system()

if osType == "Windows":  # if condtion/exrpession -> result of condtion/expression alwasy either True/False
    cmd = "echo %PATH%"
    os.system(cmd)

if osType == "Linux":  # if condtion/exrpession -> result of condtion/expression alwasy either True/False
    cmd = "echo ${PATH}"
    os.system(cmd)

elif osType == "Linux" or osType == "Darwin":  # 'Darwin' is the name for macOS
    cmd = "echo $PATH"
    os.system(cmd)
