class student:

    def __init__(self):
        self.name = input("Enter your name: ")
        self.class_name = input("Enter your class name: ")
        self.marks = int(input("Enter your marks: "))

    def get_percentage(self):
         return (self.marks / 500) * 100

    def get_grade(self):
        p = self.get_percentage()

        self.grade = "A" 

        if p >= 90:
            self.grade = "A"

        elif p >= 75:
            self.grade = "B"
        elif p >= 50:
            self.grade = "C"
        else:
            self.grade = "Fail"

        return self.grade    

    def print_data(self):
        print(f"Name: {self.name}")
        print(f"Class: {self.class_name}")
        print(f"Percentage: {self.get_percentage()}")
        print(f"Grade: {self.get_grade()}")


s1 = student()

s1.print_data()



