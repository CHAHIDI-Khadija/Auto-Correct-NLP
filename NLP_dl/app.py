import tkinter as tk
from functions import *

root= tk.Tk()

canvas1 = tk.Canvas(root, width=400, height=300, relief='raised')
canvas1.pack()

title= tk.Label(root, text='Auto-Correct')
title.config(font=('helvetica', 14))
canvas1.create_window(200, 25, window=title)
description = "suggestions are sorted by their probabilies ,the first one is the word more probable to be"
desc_label=tk.Label(root,text=description,justify="left",font=('helvetica', 10, 'bold'),bg='orange', fg='black')
canvas1.create_window(200, 50, window=desc_label)

msg = tk.Label(root, text='Type your word:')
msg.config(font=('helvetica', 10))
canvas1.create_window(200, 100, window=msg)

input_box = tk.Entry(root) 
canvas1.create_window(200, 140, window=input_box)

def on_button_click():
    corrections=""
    word= input_box.get()
    label4 = tk.Label(root, text= corrections, font=('helvetica', 10, 'bold'))
    tmp_corrections = get_corrections(word, probs, vocab)
    for i, word_prob in enumerate(tmp_corrections):
        st = "\n word "+str(i)+" : "+str(word_prob[0])
        corrections+=st
     
    if corrections:
        label4.config(text='The corrections of {"' + word + '"} is:' + corrections)
    else:
        label4.config(text="No Suggestions found")
    canvas1.create_window(200, 230, window=label4)
    
button1 = tk.Button(text='Get the word corrections', command=on_button_click, bg='orange', fg='black', font=('helvetica', 9, 'bold'))
canvas1.create_window(200, 180, window=button1)

root.mainloop()

