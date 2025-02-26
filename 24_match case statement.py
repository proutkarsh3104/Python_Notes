#Match_case statement(switch): An alternative to using many 'elif' statements
#                              Execute some code if a value matches a 'case'
#                              Benefits: Cleaner and syntax is more readable



def is_weekend(day):
    match day:
        case "saturday"| "sunday":
            return True
        case "monday"|"tuesday"|"Wednesday"|"thrusday"|"friday":
            return False
        case _:#same as else stament
            return False

print(is_weekend(input("enter the weekend")))