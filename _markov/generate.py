import random


def generate_value(model, seed):
    random.seed(seed)
    return random.choice([chr(n) for n in range(ord("a"), ord("z") + 1)])


def generate_values(model, n, seeds):
    if len(seeds) == 0 and n is None:
        n = 1

    if n is not None:
        width = len(str(n))
        for i in range(n):
            seed = random.random()
            print(f"{i+1:>{width}}/{n:>{width}}: {generate_value(model, seed)}")

    width = max(len(seed) for seed in seeds)
    for seed in seeds:
        print(f"{seed:>{width}}: {generate_value(model, seed)}")
