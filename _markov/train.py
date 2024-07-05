import math


def pairs(s):
    return zip(s[:-1], s[1:])


def double_letters(s):
    return [s[2 * i : 2 * i + 2] for i in range(math.ceil(len(s) / 2))]


def tokenise(s):
    if not s.startswith("\n"):
        s = "\n" + s
    if not s.endswith("\n"):
        s = s + "\n"

    return list(s)


def train_model(filename):
    print(f"Beginning training from {filename}")

    data = open(filename).read()

    tokens = tokenise(data)
    model = {}
    for this_token, next_token in pairs(tokens):
        if this_token not in model:
            model[this_token] = {}

        probabilities = model[this_token]

        if next_token not in probabilities:
            probabilities[next_token] = 0

        probabilities[next_token] += 1

    print(f"Training complete")

    return model
