from tkinter import *
import pandas
import random
BACKGROUND_COLOR = "#B1DDC6"
current_card= {}
data = pandas.read_csv("french_words.csv")
to_learn = data.to_dict(orient="records")
print(to_learn)




def next_card():
    global  current_card
    global flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    print(current_card["French"])
    canvas_front.itemconfig(card_title,text="French")
    canvas_front.itemconfig(card_word,text=current_card["French"])
    flip_timer=window.after(3000, func=flip_card)




def flip_card():
    canvas_front.itemconfig(card_title,text = "English")
    canvas_front.itemconfig(card_word, text=current_card["English"] )


def is_known():
    to_learn.remove(current_card)
    print(len(to_learn))
    next_card()



# -------------------------------- UI SETUP -------------------------------------- #

window = Tk()
window.title("FLASH CARD ")
window.config( bg = BACKGROUND_COLOR  )
window.config(padx = 50, pady = 50)
flip_timer = window.after(3000,func=flip_card)


canvas_front  = Canvas(width =800, height = 526, bg= BACKGROUND_COLOR, highlightthickness=0 )
card_front =PhotoImage(file ="card_front.png")
canvas_front.grid(column= 0 , row=0 , columnspan= 2)
canvas_front.create_image(400, 263 , image = card_front,)

card_title = canvas_front.create_text(400 , 150, text = "Title" , font= ("Ariel",40,"italic"))
card_word  = canvas_front.create_text(400,263,text= "word", font = ("Ariel",60,"bold"))



card_back = PhotoImage(file = "card_back.png")


right_button = PhotoImage(file="right.png")
button_r = Button(image=right_button, highlightthickness=0,command=next_card)
button_r.config(width =70, height = 70  )
button_r.config(padx= 20, pady = 20)
button_r.grid(column= 0, row=1 )


left_button = PhotoImage(file = "wrong.png")
button_l = Button(image = left_button, highlightthickness=0,bg=BACKGROUND_COLOR,command=is_known)
button_l.config(width =70, height = 70  )
button_l.config(padx = 20 , pady = 20)
button_l.grid(column=  1, row=1 )








next_card()












window.mainloop()


