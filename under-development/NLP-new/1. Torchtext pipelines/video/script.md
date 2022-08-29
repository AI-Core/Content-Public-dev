- popeline function
- several pre-build pipelines
  - sentiment-analysis
  - zero-shot classification
  - text generation
  - fill-mask
  - question answering
  - summarisation
  - translation
- you can specify the model in the pipeline
- when initialising or calling different pipelines you can specify kwarg arguments to change their behaviour
  - specify model in text generation
  - specify top_k in ner
  - grouped-entities
- create and instance of it

- types of transformer models
- auto-regressive models like GPT
- auto-encoding models like BERT
- sequence-to-sequence models like

# transformers

_show transformer diagram_

- encoder on the left
- decoder on the right
- encoder creates embeddings using bidirectional self-attention
- the decoder also takes in text
- it is unidirectional and typically autoregressive
- it uses masked self-attention
- combining them gives a encoder-decoder architecture
- also known as seq-to-sqe
- the encoder gives a high-level output which it shares with the encoder
- the encoder then produces a prediction which it stores and uses to make the next predictions

# encoders

- BERT is the most popular encoder model
- encoder generates an embedding of each word
- 768 for bert by default
- the representations are not just isolated embeddings, but are contextualised based on the surrounding words
- all of the context contribute to the value of the embedding
- so they represent the meaning of the word within the text
- encoders are extremely powerful for generating these embeddings
- encoders can be used for many tasks
  - sequence classification
  - masked language modelling
    - one of the ways that BERT was trained
    - bidirectionality is important for providing context

# decoders

- similar to encoders but typically little worse performance
- GPT(2/3?) is a decoder
- they generate an embedding for each word
- decoder uses masked self-attention
- this is because it is not bidirectional
- they are autoregressive
- the mask hides the context in one direction
- hence the representation of each word does not contain information from the hidden context
- we typically call the hidden context the right or left context
- they are powerful for problems where the right-context is hidden such as causal language modelling

# encoder-decoder architectures

- T5 is an example
- the encoder encodes the prompt and passes it to the encoder
- decoder receives output of encoder as well as the start word
- ENC-DEC can handle sequence to sequence tasks including tasks where num inputs number of inputs and outs can be differetns
- such as translation or summarization
- dec does not have to share weights with enc
- you can pull different combinations of enc-decs off the shelf

# TODO what is self-supervised data?

# TODO what are zero shot predictions?

# TODO what is NER?

<!--
TODO remove below in place of huggingface replacing as standard
 # What is Torchtext?

- NLP datasets
- text processing pipelines
- NLP operators

## Datasets

#

# Typical workflow

- preprocessing
  - define in fields
- file loading
  - use tabularDataset
- bucket iterator for batching and padding
- numericalisation
- embedding lookup

# creating a dataset

- be careful of the deprecated docs which still show up in search

- build vocab from training dataset which was created from fields
  - sets a .vocab attribute of each field
- compare situations when you might build from iterator vs from tabular

  - iterator: many large files too big to open and store in RAM

- create iterators from BucketIterator
- why? so you can ierate through them and pad them

- using pretrained GloVE in build_vocab -->

# TODO what is spacy?

# TODO insert glove embeddings into model building a model

# TODO other tokenizers from spacy and what they do

# TODO JIT

# TODO torchscript

# TODO distributed training
