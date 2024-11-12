class Pet:
    def __init__(self, name, pet_type):
        # Attributes to store the pet's name, type, hunger, and happiness levels
        self.name = name
        self.pet_type = pet_type
        self.hunger = 5  # scale of 0-10; 0 means full, 10 means very hungry
        self.happiness = 5  # scale of 0-10; 10 means very happy

    def feed(self):
        # Decrease hunger level by feeding
        if self.hunger > 0:
            self.hunger -= 1
            self.happiness += 1
            print(f"{self.name} is enjoying the food! Yum!")
        else:
            print(f"{self.name} is not hungry right now.")

    def play(self):
        # Increase happiness by playing, but it makes the pet hungry
        self.happiness += 2
        self.hunger += 1
        print(f"{self.name} is having a blast playing!")

    def status(self):
        # Check the pet's current hunger and happiness levels
        print(f"{self.name} the {self.pet_type}:")
        print(f"  Hunger level: {self.hunger}/10")
        print(f"  Happiness level: {self.happiness}/10")

    def check_mood(self):
        # Prints mood based on happiness level
        if self.happiness > 7:
            print(f"{self.name} is feeling really happy!")
        elif self.happiness > 4:
            print(f"{self.name} is doing okay.")
        else:
            print(f"{self.name} seems a bit down...")

# Example usage
my_pet = Pet("Fluffy", "cat")
my_pet.status()
my_pet.feed()
my_pet.play()
my_pet.check_mood()
my_pet.status()
