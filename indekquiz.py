import csv
import numpy
import random

with open("ks1.csv", newline="") as csvfile:
    file = csv.reader(csvfile, delimiter=',')
    questions = []
    for row in file:
        question = [row[0], row[1], row[2], row[3], row[4], row[5]]
        questions.append(question)

amount = list(range(1, 47))
random.shuffle(amount)

print("Welcome to POPPES INDEK Quiz! Let's begin.")
print("---------------------------------------")
correct = 0
asked_questions = []
amountOfQuestions = 0
for i in amount:

    amountOfQuestions += 1

    alternatives = ["A", "B", "C", "D"]
    questionOrder = [ questions[i][1], questions[i][2], questions[i][3], questions[i][4] ]

    index = [1, 2, 3, 4]
    random.shuffle(index)

    print("Question", i, ": ", questions[i][0])
    print("1: ", questions[i][index[0]])
    print("2: ", questions[i][index[1]])
    print("3: ", questions[i][index[2]])
    print("4: ", questions[i][index[3]])
    answerinput = input("Answer: ")

    while True:    
        try: 
            answer = questions[i][index[int(answerinput)-1]]
            answer_index = questionOrder.index(answer)
            break
        except (TypeError, ValueError) as e: 
            print("Either you made the wrong input or I'm bad at coding")
            answerinput = input("Try again: ")

    if alternatives[answer_index] == questions[i][5]:
        print("GREAT!")
        correct = correct + 1
    else:
        for j in range(0, 4):
            if questions[i][index[j]] == questionOrder[alternatives.index(questions[i][5])]:
                print("FAKE NEWS! The correct answer is:", j+1)

    print(correct, "right out of", amountOfQuestions)


if correct >=(47/6):
    print("Total result:",correct, "out of 46. Good job!")
else:
    print("Total result:", correct, "out of 46. Not godkänd, study more for kontrollskrivning of DOOM!")