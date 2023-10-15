from tkinter import *

def calc(event):
    label.config(text="계산결과 : " + str(eval(entry.get())))

root = Tk()
label = Label(root, text="0")
label.pack()

entry = Entry(root, width=30)
# entry 이벤트 부여
entry.bind("<Return>", calc)
entry.pack()

root.mainloop()