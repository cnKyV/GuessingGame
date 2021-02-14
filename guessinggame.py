import random

a = random.randint(0,100)
counter = 0
lastnumber = 0
print(a)
while(True):
    number = int(input())
    if(number > 100 or number < 0):
        print('OUT OF BOUNDS')
    elif counter == 0:
        if number == a:
            print('Congratz!')
            break
        elif number>a:
            if (number-a) < 10:
                print('WARM!')
                counter+=1
                lastnumber = number          
            else:
                print('COLD!')
                counter+=1
                lastnumber = number
        elif number < a:
            if(a-number) < 10:
                print('WARM!')
                counter+=1
                lastnumber = number          
            else:
                print('COLD!')
                counter+=1
                lastnumber = number
    else:
        if number == a:
            print("Congratz!")
            break
        elif (number-a) < (lastnumber-a):
            print('COLDER!')
            lastnumber = number
        else:
            print('WARMER!')
            lastnumber = number
