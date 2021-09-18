import sys
import requests
import threading

MAX_THREADS = 75

threadLock = threading.Lock()   # Establish a lock for global counter (and potential friends)

url = sys.argv[1] if len(sys.argv) > 1  else 'http://scanme.nmap.org/postmenot'
token = sys.argv[2] if len(sys.argv) > 2 else None

header =  {'Authorization': 'Bearer ' + token} if token else None

data = {
    'name': 'Bozo',   
}

def thread_request():
    while True:
        response = requests.post(url, json=data, headers=header).text
        print(response)
        with threadLock:
            threadexecutions += 1
       
threads = []
threadexecutions = 0

for i in range(MAX_THREADS):
    thread = threading.Thread(target=thread_request)
    thread.daemon = True
    threads.append(thread)

for i in range(MAX_THREADS):
    threads[i].start()

for i in range(MAX_THREADS):
    threads[i].join()
import sys
import requests
import threading

MAX_THREADS = 75

url = sys.argv[1] if len(sys.argv) > 1  else 'http://scanme.nmap.org/postmenot'
token = sys.argv[2] if len(sys.argv) > 2 else None

header =  {'Authorization': 'Bearer ' + token} if token else None

data = {
    'name': 'Bozo',   
}

def thread_request():
    while True:
        response = requests.post(url, json=data, headers=header).text
        print(response)
       
threads = []

for i in range(MAX_THREADS):
    thread = threading.Thread(target=thread_request)
    thread.daemon = True
    threads.append(thread)

for i in range(MAX_THREADS):
    threads[i].start()

for i in range(MAX_THREADS):
    threads[i].join()
