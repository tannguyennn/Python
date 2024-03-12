s="Đại học Nha Trang"
print("Độ dài chuỗi: ", len(s))

print("Số từ: ", len(s.split()))

# in ký tự cuối
print(s[-1])

# in 7 ký tự đâu
print(s[:7])

# in 10 ký tự cuối
print(s[-10:])

name = "Tấn Lập"
age = 20
print(f"Hi there, my name is {name} and I is {age}")
print("Hi there, my name is {} and I is {}".format(name, age))
print("Hi there, my name is %s and I is %d" % (name, age))

a,b,c = 3,4,5
print(a,b,c)

PI= 3.141592
print(type(PI))

import math

b= math.sqrt(5)
print(b)

l=['Ford', 1901, 'Mustang', 3.14, False,"Lập"]

print(l[1:4])

l.append("Toyota")
print(l)

l.insert(1,"Huyndai")
print(l)

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

z = x.union(y)

print(z)

print(x.intersection(y))