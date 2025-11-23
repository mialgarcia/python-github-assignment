# ---------------------------------------------
# Simple Study Hours Calculator Program
# ---------------------------------------------

# Task 1: Welcome message
print("Welcome to my Python program!")

# Task 2: Ask the user for input
hours = input("How many hours did you study today? ")

# Task 5: Error handling (must wrap conversion)
try:
    # Task 3: Convert input & perform calculation
    hours = float(hours)
    weekly_hours = hours * 7

    # Task 4: Display the result
    print(f"You are on track to study {weekly_hours} hours this week.")

except ValueError:
    print("Error: Please enter a valid number.")
    exit()

# End of program
# ---------------------------------------------
