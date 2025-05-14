from tkinter import *
import pandas as pd
from random import choice

BACKGROUND_COLOR = "#B1DDC6"
CANVAS_HEIGHT = 526
CANVAS_WIDTH = 800
current_card = None
timer = None

# Reading the csv file
try:
    data = pd.read_csv("data/words_to_learn.csv")
except:
    data = pd.read_csv("data/french_words.csv")
finally:
    data_dict = data.to_dict(orient="records")


def flip_flash_card():

    global current_card

    flash_card.itemconfigure(flash_card_image, image=card_back_image)
    flash_card.itemconfigure(word_text, text=current_card["English"], fill="white")
    flash_card.itemconfigure(title_text, text="English", fill="white")


def update_flash_card():

    global current_card, timer
    
    try:
        current_card = choice(data_dict)
    except:
        root.mainloop()

    try:
        root.after_cancel(timer)
    except:
        pass

    flash_card.itemconfigure(flash_card_image, image=card_front_image)
    flash_card.itemconfigure(word_text, text=current_card["French"], fill="black")
    flash_card.itemconfigure(title_text, text="French", fill="black")
    
    timer = root.after(3000, flip_flash_card)


def update_data():

    data_dict.remove(current_card)
    print(len(data_dict))
    update_flash_card()


root = Tk()
root.title("Flash Card Application")
root.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

# image components that are going to be used in program later
card_front_image = PhotoImage(file = "images/card_front.png")
card_back_image = PhotoImage(file = "images/card_back.png")
tick_image = PhotoImage(file = "images/wrong.png")
cross_image = PhotoImage(file = "images/right.png")

# --------------------------------------- The main canvas screen ------------------------------

flash_card = Canvas(root, height=CANVAS_HEIGHT, width=CANVAS_WIDTH)
flash_card_image = flash_card.create_image(CANVAS_WIDTH//2, CANVAS_HEIGHT//2, image=card_front_image)
title_text = flash_card.create_text(400, 150, text="Title", font=("Arial", 60, "italic"))
word_text = flash_card.create_text(400, 263, text="Word", font=("Arial", 40, "bold"))
flash_card.config(background=BACKGROUND_COLOR, highlightthickness=0)
flash_card.grid(row=0, column=0, columnspan=2)

# ----------------------------------------------------------------------------------------------


# ------------------------------------ The remaining buttons ---------------------------------

tick_button = Button(root, image=tick_image, highlightthickness=0, height=50, width=50, command=update_data)
tick_button.grid(row=1, column=0)

cross_button = Button(root, image=cross_image, highlightthickness=0, height=50, width=50, command=update_flash_card)
cross_button.grid(row=1, column=1, pady=10)

# ------------------------------------------------------------------------------------------------

update_flash_card()
timer = root.after(3000, flip_flash_card)

root.mainloop()

data_dataframe = pd.DataFrame(data_dict)
data_dataframe.to_csv("data/words_to_learn.csv", index=False)