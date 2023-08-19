from tkinter import *
import snakegame as snakegame
import pong as ponggame
import blackjack as blackjackgame
import stateguesser as stategame
import crosstheroad as crossgame

def play_crossgame():
    crossgame.cross()

def play_stategame():
    stategame.guesser()

def play_blackjack():
    blackjackgame.play()
def play_snake():
    snakegame.run_snake()

def play_pong():
    ponggame.run_pong()

root = Tk()
root.title("Arcade")


button_snake = Button(root, text="Play Snake", command=play_snake)
button_snake.grid(row=0, column=0)

button_pong = Button(root, text="Play Pong", command=play_pong)
button_pong.grid(row=0,column=1)

button_blackjack = Button(root, text="Play Blackjack", command=play_blackjack)
button_blackjack.grid(row=0, column=2)

button_stategame = Button(root, text="Play U.S. State Guesser", command=play_stategame)
button_stategame.grid(row=0, column=3)

button_road = Button(root, text="Play Cross The Road", command=play_crossgame)
button_road.grid(row=0, column=4)

root.mainloop()
