class Animal:
    #class attribute(shared by all instances of this class)
    kingdom = "animalia"

    def __init__(self, name, species):
        #instance attributes (unique to each instance)
        self.name = name 
        self.species = species 
        print (f"a new animal object({self.species}) named '{self.species}'has been created.")

    def eat(self):
        print(f"{self.name} the {self.species} is eating.")
    def sleep(self):
        print(f"{self.name} the {self.species} is sleeping.")
        