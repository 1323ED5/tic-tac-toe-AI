from src.game_mechanic import GameMechanic
from src.turn import generate_turns, Turn


def generate_dimensions(area, active_player, turns):
    return [Dimension(area, active_player) for _ in range(len(turns))]


def calculate_dimensions(dimensions, turns):
    return tuple(map(lambda x: x[1].calculate_turn(x[0]), list(zip(turns, dimensions))))


class Dimension(GameMechanic):
    def __init__(self, area, active_player: int) -> None:
        self.area = area[:]
        self.active_player = active_player

    def born(self):
        turns = generate_turns(self.area)
        dimensions = generate_dimensions(self.area, self.active_player, turns)
        calculations = calculate_dimensions(dimensions, turns)
        return calculations

    def calculate_turn(self, turn: Turn):
        self.make_turn(turn.cell_id)

        gameover = self.check_game_over()

        # somebody won
        if gameover is not None:
            return gameover

        # Nobody won
        calculations = self.born()
        if self.active_player == 0:
            return min(calculations)
        else:
            return max(calculations)
