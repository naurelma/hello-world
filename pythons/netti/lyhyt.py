from time import sleep
from winsound import Beep
from time import ctime

try:
    import httplib
except:
    import http.client as httplib

def have_internet():
    conn = httplib.HTTPConnection("www.google.com", timeout=5)
    try:
        conn.request("HEAD", "/")
        conn.close()
        return True
    except:
        conn.close()
        return False
		
if __name__ == "__main__":
    t = input("ääni?")
    last = None
    print(have_internet())
    while True:
        sleep(2)
        new = have_internet()
        if last != new:
            if t == "y":
                Beep(250,2000)
            print(new,ctime()[11:-5])
        last = new
		
