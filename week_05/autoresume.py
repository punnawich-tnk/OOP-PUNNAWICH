resume = {"Nickname":"","number":"","Hobby":"","color":""}
quantity = int(input("จำนวนค่าที่จะป้อน : "))
for i in range(1, quantity + 1):
    print(f"ข้อมูลคนที่ {i}")
    Playname = str(input("กรอกชื่อเล่น :"))
    resume["Nickname"] = Playname
    lagty = str(input("กรอกเลขที่ :"))
    resume["number"] = lagty
    Adelag = str(input("กรอกงานอดิเรก :"))
    resume["Hobby"] = Adelag
    Likecolor = str(input("กรอกสีที่ชอบ :"))
    resume["color"] = Likecolor
    print(resume)


#num = int(input("กรอกจำนวนคนที่จะป้อน : "))
#resume = {}
#for i in range(1,num+1):
#    print(f"กรุณากรอกเลขที่ {i}")
#    resume["nickname"] = str(input("")) 
#    resume["stid"] = str(input(""))
#    resume["Hobby"] = str(input(""))  
#    resume["color"] = str(input(""))
#    print(f"ข้อมูลคนที่ {str(i)}\n{resume}")         