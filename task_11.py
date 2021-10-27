

class Dessert(object):
    def __init__(self, name = None, calories = None):
        self.name = name
        self.calories = calories

    def get_name(self):
        return self.name

    def get_calories(self):
        return self.calories

    def set_name(self, name):
        self.name = name

    def set_calories(self, calories):
        self.calories = calories

    def is_healthy(self):
        if type(self.calories) is not int:
            for x in self.calories:
                if x not in "1234567890":
                    return False
        if int(self.calories) < 200:
            return True
        else:
            return False

    def is_delicious(self):
        return True

dessert = Dessert("Boobba", "100")
print(dessert.is_healthy())