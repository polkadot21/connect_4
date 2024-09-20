from typing import List
from .board import Board
from .player import Player
from .settings import GameSettings


class Game:
    def __init__(self, game_settings: GameSettings):
        self.board: Board = Board(game_settings)
        self.players: List[Player] = [
            Player("Player 1", "X", game_settings),
            Player("Player 2", "O", game_settings),
        ]
        self.turn: int = 0
        self.game_over: bool = False

    def start(self) -> None:
        print("Welcome to Connect 4!")
        self.board.display()

        while not self.game_over:
            current_player: Player = self.players[self.turn % 2]
            print(f"{current_player.name}'s turn.")
            self.take_turn(current_player)

    def take_turn(self, player: Player) -> None:
        col: int = player.choose_column()

        if self.board.is_valid_move(col):
            row: int = self.board.get_next_open_row(col)
            self.board.drop_piece(row, col, player.piece)
            self.board.display()

            if self.board.check_win(player.piece):
                print(f"{player.name} wins!")
                self.game_over = True
            elif self.board.is_full():
                print("It's a tie!")
                self.game_over = True
            else:
                self.turn += 1
        else:
            print("Invalid move. Try again.")
