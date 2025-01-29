# ChromaDB and Langchain for embedding and vector search

This is a simple example of how to use ChromaDB and Langchain to embed and vector search text.

## Setup

0. Install [uv](https://docs.astral.sh/uv/)

```bash
brew install uv
```

1. Install the dependencies with uv (see below for notes on Mac OS)

```bash
uv pip install
```

2. Run the script

```bash
uv run src/main.py
```

## Mac OS Notes

If you have an M1 series chip or later, you will need to do some additional setup to get the embedding model to work.

The `langchain-huggingface` package uses the PyTorch framework, which is not supported on the M series chips.

0. Ensure that you have XCode and developer tools installed. (I had to install XCode from the App Store to get this working. The usual `xcode-select --install` did not work for some reason.)

1. Install the PyTorch CPU version

```bash
uv pip add --pre torch torchvision torchaudio --extra-index-url https://download.pytorch.org/whl/nightly/cpu
```

You can verify that the installation was successful by running the following command:

```bash
uv run torch_test.py
```

More information can be foundhere: https://developer.apple.com/metal/pytorch/

2. Then install the langchain-huggingface package

```bash
uv pip install langchain-huggingface
```


## Notes

- The script will create a new ChromaDB collection add documents to it from the `prizes.json` file.
- The script will then vectorize the documents and store them in the ChromaDB collection.
- The script will then query the ChromaDB collection for the most similar documents to the query "What year did albert einstein win the nobel prize?"
- The script will then print the results.
- Expect the output to be:

```
{"year": "1921", "category": "physics", "laureates": [{"id": "26", "firstname": "Albert", "surname": "Einstein", "motivation": "\"for his services to Theoretical Physics, and especially for his discovery of the law of the photoelectric effect\"", "share": "1"}]}
```

With help from the following resources:

- https://how.wtf/how-to-use-json-files-in-vector-stores-with-langchain.html
- https://docs.astral.sh/uv/concepts/projects/dependencies/#index
- https://developer.apple.com/metal/pytorch/
- https://medium.com/@garysvenson09/how-to-use-sentence-transformers-in-langchain-projects-c279bb535e0f
- https://python.langchain.com/docs/integrations/text_embedding/sentence_transformers/
- https://medium.com/@dimitrios_/setting-up-a-langchain-on-your-m2-macbook-pro-a-mac-users-guide-f100688aa22d
