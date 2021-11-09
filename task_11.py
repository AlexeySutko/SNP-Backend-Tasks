

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
        if self.calories is None:
            return False

        if type(self.calories) is int:
            value = self.calories
        elif type(self.calories) is float:
            value = self.calories
        else:
            try:
                self.calories = int(self.calories)
                value = int(self.calories)
            except ValueError:
                try:
                    self.calories = float(self.calories)
                    value = float(self.calories)
                except ValueError:
                    return False

        if value < 200:
            return True
        else:
            return False

    def is_delicious(self):
        return True