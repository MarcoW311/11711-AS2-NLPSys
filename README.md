# 11711-AS2-NLPSys

This repo is for 11711 assignment 2 at CMU. The task is scientific entity recognition, specifically in the domain of NLP papers from recent NLP conferences (e.g. ACL, EMNLP, and NAACL). We will need to identify entities such as task names, model names, hyperparameter names and their values, and metric names and their values in these papers.

## Steps to run the code
Install all required packages using following command:
```
pip install -r requirements.txt
```
Then run the following command to download spaCy corpus used for tokenization:
```
pip install https://github.com/explosion/spacy-models/releases/download/en_core_web_lg-3.6.0/en_core_web_lg-3.6.0.tar.gz
```

### Data Crawling
1. Run the web_crawler.py (src/data preparation/web_crawler.py). It will download all papers in PDF format from 2023 ACL to your local computer
2. Run the pdf2text.py (src/data preparation/pdf2text.py) to extract, pre-process, and tokenize all the text in a PDF file

### Model Fine-tuning
We uploaded a jupyter notebook file in "src/training/finetuning.ipynb". Execute the cell one by one to replicate our training process. P.S. You need to run:
```
accelerate config
```
to use accelerate. Otherwise the code will use CPU for training resource.