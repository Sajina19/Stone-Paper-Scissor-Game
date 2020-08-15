import random
import tkinter

stats = []


def get_winner(call):
    if random.random() <= (1 / 3):
        throw = "stone"
    elif (1 / 3) < random.random() <= (2 / 3):
        throw = "scissors"
    else:
        throw = "paper"

    if (throw == "stone" and call == "paper") or (throw == "paper" and call == "scissors") \
            or (throw == "scissors" and call == "stone"):
        stats.append('W')
        result = "You won!"
    elif throw == call:
        stats.append('D')
        result = "It's a draw"
    else:
        stats.append('L')
        result = "You lost!"

    global output
    output.config(text="Computer did: " + throw + "\n" + result)


def pass_s():
    get_winner("scissors")


def pass_r():
    get_winner("stone")


def pass_p():
    get_winner("paper")


window = tkinter.Tk()

scissors = tkinter.Button(window, text="Scissors", bg="#ff9999", padx=10, pady=5, command=pass_s, width=20)
stone = tkinter.Button(window, text="Stone", bg="#80ff80", padx=10, pady=5, command=pass_r, width=20)
paper = tkinter.Button(window, text="Paper", bg="#3399ff", padx=10, pady=5, command=pass_p, width=20)
output = tkinter.Label(window, width=20, fg="red", text="What's your call?")

scissors.pack(side="left")
stone.pack(side="left")
paper.pack(side="left")
output.pack(side="right")
window.mainloop()

for i in stats: print(i, end=" ")
if stats.count('L') > stats.count('W'):
    result = "\nYou loose the series."
elif stats.count('L') == stats.count('W'):
    result = "\nSeries ended in a draw."
else:
    result = "\nYou win the series."

print(result)
