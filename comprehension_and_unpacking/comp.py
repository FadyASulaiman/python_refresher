nums = [1,2,3,4,5,6,8]
evens = [n for n in nums if n % 2 == 0]
squares = (n*n for n in nums)           # generator, lazy


# ★ Sequence unpacking
a, b, *rest = range(5)          # a=0 b=1 rest=[2,3,4]