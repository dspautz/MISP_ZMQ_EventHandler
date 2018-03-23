from .model import Model


class Sighting(Message):
    """The MISP Sighting Model"""

    def __init__(self):
        pass

    def from_json(self, json):
        sighting = Sighting()
        for key,value in json.items():
            setattr(event,key,value)

        return sighting

    def to_json(self):
        return json.dumps(self.__dict__)
