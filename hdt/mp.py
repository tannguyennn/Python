# Nhập 1 danh sách n điểm trong mặt phẳng. mổi điểm có tọa độ (x, y)
# In ra danh sách điểm va tạo độ
# Tìm điểm xa gốc tọa độ nhất
# Tìm cặp điểm gần nhau nhất
# Loại bỏ các điểm trùng nhau


#import thư viện
import math

class Point2D:

    def __init__(self,x=0,y=0):
        if(x>0):
            print("sai x")
        self.x=x
        self.y=y
    #Phương thức tính khoảng cách giửa hai điểm
    def distance(self,p):
        return math.sqrt((self.x - p.x)**2 + (self.y - p.y)**2)
    #Phương thức in tọa độ
    def print_info(self):
        print("({},{})".format(self.x,self.y))
    def compare(self,p):
        if self.x == p.x & self.y == p.y: return True
        return False

#Tạo danh sách điểm
n = int(input("Nhập số điểm trong mặt phẳng: "))
point_list=[]

for i in range(n):
    print("Nhập điểm thứ {}:".format(i+1))
    x =int (input("x= "))
    y =int (input("y= "))
    p=Point2D(x,y)
    point_list.append(p)

for p in point_list:
    p.print_info()

m = 0
g=Point2D() #Gốc tọa độ

pm=Point2D() 
for p in point_list:
    if(p.distance(g) > m):
        m=p.distance(g)
        pm=p
print("Điểm xa tọa độ nhất: ")
pm.print_info()
print( pm.distance(g))

#thiết lập
pm1=point_list[0]
pm2=point_list[1]
m= pm1.distance(pm2)

for p in point_list:
    for p1 in point_list:
        if(p != p1):
            d=p.distance(p1)
            if(d<m):
                m=d
                pm1=p
                pm2=p1

print("Hai điểm gần nhau nhất:")
pm1.print_info()
pm2.print_info()
print(m)

for p in point_list:
    for p1 in point_list:
        if p!=p1:
            if p.compare(p1):
                point_list.remove(p1)

print("Danh sách sau khi xóa:")
for p in point_list:
    p.print_info()

