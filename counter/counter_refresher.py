from collections import Counter

c = Counter({'a': 3, 'b': 1})
c.update({'a': 1, 'c': 2})  # Result: Counter({'a': 4, 'b': 1, 'c': 2})
c.update('abc')  # Adds counts from iterable
c.update(a=2, b=3)  # Adds counts from keyword arguments

# Counter's update method can accept various inputs and adds (not replaces) counts
# The key difference from dict.update() is that Counter.update() adds values rather than replacing them.