class Student:
    def __init__(self, name, marks, result):
        self.name = name
        self.marks = marks
        self.result = result

    #def result(self):
        #if self.marks >= 40:
            #return "pass"
        #else:
            #return "fail"


s1 = Student("A", 67, "pass")
s2 = Student("B", 32, "fail")

#print(s1.name, "marks are", s1.marks)
print(s1.name, "marks are",s1.marks, "and result is", s1.result)
print(s2.name, "marks are",s2.marks, "and result is", s2.result)
