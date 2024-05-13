
#Đề 2
import datetime

#kiểm tra biển số xe
def ktrBS(n):
    # Lấy hai ký tự đầu tiên của chuỗi
    two_chars = n[:2]
    # Kiểm tra xem cả hai ký tự có đều là số hay không
    if two_chars.isdigit():
        if(len(n) == 9):
            return True
    return False
#kiểm tra năm sản xuất
def ktrNamSX(nam):
    n = datetime.datetime.now().year
    if(nam > n):
        return False
    if(nam < 1980):
        return False
    return True

class Xe:
        
    # Phương thức khởi tạo và nhập thông tin xe
    def __init__(self,bienSo,hangSX,namSX= datetime.datetime.now().year,namLH=20):
        c=0
        if (ktrBS(bienSo) == False):
            c=1
            print("Biển số sai")
        if(ktrNamSX(namSX) == False):
            c=1
            print("Năm sản xuất sai")
        if(c==0):
            self.bienSo=bienSo
            self.hangSX=hangSX
            self.namSX=namSX
            self.namLH=namLH
    def nhapTTXe(self,x):
        Xe(x)
    #Phương thức xuất thông tin xe
    def xuatTTXe(self):
        print("Biển số: {}, hãng sản xuất: {}, năm sản xuất: {}, năm lưu hành: {} năm"
              .format(self.bienSo,self.hangSX,self.namSX,self.namLH))
    #Phương thức tính sô năm mà xe đã lưu hành
    def soNamLH(self):
        n=int(datetime.datetime.now().year - self.namSX)
        return n


#chương trình chính
#Tạo danh sách xe
ds_xe=[]
ds_xe.append(Xe("79A-12345",'Honda',2019,20))
ds_xe.append(Xe("78A-32322",'Honda',2015,23))
ds_xe.append(Xe("77A-71260",'Honda',2012,24))
ds_xe.append(Xe("79A-93012",'Honda',2010,25))
ds_xe.append(Xe("78A-91823",'Honda',2020,20))

# n = int(input("Nhập số lượng xe:"))
# for i in n:
#     print("Nhập thông tin xe thứ %d",i)
#     bs = input("Nhập biển số:")
#     hsx = input("Nhập hãng sản xuất:")
#     nsx = input("Nhập năm sản xuất:")
#     nlh = input("Nhập năm lưu hành:")
    

print("thông tin các xe:")
for i in ds_xe:
    i.xuatTTXe()

# in thông tin các xe có số năm lưu hành lớn nhất
nmax = ds_xe[0].soNamLH()

for x in ds_xe:
    n = x.soNamLH()
    if n > nmax:
        nmax = x.soNamLH()
print("---------------------------------------------")
print("thông tin xe có năm lưu hành lớn nhất")
for x in ds_xe:
    n=x.soNamLH()
    if(n == nmax):
        x.xuatTTXe()
print("Số năm xe đã lưu hành: {}".format(nmax))

# xóa các xe có biển số bắt đầu là 79
for x in ds_xe:
    two_chars = int(x.bienSo[:2])
    
    if(two_chars == 79):
        ds_xe.remove(x)
print("-----------------------------------------------")
print("thông tin các xe sau khi loại bỏ:")
for i in ds_xe:
    i.xuatTTXe()