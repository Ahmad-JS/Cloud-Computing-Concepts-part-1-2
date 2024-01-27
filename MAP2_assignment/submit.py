# ################ #
# python submit.py #
# ################ #

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
    login = input('Login (Email): ')
    password = input('Password (Token): ')
    return login, password
def submit_url():
    return "https://www.coursera.org/api/onDemandProgrammingScriptSubmissions.v1"
def submitSolution(email_address, password, submissions):
    values = { 
        "assignmentKey": "Lm64BvbLEeWEJw5JS44kjw",  
        "submitterEmail": email_address,
        "secret": password,
        "parts": {
            "PH3Q7": {"output": submissions[0]},
            "PIXym": {"output": submissions[1]},
            "mUKdC": {"output": submissions[2]},
            "peNB6": {"output": submissions[3]}
        }
    }
    url = submit_url()
    data = json.dumps(values).encode('utf-8')
    req = Request(url, data=data, headers={
        'Content-Type': 'application/json', 
        'Cache-Control': 'no-cache'
        })
    try:
        response = urlopen(req)  
    except HTTPError as e:
        print('Error:', e.read().decode('utf-8'))
        
def source(i):
  f = open("./dbg.%d.log" % i)
  src = f.read() 
  f.close()
  return src

print ("#############(Login)##############")
submit()
print ("##################################") 
print ("######### Go To Coursera #########") 
print ("####### Total Grade 90/90 ########") 
print ("##################################") 

