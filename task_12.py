from task_11 import Dessert


class JellyBean(Dessert):

    def __init__(self, name, calories, flavour):
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

x = JellyBean("Bobba", 200, "tasty")
print(x.get_name())
print(x.get_calories())
print(x.is_healthy())
print(x.get_flavour())
print(x.is_delicious())