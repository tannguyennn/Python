#in ra các số từ 1 đến 100 , mỗi dòng 10 số

for i in range(1,101):
    print("%3d" %i, end=" ")
    if i % 10 == 0:
        print()