import random
print("Math Test For Beginner")
print("==================================")
print("Please Login To Your Account ID")
name = str(input("Nickname: "))
password = int(input("Password: "))
if password != str:
    print(f"Account {name} Verified")
    print(f"Goodluck for the test {name}")
elif password == str:
    exit("Please check again your password")
print()
print("===============================")
print()

#otp generator

def generate_OTP():
    return str(random.randint(100000,999999)) #membuat otp
Verifikasi_OTP = generate_OTP()
print("This is your OTP number" , Verifikasi_OTP)
number_OTP = input("Enter OTP Number: ") 
while number_OTP != Verifikasi_OTP:
    print("Failed to Verified")
    Verifikasi_OTP = generate_OTP()
    print("This is Your New OTP Number:", Verifikasi_OTP)
    number_OTP = input("Enter OTP Number: ")
print("Verified")
print()
print("===============================")
print()

#start question

print("First Question:")        #first question
print("(2² + 2) + (2² + 2)")
first_answer = int(input("Answer : "))
if first_answer == 12:
    print("Good Job, Mate!")
else:
    print(f"Wrong answer, the answer is: 12, but your answer is {first_answer}")      
answer_score = 0
if first_answer == 12:
    print("Your Score :", str(answer_score+1)+"/5")
elif first_answer != 12:
    print("Your Score :", str(answer_score)+"/5")   
    
print()     #end for first question

next_question = str(input("Are you ready for the next question? (Yes or No): "))
answer1 = "Yes"
answer2 = "No"
if next_question == answer1:
    print("Alright, let's move to the next question")
elif next_question == answer2:
    print(exit("Okay, see you next time"))
print()
print("Second Question:")         #second question
print("(40**2) * (40**2)")
second_answer = int(input("Your Answer: "))
if second_answer == 2560000:
    print("Well done, Mate!")
else:
    print(f"Wrong answer, the answer is: 2560000, and your answer is {second_answer}")
if second_answer == 2560000 and first_answer == 12:
    print("Your Score :", str(answer_score+2)+"/5")
elif first_answer != 12 and second_answer == 2560000:
    print("Your Score :", str(answer_score+1)+"/5")
elif first_answer != 12 and second_answer != 2560000:
    print("Your Score :", str(answer_score)+"/5")
elif first_answer == 12 and second_answer != 2560000:
    print("Your Score :", str(answer_score+1)+"/5")
print()     #end for second question


next_question_2 = str(input("你还要继续吗？要 / 不要： "))    #third qustion
answer3 = "要"
answer4 = "不要"
if next_question_2 == answer3:
    print("加油小朋友！")
else:
    print(exit("好吧，再见小朋友!"))
print()
print("第三题:")         #third question
print("(3³) × (3³)")
third_answer = int(input("你的答案: "))
if third_answer == 729:
    print("哇，你的数学不错啊兄弟！")
else:
    print(f"答案错了小兄弟,应该答案是729,你的答案就是{third_answer}")
if third_answer == 729 and first_answer == 12 and second_answer == 2560000:
    print("Your Score :", str(answer_score+3)+"/5")
elif third_answer == 729 and first_answer != 12 and second_answer == 2560000:
    print("Your Score :", str(answer_score+2)+"/5")
elif third_answer != 729 and first_answer == 12 and second_answer == 2560000:
    print("Your Score :", str(answer_score+2)+"/5")
elif third_answer == 729 and first_answer == 12 and second_answer != 2560000:
    print("Your Score :", str(answer_score+2)+"/5")
elif third_answer != 729 and first_answer != 12 and second_answer == 2560000:
    print("Your Score :", str(answer_score+1)+"/5")
elif third_answer == 729 and first_answer != 12 and second_answer != 2560000:
    print("Your Score :", str(answer_score+1)+"/5")
elif third_answer != 729 and first_answer == 12 and second_answer != 2560000:
    print("Your Score :", str(answer_score+1)+"/5")
elif third_answer != 729 and first_answer != 12 and second_answer != 2560000:
    print("Your Score :", str(answer_score)+"/5")
print()      #end of third question


next_question_2 = str(input("你还要继续吗？要 / 不要： "))    #fourth qustion
answer3 = "要"
answer4 = "不要"
if next_question_2 == answer3:
    print("加油小朋友！")
else:
    print(exit("好吧，再见小朋友!"))
print()
print("第四题:")         #fourth question
print("(90⁴) + (90⁴)")
fourth_answer = int(input("你的答案: "))
if fourth_answer == 131220000:
    print("哇, 真厉害啊！")
else:
    print(f"答案错了小兄弟,应该答案是: 131220000,你的答案就是{fourth_answer}")
if third_answer == 729 and first_answer == 12 and second_answer == 2560000 and fourth_answer == 131220000:
    print("Your Score :", str(answer_score+4)+"/5")
elif third_answer != 729 and first_answer == 12 and second_answer == 2560000 and fourth_answer == 131220000:
    print("Your Score :", str(answer_score+3)+"/5")
elif third_answer == 729 and first_answer != 12 and second_answer == 2560000 and fourth_answer == 131220000:
    print("Your Score :", str(answer_score+3)+"/5")
elif third_answer == 729 and first_answer == 12 and second_answer != 2560000 and fourth_answer == 131220000:
    print("Your Score :", str(answer_score+3)+"/5")
elif third_answer == 729 and first_answer == 12 and second_answer == 2560000 and fourth_answer != 131220000:
    print("Your Score :", str(answer_score+3)+"/5")
elif third_answer != 729 and first_answer != 12 and second_answer == 2560000 and fourth_answer == 131220000:
    print("Your Score :", str(answer_score+2)+"/5")
elif third_answer == 729 and first_answer != 12 and second_answer != 2560000 and fourth_answer == 131220000:
    print("Your Score :", str(answer_score+2)+"/5")
elif third_answer == 729 and first_answer == 12 and second_answer != 2560000 and fourth_answer != 131220000:
    print("Your Score :", str(answer_score+2)+"/5")
elif third_answer != 729 and first_answer == 12 and second_answer == 2560000 and fourth_answer != 131220000:
    print("Your Score :", str(answer_score+2)+"/5")
elif third_answer != 729 and first_answer == 12 and second_answer != 2560000 and fourth_answer == 131220000:
    print("Your Score :", str(answer_score+2)+"/5")
elif third_answer == 729 and first_answer != 12 and second_answer == 2560000 and fourth_answer != 131220000:
    print("Your Score :", str(answer_score+2)+"/5")
elif third_answer != 729 and first_answer != 12 and second_answer != 2560000 and fourth_answer == 131220000:
    print("Your Score :", str(answer_score+1)+"/5")
elif third_answer != 729 and first_answer == 12 and second_answer != 2560000 and fourth_answer != 131220000:
    print("Your Score :", str(answer_score+1)+"/5")
elif third_answer != 729 and first_answer != 12 and second_answer == 2560000 and fourth_answer != 131220000:
    print("Your Score :", str(answer_score+1)+"/5")
elif third_answer == 729 and first_answer != 12 and second_answer != 2560000 and fourth_answer != 131220000:
    print("Your Score :", str(answer_score+1)+"/5")
elif third_answer != 729 and first_answer != 12 and second_answer != 2560000 and fourth_answer != 131220000:
    print("Your Score :", str(answer_score)+"/5")
print()      #end of fourth question


                                                #需要改变#

print("这是最后的考试，加油小朋友！")       #Your question
print("第五题")
print("(10² + 10²) ÷ (10² + 10²) ")
fifth_answer = int(input("你的答案："))
if fifth_answer == 1:
    print("哇, 真厉害啊小朋友！")
elif fifth_answer != 1:
    print(f"答案错了小兄弟,应该答案是: 1,你的答案就是{fifth_answer}")
if first_answer == 12 and second_answer == 2560000 and third_answer == 729 and fourth_answer == 131220000 and fifth_answer == 1:
    print("You get a perfect score :", str(answer_score+5)+"/5")
elif first_answer != 12 and second_answer == 2560000 and third_answer == 729 and fourth_answer == 131220000 and fifth_answer == 1:
    print("Final Score:", str(answer_score+4)+"/5")
elif first_answer == 12 and second_answer != 2560000 and third_answer == 729 and fourth_answer == 131220000 and fifth_answer == 1:
    print("Final Score:", str(answer_score+4)+"/5")
elif first_answer == 12 and second_answer == 2560000 and third_answer != 729 and fourth_answer == 131220000 and fifth_answer == 1:
    print("Final Score:", str(answer_score+4)+"/5")
elif first_answer == 12 and second_answer == 2560000 and third_answer == 729 and fourth_answer != 131220000 and fifth_answer == 1:
    print("Final Score:", str(answer_score+4)+"/5")
elif first_answer == 12 and second_answer == 2560000 and third_answer == 729 and fourth_answer == 131220000 and fifth_answer != 1:
    print("Final Score:", str(answer_score+4)+"/5")
elif first_answer != 12 and second_answer != 2560000 and third_answer == 729 and fourth_answer == 131220000 and fifth_answer == 1:
    print("Final Score:", str(answer_score+3)+"/5")
elif first_answer != 12 and second_answer == 2560000 and third_answer != 729 and fourth_answer == 131220000 and fifth_answer == 1:
    print("Final Score:", str(answer_score+3)+"/5")
elif first_answer != 12 and second_answer == 2560000 and third_answer == 729 and fourth_answer != 131220000 and fifth_answer == 1:
    print("Final Score:", str(answer_score+3)+"/5")
elif first_answer != 12 and second_answer == 2560000 and third_answer == 729 and fourth_answer == 131220000 and fifth_answer != 1:
    print("Final Score:", str(answer_score+3)+"/5")
elif first_answer == 12 and second_answer != 2560000 and third_answer != 729 and fourth_answer == 131220000 and fifth_answer == 1:
    print("Final Score:", str(answer_score+3)+"/5")
elif first_answer == 12 and second_answer != 2560000 and third_answer == 729 and fourth_answer != 131220000 and fifth_answer == 1:
    print("Final Score:", str(answer_score+3)+"/5")
elif first_answer == 12 and second_answer != 2560000 and third_answer == 729 and fourth_answer == 131220000 and fifth_answer != 1:
    print("Final Score:", str(answer_score+3)+"/5")
elif first_answer == 12 and second_answer == 2560000 and third_answer != 729 and fourth_answer != 131220000 and fifth_answer == 1:
    print("Final Score:", str(answer_score+3)+"/5")
elif first_answer == 12 and second_answer == 2560000 and third_answer != 729 and fourth_answer == 131220000 and fifth_answer != 1:
    print("Final Score:", str(answer_score+3)+"/5")
elif first_answer == 12 and second_answer == 2560000 and third_answer == 729 and fourth_answer != 131220000 and fifth_answer != 1:
    print("Final Score:", str(answer_score+3)+"/5")
elif first_answer != 12 and second_answer != 2560000 and third_answer != 729 and fourth_answer == 131220000 and fifth_answer == 1:
    print("Final Score:", str(answer_score+2)+"/5")
elif first_answer == 12 and second_answer != 2560000 and third_answer != 729 and fourth_answer != 131220000 and fifth_answer == 1:
    print("Final Score:", str(answer_score+2)+"/5")
elif first_answer == 12 and second_answer == 2560000 and third_answer != 729 and fourth_answer != 131220000 and fifth_answer != 1:
    print("Final Score:", str(answer_score+2)+"/5")
elif first_answer != 12 and second_answer == 2560000 and third_answer != 729 and fourth_answer != 131220000 and fifth_answer == 1:
    print("Final Score:", str(answer_score+2)+"/5")
elif first_answer != 12 and second_answer == 2560000 and third_answer == 729 and fourth_answer != 131220000 and fifth_answer != 1:
    print("Final Score:", str(answer_score+2)+"/5")
elif first_answer == 12 and second_answer != 2560000 and third_answer == 729 and fourth_answer != 131220000 and fifth_answer != 1:
    print("Final Score:", str(answer_score+2)+"/5")
elif first_answer == 12 and second_answer != 2560000 and third_answer != 729 and fourth_answer == 131220000 and fifth_answer != 1:
    print("Final Score:", str(answer_score+2)+"/5")
elif first_answer != 12 and second_answer != 2560000 and third_answer == 729 and fourth_answer == 131220000 and fifth_answer != 1:
    print("Final Score:", str(answer_score+2)+"/5")
elif first_answer != 12 and second_answer == 2560000 and third_answer != 729 and fourth_answer == 131220000 and fifth_answer != 1:
    print("Final Score:", str(answer_score+2)+"/5")
elif first_answer != 12 and second_answer != 2560000 and third_answer == 729 and fourth_answer != 131220000 and fifth_answer == 1:
    print("Final Score:", str(answer_score+2)+"/5")
elif first_answer != 12 and second_answer != 2560000 and third_answer != 729 and fourth_answer != 131220000 and fifth_answer == 1:
    print("Final Score:", str(answer_score+1)+"/5")
elif first_answer != 12 and second_answer != 2560000 and third_answer != 729 and fourth_answer == 131220000 and fifth_answer != 1:
    print("Final Score:", str(answer_score+1)+"/5")
elif first_answer != 12 and second_answer != 2560000 and third_answer == 729 and fourth_answer != 131220000 and fifth_answer != 1:
    print("Final Score:", str(answer_score+1)+"/5")
elif first_answer != 12 and second_answer == 2560000 and third_answer != 729 and fourth_answer != 131220000 and fifth_answer != 1:
    print("Final Score:", str(answer_score+1)+"/5")
elif first_answer == 12 and second_answer != 2560000 and third_answer != 729 and fourth_answer != 131220000 and fifth_answer != 1:
    print("Final Score:", str(answer_score+1)+"/5")
elif first_answer != 12 and second_answer != 2560000 and third_answer != 729 and fourth_answer != 131220000 and fifth_answer != 1:
    print("Final Score:", str(answer_score)+"/5")
print(f"谢谢 {name} 参观考试了")
exit("考试结束了。其实，这个不是真正的考试，这个还是练习， 所以你们要加油哦")  #end of Your question

