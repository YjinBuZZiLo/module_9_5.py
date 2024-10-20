class StepValueError(ValueError):
    pass


class Iterator:
    def __init__(self, start, stop, step=1):
        self.start = start
        self.stop = stop
        self.step = step
        self.pointer = self.start

    def __iter__(self):
        self.pointer = self.start - self.step
        return self

    def __next__(self):
        if self.step > 0 and self.pointer + self.step <= self.stop:
            self.pointer += self.step
            return self.pointer
        if self.step < 0 and self.pointer + self.step >= self.stop:
            self.pointer += self.step
            return self.pointer
        if self.step == 0:
            try:
                if self.step == 0:
                    raise StepValueError("шаг не может быть равен 0")
            except StepValueError:
                print('Шаг указан неверно')
        if self.start > self.stop and self.step > 0:
            print("Операция не возможна")

        raise StopIteration


iter1 = Iterator(100, 200, 0)
iter2 = Iterator(-5, 1)
iter3 = Iterator(6, 15, 2)
iter4 = Iterator(5, 1, -1)
iter5 = Iterator(10, 1)


for i in iter1:
    print(i, end=' ')
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
print()

