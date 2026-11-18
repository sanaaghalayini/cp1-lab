
class Airlock:
    def __init__(self, code):
        self.code = code.strip()
        self.__sealed = False

    def is_sealed(self):
        return self.__sealed

    def lock_bolts(self):
        print("Bolts locked.")

    def unlock_bolts(self):
        print("Bolts unlocked.")

    def seal(self):
        if self.__sealed:
            print("Already sealed.")
        else:
            self.lock_bolts()
            self.__sealed = True
            print("Airlock sealed.")

    def unseal(self):
        if not self.__sealed:
            print("Already open.")
        else:
            self.unlock_bolts()
            self.__sealed = False
            print("Airlock open.")

    def __str__(self):
        if self.__sealed:
            return f"Airlock {self.code}: sealed"
        else:
            return f"Airlock {self.code}: open"
