import random


def generate_value(model, seed):
    random.seed(seed)
    s = ["\n"]
    while True:
        current_state = s[-1]
        probabilities = model[current_state]
        choice = random.choices(list(probabilities.keys()), weights=list(probabilities.values()))[0]
        if choice == "\n":
            break
        s += [choice]

        "running" => "run", "ning"

    return ' '.join(s).strip()


def generate_values(model, n, seeds, porcelain=False):
    if len(seeds) == 0 and n is None:
        n = 1

    if n is not None:
        print(f"Generating {n} random value{'s' if n > 1 else ''}")
        width = len(str(n))
        for i in range(n):
            seed = int(random.random() * 1000)
            value = generate_value(model, seed)
            if porcelain:
                print(value)
            else:
                print(
                    f"{i+1:>{width}}/{n:>{width}} [seed={seed:>3}]: {generate_value(model, seed)}"
                )

    if len(seeds) > 0:
        print(
            f"Generating from {len(seeds)} deterministic seed{'s' if len(seeds) > 1 else ''}"
        )
        width = max(len(seed) for seed in seeds)
        for seed in seeds:
            value = generate_value(model, seed)
            if porcelain:
                print(value)
            else:
                print(f"{seed:>{width}}: {generate_value(model, seed)}")
