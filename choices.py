class Pizza():
    def __init__(self, description, cost):
        self.description = description
        self.cost = cost

    def get_description(self):
        return self.description

    def get_cost(self):
        return self.cost


class Classic(Pizza):
    def __init__(self):
        self.description = "mixed classic"
        self.cost = 100
        self.name = "Classic Pizza"


class Margherita(Pizza):
    def __init__(self):
        self.description = "with tomatoes sauce"
        self.cost = 100
        self.name = "Margherita Pizza"


class Turkish(Pizza):
    def __init__(self):
        self.description = "with bacon"
        self.cost = 125
        self.name = "Turkish Pizza"


class Italiano(Pizza):
    def __init__(self):
        self.description = "with basil"
        self.cost = 144
        self.name = "Italiano Pizza"


class Decorator(Pizza):

    def __init__(self, description, cost):
        super().__init__(description, cost)

    def get_cost(self):
        return self.Decorator.get_cost() + Pizza.get_cost(self)

    def get_description(self):
        return Pizza.get_description(self)


# extra sauces

class Olive(Decorator):
    def __init__(self):
        self.cost = 2
        self.description = "with olive"


class Mushroom(Decorator):
    def __init__(self, ):
        self.cost = 7
        self.description = "with mushroom"


class Cheese(Decorator):
    def __init__(self, ):
        self.cost = 5
        self.description = "with cheese"


class Bacon(Decorator):
    def __init__(self, ):
        self.cost = 20
        self.description = "with bacon"


class Corn(Decorator):
    def __init__(self, ):
        self.cost = 5
        self.description = "with corn"
