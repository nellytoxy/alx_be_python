task = input("Enter your task: ")
priority=input("Priority (high/medium/low): ")
time_input=input("Is it time-bound? (yes/no): ")
match priority:
     case priority if priority == "high":
        if time_input == "yes":
          print(f"{task}, is a high priority task that requires immediate attention today!")
        else:
          print(f"{task}, is a high priority task but dot requires immediate attention today!")
match priority:
     case priority if priority == "medium":
        if time_input == "yes":
          print(f"{task}, is a medium priority task that requires attention today!")
        else:
          print(f"{task}, is a medium priority task but do not requires immediate attention today!")
match priority:
     case priority if priority == "low":
        if time_input == "yes":
          print(f"{task}, is a low priority task that requires attention before time!")
        else:
          print(f"{task}, is a low priority task Consider completing it when you have free time!")