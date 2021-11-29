# Zendesk Intern Coding Challenge 2022
 Created by Tommy Ton


## Program Requirements:

### Zendesk Account
- Sign up for a free trial [Zendesk](https://www.zendesk.com/register/#step-1) or use an existing account   
- Log in and go to settings(The gear) -> API(Under Channels) and turn on password access or token access   
   - If you turn on token access remember to note the token down as you will no longer be able to access it when you leave

### Installing Python and its modules
- Install Python 3.9 or higher(The version used to create this repo was Python 3.9.7 incase of bugs): https://www.python.org/downloads/
- Install the following python modules via command line:
```
pip install requests
pip install tabulate
```
### Cloning the repository
Clone the repository via command line
```
git clone https://github.com/TheBreadBro/Zendesk-Intern-Coding-Challenge-2022.git
```

## Running the Ticket Viewer
1. Navigate to the cloned repo
2. In the command line run:
```
python main.py
```
3. It will ask if you are using a token(earlier when we created a zendesk account)
   - Answer Y if you are using a token and anything else if you aren't
4. Enter your subdomain, email and password/token
5. You will then be taken to a self explanatory menu
6. Enjoy!

## Running the tests
1. Navigate to the cloned repo
2. Navigate to the Tests folder
This can be done like so:
```
cd tests
```
3. Run the test
```
test_APIhandler.py
```
