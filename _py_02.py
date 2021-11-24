class Student:
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score
    def get_name(self):
        return self.name
    def to_string(self):
        return "Name: "+str(self.name)+"\tAge: "+str(self.age)+"\tScore: "+str(self.score)


def response():
    answer = input("Finish? (Y/N)").strip().lower()
    while answer != "y" and answer != "n":
        print("Your response does not correct, try again ")
        answer = input("Finish? (Y/N)").strip().lower()
    if answer == "y": return True
    else: return False
student_lst = list()
def check_name(name):
    l = list(name)
    for i in l:
        if not i.isalpha():
            if i != " ": return False
    return True

def input_name():
    check = False
    while True:
        name = input("Enter a student's name: ").strip()
        check = check_name(name)
        if check  == True:
            return name
        else:
            print("Name format does not correct, try again")

def input_num(lower, upper):
    if lower > upper:
        tmp = lower
        lower = upper
        upper = tmp
    while True:
        n = input().strip()
        try:
            num = int(n)
            if num < lower or num > upper:
                print("Input does not correct, try again.")
                continue
            else:
                return num
        except:
            print("Input does not correct, try again")



def sort_student_list(student_lst):
    length = len(student_lst)
    for i in range(length):
        for j in range(length-1):
            if student_lst[j].get_name() > student_lst[j+1].get_name():
                tmp = student_lst[j]
                student_lst[j] = student_lst[j+1]
                student_lst[j+1] = tmp

def show_student_list(student_lst):
    for student in student_lst:
        print(student.to_string())



while True:
    st_name = input_name()
    print("Enter a student's age:")
    st_age = input_num(0, 100)
    print("Enter a student's score:")
    st_score = input_num(0, 10)
    student = Student(st_name, st_age, st_score)
    student_lst.append(student)
    r = response()
    if r == True: break

print("\nStudent list before sorting: ")
show_student_list(student_lst)
sort_student_list(student_lst)
print("\nStudent list after sorting: ")
show_student_list(student_lst)