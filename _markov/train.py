import nltk


def pairs(s):
    return zip(s[:-1], s[1:])


def tokenise(s):
    tokens = ["\n"]
    for line in s.splitlines():
        tokens += nltk.tokenize.SyllableTokenizer().tokenize(line)
        tokens.append("\n")

    return tokens


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
