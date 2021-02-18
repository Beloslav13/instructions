"""
Интерфейсы.
Если это выглядит как утка, плавает как утка и крякает как утка, то это, вероятно, и есть утка.

Структура интерфейса:
- класс интерфейса (абстрактный класс (наследующий abc.ABC))
- поля интерфейса (абстрактные свойства (@property + @abstractmethod))
- методы интерфейса (абсктрактные методы (@abstractmethod))
- typing (подсказки типов)

В чем отличие от простого абстрактного классса? Абстрактный класс реализует дополнительные методы.
"""

from abc import ABC, abstractmethod


class Interface(ABC):

	@property
	@abstractmethod
	def prop(self):
		pass	

	@abstractmethod
	def method(self):
		pass


class InterfaceImpl(Interface):

	@property
	def prop(self):
		return 'Свойство переопределено'

	def method(self):
		print(self.prop)
