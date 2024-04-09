from tkinter import *  # Importing the tkinter module
from tkinter import messagebox  # Importing messagebox for showing alerts

def count_word():  # Function to count words
    text = text_entry.get("1.0", END)  # Getting the text from the Text widget
    words = text.split()  # Splitting the text into words
    words_count = len(words)  # Counting the number of words
    word_count_label.config(text=f"Word Count: {words_count}")  # Updating the label with the word count

def clear_text():  # Function to clear the text area
    text_entry.delete("1.0", END)  # Deleting all text from the Text widget

app = Tk()  # Creating the tkinter application window
app.title("Word Counter")  # Setting the title of the window
app.geometry("500x420")  # Setting the dimensions of the window
app.config(pady=10, padx=10)  # Adding padding for aesthetics

app_title = Label(app, text="Word Counter", font=("nectar bold", 15))  # Title label
app_title.pack()  # Packing the title label

underline_label = Label(app, text="_______________", font=("nectar regular", 15))  # Underline for style
underline_label.pack()  # Packing the underline label

text_entry = Text(app, borderwidth=2, relief=GROOVE, width=40, height=12)  # Text widget for input
text_entry.pack(pady=15)  # Packing the text widget

word_count_label = Label(app, font=("aria", 12), fg="#212121")  # Label to display word count
word_count_label.pack(pady=20)  # Packing the word count label

count_button = Button(app, text="Count", font=("aria", 13), width=8, borderwidth=2, relief=GROOVE, command=count_word)  # Button to trigger word count
count_button.pack(side=LEFT, padx=97)  # Packing the count button

clear_button = Button(app, text="Clear", font=("aria", 13), width=8, borderwidth=2, relief=GROOVE, command=clear_text)  # Button to clear text
clear_button.pack(side=LEFT)  # Packing the clear button

app.mainloop()  # Running the tkinter event loop