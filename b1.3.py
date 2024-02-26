#lệnh lặp với kiêu từ điển
#dict={k1:vi, k2:v2,...}

numbers = {0:'Không', 1:'Một' , 2:'Hai', 3:'Ba', 4:'Bốn', 5:'Năm'}

for i in numbers.items():
    print(i)

print("Lặp hai biến chạy")

for k,v in numbers.items():
    print("Số {} đọc là {}" .format(k,v))


