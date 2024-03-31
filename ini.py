class Human:
    number_of_legs = 2 # class atribute
    number_of_hands = 2 # class atribute

    def __init__(self,age,education) -> None: # constructor function
        self.age = age # instance atribute
        self.education = education # instance atribute

    def run(self):

        print(f'moving by {self.number_of_legs} leg')
    def how_old(self):
        print(f"i have {self.age} years old !")

mohammad = Human(23,'bachelor')
ali = Human(25, "diploma")

Human.number_of_legs = 5
mohammad.number_of_legs = 1

print(mohammad.number_of_legs)
print(ali.number_of_legs)

mohammad.run()
ali.run()
