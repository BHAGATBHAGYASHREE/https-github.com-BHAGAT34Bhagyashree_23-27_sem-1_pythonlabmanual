class Grandfather:
    def __init__(self, attribute):
        self.attribute = attribute

    def displaygrandfatherattribute(self):
        print(f"Grandfather's Attribute: {self.attribute}")


class Father(Grandfather):
    def __init__(self, attribute, propertyfather):
        super().__init__(attribute)
        self.propertyfather = propertyfather

    def displayfatherproperty(self):
        print(f"Father's Property: {self.propertyfather}")


class Child(Father):
    def __init__(self, attribute, propertyfather, toy):
        super().__init__(attribute, propertyfather)
        self.toy = toy

    def displaychildtoy(self):
        print(f"Child's Toy: {self.toy}")


if __name__ == "__main__":
    grandfatherattribute = "Grandfather's Wisdom"
    fatherproperty = "Father's House"
    childtoy = "Child's Ball"

    childobject = Child(grandfatherattribute, fatherproperty, childtoy)

    childobject.displaygrandfatherattribute()
    childobject.displayfatherproperty()
    childobject.displaychildtoy()
