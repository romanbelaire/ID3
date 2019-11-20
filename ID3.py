import pandas as pd
import math
import argparse

def Entropy(input_set):
    #takes a series or column of a dataframe as parameter
    entropy = 0
    logarithm_base = 2 #given base, part of ID3 entropy formula
    equation_string = ""
    for unique_value_count in input_set.value_counts():
        probability_type = unique_value_count / len(input_set)
        equation_string += '-(' + str(unique_value_count) + '/' + str(len(input_set)) + ')'
        try:
            entropy = entropy + ((0 - probability_type) * math.log(probability_type, logarithm_base))
            equation_string += str(math.log(probability_type, logarithm_base))
        except:
            equation_string += '0'
            entropy += 0
        equation_string += ' + '
    equation_string += ' = ' + str(entropy)
    print(equation_string)
    return entropy

def InformationGain(condition, feature, input_dataframe, condition_value):
    #condition = root
    IG = Entropy(input_dataframe[condition])
    print("Entropy for %s: %s" % (condition, IG))
    probability_type = 0
    equation_string = str(IG)
    for unique_value in input_dataframe[feature].unique():
        equation_string += ' - '
        conditional_subset = input_dataframe[input_dataframe[feature] == unique_value][condition]
        try:
            numerator = len(conditional_subset)#.value_counts()[condition_value]
            denominator = len(input_dataframe)
            equation_string += '(' + str(numerator) + '/' + str(denominator) + ')'
            probability_type = numerator / denominator#members of feature where condition is met / total members of
        except:
            equation_string += '0'
            probability_type = 0 #condition_value not found in set
        intermediate_entropy = Entropy(conditional_subset)
        print("Entropy for %s @ %s: %s\n" % (feature, unique_value, intermediate_entropy))
        equation_string += str(intermediate_entropy)
        IG -= probability_type * intermediate_entropy
    equation_string += ' = ' + str(IG)
    print(equation_string)
    return IG

def SelectRoot(condition, features, subset, condition_value, current_feature, feature_value):
    print("------------\nCalculations for %s @ %s" % (current_feature, feature_value))
    if len(subset[condition].value_counts()) == 1:
        #pure subset, make a leaf node
        print("Pure Subset; Leaf Node created: %s @ %s -> %s" % (current_feature, feature_value, subset[condition].values[0]))
        return

    best_feature_IG = 0
    best_feature = None
    for feature in features:
        #find feature with highest information gain
        feature_ig = InformationGain(condition, feature, subset, condition_value)
        print("Information Gain for %s: %s\n\n" % (feature, feature_ig))
        if feature_ig >= best_feature_IG:
            best_feature_IG = feature_ig
            best_feature = feature
    print("Node created: %s @ %d -> %s, IG = %s" % (current_feature, feature_value, best_feature, best_feature_IG))
    print("removing %s from %s " % (best_feature, features))
    features.remove(best_feature)
    for unique_value in subset[best_feature].unique():
        SelectRoot(condition, features, subset[subset[best_feature] == unique_value], condition_value, best_feature, unique_value)

if __name__ == '__main__':
    argparser = argparse.ArgumentParser()
    argparser.add_argument("path")
    args = argparser.parse_args()
    data = pd.read_csv(args.path)
    print(data)
    root = None
    #y_label = 'Action'
    y_label = data.columns.values[-1]
    x_labels = data.columns.values[:-1].tolist()
    #x_labels = ['Has_Job','Has_Insurance','Voted']

    SelectRoot(y_label, x_labels, data, 1, y_label, 1)
