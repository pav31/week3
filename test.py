import math

print "3!", math.factorial(3)

# # Lotery - 59 balls, draw 6, order is important
#
# print math.factorial(59) / math.factorial(59 - 6)
#
# num_perm = 1
# for idx in range(59, 59 - 6, -1):
#     num_perm *= idx
# print num_perm

'''
T =
n = len(T)



T = {1,2,3}
n = 3 = {1,2,3}

Sn-1 = {1,2}
Sn = {1,2,3}
n^n
S = 0-n
n
n-1
..
0(1)

{}
1
2
3
12
13
23
123

{}
1
2
3
4
12
13
14
23
24
34
123
124
134
234
1234

0 = 5!/(5-0)!*0! = 5! / 5! = 1
1 = 5!/(5-1)!*1! = (4!)*5 / (4!) = 5
2 = 5!/(5-2)!*2! = (3!)*4*5 / (3!)*2! = 10
3 = 5!/(5-3)!*3! = 5! / 2!*3! = 10
4 = 5!/(5-4)!*4! = 5! / 1!*4! = 5
5 = 5!/5! = 1

n*2
0*2 = 0
1*2 = 1



{}
1
2
3
4
5
12
13
14
15
23
24
25
34
35
45

123
124
125
134
135
145
234
235
245
345


1234
1245
1235
1345
2345


n*n



m = len(T) = n
n = len(S) = 0...n

T = {1,2,3}

n = 3! = 2^n

comb = T!/(T - n)!*n!

{1,2}
{2,1}

52

13/52
12/51
11/50
10/49
9/48

m!/(m-n)!n!
51!/(51-4)!4!

'''


num_perm = 1
for idx in range(51, 51 - 4, -1):
    num_perm *= idx
print num_perm
win_comb = num_perm/float(math.factorial(4))
all_comb = float(math.factorial(51))/float(math.factorial(51-4))
print "win", win_comb
print "all", all_comb
print "out", (win_comb / all_comb)

# []
# 51
# [][][][]
# 1 2 3 4 5 6 7 8 9 10 11 12 13
# 1 2 3 4 5 6 7 8 9 10 11 12 13
# 1 2 3 4 5 6 7 8 9 10 11 12 13
# 1 2 3 4 5 6 7 8 9 10 11 12 13

row = [
[1],
[1, 1],
[1, 2, 1],
[1, 3, 3, 1],
[1, 4, 6, 4, 1],
[1, 5, 10, 10, 5, 1],
[1, 6, 15, 20, 15, 6, 1]
]
# print "sum0", sum([1])
# print "sum1", sum([1, 1])
# print "sum2", sum([1, 2, 1])
# print "sum3", sum([1, 3, 3, 1])
# print "sum4", sum([1, 4, 6, 4, 1])
# print "sum5", sum([1, 5, 10, 10, 5, 1])
# print "sum6", sum([1, 6, 15, 20, 15, 6, 1])
# for n in range(7):
#     print "2^%d" % n, 2**n
# print


n_entry = 3
m_row = 6

print "10", float(math.factorial(m_row)) / (math.factorial(m_row - n_entry) * math.factorial(n_entry))


#
# set_t = {1,2,3}
# sets = set()
# m_outcomes = [1,2,3]
# n_length = 0/1/2/3

# 3! / 3!*0! = 1
#
#
#
# for n in range(len(set_t)):
#     m!/(m-n)!*n!

tup = (2,1,2)
st =set([()])
for i in range(3):
    temp = []
    for j in range(i, 3):
        tup_new = list(tup)
        temp.append(tup_new[j])
        st.add(tuple(temp))
print st

def subsets(my_set):
    result = [[]]
    for x in my_set:
        result += [y + [x] for y in result]

    final = set([()])
    for item in result:
        final.add(tuple(item))

    return final
set([(), (1,), (2,), (1, 2), (2, 1), (2, 2), (2, 1, 2)])
print subsets(tup)