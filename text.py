from tkinter import *

while True:
    window = Tk()
    window.title("Windows Text Extractor")
    window.minsize(820, 580)
    window.config(background="#FFFFFF")
    label = Label(window,
                  text="Extracted text",
                  font=("Uroob", 20, 'bold'),
                  fg="Black",
                  bg="#FFFFFF",
                  compound="bottom"
                  )
    label.place(relx=.5, rely=.10, anchor="center")
    frame = Frame(window, bg='white', bd=5)
    frame.place(relx=0.5, rely=0.15, relwidth=0.75, relheight=.7, anchor='n')
    label_pass_file = Label(frame, font=("Uroob", 20),
                            text=f'{ir.extract_text()}', bg="white", fg="black")
    label_pass_file.place(relwidth=.5, relheight=.1,
                          relx=.5, rely=.5, anchor="center")
    window.mainloop()
