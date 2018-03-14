import random
def random_number():
    choice = int(input("choose a random number:"))

    rand = random.randint(1,10)

    if choice == rand:
        print "your guess was correct"
    else:
        print "oh oh..wrong answer...try again.."
        print "you choose %d , but the correct answer was %d" %(choice,rand)

    ans = raw_input("want to try again? y/n")

    if ans.lower() == 'y':
        random_number()
    else:
         print "see you next time"
         exit
   
random_number()
