import pandas as pd
import random
import numpy as np

def train_test_split(df, test_size, random_sate=None):
    if isinstance(test_size, float):
        test_size = round(test_size * len(df))

    indices = df.index.tolist()
    test_indices = random.sample(population=indices, k=test_size)

    test_df = df.loc[test_indices]
    train_df = df.drop(test_indices)

    return train_df, test_df


def determine_type_of_feature(df):
    feature_types = []
    n_unique_values_threshold = 15
    for feature in df.columns:
        if feature != "label":
            unique_values = df[feature].unique()
            example_value = unique_values[0]

            if (isinstance(example_value, str)) or (len(unique_values) <= n_unique_values_threshold):
                feature_types.append("categorical")
            else:
                feature_types.append("continuous")

    return feature_types


def calculate_accuracy(predictions, labels):
    predictions_correct = predictions == labels
    accuracy = np.mean(predictions_correct)

    return accuracy