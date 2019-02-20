import json
import test_data


# Part 1 ===================================================================================
# Creates and returns a GameLibrary object(defined in test_data) from loaded json_data
def make_game_library_from_json(json_data):
    # Initialize a new game library
    game_library = test_data.GameLibrary()

    # Loop through each individual game
    for game_json in json_data["games"]:
        # Initialize a new game
        game = test_data.Game()
        game.title = game_json["title"]
        game.year = game_json["year"]

        # Loop through each detail of the platform
        for platform_json in game_json["platform"]:
            # Initialize a new platform
            game.platform = test_data.Platform()
            game.platform.name = platform_json["name"]
            game.platform.launch_year = platform_json["launch_year"]

        # Add the game to the new game library
        game_library.add_game(game)

    # return the completed library
    return game_library


# Part 2 ===================================================================================
input_json_file = "data/test_data.json"

# Open the file specified by input_json_file + use the json module to load the data from the file
with open("data/test_data.json", "r") as reader:
    test_data_json = json.load(reader)

# Print JSON Data for reference
print("JSON Data:")
print(test_data_json)

# Use make_game_library_from_json(json_data) to convert the data to GameLibrary data
test_data = make_game_library_from_json(test_data_json)

# Print the resulting Game Library
print("Test Data:")
print(test_data)
