a=[1,2,3,4]

#b chứa phần ử bình phương của dãy a b=[1,4,9,16]
b=[]
#c1
# for i in range(len(a)):
#     b.append( a[i]**2)

#c2
def Square(x):
    return x**2
b = map(Square,a)
b = list(b)

print(b)