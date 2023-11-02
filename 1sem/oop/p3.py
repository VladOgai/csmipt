class Aircraft:
    def __init__(self, capacity: int, passengers_number: int, condition: bool, is_for_passengers: bool):
        self.capacity = capacity
        self.passengers_number = passengers_number
        self.condition = condition
        self.is_for_passengers = is_for_passengers

    def get_zagruzhen(self):
        if self.is_for_passengers and self.condition:
            try:
                s = self.passengers_number / self.capacity
                if s <= 1:
                    return s
                print('Пассажиров слишком много')
                return None
            except ZeroDivisionError:
                print('Введено нулевое число мест')
                return None
        if not self.condition:
            print('Требуется ремонт')
        if not self.is_for_passengers:
            print('Судно не предназначено для перевозки пассажиров')
        return None
