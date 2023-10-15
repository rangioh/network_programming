from tkinter import *
# 메인 창 Tk instance 생성
root = Tk()

# 창 이름 설정
root.title("opt window")
# 창 크기 + 창 좌표 설정
root.geometry("300x200+300+300")
# 창 크기 변경 가능 여부
root.resizable(False, False)

# TK 화면 호출
root.mainloop()