pun = int(input("เลข :"))
for pun2 in range(1,25,1):
    ans = pun*pun2
    if pun/2 % 2 != 0 :
        print(f"{pun}x{pun2}={ans}")
      
