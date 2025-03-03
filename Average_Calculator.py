#Python program that calculates the average marks for a student in three subjects using arrays.

def subject_marks_getter(subject):
    tests=['Assignment','CourseWork','MidTerm','EndofTerm']
    marks=[]

    print(f"Enter the marks for{subject}:")
    for test in tests:
        while True:
            mark = float(input(f"Enter marks for {test}:"))
            if 0 <= mark<=100:
                marks.append(mark)
                break
            else:
                print(" Ehh! Guy enter a real mark between 0 and 100.")

    return marks


def Calc_Average(marks):
    return sum(marks)/len(marks)

def main():
    print("Welcome to the Student Mark Calculator")
    Subject_Order=['Physics','Chemistry','Math']
    print(f"The oder of entering values is {','.join(Subject_Order)}")

    subject=0
    subject_marks=[]

    for subject in range(len(Subject_Order)):
        print(f"\nNow entering marks for: {Subject_Order[subject]}")
        marks=subject_marks_getter(Subject_Order[subject])
        subject_marks.append(marks)

    print("\n ---Average Marks---")
    for subject in range(len(Subject_Order)):
        average=Calc_Average(subject_marks[subject])
        print(f"{Subject_Order[subject]} Average Mark: {average}")

main()
# Physics=subject_marks_getter("Physics")
# print(Physics)
