import json
import test_data


# Creates and returns a GameLibrary object(defined in test_data) from loaded json_data
def make_game_library_from_json(json_data):
    # Initialize a new GameLibrary
    game_library = test_data.GameLibrary()

    for game_json in json_data["games"]:
        game = test_data.Game()
        game.title = game_json["title"]
        game.year = game_json["year"]

        for platform_json in game_json["platform"]:
            game.platform = test_data.Platform()
            game.platform.name = platform_json["name"]
            game.platform.launch_year = platform_json["launch_year"]

    game_library.add_game(game)

    return game_library


# Part 2
input_json_file = "data/test_data.json"

with open("data/test_data.json", "r") as reader:
    test_data_json = json.load(reader)

print("JSON Data:")
print(test_data_json)

test_data = make_game_library_from_json(test_data_json)

print("Test Data:")
print(test_data)
