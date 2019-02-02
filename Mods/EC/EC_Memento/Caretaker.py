from Mods.EC.EC_Memento.Memento import Memento


class Caretaker:
    def __init__(self):
        if 'internal_access' in dir(Caretaker):
            if Caretaker.internal_access:
                Caretaker.internal_access = False
            else:
                raise TypeError('you are wrong')
        else:
            raise TypeError('you are wrong')

        self.map = {}

    def set(self, key, value):
        if isinstance(value, list):
            if key == '':
                key = str(len(self))

            self.map[key] = Memento(value)

    def __getattr__(self, item):
        if item in list(self.map.keys()):
            return map[item]
        else:
            raise AttributeError(item)

    def __getitem__(self, item):
        if isinstance(item, str):
            if item in self.map.keys():
                return self.map[item]
            else:
                raise KeyError()
        elif isinstance(item, int):
            l = list(self.map.keys())

            if str(item) in l:
                return self.map[str(item)]
            elif 0 <= item < len(l):
                return self.map[l[item]]
            else:
                raise KeyError()
        else:
            raise AttributeError(item)

    def __len__(self):
        return len(self.map)

    # The following functions are singleton methods.
    # We can get instance.
    # We cannot use default constructor.
    @staticmethod
    def get_instance():
        if Caretaker.has_instance():
            return Caretaker.instance
        else:
            Caretaker.internal_access = True
            Caretaker.instance = Caretaker()
            return Caretaker.instance

    # Whether Ec is created.
    @staticmethod
    def has_instance():
        return 'instance' in dir(Caretaker)
