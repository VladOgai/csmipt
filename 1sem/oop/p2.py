class Tree:
    color = 'green'

    def __init__(self, age: int, tree_type: str, country: str):
        self.age = age
        self.tree_type = tree_type
        self.country = country

    def get_age(self):
        return f'Возраст дерева равен {self.age}'

    def get_country(self):
        return f'Данное дерево произрастает в стране {self.country}'


class FruitTree(Tree):
    def __init__(self, age: int, tree_type: str, country: str, crop: float):
        super().__init__(age, tree_type, country)
        self.crop = crop

    def get_urozhai(self):
        return self.age * self.crop


class NonFruitTree(Tree):
    def __init__(self, age: int, tree_type: str, country: str, wood: bool):
        super().__init__(age, tree_type, country)
        self.wood = wood

    def can_be_used(self):
        if self.wood:
            return "Это дерево можно использовать для заготовки древесины."
        return "Это дерево нельзя использовать для заготовки древесины."
