<b>Experiments on wordcloud generation and extraction of keywords.</b>
- definition of  an italian stopword list (stopwords-it_final.txt, 644 words). This is extended with more custom words, inside the notebooks
-   generate_word_cloud_from_tweets.ipynb (generation from text (i.e. token frequency on the whole text made by the concatenation of (cleaned tweets)))
-   generate_wordclouds_extract_keywords.ipynb (contains the code of the previous nb plus code to generate wordcloud and extraxt keywords with the TF-IDF method and also to extract keywords with the RAKE method)
- In results folder an analysis on time windows: half-year analysis and quarterly analysis
- keyword_time_series_v2.ipynb is an anlysis of keywords evolution from July 2021 to July 2022 on a quarterly scale. One or more keywords evolution can be visualized. The word frequency can be calculated by the whole batch of tweets in a quarter (whole_text option) or with the TF-IDF method (where term frequency is of uni-gram bi-grams and Document is a single tweet). 
stopwords-check.txt is an auxiliary file loaded in keyword_time_series_v2.ipynb and containing all the stopwords of stopwords-it_final.txt plus a bunch of custom stopwords, corresponding to high frequent but unininformative terms (as an example Covid, covid-19,..). In total the file contains 702 stopwords.
