import cc_dat_utils
import json
import cc_data


#Part 3
#Load your custom JSON file
#Convert JSON data to cc_data
#Save converted data to DAT file





# Part 1 ===================================================================================
# Creates and returns a GameLibrary object(defined in test_data) from loaded json_data
def make_cc_data_file_from_json(json_data):
    # Initialize a new game library
    cc_data_file = cc_data.CCDataFile()

    # Loop through each individual game
    for level_json in json_data["levels"]:
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