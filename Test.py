from random import choice


def get_days():
    days = ['mon', 'tue', 'wed', 'thurs', 'fri', 'sat', 'sun']
    return days


def get_random_report():
    weather = ['sunny', 'lovely', 'cold']
    return weather[choice.randint(0, len(weather) - 1)]


class Person:
    def __init__(self, name):
        self.name = name
        self.greeting = 'Hi {name}'

    def __str__(self):
        return self.make_greeting

    @property
    def make_greeting(self):
        return self.greeting.format(name=self.name)


def main():
    people = [
        Person('Jane'),
        Person('Jill'),
        Person("Bob")
    ]
    person = choice(people)
    print(person)


if __name__ == "__main__":
    main()
