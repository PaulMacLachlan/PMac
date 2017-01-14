def scoresAndGrades():
    for counter in range(10):
        grade = ''
        scores = {'key':'value'}
        score = raw_input("Please provide a test score between 60-100: ")
        if score in range(90,101):
            grade = "A"
            scores.append(score,grade)

        elif score in range(80,90):
            grade = "B"
            scores.append(score,grade)

        elif score in range(70,80):
            grade = "C"
            scores.append(score,grade)

        elif score in range(60,70):
            grade = "D"
            scores.append(score,grade)

        elif score <= 59:
            grade = "Invalid Grade"
            continue

            # Score: 87; Your grade is B
    print "Scores and Grades"
    print scores
    print "End of the program. Bye!"


scoresAndGrades()
