import pyinputplus as pyip
import random, time


numberOfQuestions = 10
correctAnswers = 0
for questionNumber in range(numberOfQuestions):
    num1 = random.randint(0, 9)
    num2 = random.randint(0, 9)

    prompt = '#%s: %s x %s = ' % (questionNumber+1, num1, num2)  # '#questionNumber: 'number' * 'number' = '
    # %s is a string holder, %d for integer holder
    # %s in this case, not %d, because 'prompt' is a string

    try:  # run this code first
        pyip.inputStr(prompt, allowRegexes=['^%s$' % (num1 * num2)],  # run the prompt which displays the prompt text
                      # only allows regexes that start and end with num1/num2
                      blockRegexes=[('.*', 'Incorrect!')],
                      timeout=8, limit=3)  # 8 seconds, 3 tries

    except pyip.TimeoutException:  # run this code if there is an exception
        print('Out of time!')
    except pyip.RetryLimitException:
        print('Out of tries!')

    else:  # if there are no exceptions to 'try' code
        print('Correct!')
        correctAnswers += 1

print('Score: %s / %s' % (correctAnswers, numberOfQuestions))
