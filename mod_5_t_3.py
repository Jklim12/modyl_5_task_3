class  House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors
    def __len__(self):
        return self.number_of_floors
    def __str__(self):
        return f"Название: {self.name}, количество этажей {self.number_of_floors}"
    def __eq__(self, other):
        if isinstance(other, House):
            return self.number_of_floors ==other.number_of_floors
        return False
    def __lt__(self, other):
        if isinstance(other, House):
            return self.number_of_floors < other.number_of_floors
        return False
    def __le__(self, other):
        if isinstance(other, House):
            return self.number_of_floors <= other.number_of_floors
        return False
    def __gt__(self, other):
        if isinstance(other, House):
            return self.number_of_floors > other.number_of_floors
        return False
    def __ge__(self, other):
        if isinstance(other, House):
            return self.number_of_floors >= other.number_of_floors
        return False
    def __ne__(self, other):
        if isinstance(other, House):
            return self.number_of_floors != other.number_of_floors
        return False
    def __add__(self, value):
        if isinstance(value, int):
            self.number_of_floors += value
            return self
        return False
    def __radd__(self, value):
        if isinstance(value, int):
           return self.__add__(value)
        return False
    def __iadd__(self, value):
        if isinstance(value, int):
           return self.__add__(value)
        return False


    def go_to(self,new_floor):
        if 1> new_floor or new_floor > self.number_of_floors:
            print('Такого этажа не существует')
        else:
            for i in range(1,new_floor+1):
                print(i)

h1 = House('ЖК Эльбрус', 10)

h2 = House('ЖК Акация', 20)



print(h1)

print(h2)



print(h1 == h2) # __eq__



h1 = h1 + 10 # __add__

print(h1)

print(h1 == h2)



h1 += 10 # __iadd__

print(h1)



h2 = 10 + h2 # __radd__

print(h2)



print(h1 > h2) # __gt__

print(h1 >= h2) # __ge__

print(h1 < h2) # __lt__

print(h1 <= h2) # __le__

print(h1 != h2) # __ne__


