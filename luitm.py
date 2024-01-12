class LU:
    def __init__(self, luvalue):
        self.luvalue = luvalue

    def displaylu(self):
        print(f"LU Value: {self.luvalue}")


class ITM:
    def __init__(self, itmvalue):
        self.itmvalue = itmvalue

    def displayitm(self):
        print(f"ITM Value: {self.itmvalue}")


class DerivedClass(LU, ITM):
    def __init__(self, luvalue, itmvalue, derivedvalue):
        LU.__init__(self, luvalue)
        ITM.__init__(self, itmvalue)
        self.derivedvalue = derivedvalue

    def displayderived(self):
        print(f"Derived Value: {self.derivedvalue}")


if __name__ == "__main__":
    derived_object = DerivedClass(luvalue=10, itmvalue=20, derivedvalue=30)
    derived_object.displaylu()
    derived_object.displayitm()
    derived_object.displayderived()
