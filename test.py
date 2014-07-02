import math

print math.factorial(6)

# Lotery - 59 balls, draw 6, order is important

print math.factorial(59) / math.factorial(59 - 6)

num_perms = 1
for idx in range(59, 59 - 6, -1):
    num_perms *= idx
print num_perms

'''
enum = 10!
(1,2,3,4,5)
m = E(0,1,2,3,4,5,6,7,8,9)
n = 5
perm = m!/(m-n)!
comb = m
'''

print (10 ** 5)
variants = 100000
variant = (12.0 / 100000.0)
print variant

# (0,1,2,3,4,5,6,7,8,9)
#
# 10! / (10 - 5)!*10!

print math.factorial(10) / math.factorial(10 - 5)
# m!/(m-n)!n!

num_perms = 1
for idx in range(10, 10 - 5, -1):
    num_perms *= idx
print num_perms

print 12.0 / num_perms

# enum = 100000
# 12 / 100000 = 0.00012

# perm = 30240
# 12 / 30240 = 0.000396825396825