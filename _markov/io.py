import json
import os


def save_model(model, filename):
    dirname = os.path.dirname(filename)
    if not os.path.exists(dirname):
        print(f"Directory {dirname} doesn't exist - creating it now")
        os.makedirs(dirname, exist_ok=True)

    print(f"Saving model to {filename}")
    json.dump(model, open(filename, "w"), indent=2)


def load_model(filename):
    print(f"Loading model from {filename}")
    return json.load(open(filename, "r"))
