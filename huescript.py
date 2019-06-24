#!/usr/bin/env python

import requests,time,json,arrow

userid = "3cf76ab42349b4ef221220dc9b1a257"
bridgeip = "192.168.1.239"

def getbridgeip():
    pass

def getuserid():
    pass

def geturl(bridgeip, userid):
    return("http://"+bridgeip+"/api/"+userid)

def getlightstates():
    r = requests.get(url+'/lights')
    return(r.json())

def setlightstate(lightid,on=None,bri=None,hue=None,sat=None,xy=None,ct=None,alert=None,effect=None,transitiontime=None,bri_inc=None,sat_inc=None,hue_inc=None,ct_inc=None,xy_inc=None):
    params = dict()
    if on is not None: # on = [True/False]
        params['on']=on
    if bri is not None: # bri = [0..255]
        params['bri']=bri
    if hue is not None:
        params['hue']=hue
    if sat is not None:
        params['sat']=sat
    if xy is not None:
        params['xy']=xy
    if ct is not None:
        params['ct']=ct
    if alert is not None:
        params['alert']=alert
    if effect is not None:
        params['effect']=effect
    if transitiontime is not None:
        params['transitiontime']=transitiontime
    if bri_inc is not None:
        params['bri_inc']=bri_inc
    if sat_inc is not None:
        params['sat_inc']=sat_inc
    if hue_inc is not None:
        params['hue_inc']=hue_inc
    if xy_inc is not None:
        params['xy_inc']=xy_inc
    if type(lightid) == int:
        r = requests.put(url+'/lights/'+str(lightid)+'/state',data=json.dumps(params))
    else:
        r = requests.put(url+'/lights/'+lightid+'/state',data=json.dumps(params))

def lighton(lightid):
    if type(lightid) == int:
        setlightstate(str(lightid),on=True)
    else:
        setlightstate(lightid,on=True)
    # requests.put(url+"/lights/1/state", data=json.dumps({"on":True,"bri":bri,"sat":0,"hue":25555}))

def lightoff(lightid):
    if type(lightid) == int:
        setlightstate(str(lightid),on=False)
    else:
        setlightstate(lightid,on=False)
    # requests.put(url+"/lights/1/state", data=json.dumps({"on":False}))

url = geturl(bridgeip, userid)
now = arrow.now()

def setall(on=None,bri=None,hue=None,sat=None,xy=None,ct=None,alert=None,effect=None,transitiontime=None,bri_inc=None,sat_inc=None,hue_inc=None,ct_inc=None,xy_inc=None):
    lights=['1','3','2']
    for x in lights:
        setlightstate(x,on=on,bri=bri,hue=hue,sat=sat,xy=xy,ct=ct,alert=alert,effect=effect,transitiontime=transitiontime,bri_inc=bri_inc,sat_inc=sat_inc,hue_inc=hue_inc,ct_inc=ct_inc,xy_inc=xy_inc)

if (now.hour==6 and now.minute==30):
    setall(sat=100,bri=1,on=True)
    time.sleep(5)
    setall(bri=255,transitiontime=600)
elif (now.hour == 7 and now.minute == 45):
    setall(on=False)
elif (now.hour == 17 and now.minute==00):
    setall(hue=14910,bri=254,sat=0,on=True)
elif (now.hour==20 and now.minute==00):
    setall(bri_inc=-54,sat_inc=50,transitiontime=50)
elif (now.hour == 20 and now.minute == 30):
    setall(bri=115,sat=200,transitiontime=50)
elif (now.hour==21 and now.minute==00):
    setall(bri_inc=-100,sat=225,transitiontime=20)
elif (now.hour==21 and now.minute==30):
    setall(on=False)
