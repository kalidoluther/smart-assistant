from abc import ABC, abstractmethod

class ServiceInterface(ABC):
    @abstractmethod
    def method(self):
        pass
