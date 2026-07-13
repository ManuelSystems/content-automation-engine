import json
def cargar_juegos():
    with open(
        "games.json",
        "r",
        encoding="utf-8"
    ) as file:

        game_database = json.load(file)

    return game_database