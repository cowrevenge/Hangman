import os
import random
from numpy import*
import tkinter as tk
import tkinter.ttk as ttk
import pygubu

PROJECT_PATH = os.path.abspath(os.path.dirname(__file__))
PROJECT_UI = os.path.join(PROJECT_PATH, "newproject")

words = {
    1: "doggie",
    2: "kitten",
    3: "horse",
}


def start_hang():
    random_number = random.randint(1, 3)
    secret_word = words[random_number]
    print(secret_word)


class HangmanApp:

    def __init__(self, master=None):
        # build ui
        self.frame1 = tk.Frame(master)
        self.hang_title = tk.Label(self.frame1)
        self.hang_title.configure(cursor='arrow', justify='center', text='Hangman!')
        self.hang_title.pack(fill='x', side='top')
        self.label2 = tk.Label(self.frame1)
        self.a1_png = tk.PhotoImage(file='hangman/1.png')
        self.label2.configure(image=self.a1_png, text='label2')
        self.label2.pack(side='left')
        self.text1 = tk.Text(self.frame1)
        self.text1.configure(height='10', setgrid='false', takefocus=False, width='50')
        _text_ = '''Welcome to Hangman!
You have 8 tries to guess the secret password.'''
        self.text1.insert('0.0', _text_)
        self.text1.pack(anchor='n', expand='false', side='top')
        entry1 = tk.Entry(self.frame1)
        _text_ = '''Enter your guess'''
        entry1.delete('0', 'end')
        entry1.insert('0', _text_)
        entry1.pack(anchor='center', pady='25', side='top')
        self.Guess = tk.Button(self.frame1)
        self.Guess.configure(text='Guess')
        self.Guess.pack(anchor='center', side='top')
        self.start_game = tk.Button(self.frame1)
        self.start_game.configure(text='Start Game', command=start_hang)
        self.start_game.pack(pady='25', side='top')
        self.frame1.configure(height='200', width='200')
        self.frame1.pack(side='top')

        # Main widget
        self.mainwindow = self.frame1

    def run(self):
        self.mainwindow.mainloop()


if __name__ == '__main__':
    root = tk.Tk()
    app = HangmanApp(root)
    app.run()

