class Item:
    def __init__(self, id, name, firstMessage, secondMessage):
        self.id = id
        self.name = name
        self.firstMessage = firstMessage
        self.secondMessage = secondMessage
    
    def get_name(self):
        return self.name.upper()

    def get_message(self):
        return self.firstMessage

    def __repr__(self):
        return f'<Item: {self.name}>'

class Weapon(Item):
    def __init__(self, id, name, firstMessage, secondMessage, damage):
        super().__init__(id, name, firstMessage, secondMessage)
        self.damage = damage
    
    def is_weapon(self):
        return True 

    def is_consumable(self):
        return False

class Consumable(Item):
    def __init__(self, id, name, firstMessage, secondMessage, restoreHealth):
        super().__init__(id, name, firstMessage, secondMessage)
        self.restoreHealth = restoreHealth
    
    def is_weapon(self):
        return False 

    def is_consumable(self):
        return True