import pandas as pd


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


data = pd.read_csv('datasets/PSCompPars_2024.10.04_09.06.22.csv', delimiter=',')
data.columns = data.columns.str.strip()

print("Columns in the DataFrame:", data.columns)
print(data.head(10))


columns_of_interest = [
    'pl_name', 'pl_orbsmax', 'pl_insol',
    'pl_eqt', 'pl_rade', 'pl_bmasse',
    'pl_orbeccen', 'st_spectype', 'st_teff'
]


missing_columns = [col for col in columns_of_interest if col not in data.columns]
if missing_columns:
    print(f"Missing columns: {missing_columns}")
else:
    
    planet_data = data[columns_of_interest].dropna(subset=columns_of_interest)

    
    def calculate_similarity(row):
        score = 0
        score += (1 - abs(row['pl_orbsmax'] - earth_factors['pl_orbsmax']) / earth_factors['pl_orbsmax']) * 20
        score += (1 - abs(row['pl_insol'] - earth_factors['pl_insol']) / earth_factors['pl_insol']) * 20
        score += (1 - abs(row['pl_eqt'] - earth_factors['pl_eqt']) / earth_factors['pl_eqt']) * 15
        score += (1 - abs(row['pl_rade'] - earth_factors['pl_rade']) / earth_factors['pl_rade']) * 15
        score += (1 - abs(row['pl_bmasse'] - earth_factors['pl_bmasse']) / earth_factors['pl_bmasse']) * 15
        score += (1 - abs(row['pl_orbeccen'] - earth_factors['pl_orbeccen']) / earth_factors['pl_orbeccen']) * 10
        score += (1 if row['st_spectype'] == earth_factors['st_spectype'] else 0) * 5
        score += (1 - abs(row['st_teff'] - earth_factors['st_teff']) / earth_factors['st_teff']) * 5
        return score

    
    planet_data['habitability_score'] = planet_data.apply(calculate_similarity, axis=1)

    
    max_score = 100
    planet_data['habitability_percentage'] = (planet_data['habitability_score'] / max_score) * 100

    
    planet_data.loc[planet_data['habitability_score'] < 0, 'habitability_percentage'] = 0

    
    for index, row in planet_data.iterrows():
        print(f"Analyzing planet: {row['pl_name']}")
        print(f"Habitability Score: {row['habitability_score']:.2f}")
        print(f"Habitability Percentage: {row['habitability_percentage']:.2f}%\n")

    print("Analysis complete for all planets.")
