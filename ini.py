class Human:
    number_of_legs = 2 # class atribute
    number_of_hands = 2 # class atribute

    def __init__(self,age,education) -> None: # constructor function
        self.age = age # instance atribute
        self.education = education # instance atribute

mohammad = Human(23,'bachelor')
ali = Human(25, "diploma")

print(mohammad.age)
print(ali.age)