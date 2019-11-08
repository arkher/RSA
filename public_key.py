class Public_key:
    def __init__(self, e, n):
        self.__e = e
        self.__n = n
    
    def get_e(self):
        return self.__e

    def get_n(self):
        return self.__n