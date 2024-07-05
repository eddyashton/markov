from tokenizers import Tokenizer
from tokenizers.models import BPE
from tokenizers.trainers import BpeTrainer
from tokenizers.pre_tokenizers import Whitespace


def pairs(s):
    return zip(s[:-1], s[1:])


def tokenise(s, tokenizer):
    tokens = ["\n"]
    for line in s.splitlines():
        tokens += tokenizer.encode(line).tokens
        tokens.append("\n")

    return tokens


def train_model(filename):
    print(f"Beginning training from {filename}")

    data = open(filename).read()

    tokenizer = Tokenizer(BPE(unk_token="[UNK]"))
    trainer = BpeTrainer(special_tokens=["[UNK]"], show_progress=False)
    tokenizer.train([filename], trainer)

    tokens = tokenise(data, tokenizer)
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
