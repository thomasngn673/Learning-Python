import pyinputplus as pyip
import random

numberOfQuestions = 10
correctNumQuestions = 0

for questionNumber in range(numberOfQuestions):
    num1 = random.randint(0, 9)  # must be inside the 'for' loop
    num2 = random.randint(0, 9)  # if before 'for' loop, the values will not change every time
    # since it is inside the 'for' loop, the value of the random int changes every time it loops back
    print('')

    question = '#%s: %s * %s = ' % (questionNumber + 1, num1, num2)

    try:  # run this code
        answer = pyip.inputStr(question, allowRegexes=['^%s$' % (num1 * num2)],
                               blockRegexes=[('.*', 'Incorrect!')],
                               timeout=8, limit=3)

    except pyip.TimeoutException:  # unless there is an exception
        print('Out of time!')
    except pyip.RetryLimitException:
        print('Out of attempts!')

    else:  # run if there are no exceptions
        print('Correct!')
        correctNumQuestions = correctNumQuestions + 1

print('')
print('Score: %s / %s' % (correctNumQuestions, numberOfQuestions))