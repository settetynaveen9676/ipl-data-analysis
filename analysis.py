import pandas as pd
import matplotlib.pyplot as plt

matches = pd.read_csv("matches.csv")

# Top teams
top_teams = matches["winner"].value_counts().head(5)
print("Top Teams:\n", top_teams)

# Top players
top_players = matches["player_of_match"].value_counts().head(5)
print("\nTop Players:\n", top_players)

# Visualization
top_teams.plot(kind='bar', title="Top IPL Teams")
plt.xlabel("Teams")
plt.ylabel("Wins")
plt.show()
