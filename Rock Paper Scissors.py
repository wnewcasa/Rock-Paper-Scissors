import tkinter as tk
import random
import time

class MyGame:


    Wcount = 0
    Lcount = 0
    Dcount = 0
    Rcount = 0

    def __init__(self):

        # Making the window
        self.root = tk.Tk()
        self.root.geometry("1000x1000")
        self.root.configure(bg="#ffc6d9")
        self.root.title("ROCK PAPER SCISSORS")
        


        # Adding the labels
        self.label = tk.Label(self.root, text="Rock Paper Scissors\n", bg="#ffc6d9", font=("fixedsys", 40, "bold", "underline"))
        self.label.pack()
        self.label2 = tk.Label(self.root, text="  PLAYER    V.S   COMPUTER", borderwidth="10", relief="ridge", fg="black", font=("fixedsys", 35, "bold"))
        self.label2.pack()
        self.label3 = tk.Label(self.root, text="\nCHOOSE YOUR WEAPON!\n", bg="#ffc6d9", fg="red", font=("fixedsys", 40, "bold"))
        self.label3.pack()

        # Adding the frame for the buttons
        self.buttonframe = tk.Frame(self.root)
        self.buttonframe.columnconfigure(0, weight=1)
        self.buttonframe.columnconfigure(1, weight=1)
        self.buttonframe.columnconfigure(2, weight=1)

        # Adding the buttons

        # Rock
        self.rock = tk.Button(self.buttonframe, text="Rock", height=3, width=15, borderwidth="10", relief="raised", bg="black", fg="white", font=("fixedsys", 25, "bold"), command=self.rock)
        self.rock.grid(row=0, column=0, sticky="we")
        # Paper
        self.paper = tk.Button(self.buttonframe, text="Paper", height=3, width=15, borderwidth="10", relief="raised", bg="black", fg="white",  font=("fixedsys", 25, "bold"), command = self.paper)
        self.paper.grid(row=0, column=1, sticky="we")
        # Scissors
        self.scissors = tk.Button(self.buttonframe, text="Scissors", height=3, width=15, borderwidth="10", relief="raised", bg="black", fg="white", font=("fixedsys", 25, "bold"), command = self.scissors)
        self.scissors.grid(row=0, column=2, sticky="we")
        # Making button stretch acrros the window
        self.buttonframe.pack()
        

        self.root.mainloop()
        
    # Rock is value 1
    def rock(self):
        self.play_round(1)
        

    # Paper is 2
    def paper(self):
        self.play_round(2)
        

    # Scissors is 3
    def scissors(self):
        self.play_round(3)
        
    def play_round(self, player_choice):
        rand = random.randint(1, 3)

        # Player draws
        if player_choice == rand:
            if player_choice == 1:
                self.newL = tk.Label(self.root, text="You Drew\nComputer Chose Rock", bg="#ffc6d9", fg="#333132", font=("fixedsys", 25, "bold"))
            elif player_choice == 2:
                self.newL = tk.Label(self.root, text="You Drew\nComputer Chose Paper", bg="#ffc6d9", fg="#333132", font=("fixedsys", 25, "bold"))
            else:
                self.newL = tk.Label(self.root, text="You Drew\nComputer Chose Scissors", bg="#ffc6d9", fg="#333132", font=("fixedsys", 25, "bold"))
            MyGame.Dcount += 1
        # Player wins
        if(player_choice == 1 and rand == 3) or (player_choice == 2 and rand == 1) or (player_choice == 3 and rand == 2):
            if player_choice == 1:
                self.newL = tk.Label(self.root, text="You Won :)\nComputer Chose Scissors", bg="#ffc6d9", fg="#249e2b", font=("fixedsys", 25, "bold"))
            elif player_choice == 2:
                self.newL = tk.Label(self.root, text="You Won :)\nComputer Chose Rock", bg="#ffc6d9", fg="#249e2b", font=("fixedsys", 25, "bold"))
            else:
                self.newL = tk.Label(self.root, text="You Won :)\nComputer Chose Paper", bg="#ffc6d9", fg="#249e2b", font=("fixedsys", 25, "bold"))
            MyGame.Wcount += 1
        # Player loses
        if(player_choice == 1 and rand == 2) or (player_choice == 2 and rand == 3) or (player_choice == 3 and rand == 1):
            if player_choice == 1:
                self.newL = tk.Label(self.root, text="You Lost :(\nComputer Chose Paper", bg="#ffc6d9", fg="red", font=("fixedsys", 25, "bold"))
            elif player_choice == 2:
                self.newL = tk.Label(self.root, text="You Lost :(\nComputer Chose Scissors", bg="#ffc6d9", fg="red", font=("fixedsys", 25, "bold"))
            else:
                self.newL = tk.Label(self.root, text="You Lost :(\nComputer Chose Rock", bg="#ffc6d9", fg="red", font=("fixedsys", 25, "bold"))
            MyGame.Lcount += 1
        
        self.newL.pack()
        MyGame.Rcount += 1

        # Check if 3 rounds are completed
        if MyGame.Rcount == 3:
            # Delay the series result by 1 second (1000ms)
            self.root.after(500, self.results)

    # Check results of series
    def results(self):
        if(MyGame.Wcount >= 2):
            self.result_label = tk.Label(self.root, text="YOU WON THE SERIES!", height = 10, width = 80, bg="#37f543", fg="white", font=("fixedsys", 100, "bold", "underline"))
            self.result_label.place(relx=0.5, rely=0.5, anchor = 'center')
        if(MyGame.Lcount >= 2):
            self.result_label = tk.Label(self.root, text="YOU LOST THE SERIES!", height = 10, width = 80, bg="#ff2400", fg="black", font=("fixedsys", 100, "bold", "underline"))
            self.result_label.place(relx=0.5, rely=0.5, anchor = 'center')
        if(MyGame.Dcount == 1 and MyGame.Wcount == 1 and MyGame.Lcount == 1):
            self.result_label = tk.Label(self.root, text="YOU DREW THE SERIES!", height = 10, width = 80, bg="grey", fg="#333132", font=("fixedsys", 100, "bold", "underline"))
            self.result_label.place(relx=0.5, rely=0.5, anchor = 'center')
        if(MyGame.Dcount >= 2):
            if(MyGame.Dcount == 3):
                self.result_label = tk.Label(self.root, text="YOU DREW THE SERIES!", height = 10, width = 80, bg="grey", fg="#333132", font=("fixedsys", 100, "bold", "underline"))
                self.result_label.place(relx=0.5, rely=0.5, anchor = 'center')
            elif(MyGame.Wcount > 0):
                self.result_label = tk.Label(self.root, text="YOU WON THE SERIES!", height = 10, width = 80, bg="#37f543", fg="white", font=("fixedsys", 100, "bold", "underline"))
                self.result_label.place(relx=0.5, rely=0.5, anchor = 'center')
            elif(MyGame.Lcount > 0):
                self.result_label = tk.Label(self.root, text="YOU LOST THE SERIES!", height = 10, width = 80, bg="#ff2400", fg="black", font=("fixedsys", 100, "bold", "underline"))
                self.result_label.place(relx=0.5, rely=0.5, anchor = 'center')

        self.resetbutton = tk.Button(self.root, text="Reset", height=3, width=15, borderwidth=5, relief="raised", bg="red", fg="white", font=("fixedsys", 25, "bold"), command=self.reset)
        self.resetbutton.place(relx=0.5, rely=0.8, anchor="center")
    
    def reset(self):
        print("Resetting")
        MyGame.Wcount = 0
        MyGame.Lcount = 0
        MyGame.Dcount = 0
        MyGame.Rcount = 0
        
        if hasattr(self, 'newL'):
            self.newL.destroy()
        if hasattr(self, 'result_label'):
            self.result_label.destroy()
        if hasattr(self, 'resetbutton'):
            self.resetbutton.destroy()

        self.root.destroy()
        MyGame()
        
        
        


        

    


MyGame()