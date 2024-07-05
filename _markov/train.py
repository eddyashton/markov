import math
from collections import defaultdict
import nltk


def pairs(s):
    return zip(s[:-1], s[1:])


def double_letters(s):
    return [s[2 * i : 2 * i + 2] for i in range(math.ceil(len(s) / 2))]


MAX_NGRAM_SIZE = 6


def ngrams(s, n):
    for i in range(0, len(s) - n + 1):
        yield s[i : i + n]


def find_tokens(s):
    counts = defaultdict(int)
    for ngram_size in range(1, MAX_NGRAM_SIZE):
        for ngram in ngrams(s, ngram_size):
            counts[ngram] += 1

    sorted_counts = sorted(list(counts.items()), key=lambda p: p[1], reverse=True)

    tokens = [sc[0] for sc in sorted_counts]
    return tokens


def find_best_token(s, i, ranked_tokens):
    candidates = [s[i : i + n] for n in range(1, MAX_NGRAM_SIZE)]
    candidate_indices = [ranked_tokens.index(candidate) for candidate in candidates]
    index_of_min = candidate_indices.index(min(candidate_indices))
    return candidates[index_of_min]


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
