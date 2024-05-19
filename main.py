from googletrans import Translator
from tkinter import * 
from tkinter import ttk,messagebox
import googletrans


def translate():
    global language
    try:
        txt=text1.get(1.0,END)
        c1=combo1.get()
        c2=combo2.get()
        if c1=='Auto Detect':
            c1='auto'
        if txt:
            translation=translator.translate(txt,src=c1,dest=c2)
            text2.delete(1.0,END)
            print(translation)
            text2.insert(END,translation.text)
    except Exception as e:
        messagebox.showerror(title="Error",message="Something went wrong.")

translator = Translator()
language=googletrans.LANGUAGES
lang_value1=list(language.values())
lang_value1.insert(0,"Auto Detect")
lang_value2=list(language.values())
lang1=language.keys()

window=Tk()
window.title("Translator")
window.minsize(height=450,width=700)
window.maxsize(height=450,width=700)

combo1=ttk.Combobox(window,values=lang_value1,state='r')
combo1.place(x=120,y=70)
combo1.set("choose a language")

f1=Frame(window,bg='black',bd=1)
f1.place(x=70,y=150,width=250,height=150)

text1=Text(f1,font="Roboto 14",bg='white',relief=GROOVE,wrap=WORD)
text1.place(x=0,y=0,width=250,height=150)


combo2=ttk.Combobox(window,values=lang_value2,state='r')
combo2.place(x=400,y=70)
combo2.set("choose a language")

f2=Frame(window,bg='black',bd=1)
f2.place(x=350,y=150,width=250,height=150)

text2=Text(f2,font="Roboto 14",bg='white',relief=GROOVE,wrap=WORD)
text2.place(x=0,y=0,width=250,height=150)

button = Button(text='Translate',font=('normal',15), bg='grey',command=translate)
button.place(x=275,y=350)

window.mainloop()
