import tkinter as tk
import random
from tkinter import messagebox

computer_number = random.randint(1,20)
computer_label = None
last_guess_label = None
guess_count_label = None
result_label = None
Number_of_guess = 0

def show_num():
    messagebox.showwarning("Secret Number", f'The secret number is {computer_number}')


def gen_rand_num():
    global computer_label, computer_number, Number_of_guess
    computer_number = random.randint(1,20)
    Number_of_guess = 0
    
    if computer_label is None:
       computer_label = tk.Label(app, text='Computer chose a number')
       computer_label.pack(pady=10)
    else:
       computer_label.config(text='Computer chose a number')
    
    # Reset labels
    last_guess_label.config(text='Last guess: None')
    guess_count_label.config(text='Number of guesses: 0')
    result_label.config(text='')

def check_guess():
   global Number_of_guess, last_guess_label, guess_count_label, computer_number, result_label
   try:
       guess = int(user_entry.get())
       if 1 <= guess <= 20:
           Number_of_guess += 1
           
           if last_guess_label is None:
               last_guess_label = tk.Label(app, text=f'Last guess: {guess}')
               last_guess_label.pack(pady=5)
           else:
               last_guess_label.config(text=f'Last guess: {guess}')

           if guess_count_label is None:
               guess_count_label = tk.Label(app, text=f'Number of guesses: {Number_of_guess}')
               guess_count_label.pack(pady=5)
           else:
               guess_count_label.config(text=f'Number of guesses: {Number_of_guess}')

           if result_label is None:
               result_label = tk.Label(app, text='')
               result_label.pack(pady=5)

           user_entry.delete(0, tk.END)

           if guess < computer_number:
               result_label.config(text='Number is too small, please guess again')
           elif guess > computer_number:
               result_label.config(text='Number is too big, please guess again')
           else:
               result_label.config(text=f'Correct! You won in {Number_of_guess} guesses!')
               computer_number = random.randint(1,20)
               Number_of_guess = 0
               last_guess_label.config(text='Last guess: None')
               guess_count_label.config(text='Number of guesses: 0')

       else:
           messagebox.showwarning("Invalid Input", "Please enter a number between 1-20")
   except ValueError:
       messagebox.showwarning("Invalid Input", "Please enter a valid whole number")

def close_app():
   messagebox.showinfo('Goodbye', 'Thanks for playing!')
   app.destroy()

def on_enter(event):
   check_guess()

app = tk.Tk()
app.title('The Guessing Game')
app.geometry('400x400')

user_input_lbl = tk.Label(app, text="Enter a whole number between 1-20:", wraplength=350)
user_input_lbl.pack(pady=10)

user_entry = tk.Entry(app)
user_entry.pack(pady=10)
user_entry.bind('<Return>', on_enter)

try_guess_btn = tk.Button(app, text='Try this guess!', width=25, command=check_guess)
try_guess_btn.pack(pady=10)

result_label = tk.Label(app, text='')
result_label.pack(pady=5)

last_guess_label = tk.Label(app, text='Last guess: None')
last_guess_label.pack(pady=5)

guess_count_label = tk.Label(app, text='Number of guesses: 0')
guess_count_label.pack(pady=5)

generate_new_number_btn = tk.Button(app, text='Generate new number', width=25, command=gen_rand_num)
generate_new_number_btn.pack(pady=10)

show_num_btn = tk.Button(app, text='Show secret number', width=25, command=show_num)
show_num_btn.pack(pady=10)

exit_button = tk.Button(app, text='Close', width=25, command=close_app)
exit_button.pack(pady=10)

app.mainloop()