import tkinter as tk
import random

options = []

def add_option():
    new_option = new_option_entry.get()
    if new_option.strip() != "":
        if len(options) < 10:
            options.append(new_option)
            options_listbox.insert(tk.END, new_option)
            max_players_label.configure(text=f"Max players: {len(options)}/10")
        else:
            max_players_label.configure(text="MAXIMO DE 10 JOGADORES")
        new_option_entry.delete(0, tk.END)

def add_option_with_enter(event=None):
    add_option()

def remove_option():
    selected_option = options_listbox.get(options_listbox.curselection())
    options.remove(selected_option)
    options_listbox.delete(options_listbox.curselection())
    max_players_label.configure(text=f"Max players: {len(options)}/10")

def draw_options():
    selected_options = random.sample(options, 10)
    team1_listbox.delete(0, tk.END)
    team2_listbox.delete(0, tk.END)
    for i, option in enumerate(selected_options):
        if i < 5:
            team1_listbox.insert(tk.END, option)
        else:
            team2_listbox.insert(tk.END, option)

def countdown(count):
    if count > 0:
        draw_button.configure(text=str(count))
        root.after(1000, countdown, count-1)
    else:
        draw_button.configure(text="SORTEAR")
        draw_options()

# Create the GUI
root = tk.Tk()
root.geometry("500x700")
root.title("MIX by edz")

options_label = tk.Label(root, text="JOGADORES:")
options_label.pack()

options_listbox = tk.Listbox(root)
for option in options:
    options_listbox.insert(tk.END, option)
options_listbox.pack()

remove_option_button = tk.Button(root, text="REMOVER", command=remove_option)
remove_option_button.pack()

new_option_frame = tk.Frame(root)
new_option_label = tk.Label(new_option_frame, text="JOGADOR:")
new_option_label.pack(side=tk.LEFT)
new_option_entry = tk.Entry(new_option_frame)
new_option_entry.pack(side=tk.LEFT)
add_option_button = tk.Button(new_option_frame, text="Add", command=add_option)
add_option_button.pack(side=tk.LEFT)
new_option_frame.pack()

max_players_label = tk.Label(root, text="MAX PLAYERS: 0/10")
max_players_label.pack()

draw_button = tk.Button(root, text="SORTEAR", command=lambda: countdown(3))
draw_button.pack()

team1_label = tk.Label(root, text="TEAM 1:")
team1_label.pack()

team1_listbox = tk.Listbox(root)
team1_listbox.pack()

team2_label = tk.Label(root, text="TEAM 2:")
team2_label.pack()

team2_listbox = tk.Listbox(root)
team2_listbox.pack()

# Bind the "Return" or "Enter" key to the add_option_with_enter function
new_option_entry.bind("<Return>", add_option_with_enter)

root.mainloop()
