import requests
import json


def get_random_joke():
    data = requests.get(r"https://official-joke-api.appspot.com/random_joke")
    return json.loads(data.text)


def get_ten_random_jokes():
    data = requests.get(r"https://official-joke-api.appspot.com/random_ten")
    return json.loads(data.text)


def print_random_joke(joke):
    print(joke['setup'])
    print(joke['punchline'])


def print_ten_random_jokes(jokes):
    for joke in jokes:
        print(joke["type"])
        print(joke["setup"])
        print(joke["punchline"], end='\n')


if __name__ == '__main__':
    joke = get_random_joke()
    print_random_joke(joke)
