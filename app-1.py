class ExampleClass:
    v = 10

    def __init__(self, message):
        self.message = message

    # Jest to najprostszy a zarazem najczesciej wykorzystywany rodzaj metody
    # Dzieki specjalnemu parametrowi self pozwala odwolywac sie do parametrow instancji,
    # na ktorej ta metoda pracuje
    # Oczywiscie metoda moze przyjmowac znacznie wiecej parametrow
    # Ta metoda moze rowniez modyfikowac stan klasy, kiedy odwolasz sie do atrybutu self.__class__
    def method(self):
        print(f'From instance method: v = {self.__class__.v}')
        print(f'From instance method: message = {self.message}')
        return f'Instance method: {self}'

    # Ta metoda zamiast parametru self przyjmuje parametr cls, ktory odwoluje sie do klasy z ktorej
    # pochodzi metoda a nie do konkretnego obiektu
    # Nie moze modyfikowac stanu obiektu poniewaz ma tylko i wylacznie dostep do atrybutu cls
    # Ale za to modyfikujac stan klasy moze modyfikowac elementy ktore sa wspoldzielone przez kilka
    # obiektow tej klasy
    @classmethod
    def c_method(cls):
        print(f'From class method:  v = {cls.v}')
        return f'Class method: {cls}'

    # Metoda statyczna nie przyjmuje zadnego specjalnego parametru ( ani self, ani cls )
    # Nie moze przez to modyfikowac ani stanu obiektu ani stanu klasy
    # Te metody dzialaja jak zwykle funkcje tyle ze przynaleznosc do konkretnej klasy
    # pozwala grupowac ich przeznaczenie, umiescic je w konkretnym namespace
    @staticmethod
    def s_method():
        return f'Static method'


# Wywolywanie metody instancyjnej
# pod self podstawiania jest konkretna instancja na rzecz ktorej wywolujemy metode
e1 = ExampleClass('A')
# pierwszy sposob wywolania
print(e1.method())
# drugi sposob wywolania
print(ExampleClass.method(e1))
# tak mozesz sie odwolac do stanu klasy z poziomu instancji
print(f'vv = {e1.__class__.v}')

# Wywolywanie metody klasy
# tym razem nie odwolujemy sie do instancji ale do klasy
# tutaj mozemy potraktowac klase jak obiekt, ktoremu modyfikujemy stan
# to podkresla idee ze w python wszystko jest obiektem nawet klasa
print(e1.c_method())
print(ExampleClass.c_method())

# Wywolywanie metody statycznej
# jest mozliwosc wywolywania metody statycznej rowniez z poziomu obiektu
print(e1.s_method())
print(ExampleClass.s_method())


class Car:
    def __init__(self, make, model, speed):
        self.make = make
        self.model = model
        self.speed = speed

    def __str__(self):
        return f'Make: {self.make} Model: {self.model} Speed: {self.speed}'

    def is_fast(self):
        return self.speed > 200

    # uzycie classmethod jako factory function do tworzenia obiektow o z gory okreslonych
    # cechach, ktore pozniej mozemy uzywac
    @classmethod
    def porsche_911(cls):
        return cls('Porsche', '911', 290)

    @classmethod
    def bmw_x6(cls):
        return cls('BMW', 'X6', 260)

    # za pomoca classmethod mozesz dodawac rozne wersje konstruktorow do twojej klasy np
    @classmethod
    def init_make_model(cls, make, model):
        return cls(make, model, 0)

    @staticmethod
    def find_the_fastest_car(cars):
        return max(cars, key=lambda car: car.speed)

    # mozesz rowniez za pomoca metod statycznych w klasie implementowac pewne akcje pomocnicze


print("=============================================== 1 ============================")
audi_q8 = Car('AUDI', 'Q8', 250)
print(audi_q8)
print(audi_q8.is_fast())
print(Car.is_fast(audi_q8))

print("=============================================== 2 ============================")
print(Car.bmw_x6())
print(Car.porsche_911())
print(Car.init_make_model('AUDI', 'Q5'))

print("=============================================== 3 ============================")
cars = [Car.bmw_x6(), Car.porsche_911(), audi_q8]
print(Car.find_the_fastest_car(cars))
