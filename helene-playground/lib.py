print("Welcome to Helene's Language Quiz")
answer = input('Are you ready to play the Quiz ? (yes/no) :')
score = 0
total_questions = 5

if answer.lower() == 'yes':
    answer = input("Question 1: Which language has the most native speakers?")
    if answer.lower() == 'chinese':
        score += 1
        print('Correct!')
    elif answer == 'Chinese':
        score += 1
        print('Correct!')
    else:
        print('Wrong Answer :(')

    answer = input("Question 2: It is estimated that there are between 200 and 300 indigenous languages in Europe. Yes or No?")
    if answer == 'yes':
        score += 1
        print('Correct')
    elif answer == 'Yes':
        score += 1
        print('Correct')
    else:
        print('Wrong Answer :(')

    answer = input("Question 3: Who was the founder of Esperanto?")
    if answer == 'Ludwig Lazarus Zamenhof':
        score += 1
        print('correct')
    elif answer == 'ludwig lazarus zamenhof':
        score += 1
        print('Correct')
    elif answer == 'ludwig zamenhof':
        score += 1
        print('correct')
    elif answer == 'Ludwig Zamenhof':
        score += 1
        print('Correct')
    else:
        print('Wrong Answer :(')

    answer = input("Question 4: Aleut is a language spoken in parts of Alaska and Siberia. Yes Or No?")
    if answer == 'yes':
        score += 1
        print('Correct')
    elif answer == 'Yes':
        score += 1
        print('Correct')
    else:
        print('Wrong Answer :(')

    answer = input("Question 5: How many living languages do you estimate there are in the world? 500, 2000, 4000, 6000, 10000?"
                   )
    if answer == 6000:
        score += 1
        print('Correct')
    else:
        print('Wrong Answer :(')

print('Thank you for playing this small quiz game, you attempted', score,
      "questions correctly!")
mark = (score / total_questions) * 100
print('Marks obtained:', mark)
print('GOODBYE!')
