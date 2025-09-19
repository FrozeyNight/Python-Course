# a match case statement is Python's switch

def dayOfWeek(day):
    match day:
        case 1:
            return "It's Sunday"
        case 2:
            return "It's Monday"
        case 3:
            return "It's Tuesday"
        case 4:
            return "It's Wednesday"
        case 5:
            return "It's Thursday"
        case 6:
            return "It's Friday"
        case 7:
            return "It's Saturday"
        case _: # Python's default case
            return f"{day} isn't a valid day"
        
print(dayOfWeek(3))
print(dayOfWeek("pizza"))