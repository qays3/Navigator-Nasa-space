import json

earth_factors = {
    "pl_orbsmax": 1,
    "pl_insol": 1,
    "pl_eqt": 255,
    "pl_rade": 1,
    "pl_bmasse": 1,
    "pl_orbeccen": 0.0167,
    "st_spectype": "G2V",
    "st_teff": 5778
}

with open("datasets/trappist.json") as file:
    planets_data: dict[str, dict] = json.load(file)

for key, value in planets_data.items():
    globals()[key] = value

candidate_planets = [globals()[key] for key in planets_data.keys()]

data_of_interest = [
    'pl_name',
    'pl_orbsmax',
    'pl_insol',
    'pl_eqt',
    'pl_rade',
    'pl_bmasse',
    'pl_orbeccen',
    'st_spectype',
    'st_teff'
]

for planet in candidate_planets:
    missing_data = [col for col in data_of_interest if col not in planet.keys()]
    if missing_data:
        print(f"Missing data in {planet.get("pl_name")}: {missing_data}")

def calculate_similarity(planet) -> tuple[int, float]:
    score: int = 0
    score += (1 - abs(planet['pl_orbsmax'] - earth_factors['pl_orbsmax']) / earth_factors['pl_orbsmax']) * 20
    score += (1 - abs(planet['pl_insol'] - earth_factors['pl_insol']) / earth_factors['pl_insol']) * 20
    score += (1 - abs(planet['pl_eqt'] - earth_factors['pl_eqt']) / earth_factors['pl_eqt']) * 15
    score += (1 - abs(planet['pl_rade'] - earth_factors['pl_rade']) / earth_factors['pl_rade']) * 15
    score += (1 - abs(planet['pl_bmasse'] - earth_factors['pl_bmasse']) / earth_factors['pl_bmasse']) * 15
    score += (1 - abs(planet['pl_orbeccen'] - earth_factors['pl_orbeccen']) / earth_factors['pl_orbeccen']) * 10
    score += (1 - abs(planet['st_teff'] - earth_factors['st_teff']) / earth_factors['st_teff']) * 5
    score += (1 if planet['st_spectype'] == earth_factors['st_spectype'] else 0) * 5
    # return score

    planet_habitability_score: int = score

    max_score: int = 100
    if planet_habitability_score > 0:
        planet_habitability_percentage: float = planet_habitability_score
    else:
        planet_habitability_percentage: float = 0

    return planet_habitability_score, planet_habitability_percentage

json_data: dict[str, dict] = {}
for planet in candidate_planets:
    planet_score, planet_percentage = calculate_similarity(planet)
    temp_dict: dict[str, dict] = {
        f"{planet.get("pl_name")}": {
            "pl_score": f"{planet_score:.2f}",
            "pl_percentage": f"{planet_percentage:.2f}"
        }
    }

    json_data.update(temp_dict)

with open("output.json", "w") as output:
    json.dump(json_data, output, indent=4, sort_keys=True)

print("Analysis complete for all planets, output can be found in output.json.")