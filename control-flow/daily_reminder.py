task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

match priority:
    case "high":
        message = f"'{task}' is a high priority task"
    case "medium":
        message = f"'{task}' is a medium priority task"
    case "low":
        message = f"'{task}' is a low priority task"
    case _:
        message = f"'{task}' has an unknown priority level"

if time_bound == "yes":
    final_msg = f"{priority_msg} that requires immediate attention today!"
else:
    if priority in ["high", "medium", "low"]:
        final_msg = f"{priority_msg}. Consider completing it when you have free time."
    else:
        final_msg = priority_msg


print(f"Reminder: {final_msg}")