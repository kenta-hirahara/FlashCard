import os
import itertools

import tkinter as tk
from tkinter import *
# from tkinter import ttk

import numpy as np
import pandas as pd

class Application(tk.Frame):
    WIDTH, HEIGHT = 600, 400
    df_csv = pd.read_csv('/Users/kentahirahara/code/python3/wordbook/word.csv', delimiter=',')
    print(df_csv)
    row_num = len(df_csv)
    rand_row = [k for k, _ in itertools.groupby(np.random.randint(0, row_num, 2000))]
    count_space = 1
    count_arrow = 0
    rand_jap = df_csv.iat[rand_row[0], 0]
    labelTextVariable = None
    label = None

    def __init__(self, master=None):
        super().__init__(master)
        self.master.geometry(f"{Application.WIDTH}x{Application.HEIGHT}+800+50")
        self.master.title("Flash Card")
        self.create_widgets()
        print(self.count_space)

    def create_widgets(self): 
        self.label1 = tk.Label(self.master, text=str(self.rand_jap), font=('MS Gothic', 100))
        # self.word = ttk.Label(self.master, text=self.rand_jap, font=('MS UI GOthic', 50), relief='flat')

        self.label1.grid(column=0, row=0)
        # self.word.grid(column=0, row=2)

        # Bind the event to the main window
        self.master.bind('<KeyPress-space>', self.on_keypress_space)
        self.master.bind('<KeyPress-Right>', self.on_keypress_right_arrrow)
        self.master.bind('<KeyPress-Down>', self.on_keypress_right_arrrow)
        self.master.bind('<KeyPress-Left>', self.on_keypress_left_arrrow)
        self.master.bind('<KeyPress-Up>', self.on_keypress_left_arrrow)

    def on_keypress_space(self, event):  # Corrected the method signature to include 'self'
        self.count_space += 1
        self.rand_jap = self.df_csv.iat[self.rand_row[self.count_arrow], self.count_space%2]
        self.label1['text'] = str(self.rand_jap)

    def on_keypress_right_arrrow(self, event):
        self.count_arrow += 1
        self.rand_jap = self.df_csv.iat[self.rand_row[self.count_arrow], 0]
        self.label1['text'] = str(self.rand_jap)
    
    def on_keypress_left_arrrow(self, event):
        self.count_arrow -= 1
        self.rand_jap = self.df_csv.iat[self.rand_row[self.count_arrow], 0]
        self.label1['text'] = str(self.rand_jap)

def main():
    os.chdir('/Users/kentahirahara/code/python3/wordbook')
    print(os.getcwd())
    root = tk.Tk()
    root.resizable(width=False, height=False)
    app = Application(master=root)
    print(app.rand_jap)
    app.mainloop()

if __name__ == "__main__":
    main()
