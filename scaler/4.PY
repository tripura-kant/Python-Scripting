# a = 5
# if a >= 2:
#     print("TRUE")

# x = 2
# if x==2:
#     x = 3
# x = 4
# else:
#     x = 5
# print(x)
# x = 0
# if x > 2:
#     x = x * 2
# if x > 4:
#     x = 0
# print(x)
def sumRange(a: int, b: int) -> int:
    if a > b:
        # I have not explained this yet, although you can use chatgpt, you will get it
        a, b = b, a  # Ensure a is less than or equal to b

    total = 0
    i = a
    while i <= b:
        total += i
        i += 1
    return total


print(sumRange(1, 10))
