from tkinter import *
from tkinter import messagebox
import pandas as pd
import random

df = pd.read_csv("manga.csv")

def generate_random_manga(selected_genre):
    genre_recommendations = df[df["genre"].notna() & df["genre"].str.contains(selected_genre)]
    
    if not genre_recommendations.empty and len(genre_recommendations) >= 5:
        if len(genre_recommendations) >= 5:
            random_manga = genre_recommendations.sample(5, replace=False)
            show_recommendations_window(selected_genre, random_manga)
        else:
            messagebox.showinfo("Insufficient Data", "Not enough unique manga available for recommendations in this genre.")
    else:
        messagebox.showinfo("Insufficient Data", "Not enough manga available for recommendations in this genre.")

def show_recommendations_window(selected_genre, recommendations):
    window = Toplevel()
    window.title(f"Recommendations for {selected_genre}")

    for index, row in recommendations.iterrows():
        manga = row  # Assign manga variable here
        button = Button(
            window,
            text=f"{row['name']} - {row['genre']}",
            font=("Comic sans", 12),
            bg="#4779c4",
            fg="white",
            command=lambda m=manga: show_details(m['genre'])
        )
        button.pack(pady=5)
        button.bind("<Button-1>", lambda event, m=manga: show_details(m['genre']))  # Add click event for each button

    # Center the window on the screen
    window.update_idletasks()
    width = window.winfo_width()
    height = window.winfo_height()
    x = (window.winfo_screenwidth() - width) // 2
    y = (window.winfo_screenheight() - height) // 2
    window.geometry(f"+{x}+{y}")

def show_details(selected_genre):
    genre_recommendations = df[df["genre"].notna() & df["genre"].str.contains(selected_genre)]
    
    if not genre_recommendations.empty:
        random_manga = genre_recommendations.sample(5)
        
        details_window = Toplevel()
        details_window.title(f"Related Recommendations based on ( {selected_genre} )")

        for index, row in random_manga.iterrows():
            button = Button(
                details_window,
                text=f"{row['name']} - {row['genre']}",
                font=("Comic sans", 12),
                bg="#4779c4",
                fg="white",
                command=lambda manga=row: show_details(manga['genre'])
            )
            button.pack(pady=5)

        # Center the window on the screen
        details_window.update_idletasks()
        width = details_window.winfo_width()
        height = details_window.winfo_height()
        x = (details_window.winfo_screenwidth() - width) // 2
        y = (details_window.winfo_screenheight() - height) // 2
        details_window.geometry(f"+{x}+{y}")
    else:
        messagebox.showinfo("No Recommendations", f"No related recommendations found for {selected_genre}")

def click_handler(genre):
    return lambda: generate_random_manga(genre)

window = Tk()
window.geometry("1200x720")  # Adjusted width
window.title("Onaji-Pon - Manga Recommendation System")

frame1 = Frame(window, width=300, highlightbackground="white", highlightthickness=3, background="#36454F")
frame1.grid(row=0, column=0, padx=30, pady=40, ipadx=0, ipady=0)

window.configure(bg="black") 

icon = PhotoImage(file=r'C:\Users\Regiel\Downloads\ih.png')
window.iconphoto(True, icon)

colour1 = '#020f12',
colour2 = '#4779c4',
colour3 = 'white',
colour4 = 'black',
colour5='#ea5252'

anime_genres = [
    "Action",
    "Adventure",
    "Fantasy",
    "Slice of Life",
    "Mystery",
    "Psychological",
    "Supernatural",
    "Thriller",
    "Magic",
    "Space"
]

buttons = []
for i, genre in enumerate(anime_genres, start=1):
    button = Button(
        frame1,
        text=f"{genre}",
        command=click_handler(genre),
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
    buttons.append(button)

# Pack the genre buttons with additional padding
for i, button in enumerate(buttons[:5]):
    button.grid(row=i, column=0, sticky="w", padx=30, pady=10)

for i, button in enumerate(buttons[5:]):
    button.grid(row=i, column=1, sticky="w", padx=30, pady=10)

# Add an image label under the genre buttons and let it span across multiple columns
image_label = Label(frame1, image=icon, bg="#36454F", height=500, width=500)
image_label.grid(row=1, column=2, rowspan=5, padx=20, pady=0)

window.mainloop()