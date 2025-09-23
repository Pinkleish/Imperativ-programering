
# ...some people like to avoid these "early returns"
# Can we write equivalent code with a single return?

def concert_message(age, has_ticket):
    if age < 16:
        result = "You are too young to enter."
    elif has_ticket:
        result = "You can enter the concert!"
    else:
        result = "You need a ticket to enter."
    return result


print(concert_message(15, True))