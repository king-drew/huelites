''' hueboi.py '''
import requests

from light import State
from light import Light


class Hueboi(object):

    def __init__(self, ip, userid):
        self.sesh = requests.Session()
        self.ip = ip
        self.userid = userid
        self._lights = []
        self.baseurl = f'http://{self.ip}/api/{self.userid}'

    def __repr__(self):
        return f'<Hueboi({self.userid})>'

    # @property
    # def baseurl(self):
    #     return f'http://{self.ip}/api/{self.userid}'

    def lights(self):
        if not self._lights:
            url = self.baseurl + '/lights'
            r = self.sesh.get(url)
            jason = r.json()
            for id_, data in jason.items():
                state = State(**data.pop('state'))
                data['type_'] = data.pop('type')
                l = Light(id_, state=state, **data, hueboi=self)
                self._lights.append(l)
        return self._lights

    def turnoff(self, lightid):
        url = self.baseurl + '/lights/'+ lightid + '/state'
        params = {'on': False}
        self.sesh.put(url, json=params)

    def turnon(self, lightid):
        url = self.baseurl + '/lights/'+ lightid + '/state'
        params = {'on': True}
        self.sesh.put(url, json=params)
