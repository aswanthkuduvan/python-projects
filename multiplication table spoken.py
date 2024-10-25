import pyttsx3

number = int(input('Enter the number: '))
dic = {
    1:'ones',
    2:'twos',
    3:'threes',
    4:'fours',
    5:'fives',
    6:'sixes',
    7:'sevens',
    8:'eights',
    9:'nines'
}

for i in  range(1,11):
    result = str(i) + ' ' + dic[number] + ' are ' + str(i*number)
    print(result)

    engine = pyttsx3.init()
    engine.say(result)
    engine.runAndWait()