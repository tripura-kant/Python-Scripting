# Recursion is
# Function calling itself unless a specific condition is meet
#
#
#

# def greet():
#     global count
#     print(count)
#     count += 1
#     greet()
#
#
# count = 1
# greet()
# def func(i, n):
#     if i > n:
#         return
#     print("Anirudh")
#     func(i + 1, n)
#
#
# func(1, 4)


def func(i, n):
    if i < 1:
        return
    func(i - 1, n)
    print(i)


func(4, 4)
