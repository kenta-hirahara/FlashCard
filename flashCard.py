import os
import webbrowser
import itertools

import tkinter as tk
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk

import numpy as np
import pandas as pd

class Application(tk.Frame):
    directory = '/Users/kentahirahara/code/python3/wordbook/'
    WIDTH, HEIGHT = 750, 500
    reqUrl = 'mkdictionaries:///?text='
    df_csv = pd.read_csv(f'{directory}word.csv', delimiter=',')
    row_num = len(df_csv)
    rand_row = [k for k, _ in itertools.groupby(np.random.randint(0, row_num, 2000))]
    count_space = 1
    count_arrow = 0
    gender_color = 'white'
    rand_jap = df_csv.iat[rand_row[0], 0]
    labelTextVariable = None
    label = None

    def __init__(self, master=None):
        super().__init__(master)
        os.chdir(self.directory)
        self.master.geometry(f"{Application.WIDTH}x{Application.HEIGHT}+400+50")
        self.master.title("Flash Card")
        self.icon_image = self.load_image("icons8-dictionary-50.png", 80, 80)
        self.create_widgets()

    def create_widgets(self): 
        self.button = ttk.Button(self.master, text=None, compound="none")
        self.label1 = ttk.Label(self.master, text=str(self.rand_jap), font=('MS Gothic', 80), foreground=self.gender_color)

        self.label1.pack(expand = True)

        # Bind the event to the main window
        self.master.bind('<KeyPress-space>', self.on_keypress_space)
        self.master.bind('<KeyPress-Return>', self.on_keypress_space)
        self.master.bind('<KeyPress-Right>', self.on_keypress_right_arrrow)
        self.master.bind('<KeyPress-Down>', self.on_keypress_right_arrrow)
        self.master.bind('<KeyPress-Left>', self.on_keypress_left_arrrow)
        self.master.bind('<KeyPress-Up>', self.on_keypress_left_arrrow)

        # self.button.bind('<ButtonPress>', self.on_buttonpress_dictionary)
        
    # def on_buttonpress_dictionary(self, event): #Button press launches the German dictionary and search the word
    #     webbrowser.open(f'{self.reqUrl}{self.rand_jap}', new=0, autoraise=True)

    def on_keypress_space(self, event):  # Corrected the method signature to include 'self'
        self.count_space += 1
        self.rand_jap = self.df_csv.iat[self.rand_row[self.count_arrow], self.count_space%2]
        self.label1['text'] = str(self.rand_jap)
        if self.count_space%2:
            self.label1['foreground'] = self.gender_switcher()
            self.button.pack()
        else:
            self.label1['foreground'] = 'white'
            self.button.pack_forget()

    def on_keypress_right_arrrow(self, event):
        self.count_arrow += 1
        self.rand_jap = self.df_csv.iat[self.rand_row[self.count_arrow], 0]
        self.label1['text'] = str(self.rand_jap)
        self.label1['foreground'] = 'white'
    
    def on_keypress_left_arrrow(self, event):
        self.count_arrow -= 1
        self.rand_jap = self.df_csv.iat[self.rand_row[self.count_arrow], 0]
        self.label1['text'] = str(self.rand_jap)
        self.label1['foreground'] = 'white'
    
    def gender_switcher(self):
        match self.df_csv.iat[self.rand_row[self.count_arrow], 2]:
            case 'r':
                return 'light sky blue'
            case 'e':
                return 'hot pink'
            case 's':
                return 'pale green'
            
    def load_image(self, file_path, width, height):
        img = Image.open(file_path)
        img = img.resize((width, height), Image.ANTIALIAS)
        return ImageTk.PhotoImage(img)


def main():
    root = tk.Tk()
    root.update() 
    app = Application(master=root)
    app.mainloop()

if __name__ == "__main__":
    main()
