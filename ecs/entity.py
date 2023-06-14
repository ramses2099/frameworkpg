import uuid

class Entity:
    def __init__(self) -> None:
        self.id = str(uuid.uuid4().fields[-1])[:5]
        self.components = {}

    def addcomponent(self, value):
        name = value.name
        self.components[name] = value

    def getcomponents(self):
        return self.components

    def getcomponent(self, name):
        return self.components.get(name)

    def removecomponent(self, name):
        self.components.pop(name)

    def getallkeys(self):
        return self.components.keys()

    def existscomponent(self, name):
        return self.components.setdefault(name)

    def printcomponents(self):
        comptype = self.getcomponent("Type")
        print(f"entity id {self.id}")
        if comptype is not None:
            print(f"entity type {comptype.typename}")
        for name in self.getallkeys():
            print(f"component name {name}")
