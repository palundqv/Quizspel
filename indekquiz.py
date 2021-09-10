import csv
import numpy
import random

with open("ks1.csv", newline="") as csvfile:
    file = csv.reader(csvfile, delimiter=',')
    questions = []
    for row in file:
        question = [row[0], row[1], row[2], row[3], row[4], row[5]]
        questions.append(question)

chosen = []
for i in range(0, len(questions)):
    number = numpy.random.random_integers(1, len(questions))
    while number in chosen:
        number = numpy.random.random_integers(1, len(questions))
    chosen.append(number)


print("Welcome to the INDEK Quiz! Let's begin.")
print("--------------------------------------")
correct = 0
for i in chosen:
    alternatives = ["A", "B", "C", "D", "E"]
    order = [ questions[i][0], questions[i][1], questions[i][2], questions[i][3] ]

    index = [1, 2, 3, 4]
    random.shuffle(index)

    print(questions[i][0])
    print("1: ", questions[i][index[0]])
    print("2: ", questions[i][index[1]])
    print("3: ", questions[i][index[2]])
    print("4: ", questions[i][index[3]])
    answerinput = int((input("Answer: ")))
    try: 
        answer = questions[i][index[answerinput-1]]
        answer_index = order.index(answer)
    except (TypeError, ValueError) as e: 
        print("Something went wrong")
        answer_index = 4

    if alternatives[answer_index-1] == questions[i][5]:
        print("GREAT!")
        correct = correct + 1
    else:
        print("FAKE NEWS! The correct answer is", alternatives.index(questions[i][5])+1)

if correct >=6:
    print("Total result:",correct, "out of 10. Good job!")
else:
    print("Total result:", correct, "out of 10. Better luck next time!")


