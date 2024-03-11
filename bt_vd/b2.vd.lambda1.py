#tính tổng 
n=5
# #c1
# s=0
# for i in range(n+1):
#     s =s + i*i

# #c2
# def Square(x):
#     return x**2
# s=0
# for i in range(n+1):
#     s=s+Square(i)

# #c3
s=0
k=lambda i: i**2
for i in range(n+1):
    s= s+ k(i)
    

print('S= {}'.format(s))