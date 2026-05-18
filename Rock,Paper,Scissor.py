from tkinter import *
import random


def play():
    def enter():
        x = ["Rock", "Paper", "Scissor"]
        y = random.choice(x)

        label5 = Label(window1, text=f"I choose {y}...",
                       font=("Pacifico", 40, "bold", "italic"),
                       fg="#07097a", bg="#a3987a")
        label5.pack()

        if entry.get().capitalize() == "Rock" and y == "Scissor":
            label = Label(window1, text="You won...",
                          font=("Pacifico", 65, "italic"),
                          fg="#31e034", bg="#a3987a")
            label.pack()
        elif entry.get().capitalize() == "Paper" and y == "Rock":
            label = Label(window1, text="You won...",
                          font=("Pacifico", 65, "italic"),
                          fg="#31e034", bg="#a3987a")
            label.pack()
        elif entry.get().capitalize() == "Scissor" and y == "Paper":
            label = Label(window1, text="You won...",
                          font=("Pacifico", 65, "italic"),
                          fg="#31e034", bg="#a3987a")
            label.pack()
        elif entry.get().capitalize() == y:
            label = Label(window1, text="It's a tie...",
                          font=("Pacifico", 65, "italic"),
                          fg="#31e034", bg="#a3987a")
            label.pack()
        else:
            label = Label(window1, text="You lose...",
                          font=("Pacifico", 65, "italic"),
                          fg="#31e034", bg="#a3987a")
            label.pack()

    window1 = Tk()

    window1.geometry("1250x680")
    window1.title("Incredible games")
    window1.config(bg="#a3987a")

    label4 = Label(window1, text="You choose...",
                   font=("Pacifico", 40, "bold", "italic"),
                   fg="#07097a", bg="#a3987a")
    entry = Entry(window1, font=("Roboto", 30), fg="White", bg="Black")
    button1 = Button(window1, text="ENTER", font=("Roboto", 25), bd=10, command=enter)

    label4.pack()
    entry.pack()
    button1.pack()


window = Tk()

window.geometry("1250x680")
window.title("Incredible games")
window.config(bg="#a3987a")

label1 = Label(window, text="Rock, Paper and Scissors", font=("Pacifico", 50, "bold", "italic"), fg="#07097a",
               bg="#a3987a")
label2 = Label(window,
               text="Remember Rock always cut Scissors,\nPaper always cut Rock and\nScissor always cut Paper...",
               font=("Pacifico", 35, "italic"),
               fg="#07097a", bg="#a3987a")
label3 = Label(window, text="First you choose then I",
               font=("Pacifico", 35, "italic"),
               fg="#31e034", bg="#a3987a")
button = Button(window, text="PLAY", font=("Roboto", 30, "bold"), bd=20, command=play)

label1.pack()
label2.pack()
label3.pack()
button.pack()
window.mainloop()
