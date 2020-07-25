if __name__ == "__main__":
    num=int(input("Enter number of players: "))
    student_answers=[]
    for _ in range(num):
        student_answer = input("Enter name: " )
        student_answers.append(student_answer)

    print(student_answers)