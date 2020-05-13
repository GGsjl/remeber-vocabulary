import tkinter as tk
from tkinter import messagebox

window = tk.Tk()
window.geometry('500x300')
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

show = []
def Get():
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

l = tk.Label(window, textvariable=eng, bg='green', font=('Arial', 12), width=15, height=2)
l.pack()

def check(msg):
    if msg == cnt[show[4]]:
        messagebox.showinfo(title='提示', message='选择正确！')
        cnt.pop(show[4])
        update()
    else:
        messagebox.showinfo(title='提示', message='选择错误！')

b1 = tk.Button(window, text=c1, font=('Arial', 12), width=30, height=1, command=lambda:check(show[0]))
b1.pack(side=tk.TOP, pady=10)
b2 = tk.Button(window, text=c2, font=('Arial', 12), width=30, height=1, command=lambda:check(show[1]))
b2.pack(side=tk.TOP, pady=10)
b3 = tk.Button(window, text=c3, font=('Arial', 12), width=30, height=1, command=lambda:check(show[2]))
b3.pack(side=tk.TOP, pady=10)
b4 = tk.Button(window, text=c4, font=('Arial', 12), width=30, height=1, command=lambda:check(show[3]))
b4.pack(side=tk.TOP, pady=10)


def update():
    Get()
    eng.set(show[4])
    b1.config(text=show[0])
    b2.config(text=show[1])
    b3.config(text=show[2])
    b4.config(text=show[3])
    

def del_v():
    f = messagebox.askyesno(title='提示', message='是否删除此单词')
    if f:
        cnt.pop(show[4])
        update()

d = tk.Button(window, text='del', bg='red', font=('Arial', 12), width=5, height=200, command=del_v)
d.pack(side=tk.LEFT, fill=tk.Y)

def Quit():
    f = tk.messagebox.askokcancel('提示', '真的要退出吗？')
    if f:
        try:
            with open(r'1.txt', 'w') as f:
                for key in cnt.keys():
                    f.write(key + ' ' + cnt[key])
                    f.write('\n')
            window.destroy()
        except:
            print('wrong')

q = tk.Button(window, text='Quit', bg='red', font=('Arial', 12), width=5, height=200, command=Quit)
q.pack(side=tk.RIGHT, fill=tk.Y)

window.mainloop()
