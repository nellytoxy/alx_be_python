task = input("Enter your task: ")
priority=input("Priority (high/medium/low): ")
match priority:
     case priority if priority == "high":
        time_input=input("Is it time-bound? (yes/no): ")
        match time_input:
            case time_input if time_input== "yes":
                print(task, "is a high priority task that requires immediate attention today!")
            
            case time_input if time_input == "no":
                print(task, "is a high priority task but dot requires immediate attention today!")
match priority:
     case priority if priority == "medium":
        time_input=input("Is it time-bound? (yes/no)")
        match time_input:
            case time_input if time_input== "yes":
                print(task, "t is a medium priority task that requires your attention today!")
            
            case time_input if time_input == "no":
                print(task, "is a medium priority task but do not requires your attention today!")
match priority:
     case priority if priority == "low":
        time_input=input("Is it time-bound? (yes/no)")
        match time_input:
            case time_input if time_input == "yes":
                print(task, " is a low priority that is time bound. Consider completing it before time.!")
            
            case time_input if time_input == "no":
                print(task, "is a low priority task Consider completing it when you have free time.!")