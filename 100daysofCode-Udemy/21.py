# Write a function that checks whether a number is in a given range (inclusive of high and low)


def ran_check(num,low,high):
    return num in range(low, high+1)

print(ran_check(5,2,4))