import sys
a = [x for x in range(1000000)] 
b = (x for x in range(1000000))

print('list comp byte size is ', sys.getsizeof(a))
print('generator expression byte size is ', sys.getsizeof(b))