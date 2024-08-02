class GlobalMap:
    my_dict = {}

    def set(self, key, value):
        self.my_dict[key] = value

    def get(self, key):
        return self.my_dict[key]

    def delete(self, key):
        self.my_dict.pop(key)