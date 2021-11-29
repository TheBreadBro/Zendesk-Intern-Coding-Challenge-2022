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


    def getPage(self, pageNum, pageSize = 25):
        url = self.domain + "/api/v2/tickets.json?page={page_num}&per_page={page_size}".format(page_num=pageNum, page_size=pageSize)
        json = self.getJSON(url)
        return json

    def getJSON(self, url):
        request = requests.get(url,auth=self.auth)
        if request.status_code<400:
            return request.json()
        else:
            self.check_error(request)
            return None

    def check_error(self, request):
        if request.status_code < 200 or request.status_code > 404:
            raise Exception("Request failed with code {code}".format(code=request.status_code))
        elif request.status_code == 401:
            raise Exception("Invalid Login")
        elif request.status_code == 403:
            raise Exception("Access Denied")
        elif request.status_code == 404:
            print("Ticket not Found")
