import requests

class APIhandler:
    def __init__(self, subdomain, email, password, token=False):
        self.domain = "https://{subdomain}.zendesk.com".format(subdomain=subdomain)
        self.email = email if not token else email + "/token"
        self.password = password
        self.auth = (self.email,self.password)
        self.sortedby="&sort_by=created_at&sort_order=desc"

    def getTicket(self,id):
        url = self.domain + "/api/v2/tickets/{id}.json".format(id=id)
        return self.getJSON(url)


    def getPage(self, pageNum, pageSize = 20):
        url = self.domain + "/api/v2/tickets.json?page={page_num}&per_page={page_size}".format(page_num=pageNum, page_size=pageSize)
        json = self.getJSON(url)
        if json: 
            return json
        else:
            return

    def getJSON(self, url):
        request = requests.get(url,auth=self.auth)
        if request.ok:
            return request.json()
        else:
            self.check_error(request)
            return None

    def check_error(self, request):
        if request.status_code < 200 or request.status_code > 404:
            print("Request failed with code {code}".format(code=request.status_code))
        elif request.status_code == 401:
            print("Invalid Login")
        elif request.status_code == 403:
            print("Access Denied")
        elif request.status_code == 404:
            print("Ticket not Found")
