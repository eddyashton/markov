# Markov Chains

A test project for exploring and experimenting with Markov chain generation of strings


## Plan

- [ ] Discuss Markov chains
  - [ ] [Markov chains on Wikipedia](https://en.wikipedia.org/wiki/Markov_chain)
  - [ ] String generation from a Markov state machine
  - [ ] Procedural generation, learnt models, generative AI
- [ ] Clone local copies of this repo in Codespaces
  - [ ] GitHub accounts
  - [ ] IDEs, VSCode, Codespaces
  - [ ] Python REPL (Read-Eval-Print-Loop)
  - [ ] Terminal 101
- [ ] Repo walkthrough
  - [ ] Basic CLI
  - [ ] Separated steps for ease of testing
  - [ ] Sample data files and test files to look at later
  - [ ] Determinism and pseudo-randomness
- [ ] Implement `train_model()`
  - [ ] Pairs of characters
  - [ ] Nested dict construction, access
  - [ ] printf debugging
- [ ] Implement `generate_value()`, with a hand-built hard-coded model value
  - [ ] Loop
  - [ ] Tombstone values
  - [ ] [Python random module](https://docs.python.org/3/library/random.html)
  - [ ] Weighted randomness
  - [ ] [random.choices](https://docs.python.org/3/library/random.html#random.choices)
  - [ ] Loop termination
  - [ ] String concatenation
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
