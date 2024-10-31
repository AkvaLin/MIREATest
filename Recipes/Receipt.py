from Ingredient import Ingredient
from pydantic import BaseModel, field_validator

class Receipt(BaseModel):
    """Класс для описания рецепта."""

    name: str
    ingredients: list[Ingredient]

    @field_validator('name')
    def validate_name(cls, v):
        if v == '' or v == None:
            raise ValueError('Неверное имя')
        else:
            return v
        
    @field_validator('ingredients')
    def validate_ingridients(cls, v):
        if all(isinstance(ing, Ingredient) for ing in v) and len(v) > 0:
            return v
        else: 
            raise ValueError('неверные ингредиенты')
    
    def calc_cost(self, portions=1):
        """Рассчитать себестоимость на указанное количество порций."""
        total_cost = sum(ingredient.cost_per_unit for ingredient in self.ingredients) * portions
        return total_cost

    def calc_weight(self, portions=1, raw=True):
        """Рассчитать вес сырого или готового продукта."""
        total_weight = sum(
            ingredient.raw_weight if raw else ingredient.cooked_weight
            for ingredient in self.ingredients
        ) * portions
        return total_weight

    def __str__(self):
        ingredients_str = "\n".join([f"{ingredient.name}: {ingredient.raw_weight}g (raw), {ingredient.cooked_weight}g (cooked), {ingredient.cost_per_unit} rub" for ingredient in self.ingredients])
        return f"Recipe: {self.name}\nIngredients:\n{ingredients_str}"

if __name__ == '__main__':
    # Рецепт "Пивной кекс"
    receipt_from_api = {
        "title": "Пивной кекс",
        "ingredients_list": [
            Ingredient(name='Мука', raw_weight=500, cooked_weight=500, cost_per_unit=50),
            Ingredient(name='Яйца', raw_weight=200, cooked_weight=180, cost_per_unit=100),
            Ingredient(name='Пиво', raw_weight=300, cooked_weight=290, cost_per_unit=80),
            Ingredient(name='Сахар', raw_weight=100, cooked_weight=100, cost_per_unit=40),
            Ingredient(name='Масло сливочное', raw_weight=150, cooked_weight=140, cost_per_unit=60)
        ],
    }

    receipt = Receipt(name=receipt_from_api['title'], ingredients=receipt_from_api['ingredients_list'])

    # Рецепт "Неаполитанская пицца"
    pizza_receipt_from_api = {
        "title": "Неаполитанская пицца",
        "ingredients_list": [
            Ingredient(name='Мука', raw_weight=300, cooked_weight=300, cost_per_unit=30),
            Ingredient(name='Вода', raw_weight=200, cooked_weight=200, cost_per_unit=5),
            Ingredient(name='Томатный соус', raw_weight=150, cooked_weight=140, cost_per_unit=50),
            Ingredient(name='Моцарелла', raw_weight=200, cooked_weight=180, cost_per_unit=120),
            Ingredient(name='Оливковое масло', raw_weight=20, cooked_weight=20, cost_per_unit=40),
            Ingredient(name='Дрожжи', raw_weight=10, cooked_weight=10, cost_per_unit=15)
        ],
    }

    pizza_receipt = Receipt(name=pizza_receipt_from_api['title'], ingredients=pizza_receipt_from_api['ingredients_list'])


    # Самопроверка для "Пивного кекса"
    print(receipt)
    print("Общая себестоимость (Пивной кекс):", receipt.calc_cost())
    print("Вес сырого продукта (Пивной кекс):", receipt.calc_weight(raw=True))
    print("Вес готового продукта (Пивной кекс):", receipt.calc_weight(raw=False))

    # Самопроверка для "Неаполитанской пиццы"
    print(pizza_receipt)
    print("Общая себестоимость (Неаполитанская пицца):", pizza_receipt.calc_cost())
    print("Вес сырого продукта (Неаполитанская пицца):", pizza_receipt.calc_weight(raw=True))
    print("Вес готового продукта (Неаполитанская пицца):", pizza_receipt.calc_weight(raw=False))
