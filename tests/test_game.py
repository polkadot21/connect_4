import pytest
from connect_4.board import Board
from connect_4.settings import GameSettings


@pytest.fixture
def game_settings() -> GameSettings:
    return GameSettings(rows=6, columns=7)


@pytest.fixture
def board(game_settings: GameSettings) -> Board:
    return Board(game_settings)


def test_board_initialization(board: Board):
    assert len(board.board) == 6
    assert len(board.board[0]) == 7
    assert all(cell == " " for row in board.board for cell in row)


def test_is_valid_move(board: Board):
    assert board.is_valid_move(0) is True
    board.board[0][0] = "X"
    assert board.is_valid_move(0) is False


def test_get_next_open_row(board: Board):
    assert board.get_next_open_row(0) == 5
    board.board[5][0] = "X"
    assert board.get_next_open_row(0) == 4


def test_drop_piece(board: Board):
    board.drop_piece(5, 0, "X")
    assert board.board[5][0] == "X"


def test_check_horizontal_win(board: Board):
    for col in range(4):
        board.drop_piece(5, col, "X")
    assert board.check_horizontal_win("X") is True


def test_check_vertical_win(board: Board):
    for row in range(4):
        board.drop_piece(row, 0, "X")
    assert board.check_vertical_win("X") is True


def test_check_negative_diagonal_win(board: Board):
    for i in range(4):
        board.drop_piece(5 - i, i, "X")
    assert board.check_negative_diagonal_win("X") is True


def test_check_positive_diagonal_win(board: Board):
    for i in range(4):
        board.drop_piece(i, i, "X")
    assert board.check_positive_diagonal_win("X") is True


def test_is_full(board: Board):
    assert board.is_full() is False
    for row in range(6):
        for col in range(7):
            board.drop_piece(row, col, "X")
    assert board.is_full() is True
