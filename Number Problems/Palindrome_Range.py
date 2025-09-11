min_ = 100
max_ = 150
arr = []

for num in range(min_, max_+1):
    rev = 0
    dup = num
    while num > 0:         # <-- modifies num
        ld = num % 10
        rev = (rev * 10) + ld
        num //= 10
    if dup == rev:
        arr.append(dup)
print(arr)
