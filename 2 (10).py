# 20. Set.add() - HackerRank
n = int(input("Enter number of countries: "))
countries = set()

for _ in range(n):
    country = input("Enter country name: ")
    countries.add(country)

print(f"Total distinct countries: {len(countries)}")