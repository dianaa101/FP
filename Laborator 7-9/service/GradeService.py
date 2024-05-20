from entities.Grade import Grade
from repo.Repository import Repository
from validator.GradeValidator import GradeValidator
from sort import *


class GradeService:
    def __init__(self, repo: Repository, validator: GradeValidator, student_repo: Repository, subject_repo: Repository):
        """
        Create a grade service
        :param repo: The repository of the grade
        """
        self.__repo = repo
        self.__validator = validator
        self.__student_repo = student_repo
        self.__subject_repo = subject_repo

    def create(self, student, subject, value):
        """
        Create a grade
        :param student: The name of the student
        :param subject: The subject of the grade
        :param value: The value of the grade
        :return: The created grade
        """
        id_student = student.get_id()
        id_subject = subject.get_id()
        id_ = self.__repo.get_available_id()
        grade = Grade(id_, id_student, id_subject, value)
        self.__validator.validate_grade(grade)
        self.__repo.add(grade)
        return grade

    def get_all(self):
        """
        Get all the grades
        :return: All the grades
        """
        return self.__repo.get_all()

    def remove_grades_for_student(self, student):
        """
        Remove grades for student.
        :param student: The student to remove the grades for
        """
        grades = self.__repo.get_all()
        student_id = student.get_id()
        for x in grades:
            if student_id == x.get_id_student():
                self.__repo.remove_by_id(x.get_id())

    def remove_grades_for_subject(self, subject):
        """
        Remove grades for subject.
        :param subject: The subject to remove the grades for.
        """
        grades = self.__repo.get_all()
        subject_id = subject.get_id()
        for x in grades:
            if subject_id == x.get_id_subject():
                self.__repo.remove_by_id(x.get_id())

    def get_filtered_by_subject(self, searched_subject_id):
        grades = self.__repo.get_all()
        filtered_grades = []

        for grade in grades:
            if searched_subject_id != grade.get_id_subject():
                continue

            filtered_grades.append(grade)

        return filtered_grades

    def get_filtered_by_subject_rec(self, searched_subject_id, grades=None):
        if grades is None:
            grades = self.__repo.get_all()

        if len(grades) == 0:
            return []

        # ia prima nota din lista
        grade = grades[0]

        # ia restul notelor
        remaining_grades = grades[1:]

        #verifica daca id-ul subiectului se potriveste cu id-ul subiectului cautat
        if grade.get_id_subject() == searched_subject_id:
            # daca se potriveste, include nota curenta + functia cu restul notelor
            return [grade] + self.get_filtered_by_subject_rec(searched_subject_id, remaining_grades)
        else:
            return self.get_filtered_by_subject_rec(searched_subject_id, remaining_grades)

    def get_grades_for_subject(self, searched_subject_id):
        """
        Get grades for subject.
        :param searched_subject_id: The id of the subject to look for
        :return: The grades for the subject
        """
        # grades = self.get_filtered_by_subject(searched_subject_id)
        grades = self.get_filtered_by_subject_rec(searched_subject_id)

        def sort_fn(grade):
            student = self.__student_repo.find_by_id(grade.get_id_student())
            return student.get_name(), grade.get_value()

        grades.sort(key=sort_fn)

        return grades

    def get_student_avg_grade(self, student_id, subject_id=None):
        s = 0 # sum of grades
        n = 0 # count of grades

        # Get all grades
        grades = self.__repo.get_all()
        # O(n) unde n = numarul de note
        for grade in grades:
            if student_id != grade.get_id_student():
                continue
            if subject_id is not None and subject_id != grade.get_id_subject():
                continue
            s = s + grade.get_value()
            n = n + 1
        if n == 0:
            return 0
        return s / n

    def get_top_20p_avg_grades(self):
        students = self.__student_repo.get_all()
        avg_grades = []
        # O(n) unde n = numarul de stundenti
        for student in students:
            # O(m) unde m = numarul de note
            avg_grade = self.get_student_avg_grade(student.get_id())
            avg_grades.append([student.get_name(), avg_grade])
        # => O(n * m)

        # Selection sort are complexitate O(n^2) unde n = numarul de elemente
        # avem cate un element pentru fiecare student format din [nume, nota]
        # => O(n^2) unde n = numarul de studenti
        avg_grades = selection_sorted(avg_grades, key=lambda x: x[1], reverse=True)

        # => complexitatea totala este O(n * m + n^2)

        n = int(len(avg_grades) * 0.2)
        n = max(n, 1)

        return avg_grades[:n]

    def stat_1(self, searched_subject):
        students = self.__student_repo.get_all()
        avg_grades = []
        for student in students:
            avg_grade = self.get_student_avg_grade(student.get_id(), subject_id=searched_subject.get_id())
            if avg_grade >= 5:
                continue

            avg_grades.append([student.get_name(), avg_grade])

        avg_grades = cocktail_sorted(avg_grades, key=lambda y: (-y[1], y[0]))

        return avg_grades

    def stat_1_rec(self, searched_subject, students=None):
        if students is None:
            students = self.__student_repo.get_all()

        if len(students) == 0:
            return []

        student = students[0]
        students = students[1:]

        avg_grade = self.get_student_avg_grade(student.get_id(), subject_id=searched_subject.get_id())
        if avg_grade >= 5:
            return self.stat_1_rec(searched_subject, students)
        else:
            avg_grades = [avg_grade] + self.stat_1_rec(searched_subject, students)
            avg_grades = cocktail_sorted(avg_grades, key=lambda y: (-y[1], y[0]))
            return avg_grades
