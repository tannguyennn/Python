# một máy Atm co cac loai tien 100,20,5 usd
#một người cần rút số tiên m
# liệt kê tất cả các cách rút dc số tiền m , có tất cả ban nhiu cácnh

while True:
    m = int (input("Nhập số tiền cần rút: "))
    if m<=0 or m%5!=0: print('Sô tiền không thỏa mản.')
    if(m > 0 & m%5==0):
        break

n = m
tien =[100,20,5]
i=0
while m >0:
    if(m >= tien[i]):
       print("{} :{}".format(tien[i], m//tien[i]))
    m = m %tien[i] 
    i=i+1
t=0
for i in range(n//tien[0]+1):
    for j in range (n//tien[1]+1):
        for k in range(n//tien[2]+1):
            s = i * tien[0] +j*tien[1]+k*tien[2]
            if(s == n):
                print('{}: {},  {}: {} , {}: {}'.format(tien[0],i,tien[1],j,tien[2],k))
                t=t+1

print(t)

