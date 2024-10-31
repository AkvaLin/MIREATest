from pydantic import BaseModel, field_validator

class Ingredient(BaseModel):
    """Класс для описания ингредиента."""
    name: str
    raw_weight: float
    cooked_weight: float
    cost_per_unit: float
    
    @field_validator('name')
    def validate_name(cls, v):
        if v == '' or v == None:
            raise ValueError('Неверное имя')
        else:
            return v
        
    @field_validator('raw_weight')
    def validate_name(cls, v):
        if v <= 0:
            raise ValueError('Неверный сырой вес')
        else:
            return v
        
    @field_validator('cooked_weight')
    def validate_name(cls, v):
        if v <= 0:
            raise ValueError('Неверный готовый вес')
        else:
            return v
        
    @field_validator('cost_per_unit')
    def validate_name(cls, v):
        if v <= 0:
            raise ValueError('Неверная цена')
        else:
            return v

    
    def __repr__(self):
        return f"{self.name}: raw_weight={self.raw_weight}, cooked_weight={self.cooked_weight}, cost={self.cost_per_unit}"