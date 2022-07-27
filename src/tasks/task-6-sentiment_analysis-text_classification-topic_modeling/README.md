# Current plan 

## sentiment analysis

Two models were compared to our dataset of manual labels (199 labels) so that we can choose the model with the highest performance. The models were 

XLM-T and neuraly models. Both are available on huggingface. Both models yielded a very low performance. We couldn't compare the feel-it model because its sentiments contained only positive and negative. However, our manual labeling contained negative, neutral and positive. 

We have chosen the feel-it model. Firstly, we have found a high concordance between the manual label and feel-it label in the positive and negative classes. In addition, feel-it emotion is the only model that we found that provides emotions as well as sentiments. 

We have applied the emotion classification to our full long-covid dataset (around 22500 tweets). Next, we created word clouds and some exploratory data analysis for the tweets with their corresponding emotion. 





