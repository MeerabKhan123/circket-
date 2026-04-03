import pandas as pd

# ==========================================
#     CRICKET PLAYER PERFORMANCE ANALYZER
# ==========================================

print("=" * 45)
print("   CRICKET PLAYER PERFORMANCE ANALYZER")
print("=" * 45)

# Step 1: Player scores in 5 matches
babar = pd.Series([85, 120, 45, 90, 110])
rizwan = pd.Series([60, 75, 80, 55, 95])
fakhar = pd.Series([30, 140, 20, 70, 50])

players = {
    "Babar Azam": babar,
    "Rizwan": rizwan,
    "Fakhar Zaman": fakhar
}

# Step 2: Display scores
print("\nPlayer Scores:")
for name, scores in players.items():
    print(f"\n{name}:")
    print(scores.to_string(index=False))

# Step 3: Summary statistics
print("\n" + "=" * 45)
print("PLAYER STATISTICS")
print("=" * 45)
print(f"\n{'Player':<15}{'Total':<10}{'Average':<10}{'Best':<10}")

for name, scores in players.items():
    print(f"{name:<15}{scores.sum():<10}{scores.mean():<10.1f}{scores.max():<10}")

# Step 4: Best performance
print("\nBest Performance:")
for name, scores in players.items():
    print(f"{name}: {scores.max()} runs")

# Step 5: Half-centuries (50+)
print("\nHalf-Centuries (50+ runs):")
for name, scores in players.items():
    count = (scores >= 50).sum()
    print(f"{name}: {count}")

# Step 6: Team total per match
team_total = babar + rizwan + fakhar
print("\nTeam Total Per Match:")
print(team_total.to_string(index=False))

print(f"\nHighest Team Score: {team_total.max()} runs")

# Step 7: Handling missing values
shaheen = pd.Series([15, None, 8, None, 20])

print("\nShaheen Scores (with missing values):")
print(shaheen)

shaheen_filled = shaheen.fillna(0)

print("\nAfter filling missing values with 0:")
print(shaheen_filled)

print("\n" + "=" * 45)
print("Project Completed Successfully!")
print("=" * 45)
