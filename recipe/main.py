from recipe import Recipe


# replace redundant code with a creation method
def create_recipe(name, chocolate=0, coffee=0, sugar=0, milk=0, price=0.0):
    recipe = Recipe(name)
    recipe.coffee = coffee
    recipe.chocolate = chocolate
    recipe.sugar = sugar
    recipe.milk = milk
    recipe.price = price
    print(recipe)


if __name__ == '__main__':
    create_recipe("Coffee with sugar", 0, 4, 2, 0, 30.0)
    create_recipe("Latte", 0, 3, 2, 1, 40.0)
    create_recipe("Hot Chocolate", 3, 0, 2, 4, 30.0)


