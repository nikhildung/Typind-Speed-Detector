from tkinter import *
import random
from timeit import default_timer as timer

root = Tk()
root.title("Typing Speed Detector ")
root.geometry("500x300")
root.configure(bg="black")



def Game():
    window = Tk()
    window.title("Typing Speed Detector ")
    window.geometry("1000x500")
    window.configure(bg="black")
    UserWord = StringVar()


    def Result():
        if text_Entry.get() == word:
            global res_label
            end = timer()
            res = end - start
            res_float = float(res)
            seconds = f"{res_float} Seconds"
            res_label = Label(window, text=seconds,bg="black",fg="#03fcf8",font="Times 20 bold")
            res_label.place(x=180, y=300)
            wpm = int(len(word) * 5 / res)
            wpm2 = f"{wpm} WPM"
            wpm_label = Label(window, text=wpm2, bg="black", fg="#03fcf8", font="Times 20 bold")
            wpm_label.place(x=580, y=300)


        else:
            res_label = Label(window, text="Wrong Spelling",bg="black",fg="#03fcf8",font="Times 20 bold")
            res_label.place(x=280, y=300)





    def TryAgain():

        Game()

    def Destroy():
        window.destroy()




    global words
    words = ["Python Project", "Java C Python Web", "Most Popular Language is Python", "We are Python Developers"]

    global word
    word = random.choice(words)

    global start
    start = timer()

    global word_Label
    word_Label = Label(window, text=word, font="Times 17 bold", bg="black",fg="white")
    word_Label.place(x=221, y=21)

    text_Label = Label(window, text="Enter Your Word Here", bg="#fcba03",font="Times 17 bold")
    text_Label.place(x=60, y=100)

    global text_Entry
    text_Entry = Entry(window, width=45, textvariable=UserWord, font="Times 17 bold")
    text_Entry.place(x=330, y=100)

    text_Button_Submit = Button(window, text="Result", font="Times 17 bold", command=Result, bg="#03fcf8")
    text_Button_Submit.place(x=100, y=200)

    text_Button_Again = Button(window, text="Try again?", font="Times 17 bold", command=TryAgain, bg="#03fcf8")
    text_Button_Again.place(x=230, y=200)

    text_Button_Exit = Button(window, text="Exit",font="Times 17 bold", command = Destroy,bg="#03fcf8")
    text_Button_Exit.place(x=400,y=200)





text1 = Label(root,text="Let's Test Your Typing Speed",font="Times 21 bold",bg="black",fg="White")
text1.pack()
text1.place(x=100,y=50)

Go_button = Button(root,text="GO!",font="Times 21 bold",bg="#fcba03",width=7,command=Game)
Go_button.pack()
Go_button.place(x= 190,y= 150)





root.mainloop()
