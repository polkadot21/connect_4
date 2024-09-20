from typing import List
from connect_4.settings import GameSettings


class Board:
    def __init__(self, game_settings: GameSettings):
        self.game_settings: GameSettings = game_settings
        self.board: List[List[str]] = [
            [" " for _ in range(self.game_settings.columns)]
            for _ in range(self.game_settings.rows)
        ]

    def display(self) -> None:
        for row in self.board:
            print("| " + " | ".join(row) + " |")
        print("-" * (self.game_settings.columns * 4 + 1))

    def is_valid_move(self, col: int) -> bool:
        return self.board[0][col] == " "

    def get_next_open_row(self, col: int) -> int:
        for row in reversed(range(self.game_settings.rows)):
            if self.board[row][col] == " ":
                return row
        raise ValueError(
            "No open row available."
        )  # Handles edge case if there's no open row

    def drop_piece(self, row: int, col: int, piece: str) -> None:
        self.board[row][col] = piece

    def check_win(self, piece: str) -> bool:
        return (
            self.check_horizontal_win(piece)
            or self.check_vertical_win(piece)
            or self.check_positive_diagonal_win(piece)
            or self.check_negative_diagonal_win(piece)
        )

    def check_horizontal_win(self, piece: str) -> bool:
        for row in range(self.game_settings.rows):
            for col in range(self.game_settings.columns - 3):
                if (
                    self.board[row][col] == piece
                    and self.board[row][col + 1] == piece
                    and self.board[row][col + 2] == piece
                    and self.board[row][col + 3] == piece
                ):
                    return True
        return False

    def check_vertical_win(self, piece: str) -> bool:
        for row in range(self.game_settings.rows - 3):
            for col in range(self.game_settings.columns):
                if (
                    self.board[row][col] == piece
                    and self.board[row + 1][col] == piece
                    and self.board[row + 2][col] == piece
                    and self.board[row + 3][col] == piece
                ):
                    return True
        return False

    def check_positive_diagonal_win(self, piece: str) -> bool:
        for row in range(self.game_settings.rows - 3):
            for col in range(self.game_settings.columns - 3):
                if (
                    self.board[row][col] == piece
                    and self.board[row + 1][col + 1] == piece
                    and self.board[row + 2][col + 2] == piece
                    and self.board[row + 3][col + 3] == piece
                ):
                    return True
        return False

    def check_negative_diagonal_win(self, piece: str) -> bool:
        for row in range(3, self.game_settings.rows):
            for col in range(self.game_settings.columns - 3):
                if (
                    self.board[row][col] == piece
                    and self.board[row - 1][col + 1] == piece
                    and self.board[row - 2][col + 2] == piece
                    and self.board[row - 3][col + 3] == piece
                ):
                    return True
        return False

    def is_full(self) -> bool:
        for col in range(self.game_settings.columns):
            if self.is_valid_move(col):
                return False
        return True
