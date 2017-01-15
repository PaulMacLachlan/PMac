def scoresAndGrades():
    print "Scores and Grades"
    for response in range(2): #change to 10 once functions runs correctly
        scores = {'score': 'grade'}
        grade = ''
        score = ''

        response = raw_input("Please provide a test score between 60-100: ")
        print response
        if response == 90:# and response <= 101:
            print 'I got an A'
            print "End of the program. Bye!"
            # grade = 'A'
            # # scores.append('score',grade)
            # scores['response'] = 'grade'
        #
        # elif score in range(80,90):
        #     print 'I got a B'
        #     grade = 'B'
        #     scores.append(score,grade)
        #
        # elif score in range(70,80):
        #     print 'I got a C'
        #     grade = 'C'
        #     scores.append(score,grade)
        #
        # elif score in range(60,70):
        #     print 'I got a D'
        #     grade = 'D'
        #     scores.append(score,grade)
        #
        # elif score <= 59:
        #     print 'I got an F'
        #     grade = 'Invalid Grade'
        #     continue

    #         def determine_grade(grade):
    # if grade >= 90 and grade <= 100:
    #     return 'A'
    # elif grade >= 80 and grade <= 89:
    #     return 'B'
    # elif grade >= 70 and grade <= 79:
    #     return 'C'
    # elif grade >= 60 and grade <= 69:
    #     return 'D'
    # else:
    #     return 'F'

            # Score: 87; Your grade is B

    #print scores



scoresAndGrades()
