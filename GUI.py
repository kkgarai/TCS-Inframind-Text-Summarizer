from tkinter import *
from Summarizer import *

root = Tk()
root.geometry('600x750+150+0')
root.title("TEXT SUMMARIZER")

f1 = Frame(root)
f2 = Frame(root)
f3 = Frame(root)
f4 = Frame(root)

f1.pack()
f2.pack(pady=20)
f3.pack()
f4.pack(pady=10)


def fetch(url_box, txt):
    url = url_box.get()
    print(url)
    text = fetchText(url)
    # print(text)
    txt.insert("1.0", text)
    print(type(text))


def summary(txt):
    print('Summarize')
    text = txt.get("1.0", END)
    output = summarize(text)
    txt.insert("1.0", f"\t\t\t\tSUMMARY\n\n{output}")


def clear(url_box, txt):
    print('Clear')
    url_box.delete("0", END)
    txt.delete("1.0", END)


Label(f1,
      text='Enter the URL and click o fetch to fetch text from the URL or enter the text directly in the textbox below',
      font='aerial 12', anchor=CENTER, wraplength=500).pack(padx=10, pady=10)

url_box = Entry(f2, borderwidth=2, width=65)
url_box.pack(side=LEFT, ipady=6, ipadx=5)

txt = Text(f3, height=35, width=70)
scroll = Scrollbar(f3)

Button(f2, text='Fetch Text', command=lambda: fetch(url_box, txt)).pack(padx=10, ipady=3)

scroll.pack(side=RIGHT, fill=Y)
scroll.config(command=txt.yview)
txt.pack()

Button(f4, text='Generate Summary', borderwidth=3, command=lambda: summary(txt)).pack(side=LEFT, padx=20)
Button(f4, text="Clear All", borderwidth=3, command=lambda: clear(url_box, txt)).pack()

root.mainloop()
