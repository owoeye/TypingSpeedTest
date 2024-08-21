from tkinter import *
import random
import json


def key_pressed(event):
    if event.char == rightOfLabel.cget("text")[0]:
        # shift from right to left
        rightOfLabel.configure(text=rightOfLabel.cget("text")[1:])
        # shift from center to the right
        leftOfLabel.configure(text=leftOfLabel.cget("text") + event.char)
        # place next char in center
        currentOfLabel.configure(text=rightOfLabel.cget("text")[0])


def update_timer(time):
    time += 1
    if time <= 60:
        timerOfLabel.configure(text=f"Time: {time}s")
        typetest.after(1000, update_timer, time)
    else:
        stop()


def stop():
    # Count the rest of the words
    if "" in leftOfLabel.cget("text").split(" "):
        numOfWords = 0
    else:
        numOfWords = len(leftOfLabel.cget("text").split(" "))

    # hide widgets not in use
    rightOfLabel.place_forget()
    leftOfLabel.place_forget()
    timerOfLabel.place_forget()
    currentOfLabel.place_forget()

    # update result
    result.configure(text=f"Words per minute: {numOfWords}")
    result.place(relx=0.5, rely=0.3, anchor=CENTER)

    # Show button for reply
    retryButton.configure(text="Retry", command=restart)
    retryButton.place(relx=0.51, rely=0.7, anchor=CENTER)


def restart():
    # hide result widgets and retry button
    result.place_forget()
    retryButton.place_forget()

    # reset-up
    text = random.choice(story["short_stories"])["content"]

    leftOfLabel.configure(text=text[0:active_letter])
    leftOfLabel.place(relx=0.5, rely=0.5, anchor=E)

    rightOfLabel.configure(text=text[active_letter:])
    rightOfLabel.place(relx=0.5, rely=0.5, anchor=W)

    currentOfLabel.configure(text=text[active_letter])
    currentOfLabel.place(relx=0.51, rely=0.7, anchor=S)

    timerOfLabel.place(relx=0.5, rely=0.3, anchor=N)

    # reset timer
    time = 0
    update_timer(time)


# creating GUI
typetest = Tk()
typetest.title("Typing Speed Test")
typetest.config(bg="light blue")

# window size
typetest.geometry("800x600")

# Set default font for all widgets
typetest.option_add("*font", "helvetica 32 bold")

# Text to type
with open("stories.json") as stories:
    story = json.load(stories)
    text = random.choice(story["short_stories"])["content"]

# Active letter
active_letter = 0

# Letters typed that are moved tp the left
leftOfLabel = Label(typetest, text=text[0:active_letter], bg="light blue")
leftOfLabel.place(relx=0.5, rely=0.5, anchor=E)

# Letters typed that are moved tp the right
rightOfLabel = Label(typetest, text=text[active_letter:], bg="light blue", fg="grey")
rightOfLabel.place(relx=0.5, rely=0.5, anchor=W)

# Current Letter
currentOfLabel = Label(typetest, text=text[active_letter], bg="light blue")
currentOfLabel.place(relx=0.51, rely=0.7, anchor=S)

# Timer
time = 0
timerOfLabel = Label(typetest, text=f"Time: {time}s", bg="light blue")
timerOfLabel.place(relx=0.5, rely=0.3, anchor=N)

# bind key strokes to the GUI
typetest.bind("<Key>", key_pressed)

# after some time
typetest.after(1000, update_timer, time)

# create result
result = Label(typetest, bg="light blue")
result.pack_forget()

# create button
retryButton = Button(typetest)
retryButton.pack_forget()

typetest.mainloop()
