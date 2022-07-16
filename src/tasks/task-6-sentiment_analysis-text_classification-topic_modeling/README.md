# Current plan 

## sentiment analysis

1- use [XLM-T](https://huggingface.co/cardiffnlp/twitter-xlm-roberta-base-sentiment)  the multilingual model as a zero shot classification on our dataset


2- fine tune XLM-T  on our dataset

3- manually label a sample of our data  both for sentiment and binary classification
4- fine tune alberto-it on our data
5- compare models

## classification


1- use the manually labelled data that we have labelled above ==> long covid - no long covid
2- fine tune a model on our data for sequence classification like this [one](https://huggingface.co/llangnickel/long-covid-classification/blob/bd8eac3a20979689a8a3bcff2e64ac71f6b5cb4c/README.md)

