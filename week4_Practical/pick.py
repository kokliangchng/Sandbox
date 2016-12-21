import random

ticket_length=6
ticket_min=1
ticket_max=44

def generateTicket():
    ticket=[]
    for i in range(ticket_length):
        toDraw=True
        while toDraw:
            num=random.randint(ticket_min,ticket_max+1)
            if num not in ticket:
                ticket.append(num)
                toDraw=False
    ticket.sort()
    return ticket

numberoftickets=int(input("Enter number of ticket to generate:"))

for i in range(numberoftickets):
    ticket=generateTicket()
    ticket_str=' '.join([str(x) for x in ticket])
    print(ticket_str)

