# ID3 Implementation in Python
File ID3.py contains my implementation of the ID3 decision tree algorithm. To run the program, execute it as a python script followed by the .csv file path containing the dataset you’d like to create a tree for, i.e. `$ python ID3.py health.csv`

##### Program limitations:
- Requires Pandas version 0.23.4 or greater. Older versions may work, but this was the version I used when programming the algorithm.

- The algorithm also assumes a binary classification problem. Multi-value input features are okay, but the class column must be binary. If it is not, the program will select one value as positive and the rest as negative.

- The dataset must be encoded into discrete integers before running. The algorithm may still work if this is not done for the feature columns, however the class column (y-value) **must** be binary and encoded to 1 or 0 output.
