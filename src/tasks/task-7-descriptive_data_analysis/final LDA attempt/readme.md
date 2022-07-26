This folder will containt the code/results of final LDA entirely performed using gensim.

4 approaches used:
## 1. LdaModel on Full corpus (~25k tweets)
   - Includes elbow-method optimization for c_v and u_mass coherence measures (for deciding no. of topics) and the drawbacks faced if we rely on these metrics to decide optimum num_topics for our topic model.
   #### Results:
   - 6 topics after u_mass optimization via elbow method for overall corpus(~25k) were not suitable for interpretation.
   - 25 topics after c_v optimization. Such a topic number too high for interpretation and showed extreme overlap in terms of intertopic distance, so stuck with lower number to interpret results (num_topics=10). Still, topics were not clear.
     - Conclusion:
        1. Performance on full corpus together is not good despite making multiple passes thru corpus in the model and performing hyperparameter tuning. So in next attempts, work with divided corpus.
        2. Poor results may also be due to inherent limitations of standard LDA, namely that standard LDA does not do well with short documents (in our case, tweets). So, we should attempt dynamic topic modeling through sequential LDA model to check if results are better.

## 2. Create LdaModel on Q1 data (4698 tweets) 
   - This LDA Model is trained on Q1 data (July to September, 2021 data) of the corpus.
   #### Results: 6 good topics were found, as follows: <br>
       0. Discussion about scientific studies <br>
       1. Anxiety about pandemic and the information about it; specific people (like public figures) involved in the context of long-covid <br>
       2. Discussion about LC impact in terms of time periods <br>
       3. Discussion about  LC impact on patient life (impact on life so far or scope for lifelong impact) <br>
       4. Treatment scenario <br>
       5. Impact/Consequences of LC on children <br>
   * It was found that distribution was quite good (i.e. when a tweet was given to the model, it assigned more weightage to the topics actually covered by the tweet and less weightage to other topics). The results of this test in text form is available in **Topic dist of test tweets_Q1_data.txt** file. <br>
   * Thus, this is a good model to train the rest of the corpus (Q2 to Q4 data) with sequential LDA model. This model is considered the pretrained model and provided as input to sequential LDA Model.
    
## 3. Sequential LdaModel on Q2 to Q4 data (20,454 tweets) 
   - Method 1: Directly creating Sequential LDA model on this data, where time_slices correspond to Q2, Q3 and Q4 respectively.
      - **Results:** No drastic changes in topic evolution over time were observed (topics of each slice are in the *ldaseq_slices* sheet of Excel workbook). This means in our corpus there isnt a huge change in the topics people talk about over the quarters. Maybe with a larger study period, we would see greater changes.
   - Method 2: Providing LdaModel trained on Q1 data to a Sequential LDA model on Q2 to Q4 data, where time_slices correspond to Q2, Q3 and Q4 respectively.
      - **Results:** <faced reproducibility issue; it has been addressed; will update results by tomorrow.>

## 4. LdaModel on Q2 to Q4 data (20,454 tweets) 
   - Create LDAModel on Q2 to Q4 data using hyperparameters of the pretrained model (i.e. LdaModel trained on Q1 data).
   - **Results:** <faced reproducibility issue; it has been addressed; will update results soon by tomorrow.>



  

