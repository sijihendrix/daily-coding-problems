# Implement division of two positive integers without using the division, multiplication, or moduos operators.
# Return the quotient as an integer, ignoring the remainder.

# find 6 / 2 using subtraction. 
## Manually 6 / 2.  6 -2 -2 -2 =  0. 2 can be subtracted 3 times.
# count amount of times value can be subtracted from the other value wihtout the value being less than 0.
### account for odd values by checking if a -b is less than 0 and a is greater than 0



def divisionOfPosInt(a, b):

    count = 0
    while a > 0:
        a -= b
        count +=1
        if  (a-b < 0 and a > 0):
            count -=1
        
    return count


print(divisionOfPosInt(5455, 3))