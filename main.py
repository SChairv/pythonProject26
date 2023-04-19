# Write a function that takes a list of numbers and returns a list with two elements:
# 1.    The first element should be the sum of all even numbers in the list.
# 2.    The second element should be the sum of all odd numbers in the list.
def sumsofoddsandevens(a):
    e=0
    o=0
    for n in (a):
        ni=int(n)
        m=ni%2
        if m==0:
            e=e+ni
        else: o=o+ni
    return (e,o)

a=[2,9,7,166,333,7074,1258,999]
print(sumsofoddsandevens(a))
a=[1,1,1,1,1,1,1,1,1,0]
print(sumsofoddsandevens(a))
a=[2,4,6,8,10,12,14,16,18,20]
print(sumsofoddsandevens(a))
