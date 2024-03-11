#viết chương tring cso các hàm sau
# Hàm kiểm tra 1 số tự nhiêu có phải số nguyên tố hay ko
# Hàm in ra các số nguyên tố <= n
# Hàm tìm só ngto nho nhất > n

def laSNT(n):
    if n<2:
        return False
    for i in range(2, n//2+1):
        if n % i == 0 :
            return False
    return True
def inSNT(n):
    if n<2: return False
    for i in range(n+1):
        if laSNT(i): print(i,end=' ')
        
def timSNT(n):
    if laSNT(n+1): return n+1
    return timSNT(n+1)


if __name__ =='__main__':
    n=int(input("Nhập n: "))
    if laSNT(n):
        print("%d là số nguyên tố" % n)
    else:
        print("%d không là số nguyên tố" % n)

    print('Số nguyên tố < n: ',end=' ')
    inSNT(n)
    print('\n số nguyên tố nhỏ nhất >n: {}'.format(timSNT(n)))
