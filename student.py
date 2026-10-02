"""Student information and marks management."""
class Student:
    def __init__(self,name,roll_number,marks):
        self.name=name
        self.roll_number=roll_number
        self.marks=marks
    def calculate_average(self):
        return sum(self.marks)/len(self.marks) if self.marks else 0
    def display_details(self):
        print(f'Name: {self.name}')
        print(f'Roll Number: {self.roll_number}')
        print(f'Marks: {self.marks}')
        print(f'Average: {self.calculate_average():.2f}')
