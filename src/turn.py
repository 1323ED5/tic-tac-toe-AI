class Turn:
    def __init__(self, cell_id: int) -> None:
        self.cell_id = cell_id

    def __str__(self) -> str:
        return f"<turn [{self.cell_id}]>"


def generate_turns(area) -> list:
    turns = []

    for index, cell in enumerate(area):
        if not cell:
            turns.append(Turn(index))

    return turns
