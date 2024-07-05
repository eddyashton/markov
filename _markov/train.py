import math


def pairs(s):
    return zip(s[:-1], s[1:])


def double_letters(s):
    return [s[2 * i : 2 * i + 2] for i in range(math.ceil(len(s) / 2))]


def train_model(filename):
    print(f"Beginning training from {filename}")

    data = open(filename).read().splitlines()

    model = {}
    for line in data:
        src = ["\n"] + double_letters(line) + ["\n"]
        for this_char, next_char in pairs(src):
            if this_char not in model:
                model[this_char] = {}

            probabilities = model[this_char]

            if next_char not in probabilities:
                probabilities[next_char] = 0

            probabilities[next_char] += 1

    print(f"Training complete")

    return model
