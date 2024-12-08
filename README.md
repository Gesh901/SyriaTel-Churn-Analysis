# SyriaTel-Churn-Analysis

![Title Image](https://github.com/Gesh901/SyriaTel-Churn-Analysis/blob/master/Churn.jpeg)

## Business Overview

Customer churn analysis has recently become increasingly important in the ever evolving and competitive telecommunication industry. Customer churn analysis involves the study of customer behaviour to identify patterns and factors that lead to customers leaving their providers. As the cost of getting a new customer is five to twenty-five times more than keeping an existing customer, telecommunication as well as mobile operators see the need to pay more attention to retaining existing customers to increase their revenues.

There are myriads of reasons why a customer might leave such as high prices, poor network coverage or customer service. However, one of the most common reasons cited is customers simply getting a better deal elsewhere, especially in markets where there is a lot of competition. Therefore, understanding these churn drivers, even though it’s not straight forward, is critical for not just knowing why customers leave but identifying the warning signs of customers about to terminate contracts or switch providers.

Thus, accurate prediction of customer’s behaviours, using machine learning solutions assists companies in identifying necessary actions to be incorporated into their customer retention management, such as whether to improve the service experience, design proactive campaigns to boost adoption, or re-engage at-risk customers. 

##  Problem Statement

SyriaTel, a telecommunications company in Syria, would like to predict whether a customer will (“soon”) stop doing business with them(“churn”). As such, it would like to get an understanding of the customers' behaviour and accurately pre-empt whether they will stop using their services.

## Objectives

Objectives for this analysis are as set out below:
 - Build a predictive model that has shows whether a customer will churn based on the customer data
 - Identify the key factors affecting customer churn amongst SyriaTel customers
 - Identify what aspects of SyriaTel services need more prioritization to prevent customer churn.


## Metrics of success

The chosen predictive model will be evaluated agains the following metrics. These metrics have been derived based on previous studies done on customer churn analysis and as such, each is a range to cater for the variation in the study results:
 - `Accuracy`: Measures the total number of correctly identified instances. An accuracy of between 75% and 85% is desired.
 - `Precision`: Measures how the predictive model is observing the actual number of positives against the predicted positives. A precision of between 50% and 60% is desired.
 - `Recall`: Measures the predictive model's ability to correctly identify churners. A recall of between 60% and 70% is desired.
 - `F1-score`: Measures how accurate the predictive model’s performance is. A F1 score of between 0.55 and 0.65 is highly desirable
 - `Area under the curve (AUC)`: A higher result indicates a more accurate model performance. 
 
 ## Data Understanding
 
 The SyriaTel dataset used in this analysis is sourced from Kaggle (https://www.kaggle.com/) and contains records of SyriaTel customers. The dataset contains 3,333 rows with each row representing a customer record. 
In addition, the dataset has twenty-one columns which broken down as follows:
 - i.	Customer usage: The following columns provide further insight to the customer phone usage based on time of day:
  - a.	Usage during the day - `total day minutes`, `total day calls`, `total day charge`
  - b.	Usage during the evening - `total eve minutes`, `total eve calls`, `total eve charge`
  - c.	Usage at night - `total night minutes`, `total night calls`, `total night charge`
  - d.	No of voicemail messages - `number vmail messages`
 - ii.	Plan subscription: These columns give us a view of the plans that each of the customer has:
  - a.	`international plan`
  - b.	`voice mail plan`
 - iii.	Unique customer details. The columns falling under this section are:
  - a.	`state`
  - b.	`account length`
  - c.	`area code`
  - d.	`phone number`
 - iv.	International phone usage/customer service: The columns under this category include:
  - a.	`total intl calls`
  - b.	`total intl minutes`
  - c.	`total intl charge`
  - d.	`customer service calls`
 - v.	Likelihood of churn: Column `churn` which takes on two values:
  - a.	True – Customer has churned.
  - b.	False – Customer is yet to churn.


## Exploratory Data Analysis
Exploratory data analysis was done to get further insights on SyriaTel customer behaviour as well as check which columns will be suitable to function as features and target variables while building the predictive model. The exploratory data analysis is divided into three sections:
1.	Univariate analysis – Examining the distinctive features independently.
2.	Bivariate Analysis - Examining the relationship between two features.
3.	Multivariate Analysis – Examining the relationship between more than two features.

## Model Building and Evaluation:
Given this is a classification problem, the analysus uses Logistic regression and Decision Tree algorithms to build the predictive model. The approach will be to start with a baseline model and refine it to get the model with the best performance. Metrics for evaluation used will be precision, recall, accuracy, F1 score and AUC score.

The model evaluation findings have been compiled and plotted to get a better view of how the models compare against each other as well as against our success metrics as shown in the bar plot.

![Evaluation of models](https://github.com/Gesh901/SyriaTel-Churn-Analysis/blob/master/output_110_0.png)

  
From the analysis, decision tree models perform better than the logistic regression models. Additional check is how the models performed against our metrics of success:
 - Accuracy of between 75% and 85% is desired: All the models evaluated were able to meet this threshold
 - Precision of between 50% and 60% is desired: Only the baseline logistic model and the decision tree models met this threshold. The baseline logistic regression model was within this range while both decision tree models (unpruned and pruned) were able to surpass it.
 - Recall of between 60% and 70% is desired. All the models were able to meet this criterion except the baseline logistic regression model. Logistic models containing tuned hyper parameters performed the best i.e. model with alternative solver, model with balanced weights and model with less regularization
 - F1 score of between 0.55 and 0.65 is highly desirable: Only the decision tree models were able to meet this criterion. Due to the precision scores being low, all logistic regression models had a F1 score less than 0.5
 - Area under the curve (AUC): A higher result indicates a more accurate model performance. The pruned decision tree had the highest AUC. However, the differences observed across all models evaluated was quite minimal.

Taking all this account, the pruned decision tree model meets all the metrics of success. It strikes a balance across precision and recall. Thus, it will be able to give a balanced view of customers who will churn as well as those who will not churn. Also, the accuracy score and the AUC is the highest making it the model that has the most accurate predictive performance.

## Recommendation
Below are the business recommendations for SyriaTel based on the analysis performed:
 - SyriaTel should go for the pruned decision tree model when predicting whether a customer will churn. It will be able to give the most accurate predictive view of customers who will churn. This model provides a balanced view across all the evaluation metrics, and it is easy to interpret the model results to stakeholders in the company.
 - Key factors making customers leave SyriaTel are high international calling charges, day charges and poor customer service. Customers who left made the highest number of day and international calls, but their charges were still quite high. In addition, customers who made more calls to customer service were more likely to leave as opposed to those who did not.
 - SyriaTel can reduce customer churn by reducing their day and international calling charges as they seem to be highly uncompetitive. They could produce discount schemes to reward customers who call more often. It should also improve on their customer service through training of its customer care agents. Finally, it should improve its service in general across the board to ensure calls by customers to customer care are reduced to a minimum.


## Conclusion
This analysis looked at SyriaTel customer data to determine a predictive customer churn model. In addition, customer's patterns have been studied to determine the reason behind customers leaving and ways in which this can be mitigated. The pruned decision tree model has been found to be the best predictive model for the data analysed as it gives the most accurate and balanced view of when a customer will churn. Moreover, customers in SyriaTel churned because of high calling charges as well as poor customer service. It is imperative for the company to offer deals in the form of discounts to customers who call much more often and improve their customer service by training their customer service agents.

## Next Steps
- Deployment of the model to end users is the next step. The model will be exported into a format suitable for integration through embedding it into a software application (such as web or mobile application) where end users can input their data and receive predictions.

- Other sophisticated models need to be considered such as Random Forest, XG Boost to get better predictive performance. In addition, a much bigger dataset should be sought to increase the training and predictive power of the models.





