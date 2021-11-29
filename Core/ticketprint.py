from tabulate import tabulate
import textwrap


def printPage(page):
    tickets = []
    headers = ['id','subject','status','created_at','requester_id','group_id']
    for ticket in page['tickets']:
        row = []
        for header in headers:
            data = str(ticket[header])
            row.append(data[:47]+'...' if len(data)>50 else data)
        tickets.append(row)
    print()
    print(tabulate(tickets,headers,tablefmt="pipe"),"\n")

def printTicket(ticket):
    print("ID: ",ticket['id'])
    print("Status: ",ticket['status'])
    print("Priority: ",ticket['priority'])
    print("Created At: ",ticket['created_at'])
    print("Created By: ",ticket['requester_id'],"\n")
    print("Subject: ",textwrap.fill(ticket['subject'],width=100),"\n")
    print(textwrap.fill(ticket['description'],width=100))