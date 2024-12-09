class Student:
    def __init__(self, name, id, age, grades):
       
        self.name = name
        self.id = id
        self.age = age
        self.grades = grades

    def update_grade(self, subject, new_grade):
        self.grades[subject] = new_grade
    def calculate_gpa(self):
        total = sum(self.grades.values())
        count = len(self.grades)
        gpa = total / count if count > 0 else 0
        return round(gpa, 2)

    def display_student_info(self):
        
        gpa = self.calculate_gpa()
        info = (
            f"ชื่อ: {self.name}\n"
            f"หมายเลขประจำตัว: {self.id}\n"
            f"อายุ: {self.age}\n"
            f"เกรดเฉลี่ย: {gpa}\n"
            f"คะแนนรายวิชา: {self.grades}"
        )
        return info

    def grade_change_message(self):
        gpa = self.calculate_gpa()
        return f"นาย {self.name} ได้เกรดเฉลี่ย {gpa:.2f}"

student = Student(
    name="ปุณณวิช",
    id="6731008",
    age=18,
    grades={"คณิต": 85, "ไทย": 90, "อังกฤษ": 80, "วิทย์": 88, "สังคม": 75}
)

student.update_grade("คณิต", 95)
print(student.display_student_info())
print(student.grade_change_message())