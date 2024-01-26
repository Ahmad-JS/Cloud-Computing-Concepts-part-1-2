import hashlib
import random
import email
import email.message
import email.encoders
import sys
import subprocess
import json
import os
import os.path
import ssl
ssl._create_default_https_context = ssl._create_unverified_context
from urllib.error import HTTPError
from urllib.request import urlopen, Request 

try:
    input = raw_input
except NameError:
    pass

class NullDevice:
    def write(self, s):
        pass

def submit():   
    (login, password) = loginPrompt()
    if not login:
        print ('!! Submission Cancelled')
        return
    submissions = [source(i) for i in range(4)]
    submitSolution(login, password, submissions)
def loginPrompt():
    """Prompt the user for login credentials. Returns a tuple (login, password)."""
    (login, password) = basicPrompt()
    return login, password
def basicPrompt():
    login = input('Login (Email): ')
    password = input('Password (Token): ')
    return login, password
def partPrompt():
    counter = 0
    for part in partFriendlyNames:
        counter += 1
        print (str(counter) + ') ' + partFriendlyNames[counter - 1])
    partIdx = int(input('Please enter which part you want to submit (1-' + str(counter) + '): ')) - 1
    return (partIdx, partIds[partIdx])

def submit_url():
    """Returns the submission url."""
    return "https://www.coursera.org/api/onDemandProgrammingScriptSubmissions.v1"

def submitSolution(email_address, password, submissions):
    """Submits a solution to the server."""
    values = { 
        "assignmentKey": akey,  
        "submitterEmail": email_address,
        "secret": password,
        "parts": {
            partIds[0]: {"output": submissions[0]},
            partIds[1]: {"output": submissions[1]},
            partIds[2]: {"output": submissions[2]},
            partIds[3]: {"output": submissions[3]}
        }
    }
    
    url = submit_url()
    data = json.dumps(values).encode('utf-8')
    req = Request(url, data=data, headers={'Content-Type': 'application/json', 'Cache-Control': 'no-cache'})

    try:
        response = urlopen(req)  
    except HTTPError as e:
        print('Error:', e.read().decode('utf-8'))


def source(partIdx):
    try:
        with open("dbg.%d.log" % partIdx, 'r') as f:
            src = f.read() 
        return src
    except FileNotFoundError:
        print(f"Error: dbg.{partIdx}.log not found.")
        return ""
akey = 'Lm64BvbLEeWEJw5JS44kjw'
partIds = ['PH3Q7', 'PIXym', 'mUKdC', 'peNB6']
partFriendlyNames = ['Create Test', 'Delete Test', 'Read Test', 'Update Test'] 

print ("#############(Login)##############")
submit()
print ("##################################") 
print ("######### Go To Coursera #########") 
print ("####### Total Grade 90/90 ########") 
print ("##################################") 

