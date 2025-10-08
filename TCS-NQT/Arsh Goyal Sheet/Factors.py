# first check the number of divisors upto sqrt(n)
# then in the second loop from sqrt(n) to the 1 if then number divisible divide it by number



n = 100

for i in range(1,int(n**0.5)):
  if n % i == 0:
    print(i, end=" ")
    
for i in range(int(n**0.5),0,-1):
  if n % i == 0:
    print(n//i, end=" ")