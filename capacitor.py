from ex1.Factories import HealingCreatureFactory, TransformCreatureFactory
from ex0 import CreatureFactory


def manage_creatures(factory: CreatureFactory) -> None:
    if isinstance(factory, HealingCreatureFactory):
        print("base:")
        base_h = factory.create_base()
        print(base_h.describe())
        print(base_h.attack())
        print(base_h.heal())
        print("evolved: ")
        evolved_h = factory.create_evolved()
        print(evolved_h.describe())
        print(evolved_h.attack())
        print(evolved_h.heal())

    elif isinstance(factory, TransformCreatureFactory):
        print("base:")
        base_t = factory.create_base()
        print(base_t.describe())
        print(base_t.attack())
        print(base_t.transform())
        print(base_t.attack())
        print(base_t.revert())
        print("evolved: ")
        evolved_t = factory.create_evolved()
        print(evolved_t.describe())
        print(evolved_t.attack())
        print(evolved_t.transform())
        print(evolved_t.attack())
        print(evolved_t.revert())
    print()


def main() -> None:
    heal_fact = HealingCreatureFactory()
    transform_fact = TransformCreatureFactory()

    print("Testing Creature with healing capability")
    manage_creatures(heal_fact)
    print("Testing Creature with healing capability")
    manage_creatures(transform_fact)


if __name__ == "__main__":
    main()
