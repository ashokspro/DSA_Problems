# we want to find the number of ways to arrange n peoples in a circular way 
# we are using like formulae approach here 
# initially passing the number less than 1 actual number w
def Circular(n):
    result = 1
    while n > 0:
        result *= n
        n -= 1
    return result


n = 4
Circular(n-1)