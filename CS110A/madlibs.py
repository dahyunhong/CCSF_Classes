import random


def getPeople():
    return ['Jesse', 'Diana', 'olando', 'Lisa', 'jacob', 'Kevin', 'Ten']


def getPlaces():
    return ['Korea', 'Mexico', 'America', 'Japan', 'China', 'San Francisco', 'San Jose']


def getAdjectives():
    return ['quick', 'careful', 'easy', 'happy', 'gentle', 'true']


def getPlurals():
    return ['children', 'teeth', 'feet', 'people', 'cats', 'women', 'men', 'mice', 'leaves']


def getVerbs():
    return ['run', 'go', 'play', 'sing', 'hide', 'hit', 'fight', 'spend', 'spread', 'cook']


def getFood():
    return ['apple', 'ham', 'carrot', 'banana', 'noodle', 'ramen', 'peanut', 'olive', 'almond']


def getNouns():
    return ['pillow', 'flower', 'bag', 'computer', 'air conditioner', 'paper', 'closet']


def getRandom(list):
    return random.randrange(len(list))


def generateMadLib(people, places, adjectives, plurals, verbs, food, nouns):
    person = people[getRandom(people)]
    first_place = places[getRandom(places)]
    second_place = places[getRandom(places)]
    adjective1 = adjectives[getRandom(adjectives)]
    adjective2 = adjectives[getRandom(adjectives)]
    plural1 = plurals[getRandom(plurals)]
    plural2 = plurals[getRandom(plurals)]
    verb = verbs[getRandom(verbs)]
    noun = nouns[getRandom(nouns)]
    food = food[getRandom(food)]

    string = (
        f"Last summer, "
        f"we went for a vacation with {person} on a trip to {first_place}.\n"
        f"The weather there is very {adjective1}!\n"
        f"Northern {first_place} has many {plural1}, \n"
        f"and they make {plural2} there.\n"
        f"Many people also go to the {second_place} to {verb}.\n"
        f"The people that live there love to eat {food}. \n"
        f"They also like to {verb} in the sun and swim in the {noun}.\n\n"
        f"It was a really {adjective2} trip!\n"
    )

    print(string)


def main():
    people = getPeople()
    places = getPlaces()
    adjectives = getAdjectives()
    plurals = getPlurals()
    verbs = getVerbs()
    food = getFood()
    nouns = getNouns()

    generateMadLib(people, places, adjectives, plurals, verbs, food, nouns)


main()
