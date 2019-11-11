import pandas as pd
import math

def Entropy(input_set):
    #takes a series or column of a dataframe as parameter
    entropy = 0
    logarithm_base = 2 #given base, part of ID3 entropy formula
    for unique_value_count in input_set.value_counts():
        probability_type = unique_value_count / len(input_set)
        try:
            entropy = entropy + (0 - probability_type) * math.log(probability_type, logarithm_base)
        except:
            entropy += 0
    return entropy

def InformationGain(condition, feature, input_dataframe, condition_value):
    #condition = root
    IG = Entropy(input_dataframe[condition])
    print("Entropy for %s: %s" % (condition, IG))
    probability_type = 0
    for unique_value in input_dataframe[feature].unique():
        conditional_subset = input_dataframe[input_dataframe[feature] == unique_value][condition]
        try:
            probability_type = conditional_subset.value_counts()[condition_value] / len(conditional_subset)#members of feature where condition is met / total members of
        except:
            probability_type = 0 #condition_value not found in
        intermediate_entropy = Entropy(conditional_subset)
        print("Entropy for %s @ %s: %s" % (feature, unique_value, intermediate_entropy))
        IG -= probability_type * intermediate_entropy
    return IG

def SelectRoot(condition, features, subset, condition_value, current_feature, feature_value):
    print("\nCalculations for %s @ %s" % (current_feature, feature_value))
    if len(subset[condition].value_counts()) == 1:
        #pure subset, make a leaf node
        print("Pure Subset; Leaf Node created: %s @ %s -> %s" % (current_feature, feature_value, subset[condition].values[0]))
        return

    best_feature_IG = 0
    best_feature = None
    for feature in features:
        #find feature with highest information gain
        feature_ig = InformationGain(condition, feature, subset, condition_value)
        print("Information Gain for %s: %s" % (feature, feature_ig))
        if feature_ig >= best_feature_IG:
            best_feature_IG = feature_ig
            best_feature = feature
    print("Node created: %s @ %d -> %s, IG = %s" % (condition, condition_value, best_feature, best_feature_IG))
    features.remove(best_feature)
    for unique_value in subset[best_feature].unique():
        SelectRoot(condition, features, subset[subset[best_feature] == unique_value], condition_value, best_feature, unique_value)

if __name__ == '__main__':
    data = pd.read_csv("health.csv")
    print(data)
    root = None
    y_label = 'Action'
    x_labels = ['Has_Job','Has_Insurance','Voted']

    #Set_Entropy = Entropy(data[y_label]) #get entropy of our class column
    SelectRoot(y_label, x_labels, data, 1, y_label, 1)
