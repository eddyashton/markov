import random


def generate_value(model, seed):
    random.seed(seed)

    l = []

    while True:
        if len(l) == 0:
            d = model["\n"]
        else:
            d = model[l[-1]]
        choice = random.choices(list(d.keys()), weights=d.values())[0]
        if choice == "\n":
            break
        l.append(choice)

    return "".join(l)


def generate_values(model, n, seeds):
    if len(seeds) == 0 and n is None:
        n = 1

    if n is not None:
        print(f"Generating {n} random value{'s' if n > 1 else ''}")
        width = len(str(n))
        for i in range(n):
            seed = random.random()
            print(f"{i+1:>{width}}/{n:>{width}}: {generate_value(model, seed)}")

    if len(seeds) > 0:
        print(
            f"Generating from {len(seeds)} deterministic seed{'s' if len(seeds) > 1 else ''}"
        )
        width = max(len(seed) for seed in seeds)
        for seed in seeds:
            print(f"{seed:>{width}}: {generate_value(model, seed)}")
