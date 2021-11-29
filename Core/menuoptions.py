from Core.APIhandler import APIhandler
from Core.ticketprint import printPage,printTicket

breakline = "-"*200

class ticketViewer:
    def __init__(self,subdomain,email,password, token=False):
        self.subdomain = subdomain
        self.email = email
        self.password = password
        self.api = APIhandler(subdomain,email,password,token)
    
    def viewAllTickets(self):
        currentpage = self.api.getPage(1)
        while True:
            printPage(currentpage)
            if currentpage['next_page']:
                print("N: Next Page")
            if currentpage['previous_page']:
                print("P: Previous Page")
            print("R: Return to Main Menu")
            selected = input("Select an option : ")
            print(breakline)
            if selected == "R": break
            if currentpage["next_page"] and selected == "N":
                currentpage = self.api.getJSON(currentpage['next_page'])
            elif currentpage["previous_page"] and selected == "P":
                currentpage = self.api.getJSON(currentpage['previous_page'])
            print()

    def viewTicket(self,id):
        ticket = self.api.getTicket(id)
        if ticket:
            print("\n\n")
            printTicket(ticket['ticket'])
        input("Press Enter to continue")
        print(breakline)

