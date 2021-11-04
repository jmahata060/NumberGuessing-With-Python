import random
l_num=int(input('Enter Lower Limit?'))
u_num=int(input('Enter Upper Limit?'))
num=random.randint(l_num,u_num+1)
count=0

while(True):
    count +=1
    guess_num=int(input('Guess The Number: '))
    if guess_num>l_num-1 and guess_num<u_num+1:
               
        if guess_num==num:
            print('Your Guess Count Is: ',count)
            break
        elif guess_num>num:
            print('Try Again ! You Guess Too High')
            continue
        else:
            print('Try Again ! You Guess Too Low')
    else:
        print('Worng Input! Enter between %d and %d' %(l_num,u_num))
              
                  
print(num)
