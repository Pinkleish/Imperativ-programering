
# We can use multiple return statement in a function.

def concert_message(age, has_ticket):
    if age < 16:
        return "You are too young to enter."
    elif has_ticket:
        return "You can enter the concert!"
    else:
        return "You need a ticket to enter."


print(concert_message(15, True))