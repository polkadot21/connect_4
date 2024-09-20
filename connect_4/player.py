from connect_4.settings import GameSettings


class Player:
    def __init__(self, name: str, piece: str, game_settings: GameSettings):
        self.game_settings = game_settings
        self.name = name
        self.piece = piece

    def choose_column(self):
        while True:
            try:
                col = (
                    int(
                        input(
                            f"{self.name}, choose a column (1-{self.game_settings.columns}): "
                        )
                    )
                    - 1
                )
                if 0 <= col < self.game_settings.columns:
                    return col
                else:
                    print("Invalid column. Try again.")
            except ValueError:
                print("Please enter a valid number.")
