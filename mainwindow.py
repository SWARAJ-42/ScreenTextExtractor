from tkinter import *
import extractor

while True:
    window = Tk()
    window.title("Windows Text Extractor")
    window.minsize(520, 90)
    window.maxsize(720, 90)
    window.config(background="#FFFFFF")
    label = Label(window,
                  text="Welcome to Text Extractor",
                  font=("Uroob", 20, 'bold'),
                  fg="Black",
                  bg="#FFFFFF",
                  compound="bottom"
                  )
    label.place(relx=.5, rely=.35, anchor="center")
    start_button = Button(window, text="Extract", command=extractor.extract, font=(
        "Uroob", 10), fg="black", bg="white", justify="center")
    start_button.place(relx=.5, rely=.75, anchor="center")
    window.mainloop()
