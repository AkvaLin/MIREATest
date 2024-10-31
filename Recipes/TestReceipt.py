# Пивоваров -> Пивной кекс
# Никита -> Неаполитанская пицца

import unittest
from Receipt import Receipt
from Ingredient import Ingredient
from pydantic import ValidationError

class TestReceipt(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.receipt_data = {
            "title": "Пивной кекс",
            "ingredients_list": [
                Ingredient(name='Мука', raw_weight=500, cooked_weight=500, cost_per_unit=50),
                Ingredient(name='Яйца', raw_weight=200, cooked_weight=180, cost_per_unit=100),
                Ingredient(name='Пиво', raw_weight=300, cooked_weight=290, cost_per_unit=80),
                Ingredient(name='Сахар', raw_weight=100, cooked_weight=100, cost_per_unit=40),
                Ingredient(name='Масло сливочное', raw_weight=150, cooked_weight=140, cost_per_unit=60)
            ],
        }
        cls.pizza_receipt_data = {
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

        cls.wrong_ing_receipt_data = {
            "name": "",
            "raw_weight": -1,
            "cooked_weight": -1,
            "cost_per_unit": -1
        }
        cls.wrong_list_receipt_data = {
            "title": "list",
            "ingredient_list": [
                123
            ]
        }
        cls.empty_list_receipt_data = {
            "title": "list",
            "ingredient_list": []
        }
        cls.wrong_title_receipt_data = {
            "title": "",
            "ingredient_list": [
                Ingredient(name='Дрожжи', raw_weight=10, cooked_weight=10, cost_per_unit=15)
            ]
        }

    def setUp(self):
        receipt = Receipt(name=self.receipt_data['title'],
                               ingredients=self.receipt_data['ingredients_list'])
        pizza_receipt = Receipt(name=self.pizza_receipt_data['title'],
                                     ingredients=self.pizza_receipt_data['ingredients_list'])
        
        self.receipts_data = [
            {
                'data': receipt,
                'cost': 330,
                'raw_weight': 1250,
                'cooked_weight': 1210
            },
            {
                'data': pizza_receipt,
                'cost': 260,
                'raw_weight': 880,
                'cooked_weight': 850
            }
        ]

    def test_calc_cost(self):
        for data in self.receipts_data:
            with self.subTest():
                self.assertEqual(data['data'].calc_cost(), data['cost'])

    def test_calc_weight_raw(self):
        for data in self.receipts_data:
            with self.subTest():
                self.assertEqual(data['data'].calc_weight(raw=True), data['raw_weight'])

    def test_calc_weight_cooked(self):
        for data in self.receipts_data:
            with self.subTest():
                self.assertEqual(data['data'].calc_weight(raw=False), data['cooked_weight'])

    def test_wrong_ingredients(self):
        with self.assertRaises(ValidationError):
            Ingredient(
                name=self.wrong_ing_receipt_data['name'],
                raw_weight=self.wrong_ing_receipt_data['raw_weight'],
                cooked_weight=self.wrong_ing_receipt_data['cooked_weight'],
                cost_per_unit=self.wrong_ing_receipt_data['cost_per_unit'])

    def test_wrong_list(self):
        with self.assertRaises(ValidationError):
            Receipt(name=self.wrong_list_receipt_data['title'],
                    ingredients=self.wrong_list_receipt_data['ingredient_list'])

    def test_empty_list(self):
        with self.assertRaises(ValidationError):
            Receipt(name=self.empty_list_receipt_data['title'],
                    ingredients=self.empty_list_receipt_data['ingredient_list'])

    def test_wrong_title(self):
        with self.assertRaises(ValidationError):
            Receipt(name=self.wrong_title_receipt_data['title'],
                    ingredients=self.wrong_title_receipt_data['ingredient_list'])

if __name__ == '__main__':
    unittest.main()
