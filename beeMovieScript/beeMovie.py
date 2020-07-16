import time 

movieScript = open("movieScript.txt","r")
for e in movieScript.readlines():
    time.sleep(1)
    print(e)