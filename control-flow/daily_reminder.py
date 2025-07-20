# daily_reminder.py

task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Define the message based on priority using match-case
match priority:
    case "high":
        priority_msg = f"The task '{task}' is HIGH priority"
    case "medium":
        priority_msg = f"The task '{task}' is MEDIUM priority"
    case "low":
        priority_msg = f"The task '{task}' is LOW priority"
    case _:
        priority_msg = f"The task '{task}' has an UNKNOWN priority"

# Final message depending on whether it's time-bound
if time_bound == "yes":
    final_msg = f"{priority_msg} that requires immediate attention today!"
else:
    final_msg = f"{priority_msg}. Plan accordingly."

print(final_msg)
