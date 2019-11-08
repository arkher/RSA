class Private_key:
    def __init__(self, d, n):
        self.__d = d
        self.__n = n

    def get_d(self):
        return self.__d

    def get_n(self):
        return self.__n