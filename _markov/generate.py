import random


def generate_value(model, seed):
    random.seed(seed)
    return random.choice([chr(n) for n in range(ord("a"), ord("z") + 1)])


def generate_values(model, n, seeds):
    if len(seeds) == 0 and n is None:
        n = 1

    if n is not None:
        print(f"Generating {n} random value{'s' if n > 1 else ''}")
        width = len(str(n))
        for i in range(n):
            seed = int(random.random() * 1000)
            print(f"{i+1:>{width}}/{n:>{width}} [seed={seed:>3}]: {generate_value(model, seed)}")

    if len(seeds) > 0:
        print(
            f"Generating from {len(seeds)} deterministic seed{'s' if len(seeds) > 1 else ''}"
        )
        width = max(len(seed) for seed in seeds)
        for seed in seeds:
            print(f"{seed:>{width}}: {generate_value(model, seed)}")
