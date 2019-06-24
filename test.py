from huescript import getlightstates
from light import State
from light import Light

if __name__ == "__main__":
    jason = getlightstates()
    for id_, data in jason.items():
        state = State(**data.pop('state'))
        data['type_'] = data.pop('type')
        l = Light(id_, state=state, **data)
        print(l.id, l.name)
