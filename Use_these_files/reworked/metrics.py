# -*- coding: utf-8 -*-
"""Metrics.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/17YQlrjI02O6HCOC6D_fc8JZtn3lALDjB

In this notebook, the third step of the structogram is implemented, which comes right after the model was run on a test dataset, and uses the models' predictions to calculate useful metrics for fairness and performance evaluation.

The output of this step is an object containing all values for the selected metrics. Additionally, bonus information can be passed on for later steps.
"""

# imports
from abc import abstractmethod, ABC

import numpy as np

class MetricDictionary():
    """
    A dictionary wrapper for name:value pairings of evaluated metrics.
    An object of this class will be passed to later steps requiring access to
    the evaluated metrics.
    """

    def __init__(self, model_name, metric_dict):
        """
        Initialize a MetricDictionary object with the given properties.

        TODO: add default model name with timestamp
              @Marius:  maybe ask the user for a model name earlier and pass it on
                        to this step via bonus information dict?
        TODO: add type checking
        """
        self.model_name = model_name
        self.metric_dict = metric_dict


    def add_metric(self, name, value):
        """
        Add metric to the dictionary, given its name and evaluated value.
        """
        self.metric_dict[name] = value


    def serialize(self):
        """
        Write metrics dictionary to disk as CSV.

        TODO: implement this method
        TODO: add "format" parameter to choose between CSV and JSON
        """
        pass

class MetricEvaluator(ABC):
    """
    This is the abstract superclass of classes which, given the predictions of
    some model, evaluate it on a custom set of metrics.
    """

    @property
    @abstractmethod
    def metrics_dict(self):
        """
        Should return the MetricDictionary containing name-value pairings for
        all calculated metrics.
        """
        pass


    @abstractmethod
    def transform_predictions(self, predictions: np.ndarray):
        """
        Given the model predictions on test data, transform them into a suitable
        format for evaluation. Store this format in self.transformed_metrics.
        """
        pass


    @abstractmethod
    def calculate_metrics(self):
        """
        The key (pipeline) method of this class. Should do the following steps:

        1. Transforming "raw" predictions into a tangible format.
        2. Calculating metric values given the transformed predictions.
        3. Updating the metrics_dict with the calculated values.
        """
        pass

class AIF360MetricEvaluator(MetricEvaluator):
    """
    This class implements the MetricEvaluator for the AIF360 framework by IBM.
    """
    pass