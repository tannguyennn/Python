can = ['Canh','Tân','Nhâm','Quý','Giáp','Ất','Binh','Đinh','Mậu','Kỷ']
chi = ['Thân','Dậu','Tuất','Hợi','Tý','Sửu','Dần','Mẹo','Thìn','Tỵ','Ngọ','Mùi'] 
namDL =int(input('Nhập năm dương lịch: '))
can1 = namDL % 10
chi1 = namDL % 12

print(can[can1] + " " +chi[chi1])