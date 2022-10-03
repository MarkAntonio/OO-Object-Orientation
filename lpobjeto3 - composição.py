class Employee:
    def __init__(self, name):
        self.name = name

    def work(self):
        print(f'{self.name} does things.')

    def __repr__(self):
        return '<Employee: nome=%s>' % self.name


class Chef(Employee):
    def __init__(self, name):
        Employee.__init__(self, name)

    def work(self):
        print(self.name, 'makes some food.')


class Waiter(Employee):
    def __init__(self, name):
        super().__init__(name)

    def work(self):
        print('Serves client')


class PizzaChef(Chef):
    def __init__(self, name):
        Chef.__init__(self, name)

    def work(self):
        print(self.name, 'makes pizza.')


class Customer:
    def __init__(self, name):
        self.name = name

    def order(self, waiter: Waiter):
        print(f'{self.name} makes a request to {waiter.name}.')

    def pay(self, waiter: Waiter):
        print(self.name, f'pays for item to {waiter.name}.')


class Oven:
    def bake(self):
        print("it' baked")


class Pizzaparlor:
    def __init__(self, waiter_name, pizza_chef_name):
        self.waiter = Waiter(waiter_name)
        self.pizza_man = PizzaChef(pizza_chef_name)
        self.oven = Oven()

    def order(self, name):
        customer = Customer(name)
        customer.order(self.waiter)
        self.pizza_man.work()
        self.oven.bake()
        customer.pay(self.waiter)



wilson_pizzas = Pizzaparlor('Francisco', 'Abraão')
print(wilson_pizzas.waiter.name)
wilson_pizzas.order('Severino')

