class Bank:
    def __inti__(self,id,name,balance):
        self.id = id 
        self.name = name
        self.balance = balance
    def deposit(self,amount):
        if amount >= 100:
            self.balance += amount
        else:
            print("ใส่ยอดเงิน 100 บาทขึ้นไป")
    def outmoney(self,out):
        if out >= 100:
            self.balance -= out
        else:
            print("ใส่ยอดเงิน 100 บาทขึ้นไป")
    def check(self):
        print(f"คุณมีเงินทั้งหมด {self.balance}")
idl = Bank(1,"pun",5000)
idl.deposit(3000)
idl.deposit(300)
print(f'เงินของ {idl.name} มีอยู่ {idl.balance} บาท')




        