##Jeopardy Quiz Maker

import pandas as pd
import random as rd

questions = pd.read_table('jeopardyQuestions.tsv', header=0)
questionsFrame = pd.DataFrame(questions)
pd.set_option('display.max_colwidth', -1)
pd.set_option('display.max_columns', None)


##for i in range(10):
##    qNum = rd.randrange(1, 10000)
##    qList.append(qNum)
##
##test = (questionsFrame.loc[qList, ['value', 'category', 'question', 'answer']].to_string(header=False))
##testForm += test
##print(testForm)
##print(questionsFrame[questionsFrame['category'] == 'AUSTRALIA'])

##Generate multiple choice answers by pulling answers from questions of the same category


def questionGen():
    otherAns = []
    finalAns = []
    qNum = rd.randrange(1,len(questions))
    jeoQues = questionsFrame.loc[qNum, ['value', 'category', 'question', 'answer']].values.tolist()
    category = questionsFrame.loc[qNum, ['category']][0]
    otherQ = questionsFrame[questionsFrame['category'] == category].values.tolist()

    for q in otherQ:
        if q[6] == jeoQues[3]:
            otherQ.pop(otherQ.index(q))
            
    otherAns = rd.sample(otherQ, 3)
    finalAns.append(jeoQues[3])
    
    for i in range(3):
        finalAns.append(otherAns[i][6])
    rd.shuffle(finalAns)
    question ="""Category: {}
Value: {}
Question: {}
A: {}
B: {}
C: {}
D: {}
"""
    return question.format(jeoQues[1], jeoQues[0], jeoQues[2], finalAns[0], finalAns[1], finalAns[2], finalAns[3]), finalAns.index(jeoQues[3]), jeoQues[0]


def startGame():
    questionNum = 0
    playerMoney = 0
    options = ['A', 'B', 'C', 'D']
    print('Lets Play Jeopardy!')
    if input("Would you like to play? Y/N").lower() in ['yes', 'y', 'ye']:
        while True:
            questionNum += 1
            question, rightAns, value = questionGen()
            print()
            print('-' * 20)
            print('Your money:', playerMoney)
            print('Here is question number', str(questionNum) + '!\n')
            print(question)
            userAns = input('Please type your answer: ').lower()
            if userAns == 'a':
                userAns = 0
            elif userAns == 'b':
                userAns = 1
            elif userAns == 'c':
                userAns = 2
            elif userAns == 'd':
                userAns = 3
            if userAns == rightAns:
                print('\nCorrect!')
                playerMoney += value
            else:
                print('\nIncorrect, the correct answer was:', options[rightAns])
                
            if input('Would you like another question? Y/N').lower() not in ['yes', 'y', 'ye']:
                print('Thanks for playing!')
                break
    else:
        print('\nBye!')
        



##print(questionGen())
startGame()
