# Day_5_python List Python

# mycloud1='aws'
# mycloud2='azure'
# mycloud3='google'

# print("I am working with three clouds")
# print("They are: ")

# print(f"1.{mycloud1}")
# print(f"2.{mycloud2}")
# print(f"3.{mycloud3}")

myClouds=['aws', 'azure', 'google', 'ibm']

print(f"I am working with {len(myClouds)} clouds")
cnt=1

for eachcloud in myClouds:
    print(f"{cnt}.{eachcloud}")
    cnt+=1
          