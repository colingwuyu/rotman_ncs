# NCS Package - Machine Learning in Business

![Python package](https://github.com/colingwuyu/rotman_ncs.git/actions/workflows/python-package.yml/badge.svg)
[![PyPI version](https://badge.fury.io/py/ncs.svg)](https://pypi.org/project/rotman-ncs)

The NCS package is designed for a case study in the "Machine Learning in Business" course at UoT Rotman. The goal of this project is to demonstrate the potential of Natural Language Processing (NLP) tools for extracting valuable insights from unstructured text data.

Utilizing earning call transcripts from S&P 500 constituents, we develop an effective investment strategy and measure its performance against the S&P 500 index.

## Data Description

The data used in this case study is comprised of earnings call transcripts and historical adjusted stock prices for S&P 500 constituents, collected from Fool.com and Yahoo Finance respectively, from the years 2018 to 2023.

The transcript data includes speaker identities and titles, which allows us to differentiate between the comments of, for example, a CEO and a financial analyst.

## Methodology

We explore the evolution of NLP techniques, from traditional methods to sophisticated large language models. We demonstrate their application to real-world data, charting the journey from basic bag-of-words models to sentiment analysis and topic modelling.

The NLP techniques used in this study are:

- **TF-IDF (Term Frequency-Inverse Document Frequency)**: This method, though older, effectively shows how important a word is to a document in a corpus.
- **Word2Vec**: This technique creates dense vector representations of words, capturing their semantic relationships.
- **BERT (Bidirectional Encoder Representations from Transformers)**: BERT uses transformers to understand the context of words in all directions.
- **Large Language Models**: Trained on vast amounts of text data, these advanced models are capable of generating coherent text, understanding sentiment, completing prompts, and more.

Additional methods used for feature extraction are sentiment analysis and topic modelling.

## Expected Outcome

Using the insights derived from these NLP techniques, we construct an investment strategy. This strategy uses sentiment scores, main topics, and contextual embeddings from earning calls to predict future stock returns, showing the practical application of NLP in investment decision-making. The performance of this strategy is compared to the S&P 500 index.

## Code Structure

- The `ncs.data` module provides functions such as `load_stock_history`, `load_call_description`, and `load_call_statements` to handle data operations. The earnings call data is already split into training and testing datasets.
- The `ncs.model` module is used to train models and make predictions from the extracted numerical features. It provides `train` and `inference` procedures.
- The `ncs.call_strategy` module is for running the investment strategy. It evaluates the performance of the built model and strategy.

## Enjoy the Learning and Investing
