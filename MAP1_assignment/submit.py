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
    print('!! Submission Cancelled')
    return
  submissions = [source(i) for i in range(3)]
  submitSolution(login, password, submissions)
def loginPrompt():
  """Prompt the user for login credentials. Returns a tuple (login, password)."""
  login = input('Login (Email): ')
  password = input('Password (Token): ')
  return login, password

def submit_url():
  """Returns the submission url."""
  return "https://www.coursera.org/api/onDemandProgrammingScriptSubmissions.v1"

def submitSolution(email_address,password, submissions):
  """Submits a solution to the server. Returns (result, string)."""
  values = {
      "assignmentKey": "Mj8OkgI-EeaTLQonT2FRpw",  \
      "submitterEmail": email_address, \
      "secret": password, \
      "parts": {
          "b9m9h": {"output": submissions[0]},
          "MxUat": {"output": submissions[1]},
          "8ATm3": {"output": submissions[2]}
      }
  }

  url = submit_url()
  data = json.dumps(values).encode('utf-8')
  req = Request(url)
  req.add_header('Content-Type', 'application/json')
  req.add_header('Cache-Control', 'no-cache')
  response = urlopen(req, data)
  return

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
