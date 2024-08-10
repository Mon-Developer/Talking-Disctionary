from tkinter import*
import json
from difflib import get_close_matches
from tkinter import messagebox
import pyttsx3



engine=pyttsx3.init()#creating instance of engine class.

voice=engine.getProperty('voices')
engine.setProperty('voice',voice[0].id) #0 -is a male voice & 1 - is a female voice..

#get_close_matches(word,possibilities,n,cutoff)
#close_match=get_close_matches('apple',['ape','apple','app','ap','peach','puppy'],n=3,cutoff=0.6) #cutoff value=0.0 - 1.0
#print(close_match)






########Functionality Part
def search():
    data=json.load(open('data.json'))
    word=enterwordEntry.get()
    word.lower()
    word=word.lower()
    if word in data:
        meaning=data[word]
        print(meaning)
        text_area.delete(1.0,END)
        #text_area.insert(END,meaning)
        for item in meaning:
            text_area.insert(END,u'\u2022'+item+'\n\n')
    #else:
        #messagebox.showerror("Error","The word doesn't exit,please double check it")
        #enterwordEntry.delete(0,END)
       # text_area.delete(1.0,END)


    elif len(get_close_matches(word,data.keys()))>0:
        close_match=get_close_matches(word,data.keys())[0]
        #messagsbox.askysno('confim','Did you mean')
        #print(close_match)
        res=messagebox.askyesno("confirm",'Did you mean'+' '+ 'instead  ?')
        if res==True:
            enterwordEntry.delete(0,END)
            enterwordEntry.insert(END,close_match)

            meaning=data[close_match]
            for item in meaning:
                text_area.insert(END,u'\u2022'+item+'\n\n')
        else:
             
             messagebox.showerror("Error","The word doesn't exit,please double check it")
             enterwordEntry.delete(0,END)
             text_area.delete(1.0,END)
                
       

    else:
          messagebox.showinfo('informetion',"The word doesn't exist")
          enterwordEntry.delete(0,END)
          text_area.delete(1.0,END)
        
def clear():
    enterwordEntry.delete(0,END)
    text_area.delete(1.0,END)


def exit():
    res=messagebox.askyesno('confirm','Do you want to exit ?>') 
    if res==True:
        root.destroy()

    else:
        pass   
  

def wordaudio():
    engine.say(enterwordEntry.get())
    engine.runAndwait()


def meaningaudio():
    engine.say(text_area.get(1.0,END))
    engine.runAndwait()

########GUI Part
root=Tk()

root.geometry('900x626+100+30')
root.title("Talking Dictionary Created by Hosnehara")
root.resizable(True,True)

bg_image=PhotoImage(file='C:/Users/WELCOME PC/Desktop/talking disc/image/im3.png')
lbl=Label(image=bg_image).pack()
bg_label=Label(root,text="hello",font=('arial',20,'underline'),justify='left',bd=10,relief='groove',bg='gray')
bg_label.place(x=0,y=0)

enter_wordlabel=Label(root,text="Enter here",font=('castellar',20,'bold'),foreground='gray',bg='whitesmoke')
enter_wordlabel.place(x=530,y=20)

enterwordEntry=Entry(root,font=('arial',25,'bold'),justify='center',bd=8,relief='groove')
enterwordEntry.place(x=510,y=80)

search_image=PhotoImage(file='C:/Users/WELCOME PC/Desktop/talking disc/image/search.png')
#lbl=Label(image=search_image).pack()
search_Button=Button(root,image=search_image,bd=5,bg='whitesmoke',cursor='hand2',activebackground='gray',command=search)
search_Button.place(x=590,y=165)


micro_image=PhotoImage(file='C:/Users/WELCOME PC/Desktop/talking disc/image/microphone.png')
#lbl=Label(image=micro_image).pack()
micro_Button=Button(root,image=micro_image,bd=5,bg='whitesmoke',cursor='hand2',activebackground='skyblue',command=wordaudio)
micro_Button.place(x=750,y=160)



meaning_label=Label(root,text="Meaning",font=('castellar',20,'bold'),foreground='red3',bg='whitesmoke')
meaning_label.place(x=640,y=250)

text_area=Text(root,width=34,height=14,font=('arial',10,'italic'),bd=8,relief='groove')
text_area.place(x=605,y=281)


audio_image=PhotoImage(file='C:/Users/WELCOME PC/Desktop/talking disc/image/microphone.png')
audio_Button=Button(root,image=audio_image,bd=0,bg='silver',activebackground='red',cursor='hand2')
audio_Button.place(x=607,y=540)

audios_image=PhotoImage(file='C:/Users/WELCOME PC/Desktop/talking disc/image/button.png')
exit_Button=Button(root,image=audios_image,bd=0,bg='gold',activebackground='red',cursor='hand2',command=clear)
exit_Button.place(x=717,y=540)

audiom_image=PhotoImage(file='C:/Users/WELCOME PC/Desktop/talking disc/image/exit.png')
audio_Button=Button(root,image=audiom_image,bd=0,bg='blue',activebackground='red',cursor='hand2',command=exit)
audio_Button.place(x=829,y=540)

print("Hello")



def enter_function(even):
    search_Button.invoke()
    

root.bind('<Return>',enter_function)


root.mainloop()
