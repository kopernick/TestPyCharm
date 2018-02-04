from random import choice


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
