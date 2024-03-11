##Tạo module tự định nghĩa và sử dụng 
###B1 tạo 1 thư mục đặt tên tùy ý, chẳng hạn như my_lib
#### trong thư mục này phải tạo file có tên '__init.py__' không cần mã nguồn
###B2 Trong thư mục 'my_lib' tạo file mã nguồn  chẳng hạn 'functions.py' chứa các thành phần tự cài đặt
## Sử dụng moldule tự định nghĩa
#tạo file mã nguồn mới
# thêm dòng khai 

from my_lib import functions

from my_lib.functions import *
print(SayHi("Nha Trang"))

n=30
if laSNT(n):
    print("%d là số nguyên tố" % n)
else :
    print("%d không là số nguyên tố" %n)

 