#lặp for comprehensive

# Hãy tạo 1 danh sách các số nguyên liên tiếp từ 1 đén 100

myList = {i for i in range (1,101)}

#tạo ra danh sách chỉ có các số lẻ

myL = {i for i in range(1,101) if i % 2 != 0}

print(myL)