import math

print math.factorial(6)

# Lotery - 59 balls, draw 6, order is important

print math.factorial(59) / math.factorial(59 - 6)

num_perm = 1
for idx in range(59, 59 - 6, -1):
    num_perm *= idx
print num_perm


print (10 ** 5)
variants = 100000
variant = (12.0 / 100000.0)
print variant


# m!/(m-n)!n!
print math.factorial(10) / math.factorial(10 - 5)

num_perm = 1
for idx in range(10, 10 - 5, -1):
    num_perm *= idx
print num_perm

print 12.0 / num_perm

# enum = 100000
# 12 / 100000 = 0.00012

# perm = 30240
# 12 / 30240 = 0.000396825396825