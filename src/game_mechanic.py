from typing import Union


class GameMechanic:
    def __init__(self) -> None:
        self.area = [None] * 9
        self.active_player = 0

    def switch_active_player(self):
        self.active_player = 1 if self.active_player == 0 else 0

    def check_won(self, sign: str) -> bool:
        return any([
            # horizontal
            all(map(lambda el: el == sign, self.area[:3])),
            all(map(lambda el: el == sign, self.area[3:6])),
            all(map(lambda el: el == sign, self.area[6:9])),

            # vertical
            all(map(lambda el: el == sign, [self.area[0], self.area[3], self.area[6]])),
            all(map(lambda el: el == sign, [self.area[1], self.area[4], self.area[7]])),
            all(map(lambda el: el == sign, [self.area[2], self.area[5], self.area[8]])),

            # diagonal
            all(map(lambda el: el == sign, [self.area[0], self.area[4], self.area[8]])),
            all(map(lambda el: el == sign, [self.area[2], self.area[4], self.area[6]])),
        ])

    def check_game_over(self) -> Union[int, None]:
        x_won = self.check_won("X")
        o_won = self.check_won("O")
        tie = all(map(lambda el: el is not None, self.area))

        if x_won:
            return -1
        if o_won:
            return 1
        if tie:
            return 0

        return None

    def make_turn(self, cell_id: int):
        player_sign = "X" if self.active_player == 0 else "O"
        self.area[cell_id] = player_sign
        self.switch_active_player()
