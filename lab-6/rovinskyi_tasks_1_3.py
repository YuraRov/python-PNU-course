import csv
from math import sqrt
from typing import Dict, List, NamedTuple

class Coordinate(NamedTuple):
    """A point in 2D space"""
    x: float
    y: float

class Vector:
    """Represents a geometric vector in Cartesian coordinate system"""
    def __init__(self, begin_point: Coordinate, end_point: Coordinate) -> None:
        self.begin_point = begin_point
        self.end_point = end_point
        self.coordinate = Coordinate(end_point.x - begin_point.x, end_point.y - begin_point.y) 
    
    def __str__(self) -> str:
        return f'Start - {self.begin_point}; end - {self.end_point}.'

    def __eq__(self, other) -> bool:
        return self.coordinate.x == other.coordinate.x and self.coordinate.y == other.coordinate.y

    def __add__(self, other):
        return Vector(self.coordinate.x + other.coordinate.x, self.coordinate.y + other.coordinate.y)
    
    def length(self) -> float:
        """Returns the length of a vector"""
        return sqrt(pow(self.coordinate.x, 2) + pow(self.coordinate.y, 2))

    def dot_product(self, other) -> float:
        """Computes the dot product of two vectors"""
        return self.coordinate.x * other.coordinate.x + self.coordinate.y * other.coordinate.y

    def is_perpendicular_to(self, other) -> bool:
        """Checks if two vectors are perpendicular"""
        return self.dot_product(other) == 0

vector1 = Vector(Coordinate(0, 0), Coordinate(0, 2))
vector2 = Vector(Coordinate(0, 0), Coordinate(2, 0))

print(vector1.is_perpendicular_to(vector2))

class Student:
    marks_data = Dict[str, List[int]]

    def __init__(self, name: str, surname: str, marks: marks_data) -> None:
        self.name = name
        self.surname = surname
        self.marks = marks
    
    def __str__(self) -> str:
        return f'Student - {self.name} {self.surname}; subjects with marks - {self.marks}.'
    
    def print_all_subjects(self) -> None:
        print(list(self.marks.keys()))

    def get_marks_from(self, subject: str) -> List[int]:
        return self.marks.get(subject, [])
    
    def get_average_mark_from(self, subject: str) -> float:
        marks = self.get_marks_from(subject)
        return sum(marks) / len(marks) if len(marks) != 0 else 0

    def get_total_average_mark(self) -> float:
        all_sums_and_lengths = [(sum(marks), len(marks)) for marks in self.marks.values()]
        return sum(one_sum for one_sum, _ in all_sums_and_lengths) / sum(one_length for _, one_length in all_sums_and_lengths)
    
    def has_credit_from(self, subject: str) -> bool:
        return self.get_average_mark_from(subject) >= 4

    def add_new_subject_with_marks(self, subject_and_marks: marks_data) -> None:
        self.marks.update(subject_and_marks)
    
    def add_new_mark_to(self, subject: str, mark: int) -> None:
        self.get_marks_from(subject).append(mark)
    
    def get_list_of_average_marks(self) -> List[float]:
        subjects_and_avg_marks = {subject: sum(marks) / len(marks) for subject, marks in self.marks.items()}
        print(f'{self.surname}:')
        for subject, marks in subjects_and_avg_marks.items():
            print(f'{subject}: average mark - {marks}')

        return list(subjects_and_avg_marks.values())

class ComputeSumFromCSV:
    def __init__(self, file_path: str) -> None:
        self.path = file_path
    
    def compute(self) -> None:
        with open('KN-2.csv', 'r') as file:
            csv_reader = csv.DictReader(file)
            student_sum: Dict[str, float] = {}
            for line in csv_reader:
                total = 0
                total += 2 if line['Lab1'] == '+' else 0
                total += 2 if line['Lab2'] == '+' else 0
                # total += if line['Lab3']



student = Student('John', 'Doe', {'math': [3, 4, 5], 'physics': [2, 1, 3, 4]})
student.print_all_subjects()
print(student.get_marks_from('algebra'))
print(student.get_average_mark_from('algebra'))
print(student.get_total_average_mark())
print(student.has_credit_from('physics'))
print(student.get_list_of_average_marks())
