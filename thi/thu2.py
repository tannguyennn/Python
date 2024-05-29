
def laSNT(n):
    if n<2:
        return False
    for i in range(2, n//2+1):
        if n % i == 0 :
            return False
    return True
def inSNT(n):
    if n<2: return False
    for i in range(n):
        if laSNT(i): print(i,end=' ')

if __name__ =='__main__':

    while(True):
        n =int(input("Nhập số nguyên n (0<n<=1000): ")) 
        if n>0 & n<=1000:
            break
    if laSNT(n):
        print("%d là số nguyên tố" % n)
    else:
        print("%d không là số nguyên tố" % n)

    print('Số nguyên tố < n: ',end=' ')
    inSNT(n)

