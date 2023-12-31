# NCS Package - Machine Learning in Business

![Build and Test](https://github.com/colingwuyu/rotman_ncs/actions/workflows/python-build.yml/badge.svg)
![Publish](https://github.com/colingwuyu/rotman_ncs/actions/workflows/python-publish.yml/badge.svg)
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

## Python Package

This Python package, `rotman-ncs`, contains a suite of functions for working with financial earnings call data. The functions are broken down into three categories: data loading, model training and inference, and strategy execution and analysis.

### Data Loading

There are four main functions for loading different types of data:

1. `load_call_description(data_type='train')`: Loads earnings call description data from the specified data type. The `data_type` parameter is a string that specifies the type of data to load, either 'train' or 'test'.

2. `load_call_statements(data_type='train')`: Loads earnings call statements data from a specified data type. Again, the `data_type` parameter can be either 'train' or 'test'.

3. `load_stock_history()`: Loads the stock price history data.

4. `load_stock_returns_on_calls(data_type='train')`: Loads stock returns on calls data, with `data_type` specifying the type of data to load.

```python
# Load training data
call_descriptions = ncs.load_call_description(data_type='train')
call_statements = ncs.load_call_statements(data_type='train')
stock_history = ncs.load_stock_history()
stock_returns = ncs.load_stock_returns_on_calls(data_type='train')
```

### Model Training and Inference

The `train` function is used to train a model using the provided feature files and parameters. The `inference` function uses the trained model to generate actions for the test set.

```python
# Train model
ncs.train(feature_files=[list_of_feature_files])

# Perform inference
ncs.inference(feature_files=[list_of_feature_files], model_file='model.pkl', action_file='actions.csv')
```

### Strategy Execution and Analysis

These functions are used to execute investment strategies and analyze their performance:

1. `ncs.run_strategy(action_file, holding_period, log_file, save_portfolio_path)`: Runs the investment strategy using the provided action file, holding period, log file, and save portfolio path.

2. `ncs.report_strategy_analysis(actions, portfolio, holding_period, model_name)`: Generates a report of the strategy analysis for a given set of actions and portfolio.

3. `ncs.demo_benchmark(strategy, holding_period)`: Runs a benchmark strategy, either 'spy' or 'random', with a specified holding period.

```python
# Run strategy
ncs.run_strategy(action_file='actions.csv', holding_period=5)

# Generate strategy report
ncs.report_strategy_analysis(actions='actions.csv', portfolio='portfolio.parquet', holding_period=5)

# Generate benchmark strategy report
ncs.demo_benchmark(strategy='random', holding_period=5)
```

The key dataset used in the case study is the `call_statements` DataFrame, which contains unique identifiers (`statement_uid`, `call_uid`), as well as text data (`text`, `clean_text`). The `text` field is original call transcript and the `clean_text` field is processed by several text cleaning steps. Apply different NLP models to convert them into numeric features that can be consumed by the model training functions. These features are then used to inform the investment strategies with the trained model.

## Usage and Examples

Please refer to the following notebooks for detailed examples and usage instructions:

- [TF-IDF Solution Notebook](https://colab.research.google.com/drive/1JYQK1IfBEBkOKRbAnNChC-aZrQsUcfGu?usp=sharing)
- Word2Vec Solution (Coming Soon)
- BERT Solution (Coming Soon)
- LLM (Language Model) Solution (Coming Soon)

These notebooks demonstrate how to utilize different NLP techniques for processing text data and building investment strategies.

Make sure to follow the instructions provided in each notebook for proper setup and execution of the code.

If you have any questions or need further assistance, please feel free to reach out.

Happy coding!

## Enjoy the Learning and Investing 🥳
