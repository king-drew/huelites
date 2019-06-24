
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



class Light:
    def __init__(self, id_, name, uniqueid, type_, modelid, manufacturername, swversion, state: State):
        self.id = id_
        self.name = name
        self.uniqueid = uniqueid
        self.type = type_
        self.modelid = modelid
        self.manufacturername = manufacturername
        self.swversion = swversion
        self.state = state
