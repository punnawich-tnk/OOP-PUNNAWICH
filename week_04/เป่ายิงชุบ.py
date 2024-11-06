import random
while True:
    ran = random.choice(["ค้อน","กรรไกร","กระดาษ"])
    print("โปรแกรมเป่ายิงฉุบ")
    print(ran)
    print("เลือก ค้อน กรรไกร กระดาษ")
    run = str(input("คุณเลือก : "))


    win = 0
    lose = 0 
    allow = 0

    if run == ran:
        print("ผลลัพธ์คือ เสมอ")
        allow += 1
    elif run == "หยุด":
        print(f"ผลชนะ  = {win} ผลแพ้  = {lose} ผลเสมอ = {allow} ")
        break
    elif (run == "ค้อน" and ran == "กรรไกร"):
        print("คุณชนะ!")
        win += 1
    elif (run == "กรรไกร" and ran == "กระดาษ"):
        print("คุณชนะ!")
        win += 1
    elif (run== "กระดาษ" and ran == "ค้อน"):
        print("คุณชนะ!")
        win += 1
    else:
        print("คุณแพ้!")
        lose += 1
