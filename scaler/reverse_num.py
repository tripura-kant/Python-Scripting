A = 123

rev = 0
copy = A

while (A != 0):
    dig = A % 10
    A = A // 10
    rev = (rev * 10) + dig
    print(f"Digit: {dig}")
    print(f"Updated A: {A}")
    print(f"Reversed number so far: {rev}")
    print(f"Original number: {copy}")

print(f"Final reversed number: {rev}")
