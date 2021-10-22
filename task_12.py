from task_11 import Dessert


class JellyBean(Dessert):

    def __init__(self, name = None, calories = None, flavour = None):
        super().__init__(name, calories)
        self.flavour = flavour
    
    def get_flavour(self):
        return self.flavour

    def set_flavour(self, flavour):
        self.flavour = flavour

    def is_delicious(self):
        if self.flavour != "black licorice":
            return True
        else:
            return False

dessert = JellyBean()