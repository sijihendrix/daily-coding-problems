# Implement division of two positive integers without using the division, multiplication, or moduos operators.
# Return the quotient as an integer, ignoring the remainder.

# find 6 / 2 using subtraction. 
## Manually 6 / 2.  6 -2 -2 -2 =  0. 2 can be subtracted 3 times.
# count amount of times value can be subtracted from another



def divisionOfPosInt(a, b):

    count = 0
    while a > 0:
        a -= b
        if  (a -b ==-1):
            count -=1
        count +=1
    return count


print(divisionOfPosInt(11, 3))