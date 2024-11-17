number1 = []
section = int(input("ต้องการป้อนทั้งหมดกี่ตัว"))
for i in range(1,section+1):
    section = (int(input(f'ใส่ตัวที่ {i} : ')))
    number1.append(section)
result = sum(number1)//len(number1)
print(f"ค่าเฉลี่ยของ คือ {numbers} = {result}")
