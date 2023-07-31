# This is file 40.py

a = print("Enter IP for bastion")

match a:
    case 10.100:
        print('bastion is 134.224.190.28')
        print('sft ssh a --via 134.224.190.28')
