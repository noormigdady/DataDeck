from abc import ABC, abstractmethod
from .creatures import Creature


class CreatureFactory(ABC):
    @abstractmethod
    def create_base(self) -> Creature:
        pass

    @abstractmethod
    def create_evolved(self) -> Creature:
        pass


class FlameFactory(CreatureFactory):
    def create_base(self) -> Creature:
        from .creatures import Flameling
        return Flameling()

    def create_evolved(self) -> Creature:
        from .creatures import Pyrodon
        return Pyrodon()


class AquaFactory(CreatureFactory):
    def create_base(self) -> Creature:
        from .creatures import Aquabub
        return Aquabub()

    def create_evolved(self) -> Creature:
        from .creatures import Torragon
        return Torragon()
