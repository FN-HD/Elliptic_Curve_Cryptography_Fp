class Fp:
    def __init__(self, p):
        if 'internal_access' in dir(Fp):
            if Fp.internal_access:
                Fp.internal_access = False
            else:
                raise TypeError('you are wrong')
        else:
            raise TypeError('you are wrong')

        self.p = p

    @staticmethod
    def get_instance(p=2):
        if Fp.has_instance():
            return Fp.instance
        else:
            Fp.internal_access = True
            Fp.instance = Fp(p)
            return Fp.instance

    @staticmethod
    def has_instance():
        return 'instance' in dir(Fp)