#!/usr/bin/env python
import os, sys
import pickle
import preprocess

# path of the data
train_data_file = '../data/train.csv'
test_data_file = '../data/test.csv'

train_tokenized_file = '../data/train_comments.p'
test_tokenized_file = '../data/test_comments.p'

# load data
train_data = preprocess.load_data(train_data_file)
test_data = preprocess.load_data(test_data_file)

# size of the training data
n_train = len(train_data)

# training data tokenzied
train_tokenized = preprocess.tokenize_df(train_data)
print "Tokenized {} comments from train data.".format(n_train)

# write tokenzied training data into .p file
with open(train_tokenized_file, 'wb') as f:
    pickle.dump(train_tokenized, f)
    print "Saved {} tokenized comments from train data to {} ".format(n_train, train_tokenized_file)

# same with the testing data as above
n_test = len(test_data)
test_tokenized = preprocess.tokenize_df(test_data)
print "Tokenized {} comments from test data.".format(n_test)
with open(test_tokenized_file, 'wb') as f:
    pickle.dump(test_tokenized, f)
    print "Saved {} tokenized comments from test data to {} ".format(n_test, test_tokenized_file)
