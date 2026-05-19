from ex0 import CreatureFactory, FlameFactory, AquaFactory
from ex1 import HealingCreatureFactory, TransformCreatureFactory
from ex2 import BattleStrategy, NormalStrategy
from ex2 import AggressiveStrategy, DefensiveStrategy


def battle(opponents: list[tuple[CreatureFactory, BattleStrategy]]) -> None:
    print("*** Tournament ***")
    print(f"{len(opponents)} opponents involved")
    for i in range(len(opponents)):
        fac1, strat1 = opponents[i]
        creature1 = fac1.create_base()
        for j in range(i+1, len(opponents)):
            fac2, strat2 = opponents[j]
            creature2 = fac2.create_base()
            print("\n* Battle *")
            print(creature1.describe())
            print("vs.")
            print(creature2.describe())
            print("Now fight!")
            try:
                strat1.act(creature1)
                strat2.act(creature2)
            except Exception as e:
                print(f"Battle Error, aborting tournament: {e}")
                return


def main() -> None:
    flame_fac = FlameFactory()
    aqua_fac = AquaFactory()
    heal_fac = HealingCreatureFactory()
    Transform_fac = TransformCreatureFactory()
    normal_strat = NormalStrategy()
    aggressive_strat = AggressiveStrategy()
    defensive_strat = DefensiveStrategy()

    print("Tournament 0 (basic)")
    print("[ (Flameling+Normal), (Healing+Defensive) ]")
    opponent0 = [
        (flame_fac, normal_strat),
        (heal_fac, defensive_strat)]
    battle(opponent0)

    print("\nTournament 1 (error)")
    print("[ (Flameling+Aggressive), (Healing+Defensive) ]")
    opponent1 = [
        (flame_fac, aggressive_strat),
        (heal_fac, defensive_strat)]
    battle(opponent1)

    print("\nTournament 2 (multiple)")
    print("[ (Aquabub+Normal), (Healing+Defensive), (Transform+Aggressive) ]")
    opponent2 = [
        (aqua_fac, normal_strat),
        (heal_fac, defensive_strat),
        (Transform_fac, aggressive_strat)]
    battle(opponent2)


if __name__ == "__main__":
    main()
