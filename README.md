# Markov Chains

A test project for exploring and experimenting with Markov chain generation of strings


## Plan

- [X] Discuss Markov chains
  - [X] [Markov chains on Wikipedia](https://en.wikipedia.org/wiki/Markov_chain)
  - [X] String generation from a Markov state machine (Q!)
  - [X] Procedural generation, learnt models, generative AI
- [X] Clone local copies of this repo in Codespaces
  - [X] Python REPL (Read-Eval-Print-Loop)
- [X] Repo walkthrough
  - [X] Basic CLI
  - [X] Separated steps for ease of testing
  - [X] Sample data files and test files to look at later
  - [X] Determinism and pseudo-randomness
- [ ] Implement `generate_value()`, with a hand-built hard-coded model value
  - [ ] Loop
  - [ ] Tombstone values
  - [ ] [Python random module](https://docs.python.org/3/library/random.html)
  - [ ] Weighted randomness
  - [ ] [random.choices](https://docs.python.org/3/library/random.html#random.choices)
  - [ ] Loop termination
  - [ ] String concatenation
- [ ] Implement `train_model()`
  - [ ] Pairs of characters
  - [ ] Nested dict construction, access
  - [ ] printf debugging
- [ ] Testing it out
  - [ ] How to measure quality?
  - [ ] Case-sensitivity
  - [ ] Structured vs unstructured? Spectrum of structure?
  - [ ] Pathological cases we can't handle at all?
- [ ] Tokenisation
  - [ ] String-generation from multi-character atoms
  - [ ] Manually finding pairs?
  - [ ] Manually finding ngrams?
  - [ ] Which ones to keep?
  - [ ] 3rd party libraries, existing tokenizers
  - [ ] [NLTK](https://www.nltk.org/api/nltk.tokenize.html#module-nltk.tokenize)
  - [ ] [HuggingFace](https://huggingface.co/docs/tokenizers/index)
  - [ ] Byte-Pair Encoding to produce a fixed-size vocabulary
  - [ ] Using HuggingFace's BpeTrainer for our Markov generator
