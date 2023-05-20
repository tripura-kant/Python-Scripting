# SWAP PROGRAM

X = int(input("Enter the value of X: "))
Y = int(input("Enter the value of Y: "))

temp = X

X = Y

Y = temp

print("The value of X after swapping: {}".format(X))
print("The value of Y after swapping: {}".format(Y))