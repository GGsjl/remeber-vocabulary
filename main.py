import tkinter as tk
from tkinter import messagebox

bg_color = '#ffa72b'
btn_color = '#3efe54'

window = tk.Tk()
window.geometry('389x318')
window['bg']=bg_color
window.title('vocabulary')
window.resizable(0,0)


def read():
    cnt = {}
    try:
        with open(r'1.txt', 'r') as f:
            for line in f.readlines():
                line = line.strip('\n')
                line = line.split()
                cnt[line[0]] = line[1]
        return cnt
    except:
        print('wrong')


cnt = read()
wrong = {}
show = []

def Get():#获取展示的英语单词和四个汉语意思
    global show
    show.clear()
    rec = ""
    i = 0
    for key in cnt:
        if(i == 0):
            rec = key
        show.append(cnt[key])
        if i == 3:
            show = sorted(show, reverse=True)
            show.append(rec)
            break
        i += 1

Get()
eng = tk.StringVar(value=show[4])
c1 = tk.StringVar();c1 = show[0]
c2 = tk.StringVar();c2 = show[1]
c3 = tk.StringVar();c3 = show[2]
c4 = tk.StringVar();c4 = show[3]

l = tk.Label(window, textvariable=eng, bg=bg_color, fg='black', font=('Arial', 12), width=15, height=2)
l.grid(row=0, column=1, pady=5)

def check(msg):#用于检测用户是否选择正确
    if msg != cnt[show[4]]:
        messagebox.showinfo(title='提示', message='选择错误！已帮你加入复习队列')
        wrong[show[4]] = cnt[show[4]]
    else:
        global rev_check
        if rev_check:
            wrong[show[4]] = cnt[show[4]]
        cnt.pop(show[4])
        update()


b1 = tk.Button(window, relief=tk.GROOVE, text=c1, bg=bg_color, activebackground='#08ffc8', font=('Arial', 12), width=30, height=1, command=lambda:check(show[0]))
b1.grid(row=1, column=1, pady=5)
b2 = tk.Button(window, relief=tk.GROOVE, text=c2, bg=bg_color, activebackground='#08ffc8', font=('Arial', 12), width=30, height=1, command=lambda:check(show[1]))
b2.grid(row=2, column=1, pady=5)
b3 = tk.Button(window, relief=tk.GROOVE, text=c3, bg=bg_color, activebackground='#08ffc8', font=('Arial', 12), width=30, height=1, command=lambda:check(show[2]))
b3.grid(row=3, column=1, pady=5)
b4 = tk.Button(window, relief=tk.GROOVE, text=c4, bg=bg_color, activebackground='#08ffc8', font=('Arial', 12), width=30, height=1, command=lambda:check(show[3]))
b4.grid(row=4, column=1, pady=5)

rev_check = tk.IntVar()
rev_check = False
def rev_click():
    global rev_check
    rev_check = not rev_check

rev = tk.Checkbutton(window, text='是否还需复习该单词', bg=bg_color, command=rev_click)
rev.grid(row=5, column=1, pady=20)

def update():#更新show数组
    Get()
    eng.set(show[4])
    b1.config(text=show[0])
    b2.config(text=show[1])
    b3.config(text=show[2])
    b4.config(text=show[3])
    

def del_v():#删除某个单词
    f = messagebox.askyesno(title='提示', message='是否删除此单词')
    if f:
        cnt.pop(show[4])
        update()

d = tk.Button(window, relief=tk.GROOVE, text='del', bg=btn_color, activebackground='#f6003c', font=('Arial', 12), width=5, height=1, command=del_v)
d.grid(row=6, column=0)

def Quit():#退出该程序
    f = tk.messagebox.askokcancel('提示', '真的要退出吗？')
    if f:
        try:
            wrong.update(cnt)
            with open(r'1.txt', 'w') as f:
                for key in wrong.keys():
                    f.write(key + ' ' + wrong[key])
                    f.write('\n')
            window.destroy()
        except:
            print('wrong')

q = tk.Button(window, relief=tk.GROOVE, text='Quit', bg=btn_color, activebackground='#f6003c', font=('Arial', 12), width=5, height=1, command=Quit)
q.grid(row=6, column=5)

window.mainloop()
