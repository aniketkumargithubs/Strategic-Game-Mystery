import tkinter as tk
from tkinter import simpledialog
import random

class PuzzleGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Puzzle Mystery Game")
        self.energy = 10
        self.time = 10
        self.clues = []
        
        # Puzzle pool: Each puzzle has a corresponding answer
        self.puzzles = [
            {"question": "What has keys but can't open locks?", "answer": "piano"},
            {"question": "I speak without a mouth and hear without ears. What am I?", "answer": "echo"},
            {"question": "The more of this there is, the less you see. What is it?", "answer": "darkness"},
            {"question": "What is always in front of you but can’t be seen?", "answer": "future"},
            {"question": "What runs but never walks, has a mouth but never talks?", "answer": "river"},
            {"question": "What gets wetter as it dries?", "answer": "towel"},
            {"question": "I am not alive, but I grow; I don’t have lungs, but I need air. What am I?", "answer": "fire"},
            {"question": "I’m tall when I’m young, and I’m short when I’m old. What am I?", "answer": "candle"},
            {"question": "What can you hold in your right hand, but never in your left?", "answer": "left hand"},
            {"question": "The more you take, the more you leave behind. What am I?", "answer": "footsteps"},
        ]

        # Location pool
        self.locations = ["Library", "Garden", "Study Room", "Kitchen"]

        # Create and display the game text area
        self.text_area = tk.Text(root, height=15, width=50, wrap=tk.WORD, state=tk.NORMAL)
        self.text_area.pack(pady=10)

        # Create buttons for actions
        self.action_button = tk.Button(root, text="Choose an action", command=self.show_choices)
        self.action_button.pack(pady=5)

        # Insert welcome message
        self.location = random.choice(self.locations)
        self.display_text(f"Welcome to the Puzzle Mystery Game!\nYou are in the {self.location}.\n")
        self.update_status()

    def display_text(self, message):
        """Display a message in the text area and scroll to the end."""
        self.text_area.insert(tk.END, message)
        self.text_area.see(tk.END)
        self.root.update_idletasks()

    def update_status(self):
        """Update and display the player's status (location, time, energy)."""
        status = f"\nLocation: {self.location}\nTime: {self.time}\nEnergy: {self.energy}\n"
        self.display_text(status)

    def show_choices(self):
        """Present the player with available choices (find clue, change location)."""
        self.display_text("\nChoose an action:\n")
        self.display_text("1. Look for clues\n")
        self.display_text("2. Change location\n")
        self.display_text("3. Add a new location\n")

        # Ask the player for a choice
        choice = simpledialog.askinteger("Choose Action", "Enter the number of your action (1, 2, or 3):")
        if choice == 1:
            self.find_clue()
        elif choice == 2:
            self.change_location()
        elif choice == 3:
            self.add_location()
        else:
            self.display_text("Invalid choice! Please try again.\n")
            self.show_choices()

    def find_clue(self):
        """Randomly select a puzzle from the pool and present it to the player."""
        puzzle = random.choice(self.puzzles)  # Randomly pick a puzzle
        self.display_text(f"You found a puzzle: {puzzle['question']}\n")
        answer = simpledialog.askstring("Puzzle", "Your answer:")

        if answer and answer.lower() == puzzle['answer']:
            self.display_text("Correct! You've solved the puzzle.\n")
            self.clues.append(f"Clue: {puzzle['question']}")
            self.energy -= 2
            self.time -= 1
        else:
            self.display_text("Incorrect answer! Try again.\n")
        
        self.update_status()
        self.show_choices()

    def change_location(self):
        """Allow the player to change locations from the available options."""
        self.display_text("\nWhere would you like to go?\n")
        for idx, loc in enumerate(self.locations, start=1):
            self.display_text(f"{idx}. {loc}\n")

        new_location = simpledialog.askinteger("Change Location", f"Enter the number of the location (1 to {len(self.locations)}):")
        if new_location and 1 <= new_location <= len(self.locations):
            self.location = self.locations[new_location - 1]
            self.display_text(f"You moved to the {self.location}.\n")
        else:
            self.display_text("Invalid location! Please try again.\n")
            self.change_location()

        self.update_status()
        self.show_choices()

    def add_location(self):
        """Allow the player to add a new location dynamically."""
        new_location = simpledialog.askstring("Add Location", "Enter the name of the new location:")
        if new_location:
            self.locations.append(new_location)
            self.display_text(f"New location '{new_location}' added!\n")
        else:
            self.display_text("Location not added. Try again.\n")
        
        self.update_status()
        self.show_choices()

# Create the tkinter root window
root = tk.Tk()

# Create the game instance
game = PuzzleGame(root)

# Start the tkinter main loop
root.mainloop()
