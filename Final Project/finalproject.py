# Question tuples hold question and answer
q1 = ("This is question 1", "AnsWer1")
q2 = ("This is question 2", "AnsWer2")
q3 = ("This is question 3", "AnsWer3")
q4 = ("This is question 4", "AnsWer4")
q5 = ("This is question 5", "AnsWer5")
q6 = ("This is question 6", "AnsWer6")
q7 = ("This is question 7", "AnsWer7")
q8 = ("This is question 8", "AnsWer8")
q9 = ("This is question 9", "AnsWer9")
q10 = ("This is question 10", "AnsWer10")

# This is the point per question
question_point = 10

# Define array of question
questions = [q1, q2, q3, q4, q5, q6, q7, q8, q9, q10]

correct_count = 0

for q in questions:
    print("-----------------")
    print(q[0])
    ans = input("Your Answer : ")
    if ans == q[1]:
        correct_count += 1
        print("Correct!")
    else:
        print("Wrong! Correct answer is {}".format(q[1]))

print("-----------------")
if correct_count >= 5:
    print("You are successful. You got {} points".format(correct_count * 10))
else:
    print("You are unsuccessful. You got {} points".format(correct_count * 10))
