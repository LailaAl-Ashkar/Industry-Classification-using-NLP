# Industry-Classification-using-NLP

## Description:
You can think of the job industry as the category or general field in which you work. On a job application, "industry" refers to a broad category under which a number of job titles can fall. For example, sales is an industry; job titles under this category can include sales associate, sales manager, manufacturing sales rep, pharmaceutical sales and so on.

## Solution:
Choose a suitable supervised multi-class classifier to train the model and assign each job title to one and only one industry.

## Dataset:
1.	Dataset consists of 2 columns: job title -feature-, and industry -label- in a csv format of more than 8,500 samples.
2.	The dataset is imbalanced (Imbalance means that the number of data points available for different classes is different).

## Investigating and cleaning data:
1.	After exploring data, I found that there’s no null values. On the other hand, almost 54% of data was duplicated. I tried to drop all these duplicates and keep only unique values. However, it didn’t show a great promise and keeping duplicates gave higher performance.
2.	Also, text needed to be preprocessed to improve the training process. I started with lowering case the text, removed any word less than 2 character as it may be a useless symbol, removed all stop words, and then removed noise (non-ascii, digits, html tags, and white spaces).
3.	Dataset was imbalanced, for that I resampled the minority feature values to have the same distribution as the majority (OverSampling). This step was done after splitting data to keep Test data distribution the same.



## Model Selection:
Trying different models is the best thing to do while dealing with machine learning problem. I tried to train many models on the data and evaluate their performance. The full model is a pipeline with 3 stages:
1.	CountVectorizer: transform text data into a vector on the basis of the frequency.
2.	TfidfTransformer: learn the vocabulary and inverse document frequency weightings.
3.	The classifier it self
Comparing between different model evaluations showed that Extra Trees Classifier was the best model as it uses averaging to improve the predictive accuracy and control over-fitting.

## Model Evaluation:
Accuracy can be a deceptive metric and not give quite right indications. I tried to perform precision, recall, f1_score in addition to accuracy to make sure that the model performance is good.

## Limitations:
Data is biased towards some classes, even oversampling and text preprocessing wasn’t the best thing to make the model generalize.
