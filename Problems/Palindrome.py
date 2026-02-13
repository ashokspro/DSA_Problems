num = 13314
rev = 0
dup = num

while num > 0:
  ld = num % 10
  rev = (rev * 10) + ld
  num //= 10

if rev == dup:
  print("True")
else:
  print("False")
