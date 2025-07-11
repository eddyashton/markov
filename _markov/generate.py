import random


def generate_value(model, seed):
    random.seed(seed)
    l = []
    prev = "\n"
    while True:
        options = model[prev]
        choice = random.choices(
            list(options.keys()),
            weights=options.values(),
            k=1,
        )[0]
        if choice == "\n":
            break
        l.append(choice)
        prev = choice
    return "".join(l)


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
