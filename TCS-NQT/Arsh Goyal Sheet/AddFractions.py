
# multiplying both numerator and denominator separately and adding then multi den 
# finding gcd for the both up and down and dividing both number by hcf(gcd)

from math import gcd
def addFraction(num1, den1, num2, den2):
    up1 = int(num1*den2)
    up2 = int(num2*den1)
    
    up = up1+up2
    
    down = int(den1*den2)
    
    
    hcf = gcd(up,down)
    
    print(f"{int(up/hcf)}/{int(down/hcf)}")



#hard coded hcf finder
"""small = min(up,down)
for i in range(1,small+1):
    if up%i == 0 and down%i == 0:
        hcf = i"""