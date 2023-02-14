from jikanpy import Jikan

jikan = Jikan()

ani = jikan.anime(39587, extension="characters")

random = jikan.random(type="anime")
print(random)

# GET CHARACTERS
# for key in ani["data"]:
#     print(key['character']['name'])
#     print()

#GET STAFF AND POSITIONS
# for key in ani["data"]:
#     print(f'{key["person"]["name"]} : {key["positions"]}')
#     print()

#GET ALL
# for key, val in ani["data"]:
#     print(f"{key} : {val}")
#     print()

#GET CHARACTER DETAILS
# char = jikan.characters(22036)
# for key, val in char["data"].items():
#     print(f"{key} : {val}")
#     print()
