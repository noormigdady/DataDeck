from ex1 import HealingCreatureFactory, TransformCreatureFactory


def main() -> None:
    print("Testing Creature with healing capability")
    healing_factory = HealingCreatureFactory()
    print("base:")
    base1 = healing_factory.create_base()
    print(base1.describe())
    print(base1.attack())
    print(base1.heal())
    print("evolved:")
    evolved1 = healing_factory.create_evolved()
    print(evolved1.describe())
    print(evolved1.attack())
    print(evolved1.heal())
    print()

    print("Testing Creature with transform capability")
    transform_factory = TransformCreatureFactory()
    print("base:")
    base2 = transform_factory.create_base()
    print(base2.describe())
    print(base2.attack())
    print(base2.transform())
    print(base2.attack())
    print(base2.revert())
    print("evolved:")
    evolved2 = transform_factory.create_evolved()
    print(evolved2.describe())
    print(evolved2.attack())
    print(evolved2.transform())
    print(evolved2.attack())
    print(evolved2.revert())


if __name__ == "__main__":
    main()
