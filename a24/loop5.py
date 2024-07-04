start = 5674
end = 10983

i = start
j = end
total = 0
while i <= j:
    if i % 7 == 0:
        total = total + 1
    i += 1
print(total)
