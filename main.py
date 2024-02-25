import pandas as pd
from matplotlib import pyplot as plt

pd.options.display.max_rows = 200
pd.options.display.max_columns = 10


# Task 1
print("Task 1:")
try:
    df = pd.read_csv("Top100-2007.csv")
    print("The data has been read")
except FileNotFoundError:
    print("Oops... Can't read the data")
    exit()


# Task 2
num_rows, num_cols = df.shape
print("\nTask 2:")
print("Number of rows:", num_rows)
print("Number of columns:", num_cols)


# Task 3
K = 26
print("\nTask 3:")
print(f"Five rows from {K}:")
print(df.iloc[K-1:K+5-1].to_string())

lastCount = 3 * K + 2
print(f"\nLast {lastCount} rows:")
print(df.tail(lastCount).to_string())


# Task 4
print("\nTask 4:")
print(df.dtypes)


# Task 5
print("\nTask 5:")
text_columns = ["Name", "Country"]
for column in text_columns:
    df[column] = df[column].str.strip()
    print(f"Cleaned {column.upper()} from redundant spaces")


# Task 6
print("\nTask 6:")
df["Winning Percentage"] = df["Winning Percentage"].str.replace('%', '')
df["Winning Percentage"] = pd.to_numeric(df["Winning Percentage"])
df["Career Earnings"] = df["Career Earnings"].str.replace('$', '')
df["Career Earnings"] = pd.to_numeric(df["Career Earnings"])
print(df.dtypes)


# Task 7
print("\nTask 7:")
rows_with_missing_data = df[df.isnull().any(axis=1)]
print(rows_with_missing_data.to_string())
df.dropna(inplace=True)


# Task 8
print("\nTask 8:")
df[["Win", "Lose"]] = df["Singles Record (Career)"].str.split('-', expand=True).astype(int)
df["Total"] = df["Win"] + df["Lose"]
print(df.head(3).to_string())


# Task 9
print("\nTask 9:")
df.drop(columns=['Singles Record (Career)', 'Link to Wikipedia'], inplace=True)
print(df.head(3).to_string())


# Task 10
print("\nTask 10:")
df = df[["Rank", "Name", "Country", "Pts", "Total", "Win", "Lose", "Winning Percentage", "Career Earnings"]]
print(df.head(3).to_string())


# Task 11
print("\nTask 11:")
print("Subtask A:")
for country in sorted(df['Country'].unique()):
    print(country)

print("\nSubtask B:")
player_least_earnings = df.loc[df['Career Earnings'].idxmin()]
print("Name:", player_least_earnings['Name'])
print("Pts:", player_least_earnings['Pts'])

print("\nSubtask C:")
print(df[(df['Winning Percentage'] == 50)][["Name", "Country"]])


# Task 12
print("\nTask 12:")
print("Subtask A:")
print(df.groupby('Country')['Name'].count())

print("\nSubtask B:")
print(df.groupby('Country')['Pts'].mean())


# Task 13
df['Decade'] = (df['Rank'] - 1) // 10 + 1
matches_lost_per_decade = df.groupby('Decade')['Lose'].sum()

plt.bar(matches_lost_per_decade.index, matches_lost_per_decade.values, color='skyblue')
plt.xlabel('Десятка гравців')
plt.ylabel('Кількість програних матчів')
plt.title('Кількість програних матчів по кожній десятці гравців з Топ-100')
plt.xticks(matches_lost_per_decade.index)
plt.grid(axis='y')
plt.show()


# Task 14
total_earnings_per_country = df.groupby('Country')['Career Earnings'].sum()

plt.figure(figsize=(10, 6))
plt.pie(total_earnings_per_country, labels=total_earnings_per_country.index, autopct='%1.1f%%', startangle=140)
plt.axis('equal')
plt.title('Сумарна величина призових для кожної країни')
plt.show()


# Task 15
average_points_per_country = df.groupby('Country')['Pts'].mean()
average_matches_played_per_country = df.groupby('Country')['Total'].mean()

plt.figure(figsize=(10, 6))
plt.bar(average_points_per_country.index, average_points_per_country.values, color='skyblue', label='Середня кількість очок')
plt.plot(average_matches_played_per_country.index, average_matches_played_per_country.values, color='orange', marker='o', label='Середня кількість матчів', linewidth=2)
plt.xlabel('Країна')
plt.title('Середня кількість очок та зіграних матчів для кожної країни')
plt.xticks(rotation=45)
plt.legend()
plt.tight_layout()
plt.show()
