# class StepValueError(ValueError):  # Заменил на аналогичный класс DataValueError, но более широкого назначения
#     pass


class DataValueError(ValueError):
    pass


class Iterator:

    def __init__(self, start, stop, step=1):
        self.start = start
        self.stop = stop
        self.step = step
        if step == 0:
            # raise StepValueError('Шаг не может быть равен 0')
            raise DataValueError('Шаг не может быть равен 0')
        if start == stop:
            raise DataValueError('Start не может быть равен Stop')

    def __iter__(self):
        self.pointer = self.start
        return self

    def __next__(self):
        num = self.pointer
        if (self.pointer <= self.stop and self.step > 0 and self.start < self.stop or
            self.pointer >= self.stop and self.step < 0 and self.start > self.stop):
            self.pointer += self.step
            return num
        raise StopIteration


try:
    iter1 = Iterator(100, 200, 0)
    for i in iter1:
        print(i, end=' ')
# except StepValueError:
except DataValueError:
    print('Шаг указан неверно')

iter2 = Iterator(-5, 1)
iter3 = Iterator(6, 15, 2)
iter4 = Iterator(5, 1, -1)
iter5 = Iterator(10, 1)

for i in iter2:
    print(i, end=' ')
print()
for i in iter3:
    print(i, end=' ')
print()
for i in iter4:
    print(i, end=' ')
print()
for i in iter5:
    print(i, end=' ')
print('Ещё один вариант:')
try:
    iter6 = Iterator(100, 100)
    for i in iter6:
        print(i, end=' ')
except DataValueError:
    print('Start/Stop указаны неверно')
