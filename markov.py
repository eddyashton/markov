#!/usr/bin/env python3

import argparse

from _markov.io import save_model, load_model
from _markov.train import train_model
from _markov.generate import generate_values


def train_and_generate(args):
    print("-=[ Running training and generation ]=-")
    model = train_model(args.input_file)
    generate_values(model, args.n, args.seeds, args.porcelain)


def train_only(args):
    print("-=[ Running training only ]=-")
    model = train_model(args.input_file)
    save_model(model, args.model_file)


def generate_only(args):
    print("-=[ Running generation only ]=-")
    model = load_model(args.model_file)
    generate_values(model, args.n, args.seeds, args.porcelain)


def main():
    parser = argparse.ArgumentParser(
        description="Markov chain tool. Use subcommands to do training or generating in isolation."
    )

    subparsers = parser.add_subparsers(
        title="Sub-commands",
        dest="subcommand",
        required=True,
    )
    train_and_generate_parser = subparsers.add_parser(
        "train_and_generate",
        aliases=["tag"],
        help="Train and generate",
    )
    train_and_generate_parser.set_defaults(func=train_and_generate)

    train_parser = subparsers.add_parser(
        "train",
        aliases=["t"],
        help="Train only, dumping learned model to file",
    )
    train_parser.set_defaults(func=train_only)

    generate_parser = subparsers.add_parser(
        "generate",
        aliases=["g"],
        help="Generate only, loading previously learned model from file",
    )
    generate_parser.set_defaults(func=generate_only)

    # Arguments for training
    for sub_parser in (train_and_generate_parser, train_parser):
        sub_parser.add_argument(
            "input_file",
            help="File containing data to learn model from",
        )

    # Arguments for training-only mode
    train_parser.add_argument(
        "model_file",
        help="File where learned model should be written to",
    )

    # Arguments for generating-only mode
    generate_parser.add_argument(
        "model_file",
        help="File where learned model should be read from",
    )

    # Arguments for generating and both
    for sub_parser in (train_and_generate_parser, generate_parser):
        sub_parser.add_argument(
            "seeds",
            help="Explicit seeds to generate from, for repeatable results",
            nargs="*",
        )
        sub_parser.add_argument(
            "-n",
            help="Number of random generations to perform. Defaults to 1, if no explicit seeds are passed",
            type=int,
        )
        sub_parser.add_argument(
            "--porcelain",
            "-p",
            help="Print unformatted raw values, suitable for pasting into a data file",
            action="store_true",
        )

    args = parser.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
