from abc import ABC, abstractmethod
from ex0.CreatureFactory import Creature
from ex1.capabilities import HealCapability, TransformCapability
from typing import cast


class BattleStrategy(ABC):
    @abstractmethod
    def act(self, creature: Creature) -> None:
        pass

    @abstractmethod
    def is_valid(self, creature: Creature) -> bool:
        pass


class NormalStrategy(BattleStrategy):
    def is_valid(self, creature: Creature) -> bool:
        return True

    def act(self, creature: Creature) -> None:
        print(creature.attack())


class AggressiveStrategy(BattleStrategy):
    def is_valid(self, creature: Creature) -> bool:
        return isinstance(creature, TransformCapability)

    def act(self, creature: Creature) -> None:
        if not self.is_valid(creature):
            raise ValueError(f"Invalid Creature '{type(creature).__name__}'"
                             f" for this aggressive strategy")
        agg_creature = cast(TransformCapability, creature)
        print(agg_creature.transform())
        print(creature.attack())
        print(agg_creature.revert())


class DefensiveStrategy(BattleStrategy):
    def is_valid(self, creature: Creature) -> bool:
        return isinstance(creature, HealCapability)

    def act(self, creature: Creature) -> None:
        if not self.is_valid(creature):
            raise ValueError(f"Invalid Creature '{type(creature).__name__}'"
                             f" for this Defensive strategy")
        defens_creature = cast(HealCapability, creature)
        print(creature.attack())
        print(defens_creature.heal())
