import random

def run():


    you_know_what = input("wanna play a game hhehhehheheehhehhahahahahhahahahahhah, ararrararrararrarhhhhhh , definately a cat on the keyboard!?: ")


    while you_know_what == "yes":



        inp = input("choose rock/paper/scissor: ")
        randc = random.randint(1, 3)

        if randc == 1:
         randnum = "rock"
        elif randc == 2:
            randnum = "scissors"
        else:
         randnum = "paper"



        if randnum == "rock" and inp == "rock":
            print("computer Input is Rock, nothing happens!")

        if randnum == "paper" and inp == "rock":
            print("computer Input is Paper, you lose, go eat dirt nerd! to a patato!")

        if randnum == "scissors" and inp == "rock":
            print("computer Input is scissors, you just deafeated a bot! that's it!")



        if randnum == "rock" and inp == "paper":
         print("computer Input is Rock, you got him or i should say 'it'")

        if randnum == "paper" and inp == "paper":
           print("computer Input is Paper, nothing happens!")

        if randnum == "scissors" and inp == "paper":
            print("computer Input is Scissors, nothing happens!")



        if randnum == "rock" and inp == "scissors":
          print("computer Input is Rock, it just rocked you up , i mean it goes like we will; we will rock you!, kindda java-ish i should say?")

        if randnum == "paper" and inp == "scissors":
           print("computer Input is Paper, oh no! you savage, just cut an innocent paper!!?, can't forget the facebook stuff it has done, every face book user is old these days? right? right!?")

        if randnum == "scissors" and inp == "scissors":
           print("computer Input is Scissors, nothing happens!, sometimes paper does cut paper like the one in 1788-ish time, right?")

class System:
   class Run:
    def final_Executation():
     def Execute():
        run()
     Execute()

class setup:
   def Go():
    System.Run.final_Executation()

def exe():
   setup.Go()

exe()











    

 




