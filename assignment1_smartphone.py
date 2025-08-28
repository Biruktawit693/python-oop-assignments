# Base class
class Smartphone:
    def __init__(self, brand, model, storage):
        self.brand = brand
        self.model = model
        self.storage = storage  # in GB

    def make_call(self, number):
        print(f"{self.brand} {self.model} is calling {number}...")

    def take_photo(self):
        print(f"{self.brand} {self.model} took a photo!")

# Inheritance example
class GamingSmartphone(Smartphone):
    def __init__(self, brand, model, storage, gpu):
        super().__init__(brand, model, storage)
        self.gpu = gpu  # additional attribute

    def play_game(self, game_name):
        print(f"{self.brand} {self.model} is running {game_name} smoothly on {self.gpu} GPU!")

# Creating objects
phone1 = Smartphone("Samsung", "Galaxy S23", 128)
phone2 = GamingSmartphone("Asus", "ROG Phone 6", 256, "Adreno 730")

# Using methods
phone1.make_call("123-456-7890")
phone1.take_photo()

phone2.make_call("987-654-3210")
phone2.take_photo()
phone2.play_game("Genshin Impact")
