from Core.menuoptions import ticketViewer


def main():
    token = input("\n Are you using a token?(Enter Y for yes)")
    domain = input("\n Enter the Subdomain : ")
    email = input("\n Enter the E-mail : ")
    password = input("\n Enter the Token : ") if token == "Y" else input("\n Enter the Password : ")
    if token == "Y":
        viewer = ticketViewer(domain,email,password,True)
    else:
        viewer = ticketViewer(domain,email,password,False)


    print("Welcome to the Zendesk Ticket Viewer!")
    while True:
        print(  "\n 1: View all tickets \n",
                "2: View a ticket(by ID) \n",
                "3: Quit")
        selected = input("Select an option : ")
        if selected == '1':
            viewer.viewAllTickets()
        elif selected == '2':
            id = input("Input in an id : ")
            viewer.viewTicket(id)
        elif selected == '3':
            print("Thank you for using Zendesk Ticket Viewer!")
            break
        else:
            print("Please input in a valid option")
    


if __name__ == "__main__":
    main()