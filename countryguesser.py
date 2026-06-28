import random

continents = {
    "Asia": {
        "India": "New Delhi",
        "Japan": "Tokyo",
        "China": "Beijing",
        "South Korea": "Seoul",
        "Thailand": "Bangkok",
        "Indonesia": "Jakarta"
    },

    "Europe": {
        "France": "Paris",
        "Germany": "Berlin",
        "Italy": "Rome",
        "Spain": "Madrid",
        "United Kingdom": "London",
        "Portugal": "Lisbon"
    },

    "Africa": {
        "Egypt": "Cairo",
        "Nigeria": "Abuja",
        "Kenya": "Nairobi",
        "South Africa": "Pretoria",
        "Morocco": "Rabat",
        "Ethiopia": "Addis Ababa"
    },

    "North America": {
        "Canada": "Ottawa",
        "United States": "Washington",
        "Mexico": "Mexico City",
        "Cuba": "Havana",
        "Jamaica": "Kingston"
    },

    "South America": {
        "Brazil": "Brasília",
        "Argentina": "Buenos Aires",
        "Chile": "Santiago",
        "Peru": "Lima",
        "Colombia": "Bogotá"
    },

    "Oceania": {
        "Australia": "Canberra",
        "New Zealand": "Wellington",
        "Fiji": "Suva",
        "Samoa": "Apia"
    }
}

score = 0
lives = 3

print("=" * 50)
print("🌍 CONTINENT COUNTRY CHALLENGE 🌍")
print("=" * 50)

print("\nChoose a Continent")

continent_list = list(continents.keys())

for i, continent in enumerate(continent_list, start=1):
    print(f"{i}. {continent}")

choice = input("\nEnter your choice: ")

if not choice.isdigit() or int(choice) not in range(1, len(continent_list) + 1):
    print("Invalid choice.")
    exit()

selected = continent_list[int(choice) - 1]
countries = continents[selected]

print(f"\n🎮 Starting {selected} Quiz!")
print("You have 3 lives.\n")

while lives > 0:

    country = random.choice(list(countries.keys()))
    answer = input(f"What is the capital of {country}? ")

    if answer.lower() == "exit":
        break

    if answer.strip().lower() == countries[country].lower():
        print("✅ Correct!")
        score += 10
    else:
        print(f"❌ Wrong! Correct answer: {countries[country]}")
        lives -= 1

    print(f"⭐ Score: {score}")
    print(f"❤️ Lives: {lives}")
    print("-" * 40)

print("\n🏆 GAME OVER")
print(f"Final Score: {score}")

if score >= 100:
    rank = "🌟 World Master"
elif score >= 70:
    rank = "🎓 Geographer"
elif score >= 40:
    rank = "🧭 Traveler"
else:
    rank = "🗺️ Explorer"

print(f"Your Rank: {rank}")
print("Thanks for playing!")
