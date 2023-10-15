from tkinter import *
count = 0

def count_plus():
    global count
    count += 1
    label.config(text=str(count))

def count_minus():
    global count
    count -=1
    label.config(text=str(count))


root = Tk()

label = Label(root, text = "0")
# 레이블을 화면에 배치
label.pack()

# count_plus 이벤트를 가지는 버튼 생성
button1 = Button(root, width=10, text="plus", overrelief="solid", command=count_plus)
button1.pack()

button2 = Button(root, width=10, text="minus", overrelief="solid", command=count_minus)
button2.pack()

# Tk 화면 호출
root.mainloop()