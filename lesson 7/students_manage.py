class Student:
    def __init__(self, student_id: str, name: str, gpa: float):
        self.student_id = student_id
        self.name = name
        self.gpa = gpa

    def show_info(self):
        return f"ID: {self.student_id} | Name: {self.name} | GPA: {self.gpa:.2f}"

class StudentManager:
    def __init__(self):
        self.students = []

    def add_student(self, student: Student):
        self.students.append(student)

    def display_students(self):
        if not self.students:
            print("Empty students!")
            return
        for student in self.students:
            print(student.show_info())

    def bubble_sort_by_gpa(self):
        """Sắp xếp danh sách sinh viên theo điểm GPA bằng Bubble Sort."""
        n = len(self.students)
        for i in range(n):
            swapped = False
            for j in range(n - i - 1):
                if self.students[j].gpa > self.students[j + 1].gpa:
                    self.students[j], self.students[j + 1] = self.students[j + 1], self.students[j]
                    swapped = True
            if not swapped:
                break

    def binary_search_by_id(self, student_id):
        """Tìm kiếm sinh viên theo ID bằng thuật toán tìm kiếm nhị phân."""
        self.students.sort(key=lambda x: x.student_id)  # Đảm bảo danh sách được sắp xếp theo ID trước khi tìm kiếm
        left, right = 0, len(self.students) - 1
        while left <= right:
            mid = (left + right) // 2
            if self.students[mid].student_id == student_id:
                return self.students[mid]
            elif self.students[mid].student_id < student_id:
                left = mid + 1
            else:
                right = mid - 1
        return None

def app():
    manager = StudentManager()

    while True:
        print("\n=== Hệ thống Quản lý Sinh viên ===")
        print("1. Thêm sinh viên")
        print("2. Hiển thị danh sách sinh viên")
        print("3. Sắp xếp sinh viên theo GPA")
        print("4. Tìm kiếm sinh viên theo ID")
        print("5. Thoát")

        choice = input("Chọn chức năng (1-5): ")

        if choice == '1':
            student_id = input("Nhập ID sinh viên: ")
            name = input("Nhập tên sinh viên: ")
            gpa = float(input("Nhập điểm trung bình (GPA): "))
            manager.add_student(Student(student_id, name, gpa))
            print("Sinh viên đã được thêm!")

        elif choice == '2':
            print("\nDanh sách sinh viên:")
            manager.display_students()

        elif choice == '3':
            manager.bubble_sort_by_gpa()
            print("Danh sách sinh viên đã được sắp xếp theo GPA!")

        elif choice == '4':
            student_id = input("Nhập ID sinh viên cần tìm: ")
            student = manager.binary_search_by_id(student_id)
            if student:
                print("Tìm thấy sinh viên:", student.show_info())
            else:
                print("Không tìm thấy sinh viên có ID này!")

        elif choice == '5':
            print("Thoát chương trình.")
            break

        else:
            print("Lựa chọn không hợp lệ! Vui lòng nhập số từ 1 đến 5.")

app()