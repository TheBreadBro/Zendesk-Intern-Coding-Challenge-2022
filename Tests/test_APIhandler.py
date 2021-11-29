import sys
import os

from requests import check_compatibility

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

from Core.APIhandler import APIhandler
import unittest
from unittest.mock import patch, Mock
import requests

#Sample test tickets
tickets = [
            {
                "id" : 1,
                "status" : "open",
                "requester_id": 1,
                "assignee_id": 5,
                "subject": "velit eiusmod reprehenderit officia cupidatat",
                "description": "Aute ex sunt culpa ex ea esse sint cupidatat aliqua ex consequat sit reprehenderit. Velit labore proident quis culpa ad duis adipisicing laboris voluptate velit incididunt minim consequat nulla. Laboris adipisicing reprehenderit minim tempor officia ullamco occaecat ut laborum.\n\nAliquip velit adipisicing exercitation irure aliqua qui. Commodo eu laborum cillum nostrud eu. Mollit duis qui non ea deserunt est est et officia ut excepteur Lorem pariatur deserunt.",
                "tags": [
                    "est",
                    "nisi",
                    "incididunt"
                    ]
            },
            {
                "id" : 2,
                "status" : "open",
                "requester_id": 2,
                "assignee_id": 8,
                "subject": "excepteur laborum ex occaecat Lorem",
                "description": "Exercitation amet in laborum minim. Nulla et veniam laboris dolore fugiat aliqua et sit mollit. Dolor proident nulla mollit culpa in officia pariatur officia magna eu commodo duis.\n\nAliqua reprehenderit aute qui voluptate dolor deserunt enim aute tempor ad dolor fugiat. Mollit aliquip elit aliqua eiusmod. Ex et anim non exercitation consequat elit dolore excepteur. Aliqua reprehenderit non culpa sit consequat cupidatat elit.",
                "tags": [
                    "labore",
                    "voluptate",
                    "amet"
                    ]
            },
            {
                "id" : 3,
                "status" : "open",
                "requester_id": 3,
                "assignee_id": 10,
                "subject": "ad sunt qui aute ullamco",
                "description": "Sunt incididunt officia proident elit anim ullamco reprehenderit ut. Aliqua sint amet aliquip cillum minim magna consequat excepteur fugiat exercitation est exercitation. Adipisicing occaecat nisi aliqua exercitation.\n\nAute Lorem aute tempor sunt mollit dolor in consequat non cillum irure reprehenderit. Nulla deserunt qui aliquip officia duis incididunt et est velit nulla irure in fugiat in. Deserunt proident est in dolore culpa mollit exercitation ea anim consequat incididunt. Mollit et occaecat ullamco ut id incididunt laboris occaecat qui.",
                "tags": [
                    "laborum",
                    "mollit",
                    "proident"
                    ]
            },
        ]

class TestAPIhandler(unittest.TestCase):

    def setUp(self):
        self.api = APIhandler("test","test@gmail.com","pass")
    

    def test_init(self):
        self.assertEqual("https://test.zendesk.com",self.api.domain)
        self.assertEqual("test@gmail.com",self.api.email)
        self.assertEqual("pass",self.api.password)
    @patch('requests.get')

    def test_getTicket(self,mock_get):
        mock_get.return_value = Mock()
        mock_get.return_value.json.return_value = tickets[1]
        mock_get.return_value.status_code = 300
        response = self.api.getTicket(2)
        self.assertEqual(response,tickets[1])

    


    @patch('requests.get')

    def test_check_error(self, mock_get):
        
        mock_get.return_value.status_code = 500
        response = requests.get("")
        self.assertRaises(Exception,self.api.check_error,response)

        mock_get.return_value.status_code = 401
        response = requests.get("")
        self.assertRaises(Exception,self.api.check_error,response)

        mock_get.return_value.status_code = 403
        response = requests.get("")
        self.assertRaises(Exception,self.api.check_error,response)

        mock_get.return_value.status_code = 404
        response = requests.get("")
        self.assertRaises(Exception,self.api.check_error,response)


    @patch('requests.get')

    def test_getJSON(self, mock_get):
        mock_get.return_value.status_code = 300
        mock_get.return_value.json.return_value = tickets[1]
        self.assertEqual(tickets[1],self.api.getJSON(""))
        mock_get.return_value.status_code = 500
        self.assertRaises(Exception,self.api.getJSON,"")

    @patch('requests.get')

    def test_getPage(self,mock_get):
        mock_get.return_value.json.return_value = tickets
        mock_get.return_value.status_code = 300
        self.assertEqual(tickets,self.api.getPage(1))
        mock_get.return_value.status_code = 500
        self.assertRaises(Exception,self.api.getPage,1)

    
if __name__ == '__main__':
    unittest.main()