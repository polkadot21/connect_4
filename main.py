from connect_4 import settings
from connect_4.game import Game


def main():
    game = Game(game_settings=settings.game_settings)
    game.start()


if __name__ == "__main__":
    main()
