vals = [1,2,3]
print([y*y for x in vals if (y:=x+1) > 2]) # result: [9, 16]

# The walrus operator := assigns x+1 back to x within each iteration. So:

# x=1: x becomes 2, 2>2 is False, skip
# x=2: x becomes 3, 3>2 is True, include 3*3=9
# x=3: x becomes 4, 4>2 is True, include 4*4=16