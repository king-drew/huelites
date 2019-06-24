from huescript import getlightstates
from huescript import getbridgeip
from huescript import getuserid
from hueboi import Hueboi
from light import State
from light import Light

if __name__ == "__main__":
    # jason = getlightstates()
    hb = Hueboi(getbridgeip(), getuserid())
    print(hb.baseurl)
    for l in hb.lights():
        if l.id == '1':
            l.flip()
            break
