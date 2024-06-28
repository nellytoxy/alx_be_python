task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ")
time_bound = input("Is it time-bound? (yes/no): ")
match priority:
     case priority if priority == "high":
        match time_bound:
            case time_bound if time_bound== "yes":
                print(task, "is a high priority task that requires immediate attention today!")
            
            case time_bound if time_bound == "no":
                print(task, "is a high priority task but dot requires immediate attention today!")
match priority:
     case priority if priority == "medium":
        match time_bound:
            case time_bound if time_bound== "yes":
                print(task, "t is a medium priority task that requires your attention today!")
            
            case time_bound if time_bound == "no":
                print(task, "is a medium priority task but do not requires your attention today!")
match priority:
     case priority if priority == "low":
        match time_bound:
            case time_bound if time_bound == "yes":
                print(task, " is a low priority that is time bound. Consider completing it before time.!")
            
            case time_bound if time_bound == "no":
                print(task, "is a low priority task Consider completing it when you have free time.!")