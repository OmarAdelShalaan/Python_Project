import  random
while 1:
     n=random.randrange(20)
     flag=0
    # print("the random number is : ", n)
     print("you can enter 5 number")
     for i in range(5):
         check=int(input())
         if n==check:
             flag=1
             break
         elif n>check:
             print("low")
         else:
             print("high")
     if flag:
         print("you win")
     else:
         print("you lose")
     print("play Again ")
