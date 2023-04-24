class Human:
    def __init__(self, name = 'Name'):
        self.name = name

class Comps:
    def __init__(self, model):
        self.model = model
        self.consumers = []
    def add_consumers(self, *args):
        for consumer in args:
            self.consumers.append(consumer)
    def print_consumers_names(self):
        if self.consumers != []:
            print(f'User of {self.model} is:')
            for consumer in self.consumers:
                print(consumer.name)
        else:
            print(f'{self.model} none consumer')

nick = Human('Nick')
kate = Human('Kate')
maks = Human('Max')

comp = Comps('Asus')
comp2 = Comps('hp')
comp3 = Comps('Mac')
comp4 = Comps('Aorus')

comp.add_consumers(nick)
comp2.add_consumers(kate)
comp3.add_consumers(maks)
comp4.add_consumers()

comp.print_consumers_names()
comp2.print_consumers_names()
comp3.print_consumers_names()
comp4.print_consumers_names()