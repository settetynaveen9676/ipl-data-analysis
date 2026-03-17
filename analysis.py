import pandas as pd

matches = pd.read_csv("matches.csv")

# Top teams
print("Top Teams:")
print(matches["winner"].value_counts().head(10))

# Top players
print("\nTop Players:")
print(matches["player_of_match"].value_counts().head(10))
