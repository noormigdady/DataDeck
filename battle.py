from ex0 import CreatureFactory, FlameFactory, AquaFactory


def test_creature_factory(factory: CreatureFactory) -> None:
    print("Testing factory")
    base = factory.create_base()
    evolved = factory.create_evolved()
    print(base.describe())
    print(base.attack())
    print(evolved.describe())
    print(evolved.attack())


def test_battle(factory1: CreatureFactory, factory2: CreatureFactory) -> None:
    print("Testing battle")
    f1 = factory1.create_base()
    f2 = factory2.create_base()
    print(f1.describe())
    print("vs.")
    print(f2.describe())
    print(f1.attack())
    print(f2.attack())


def main() -> None:
    flame_fact = FlameFactory()
    aqua_fact = AquaFactory()
    test_creature_factory(flame_fact)
    print()
    test_creature_factory(aqua_fact)
    print()
    test_battle(flame_fact, aqua_fact)


if __name__ == "__main__":
    main()
