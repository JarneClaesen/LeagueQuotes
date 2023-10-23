import random

from bs4 import BeautifulSoup
import requests

champions = ['Aatrox', 'Ahri', 'Akali', 'Akshan', 'Alistar', 'Amumu', 'Anivia', 'Annie', 'Aphelios', 'Ashe', 'Aurelion Sol', 'Azir', 'Bard', "Bel'Veth", 'Blitzcrank', 'Brand', 'Braum', 'Caitlyn', 'Camille', 'Cassiopeia', "Cho'Gath", 'Corki',
             'Darius', 'Diana', 'Dr. Mundo', 'Draven', 'Ekko', 'Elise', 'Evelynn', 'Ezreal', 'Fiddlesticks', 'Fiora', 'Fizz', 'Galio', 'Gangplank', 'Garen', 'Gnar', 'Gragas', 'Graves', 'Gwen', 'Hecarim', 'Heimerdinger', 'Illaoi', 'Irelia', 'Ivern',
             'Janna', 'Jarvan IV', 'Jax', 'Jayce', 'Jhin', 'Jinx', "Kai'sa", 'Kalista', 'Karma', 'Karthus', 'Kassadin', 'Katarina', 'Kayle', 'Kayn', "Kennen", "Kha'Zix", 'Kindred', 'Kled', "Kog'Maw", 'LeBlanc', 'Lee Sin', "Leona", 'Lillia',
             'Lissandra', 'Lucian', 'Lulu', 'Lux', 'Malphite', 'Malzahar', 'Maokai', 'Master Yi', 'Miss Fortune', 'Mordekaiser', 'Morgana', 'Nami', 'Nasus', 'Nautilus', 'Neeko', 'Nidalee', 'Nilah', 'Nocturne', 'Nunu & Willump', 'Olaf', 'Orianna', 'Ornn', 'Pantheon',
             'Poppy', 'Pyke', 'Qiyana', 'Quinn', 'Rakan', 'Rammus', "Rek'Sai", 'Rell', 'Renata Glasc', 'Renekton', 'Rengar', 'Riven', 'Rumble', 'Ryze', 'Samira', 'Sejuani', 'Senna', 'Seraphine', 'Sett', 'Shaco', 'Shen', 'Shyvana', 'Singed', 'Sion', 'Sivir', 'Skarner', 'Sona', 'Soraka', 'Swain', 'Sylas',
             'Syndra', 'Tahm Kench', 'Taliyah', 'Talon', 'Taric', 'Teemo', 'Thresh', 'Tristana', 'Trundle', 'Tryndamere', 'Twisted Fate', 'Twitch', 'Udyr', 'Urgot', 'Varus', 'Vayne', 'Veigar', "Vel'Koz", 'Vex', 'Vi',
             'Viego', 'Viktor', 'Vladimir', 'Volibear', 'Warwick', 'Wukong', 'Xayah', 'Xerath', 'Xin Zhao', 'Yasuo', 'Yone', 'Yorick', 'Yuumi', 'Zac', 'Zed', 'Zeri', 'Ziggs', 'Zilean', 'Zoe', 'Zyra']
quotes = []
guesses = []


def scrape_website(champion_name):
    name = champion_name.replace(' ', '-').lower().strip()
    name = name.replace("'", "")
    name = name.replace(".", "")
    name = name.replace("&", "und")

    URL = "https://www.thyquotes.com/" + name
    webpage = requests.get(URL)

    soup = BeautifulSoup(webpage.text, "html.parser")

    quoteText = soup.find_all("p", class_=False, id=False)

    for i in quoteText:
        quote = i.text.strip().split('\n')[0]  # Get the text of the current quote, but only the sentence before a new line
        if quote != "":
            quotes.append(quote)


def create_game():
    # Randoms
    number1 = random.randint(0, len(champions))
    number2 = random.randint(0, len(quotes))

    # Champion genereren
    champion = champions[number1 - 1].lower()

    # Website scrapen en quotes in lijst zetten van de champion
    scrape_website(champion)
    quote = quotes[number2 - 1]
    print(quote)

    # Laten raden
    guess = input("Champion: ").lower()

    # Guess checken en lijst maken van gerade champions
    while guess != champion and guess != "give up":
        guesses.append(guess)
        print("Guesses: ", end='')
        for i in range(0, len(guesses)):
            print(guesses[i], end=" ")
        print()
        guess = input("Not correct. Try again: ")

    if guess == "give up":
        print(champion)
    else:
        print("Correct!")
        print()

    guesses.clear()
    quotes.clear()


def main():

    print("League of Legends quote guessing game.")
    print()
    print("Type 'give up' if you don't know the answer")
    print()

    another_game = True

    while another_game:
        create_game()
        another_game = input("Want to play another game? (y/n): ") == "y"


if __name__ == '__main__':
    main()
