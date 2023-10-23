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
congrats_list = ['Congrats!', 'You did it!', 'Bravo!', 'Hooray!', 'Cheers!', 'Three cheers!', 'Salute.', 'Impressive!', 'Awesome.', 'Amazing!', 'Attaboy', 'Attagirl', 'Fantastic.', 'Respect.', 'Props!', 'High five.', 'Take a bow.', 'Hats off to you.', 'Thumbs up!', 'You rock!', 'You rule!', 'Kudos!', 'Felicitations.', 'Compliments.', "Here's to you.", 'Sensational', 'Good one.', 'Good show.', 'Good job.', 'Good going.', 'Good for you.', 'Keep it up.', 'Nice job.', 'Nice work.', 'Nice one.', 'Nicely done.', 'Well done.', 'Good one.', 'I knew you could do it! Congratulations.', 'Bravo! We are so proud of you.', 'Congratulations! This calls for a celebration.', 'So proud of you!', 'This calls for a celebration!', 'Congratulations are in order!', 'I knew you could do it!', 'Keep up the great work.', "I'm happy for you.", "I couldn't be happier for you.", "I'm thrilled for you!", "It couldn't happen to a better person.", 'So pleased for you.', 'So thrilled for you.', 'I commend you.', 'Way to go.', 'Way to shine.', 'You amaze me.', "You're the best.", "You're a genius.", 'You deserve it.', 'This is awesome.', "I'm impressed.", 'You really deserved it.', 'You did that very well.', 'You get a gold star!', 'You win the crown!', 'You take first place!', 'You got the trophy!', 'You get the gold medal!', 'You nailed it.', 'A standing ovation for you!', 'A toast in your honor!', "You're doing beautifully.", 'Nothing can stop you now.', "Words can't express how proud I am.", "You've earned every bit of the success you're enjoying.", 'You deserve a pat on the back.', "That's the way.", "That's the best ever.", 'You did that very well.', 'You really did it.', 'You made it look easy.', "You're on the right track now.", "You're really going to town.", 'Nothing can stop you now.', 'You will always remember this day, and so will we.', 'Wishing you all the best in your new adventure.', 'Best of luck to you in the future.', "I'm excited for you.", "I'm proud of you.", "I'm wishing you the best.", 'You have accomplished a lot.', 'I think you are pretty great.', 'I always knew that good things would come your way.', 'Keep being awesome.', 'My face has a proud smile because of you.', 'Today, we celebrate you.', 'We are so inspired by you.', 'We knew you could do it.', 'Your future is so bright!', 'I have so much pride in my heart for you right now.', 'Great things come from great people.', "It's time to celebrate!", "Success like yours can't be bought.", 'Congratulations and best wishes.', 'Heartfelt congratulations to you!', 'Please accept my warmest congratulations.', 'Let me offer you my congratulations.', 'Keep up the good work.', "I'm really pleased for you.", 'You have proven your competence.', 'You have gone above and beyond expectations.', 'Congratulations. No one deserves this more.', 'Sending you heartfelt congratulations today.', 'Congratulations on your well-deserved success.', 'Warmest congratulations on your achievement.', 'So pleased to see you accomplishing great things!', 'What an impressive achievement.', 'Simply overjoyed to hear your good news.', 'You worked so hard for this. Congratulations.', 'Sincere congratulations on your hard-earned success.', 'Congratulations. Your hard work and perseverance have paid off.', 'Well done! Your hard work and determination have paid off.', 'Congratulations on achieving such a significant milestone.', 'I hope you feel proud today and confident in your ability to rise to your next challenge.', "I've got a feeling this is only the beginning of even more great things to come for you.", 'I commend you on this latest success, and I look forward to seeing even more great things from you.', "I knew you were capable, but I didn't expect this level of accomplishment."]
quotes = []
guesses = []


def scrape_website(champion_name):
    name_not_formatted = champion_name.replace(champion_name[0], champion_name[0].upper())
    name = champion_name
    if name.find(' ') != -1 or name.find("'") != -1 or name.find(" & Willump") != -1:
        name = champion_name.replace(' ', '_').lower().strip()
        name = name.replace("'", "%27")
        name = name.replace("_&_willump", "")

        if name.find("_") != -1: # Place capital letter after underscore
            letter_index = name.find("_") + 1
            name = name.replace(name[letter_index], name[letter_index].upper())
        if name.find("%27") != -1: # Place capital letter after %27
            letter_index = name.find("%27") + 3
            name = name.replace(name[letter_index], name[letter_index].upper())

    URL = "https://leagueoflegends.fandom.com/wiki/" + name + "/LoL/Audio"
    webpage = requests.get(URL)

    soup = BeautifulSoup(webpage.text, "html.parser")

    quoteText = soup.find_all("i", class_=False, id=False)

    for i in quoteText:
        quote = i.text.strip().split('\n')[0]  # Get the text of the current quote, but only the sentence before a new line
        if quote != "" and quote not in quotes and quote.find(name_not_formatted) == -1: # checken op lege en duplicate quotes en of er een naam in de quote voorkomt
            quotes.append(quote)


def create_game():
    # Randoms
    number1 = random.randint(0, len(champions) - 1)
    number3 = random.randint(0, len(congrats_list) - 1)

    # Champion genereren
    champion = champions[number1].lower()

    # Website scrapen en quotes in lijst zetten van de champion
    scrape_website(champion)
    number2 = random.randint(0, len(quotes) - 1)
    quote = quotes[number2]
    print(quote)

    # Laten raden
    guess = input("Champion: ").lower()
    if guess.lower() == "nunu":
        guess = "nunu & willump"

    # Check if guess is a champion
    champions_lower = []
    for i in range(len(champions)):
        champions_lower.append(champions[i].lower())
    while guess.lower() not in champions_lower and guess != "give up":
        guess = input("This is not a champion. Please enter a champion: ").lower()

    # Guess checken en lijst maken van gerade champions
    while guess != champion and guess != "give up":
        guesses.append(guess)
        print("Guesses: ", end='')
        for i in range(0, len(guesses)):
            print(guesses[i].capitalize(), end=" ")
        print()
        guess = input("Not correct. Try again: ")
        while guess.lower() not in champions_lower and guess != "give up": # Check if guess is a champion
            guess = input("This is not a champion. Please enter a champion: ").lower()

    if guess == "give up":
        print(champion.capitalize())
        print()
    else:
        print("Correct!", end=" ")
        print(congrats_list[number3])
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
