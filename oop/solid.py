# SOLID

"""
Single Responsibility Principle
Приниц единой ответственности - каждый объект должен иметь одну обязанность и эта обязанность должна быть
полностью инкапсулирована в класс. Все его сервисы должны быть направлены исключительно на обеспечение этой обязанности.

"""


# Не правильный подход. У класса несколько обязанностей.
class Animal:
    def __init__(self, name: str):
        self.name = name

    def get_name(self) -> str:
        pass

    def save(self, animal: Animal):
        pass


# Правильный пример. Разделили обязанности класса.
class Animal:
    def __init__(self, name: str):
        self.name = name

    def get_name(self):
        pass


class AnimalDB:
    def get_animal(self) -> Animal:
        pass

    def save(self, animal: Animal):
        pass


"""
Open Close Principle
Программные объекты (классы, модули, функции) должны быть открыты для расширения и закрыты для модификации.
"""


# Не правильноый подход.

class Discount:

    def __init__(self, customer, price):
        self.customer = customer
        self.price = price

    def give_discount(self):
        if self.customer == 'fav':
            return self.price * 0.2
        if self.customer == 'vip':
            return self.price * 0.4


# Правильный подход, один из способов.

from abc import ABC, abstractmethod


class Discount(ABC):

    def __init__(self, customer, price):
        self.customer = customer
        self.price = price

    @abstractmethod
    def give_discount(self):
        pass


class VIPDiscount(Discount):

    def give_discount(self):
        return self.price * 0.2


class SuperVIPDiscount(VIPDiscount):

    def get_discount(self):
        return self.price * 0.4


"""
Liskov Substitution Principle
Принцип в формулировке Роберта Мартина декларирует, что функции, которые используют базовый тип, должны иметь 
возможность использовать подтипы базового типа не зная об этом.
Следование принципу LSP заключается в том, что при построении иерархий наследования создаваемые наследники должны
корректно реализовывать поведение базового типа. То есть если базовый тип реализует определённое поведение,
то это поведение должно быть корректно реализовано и для всех его наследников.

LSP перекликается с контрактным программированием, определяя точные, формальные и верифицируемые описания интерфейсов.
И интерфейсы, реализумые наследниками, должны соответствовать контракту интерфейсов базового класса.

Наследник класса дополняет, но не заменяет поведение базового класса. То есть в любом месте программы замена
базового класса на класс-наследник не должна вызывать проблем. Если по каким-то причинам так не получается,
то вероятнее всего имеет место либо некорректная реализация, либо неверно выбранная абстракция для наследования.

Соблюдение принципа подстановки Барбары Лисков позволяет гарантировать, что любой созданный нами подкласс будет
без проблем использоваться ранее реализованными модулями, которые работали с надклассом.
А это существенно упрощает расширение функциональных возможностей системы.
"""


# не правильный подход
def animal_leg_count(animals: list):
    for animal in animals:
        if isinstance(animal, Lion):
            print(lion_leg_count(animal))
        elif isinstance(animal, Mouse):
            print(mouse_leg_count(animal))
        elif isinstance(animal, Pigeon):
            print(pigeon_leg_count(animal))


animal_leg_count(animals)


# Правильный подход, к примеру.
def animal_leg_count(animals: list):
    for animal in animals:
        print(animal.leg_count())


class Animal:

    def leg_count(self):
        pass


class Lion(Animal):

    def leg_count(self):
        return 'Lion have 4 leg'


class Mouse(Animal):

    def leg_count(self):
        return 'Mouse have 4 leg'


animals = [Lion, Mouse, ]
animal_leg_count(animals)


"""
Interface Segregation Principle
Создавайте мелкозернистые интерфейсы, ориентированные на клиента
Клиенты не должны зависеть от интерфейсов, которые они не используют.
Этот принцип устраняет недостатки реализации больших интерфейсов.
"""


# Не правильный подход к созданию интерфейса
class IShape:
    def draw_square(self):
        raise NotImplementedError

    def draw_rectangle(self):
        raise NotImplementedError

    def draw_circle(self):
        raise NotImplementedError


# Фигуры должны реализовать не нужный метод.
class Circle(IShape):
    def draw_square(self):
        pass

    def draw_rectangle(self):
        pass

    def draw_circle(self):
        pass


class Square(IShape):
    def draw_square(self):
        pass

    def draw_rectangle(self):
        pass

    def draw_circle(self):
        pass


class Rectangle(IShape):
    def draw_square(self):
        pass

    def draw_rectangle(self):
        pass

    def draw_circle(self):
        pass


# А если добавим новый метод в интерфейс, то все классы должны добавить к себе это метод.
class IShape:
    def draw_square(self):
        raise NotImplementedError

    def draw_rectangle(self):
        raise NotImplementedError

    def draw_circle(self):
        raise NotImplementedError

    def draw_triangle(self):
        raise NotImplementedError


# Пример правильного одного из подходовю
class IShape:
    def draw(self):
        raise NotImplementedError


class Circle(IShape):
    def draw(self):
        pass


class Square(IShape):
    def draw(self):
        pass


class Rectangle(IShape):
    def draw(self):
        pass


"""
Dependency Inversion Principle
Зависимость должна быть от абстракций, а не от деталей
A. Модули высокого уровня не должны зависеть от модулей низкого уровня. Оба должны зависеть от абстракций.
Б. Абстракции не должны зависеть от деталей. Детали должны зависеть от абстракций.
"""


# Неправильный подход.
class Gmail:
    """
    Класс нижнего уровня
    """

    def send(self, email, body):
        print(f'Отправляю письмо "{email}" с телом {body}')


class Notifier:
    """
    Класс верхнего уровня
    """

    def __init__(self):
        self.gmail = Gmail()

    def notify(self, email, body):
        self.gmail.send(email, body)

# Если класс Gmail перестает работать, все падает и нужно вносить правки.


class Mailer(ABC):
    """
    Интерфейс рассылки электронной почти.
    """

    @abstractmethod
    def send(self, email, body):
        pass


class Gmail(Mailer):
    """
    Класс нижнего уровня реализует интерфейс
    """

    def send(self, email, body):
        print(f'Отправляю письмо "{email}" с телом {body}')


class MocMailer(Mailer):
    """
    Класс-мок для тестирвоания
    """

    def send(self, email, body):
        print(f'Эмулирую отправку письма "{email}" с телом {body}')


class Notifier:
    """
    Класс верхнего уровня (бизнес-логики) инвертировал зависимость через интерфес.
    Теперь он зависит от абстракции Mailer, а не от конткретной реализации Gmail.
    """

    def __init__(self, mailer: Mailer):
        self.mailer = mailer

    def notify(self, email, body):
        self.mailer.send(email, body)

