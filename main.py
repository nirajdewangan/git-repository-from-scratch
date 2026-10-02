"""Main entry point for the Python project."""
from calculator import add, subtract, multiply, divide
from student import Student
from text_utils import to_uppercase, to_lowercase, count_words, reverse_text

def main():
    print('='*45)
    print('GIT REPOSITORY FROM SCRATCH')
    print('='*45)
    print('\n1. CALCULATOR')
    print('Addition:', add(20,10))
    print('Subtraction:', subtract(20,10))
    print('Multiplication:', multiply(20,10))
    print('Division:', divide(20,10))
    print('\n2. STUDENT MANAGEMENT')
    student=Student('Rahul',101,[85,90,78,92])
    student.display_details()
    print('\n3. TEXT UTILITIES')
    message='Learning Git with Python'
    print('Original:',message)
    print('Uppercase:',to_uppercase(message))
    print('Lowercase:',to_lowercase(message))
    print('Word Count:',count_words(message))
    print('Reverse:',reverse_text(message))
    print('\nProject executed successfully!')

if __name__=='__main__': main()
