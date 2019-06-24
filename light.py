
import weakref


class State:
    def __init__(self, alert, bri, colormode, ct,
            effect, hue, on, reachable, sat, xy):
        self.alert = alert
        self.bri = bri
        self.colormode = colormode
        self.ct = ct
        self.effect = effect
        self.hue = hue
        self.on = on
        self.reachable = reachable
        self.sat = sat
        self.xy = xy

    @property
    def state(self):
        if self.on:
            return 'On'
        else:
            return 'Off'

    def __iter__(self):
        yield 'alert', self.alert
        yield 'bri', self.bri
        yield 'colormode', self.colormode
        yield 'ct', self.ct
        yield 'effect', self.effect
        yield 'hue', self.hue
        yield 'on', self.on
        yield 'reachable', self.reachable
        yield 'sat', self.sat
        yield 'xy', self.xy

    def __repr__(self):
        return f'<State({self.state})>'



class Light:
    def __init__(self, id_, name, uniqueid, type_, modelid, manufacturername, swversion, state: State, hueboi=None):
        if hueboi is not None:
            self.hueboi = weakref.ref(hueboi)
            on_method = weakref.WeakMethod(hueboi.turnon)
            off_method = weakref.WeakMethod(hueboi.turnoff)
            self._off = off_method()
            self._on = on_method()
        else:
            self.hueboi = None
        self.id = id_
        self.name = name
        self.uniqueid = uniqueid
        self.type = type_
        self.modelid = modelid
        self.manufacturername = manufacturername
        self.swversion = swversion
        self.state = state

    @staticmethod
    def from_json(json):
        pass

    def __repr__(self):
        return f'<Light({self.id}, {self.name})>'

    def turnoff(self):
        self._off(self.id)
    
    def turnon(self):
        self._on(self.id)

    def flip(self):
        if self.state.on:
            self.turnoff()
        else:
            self.turnon()