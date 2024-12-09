class student:
    def __init__(self,name,id):
        self.name = name    
        self.id = id
        self.grader = {}
    def score(self,score):
        choice = input("เลือกวิชาที่จะกรอกคะแนน : ")
        score = int(input("ใส่คะแนน: "))
        grade = self.grade(score)
        if choice == "M":
            self.grader["MAT"] = grade
        elif choice == "T":
            self.grader["THAI"] = grade
        elif choice == "S":
            self.grader["Sienrc"]= grade
    def grade(self,score):
            if score >= 80 :
                return 4
            elif score >= 70:
                return 3
            elif score >= 60:
                return 2
            elif score >= 50:
                return 1
            else:
                return 0

stu1 = student("Sohp",1)
stu2 = student("Pond",22)
stu1.score(70)
print(stu1.grader)