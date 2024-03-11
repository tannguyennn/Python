# viết chương trình pythong nhập 1 số nguyên n thỏa 0<n<=1000
# lặp lại việc nhập cho đến khi n thỏa
# kiểm tra n có phải số nguyên tố hay ko
# in ra các số nguyên tố <=n


while(True):
    n =int(input("Nhập số nguyên n (0<n<=1000): ")) 
    if n>0 & n<=1000:
        break

def laSNT(n):
    if n<2:
        return False
    for i in range(2, n//2+1):
        if n % i == 0 :
            return False
    return True


if laSNT(n):
    print("%d là số nguyên tố" % n)
else:
    print("%d không là số nguyên tố" % n)

for i in range(2,n+1):
    if laSNT(i):
        print("%3d" % i , end=" ")



