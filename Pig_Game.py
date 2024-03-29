import random
import tkinter as tk
from tkinter import messagebox


class PigGame:
    def __init__(self, window):
        self.window = window
        window.geometry("900x600")
        window.title("Pig Game")
        self.total_score_p1 = 0
        self.total_score_p2 = 0
        self.turn_score_p1 = 0
        self.turn_score_p2 = 0

        label = tk.Label(self.window, text="Let's play a game of pig!", font=("Arial", 18))
        label.grid(column=2, row=0)

        roll_name = tk.Label(self.window, text="Roll:", font=("Arial", 18))
        roll_name.grid(row=2, column=0)

        dice_roll = ""
        self.roll_text = tk.Label(self.window, text=dice_roll, height=1, width=50, font=("Arial", 12))
        self.roll_text.grid(row=2, column=2, columnspan=2)

        #roll_button = tk.Button(self.window, text="Roll", font=("Arial", 12), command=self.roll_button_click)
        #roll_button.grid(row=3, column=2, padx=10, pady=10)

        #hold_button = tk.Button(self.window, text="Hold", font=("Arial", 12), command=self.hold_button_click)
        #hold_button.grid(row=3, column=3, padx=10, pady=10)

        turn_scorep1_label = tk.Label(self.window, text="Player 1 turn score:", font=("Arial", 12))
        turn_scorep1_label.grid(row=4, column=1)

        self.turn_scorep1 = tk.Label(self.window, text=self.turn_score_p1, height=1, width=30, font=("Arial", 12))
        self.turn_scorep1.grid(row=4, column=2)

        total_scorep1_label = tk.Label(self.window, text="Player 1 total score:", font=("Arial", 12))
        total_scorep1_label.grid(row=4, column=3)

        self.total_scorep1 = tk.Label(self.window, text=self.total_score_p1, height=1, width=30, font=("Arial", 12))
        self.total_scorep1.grid(row=4, column=4)

        turn_scorep2_label = tk.Label(self.window, text="Player 2 turn score:", font=("Arial", 12))
        turn_scorep2_label.grid(row=5, column=1)

        self.turn_scorep2 = tk.Label(self.window, text=self.turn_score_p2, height=1, width=30, font=("Arial", 12))
        self.turn_scorep2.grid(row=5, column=2)

        total_scorep2_label = tk.Label(self.window, text="Player 2 total score:", font=("Arial", 12))
        total_scorep2_label.grid(row=5, column=3)

        self.total_scorep2 = tk.Label(self.window, text=self.total_score_p2, height=1, width=30, font=("Arial", 12))
        self.total_scorep2.grid(row=5, column=4)

    def dice_roll(self):
        roll = random.randint(1, 6)
        return roll

    def player_choice(self, player_name):
        choice = messagebox.askquestion("Player Choice", f"{player_name} do you want to roll?")
        return choice

    def update_turn_scorep1(self, turn_score_p1):
        updated_text = turn_score_p1
        self.turn_scorep1.config(text=updated_text)
        root.update()
        

    def update_turn_scorep2(self, turn_score_p2):
        updated_text = turn_score_p2
        self.turn_scorep2.config(text=updated_text)
        root.update()
    

    def update_total_scorep1(self, total_score_p1):
        updated_text = total_score_p1
        self.total_scorep1.config(text=updated_text)
        root.update()
    

    def update_total_scorep2(self, total_score_p2):
        updated_text = total_score_p2
        self.total_scorep2.config(text=updated_text)
        root.update()
       
    def update_dice_roll(self, dice_roll):
        updated_text = "You rolled a", dice_roll, "."
        self.roll_text.config(text=updated_text)
        root.update()
  

    def player_turn(self):
        total_score_p1 = 0
        total_score_p2 = 0
        self.update_total_scorep1(total_score_p1)
        self.update_total_scorep2(total_score_p2)

        while total_score_p1 < 100 and total_score_p2 < 100:
            turn_score_p1 = 0
            current_score = total_score_p1

            while turn_score_p1 < 100:
                if self.player_choice("Player One") == "yes":
                    each_roll = self.dice_roll()
                    self.update_dice_roll(each_roll)
                    turn_score_p1 = turn_score_p1 + each_roll
                    self.update_turn_scorep1(turn_score_p1)

                    if each_roll == 1:
                        turn_score_p1 = 0
                        messagebox.showinfo("Oops...", "Pigged out!")
                        self.update_turn_scorep1(turn_score_p1)
                        self.update_total_scorep1(current_score)
                        break

                    elif total_score_p1 + turn_score_p1 >= 100:
                        total_score_p1 = total_score_p1 + turn_score_p1
                        self.update_turn_scorep1(turn_score_p1)
                        self.update_total_scorep1(total_score_p1)
                        messagebox.showinfo("Final", f"Final score: {total_score_p1} vs {total_score_p2}")
                        messagebox.showinfo("YAYYY!", "Player One wins!")
                        break

                else:
                    total_score_p1 = total_score_p1 + turn_score_p1
                    self.update_turn_scorep1(turn_score_p1)
                    self.update_total_scorep1(total_score_p1)
                    break

            if total_score_p1 + turn_score_p1 < 100:
                turn_score_p2 = 0
                current_score = total_score_p2

                while turn_score_p2 < 100:
                    if self.player_choice("Player Two") == "yes":
                        each_roll = self.dice_roll()
                        self.update_dice_roll(each_roll)
                        turn_score_p2 = turn_score_p2 + each_roll
                        self.update_turn_scorep2(turn_score_p2)

                        if each_roll == 1:
                            turn_score_p2 = 0
                            messagebox.showinfo("Oops...", "Pigged out!")
                            self.update_turn_scorep2(turn_score_p2)
                            self.update_total_scorep2(current_score)
                            break

                        elif total_score_p2 + turn_score_p2 >= 100:
                            total_score_p2 = total_score_p2 + turn_score_p2
                            self.update_turn_scorep2(turn_score_p2)
                            self.update_total_scorep2(total_score_p2)
                            messagebox.showinfo("Final", f"Final score: {total_score_p1} vs {total_score_p2}")
                            messagebox.showinfo("YAYYY!", "Player Two wins!")
                            break

                    else:
                        total_score_p2 = total_score_p2 + turn_score_p2
                        self.update_turn_scorep2(turn_score_p2)
                        self.update_total_scorep2(total_score_p2)
                        break


if __name__ == "__main__":
    root = tk.Tk()
    pig_game = PigGame(root)
    pig_game.player_turn()
    root.mainloop()
