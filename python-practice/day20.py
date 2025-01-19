# Question: Day 20: Write a Python program to implement a simple rock-paper-scissors game against the computer.
import random

choices = ['rock', 'paper', 'scissors']
computer = random.choice(choices)
user = input("Choose (rock/paper/scissors): ").lower()

print(f"Computer chose: {computer}")
if user not in choices:
    print("Invalid choice!")
elif user == computer:
    print("Tie!")
elif (user == 'rock' and computer == 'scissors') or \
     (user == 'paper' and computer == 'rock') or \
     (user == 'scissors' and computer == 'paper'):
    print("You win!")
else:
    print("Computer wins!")
