from pydantic_settings import BaseSettings


class GameSettings(BaseSettings):
    rows: int = 6
    columns: int = 7

    class Config:
        env_file = ".env"


game_settings = GameSettings()
