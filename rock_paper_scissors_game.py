import  random
def computer_choose():
     n=random.randrange(3)
     if n==0:
         return "rock"
     elif n==1:
         return "paper"
     else:
         return "scissors"

def play():
    player=str(input("choose(rock,paper,scissors) : "))
    com=computer_choose()
    print("computer choose ", com,"you choose", player)
    if com==player:
        print("Draw")
    elif com=="rock" and   player=="paper":
        print("You Win")
    elif com=="rock" and   player=="scissors":
        print("You Lose")
    elif com=="scissors" and   player=="paper":
        print("You Lose")
    elif com=="scissors" and   player=="rock":
        print("You Win")
    elif com=="paper" and   player=="rock":
        print("You Lose")
    elif com=="paper" and   player=="scissors":
        print("You Win")

    return


while 2:
    play()
