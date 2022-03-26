from src.dimension import Dimension
from src.game_mechanic import GameMechanic
from src.turn import generate_turns
from src.utils import clear_console


class AIMixin:
    def bot_turn(self):
        turns = generate_turns(self.area)

        root_dimension = Dimension(self.area, self.active_player)
        calculations = root_dimension.born()
        winnable_result = max(calculations)

        index_of_max = calculations.index(winnable_result)
        winnable_turn = turns[index_of_max]

        cell_id = winnable_turn.cell_id

        self.make_turn(cell_id)


class ConsoleGame(GameMechanic, AIMixin):
    def display_area(self):
        print()
        print("", " | ".join(map(lambda x: " " if x is None else x, self.area[:3])))
        print("-" * 11)
        print("", " | ".join(map(lambda x: " " if x is None else x, self.area[3:6])))
        print("-" * 11)
        print("", " | ".join(map(lambda x: " " if x is None else x, self.area[6:9])))
        print()

    def player_turn(self):
        cell_id = int(input("cell_id: "))
        self.make_turn(cell_id)

    def start(self):
        while True:
            clear_console()

            self.display_area()

            if self.active_player == 0:
                self.player_turn()
            else:
                self.bot_turn()

            gameover = self.check_game_over()

            if gameover is not None:
                print("WON:", {1: "AI", 0: "TIE", -1: "YOU"}.get(gameover))
                self.display_area()
                break
