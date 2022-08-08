# Fairness-Monitor

In this project we have created an training framework, an plotting function for our datasets and an visualization framework for evaluating different fairness metrics. 

The developed training framework can train machine models on the ACIncome Task.

The developed visualization framework can dynamically generate plots from given parameters by displaying related data from metric files. 

Furthermore, two dashboards are created.
One serves as an interface for the training framework and allows the user to generate new data from certain predefined options.
The other one serves as an interface for the visualization framework and allows the user to easily explore our collected metrics.


The focus of this work is to allow students and researchers of AI fairness to explore how changes in temporal and/or spatial context can affect the fairness and performance of a model, as measured by various metrics. 
Recent research has shown that the interpretation of the fairness of classification models and datasets drastically depends on such context. (e.g. https://arxiv.org/abs/2206.11436 )

For this reason we chose the ACIncome problem, which is similiar to the 'Adult Dataset' often used in fairness evaluations.

It uses updated data from the US Census to predict the income of a person. The problem is a binary classification problem. People with a income less than a threshold are put into class 0, while people with income above the threshold are put into class 1.

The goal of the model is to predict to which class each data sample(person) belongs to.



This is the 'performance' perspective on the problem. However a 'fairness' perspective can also be viewed.

"Is a non-white person equally as likely to be above the threshold?"

A seemingly easy question, but in practice evaluating if this is true or not is difficult. This gets even more complicated when we use machine learning (ML). Now we have an (often) blackbox model that gives no explanations for its choices.



Various studies have found that ML models often contain biases (especially against already discriminated groups). This has consequences in the real world. (e.g. see COMPAS)



This is where 'fairness-aware' machine models take the spot. They are actively working against biases and prejudices in their predictions.

We wanted to evaluate what influence context (spatial and temporal) has on these models.

e.g. Does a model trained on data from 2014 work better than a model trained on data from 2017 when predicting data from 2018

With this framework many of the basic steps to answering this question are already taken. Our intention is for this project to help the study of these effects.


This project started as part of a FU Berlin Softwareproject in the summer semester 2022.

This Repository contains the finished and refined parts of our project.
However we also have a google folder, where older stuff etc. can be found.

Authors:

Jonas Schäfer

Marius Wawerek

Tolga Yurtseven
