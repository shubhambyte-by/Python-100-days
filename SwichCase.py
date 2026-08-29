print("Enter marks to calculate Grade")
marks = int(input())
match marks:
    case marks if marks > 80 and marks <= 100:
        print("You are in A Grade")
    case marks if marks > 70 and marks <= 80:
        print("You are in B grade")
    case marks if marks >= 60 and marks <= 70:
        print("You are in C grade")
    case _:
        print("Invalid marks or F grade")