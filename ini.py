class Human:
    number_of_legs = 2 # class atribute
    number_of_hands = 2 # class atribute

    def __init__(self,age,education) -> None: # constructor function
        self.age = age # instance atribute
        self.education = education # instance atribute

    def run(self):

        print(f'moving by {self.number_of_legs} leg')

mohammad = Human(23,'bachelor')
ali = Human(25, "diploma")

print(mohammad.age)
print(ali.age)

mohammad.run()
ali.run()