from tkinter import *

def click1():
    print("Shonen")

def click2():
    print("Horror")
    
def click3():
    print("Comedy")

def click4():
    print("Manhwa")
    
def click5():
    print("Romance")
    
    
def click6():
    print("Romance")
    
     
def click7():
    print("Romance")

 
def click8():
    print("Romance")
     
def click9():
    print("Romance")

 
def click10():
    print("Romance")



window = Tk()
window.geometry("600x420")
window.title("On aji-Pon")

frame1 = Frame(window, width=90, highlightbackground="white", highlightthickness=3, background="#36454F")
frame1.grid(row=0, column=0, padx=20, pady=25, ipadx=0, ipady=0)

window.configure(bg="black") 

icon = PhotoImage(file=r'logo.png')
window.iconphoto(True, icon)

colour1 = '#020f12',
colour2 = '#4779c4',
colour3 = 'white',
colour4 = 'black',
colour5='#ea5252'

button1 = Button(
    frame1,
    text="Shonen",
    command=click1,
    font=("Comic sans", 15),
    fg=colour4,
    bg=colour2,
    activebackground=colour3,
    activeforeground=colour4,
    highlightthickness=2,
    highlightbackground=colour2,
    highlightcolor="white",
    border=5,
    cursor='hand1',
    height=2,
    width=20,
)
button2 = Button(
    frame1,
    text="Horror",
    command=click2,
    font=("Comic sans", 15),
    fg=colour4,
    bg=colour2,
    activebackground=colour3,
    activeforeground=colour4,
    highlightthickness=2,
    highlightbackground=colour2,
    highlightcolor="white",
    border=5,
    cursor='hand1',
    height=2,
    width=20,
   
)
button3 = Button(
    frame1,
    text="Comedy",
    command=click3,
  font=("Comic sans", 15),
    fg=colour4,
    bg=colour2,
    activebackground=colour3,
    activeforeground=colour4,
    highlightthickness=2,
    highlightbackground=colour2,
    highlightcolor="white",
    border=5,
    cursor='hand1',
    height=2,
    width=20,
)
button4 = Button(
    frame1,
    text="Manhwa",
    command=click4,
   font=("Comic sans", 15),
    fg=colour4,
    bg=colour2,
    activebackground=colour3,
    activeforeground=colour4,
    highlightthickness=2,
    highlightbackground=colour2,
    highlightcolor="white",
    border=5,
    cursor='hand1',
    height=2,
    width=20,
)
button5 = Button(
    frame1,
    text="Romance",
    command=click2,
   font=("Comic sans", 15),
    fg=colour4,
    bg=colour2,
    activebackground=colour3,
    activeforeground=colour4,
    highlightthickness=2,
    highlightbackground=colour2,
    highlightcolor="white",
    border=5,
    cursor='hand1',
    height=2,
    width=20,
)

button6 = Button(
    frame1,
    text="Action / Adventure",
    command=click6,
   font=("Comic sans", 15),
    fg=colour4,
    bg=colour5,
    activebackground=colour3,
    activeforeground=colour4,
    highlightthickness=2,
    highlightbackground=colour2,
    highlightcolor="white",
    border=5,
    cursor='hand1',
    height=2,
    width=20,
)

button7 = Button(
    frame1,
    text="Drama",
    command=click7,
 font=("Comic sans", 15),
    fg=colour4,
    bg=colour5,
    activebackground=colour3,
    activeforeground=colour4,
    highlightthickness=2,
    highlightbackground=colour2,
    highlightcolor="white",
    border=5,
    cursor='hand1',
    height=2,
    width=20,
)

button8 = Button(
    frame1,
    text="Martial Arts",
    command=click8,
   font=("Comic sans", 15),
    fg=colour4,
    bg=colour5,
    activebackground=colour3,
    activeforeground=colour4,
    highlightthickness=2,
    highlightbackground=colour2,
    highlightcolor="white",
    border=5,
    cursor='hand1',
    height=2,
    width=20,
)

button9 = Button(
    frame1,
    text="Sports",
    command=click9,
   font=("Comic sans", 15),
    fg=colour4,
    bg=colour5,
    activebackground=colour3,
    activeforeground=colour4,
    highlightthickness=2,
    highlightbackground=colour2,
    highlightcolor="white",
    border=5,
    cursor='hand1',
    height=2,
    width=20,
)

button10 = Button(
    frame1,
    text="Tragedy",
    command=click10,
   font=("Comic sans", 15),
    fg=colour4,
    bg=colour5,
    activebackground=colour3,
    activeforeground=colour4,
    highlightthickness=2,
    highlightbackground=colour2,
    highlightcolor="white",
    border=5,
    cursor='hand1',
    height=2,
    width=20,
)

# Pack the buttons to the top-left corner with padding to the left and bottom
button1.grid(row=0, column=0, sticky="w", padx=30, pady=10)
button2.grid(row=1, column=0, sticky="w", padx=30, pady=10)
button3.grid(row=2, column=0, sticky="w", padx=30, pady=10)
button4.grid(row=3, column=0, sticky="w", padx=30, pady=10)
button5.grid(row=4, column=0, sticky="w", padx=30, pady=10)
button6.grid(row=0, column=1, sticky="w", padx=30, pady=10)
button7.grid(row=1, column=1, sticky="w", padx=30, pady=10)
button8.grid(row=2, column=1, sticky="w", padx=30, pady=10)
button9.grid(row=3, column=1, sticky="w", padx=30, pady=10)
button10.grid(row=4, column=1, sticky="w", padx=30, pady=10)


# Add an image label under the buttons and let it span across multiple columns
image_label = Label(frame1, image=icon, bg="#36454F", height= 500,width=500)
image_label.grid(row=1, column=5, rowspan=5, padx=20, pady=0)

window.mainloop()