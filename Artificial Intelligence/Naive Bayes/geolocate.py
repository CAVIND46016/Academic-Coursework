"""
See https://www.3pillarglobal.com/insights/document-classification-using-multinomial-naive-bayes-classifier
"""

import codecs
import operator
import time
import re
from collections import Counter
import pandas as pd
from nltk.corpus import stopwords
import nltk


class TweetClassification:
    def __init__(self, train_file, test_file, output_file, alpha):
        """
        Parameterized constructor reads training and test file.
        :param train_file:
        :param test_file:
        :param output_file:
        :param alpha:
        """

        self.train_df = TweetClassification.read_input_file(train_file)
        self.test_df = TweetClassification.read_input_file(test_file)
        self.output_file = output_file
        self.alpha = alpha

        self.classes = self.categories()
        self.class_probabilities = TweetClassification.prior_probabilities(
            self.categories(all_=True)
        )
        self.cached_stop_words = stopwords.words("english") + [
            "job",
            "hiring",
            "jobs",
            "careerarc",
            "latest",
            "opening",
            "im",
            "amp",
            "click",
            "see",
            "great",
        ]
        self.tweet_lists = self.words_all_documents()
        self.unique_tweet_lists = list(set(self.tweet_lists))

    @staticmethod
    def read_input_file(filename):
        idx = 0
        df = pd.DataFrame(columns=("location", "tweet"))
        with codecs.open(filename, "r", "utf8") as file_handle:
            lines = file_handle.read().splitlines()
            for line in lines:
                try:
                    if line.find(",_") != -1:
                        df.loc[idx] = line.replace(" ", "::", 1).split("::")
                        idx += 1
                    else:
                        df.loc[idx - 1]["tweet"] += line
                except:
                    idx += 1
        return df

    @staticmethod
    def prior_probabilities(outcome):
        prob = dict(Counter(outcome))
        for key in prob.keys():
            prob[key] = prob[key] / len(outcome)
        return prob

    def feature_extraction(self, text):
        # Remove numerical data
        text = re.sub(r"\d+", "", text.lower())
        # Remove non-ASCII chars.
        text = re.sub(r"[^\x00-\x7F]+", " ", text)
        # Remove special chars.
        text = re.sub(r'[?!+%{}:.,"\'()\[\]_]', "", text)
        return [
            w for w in nltk.word_tokenize(text) if (len(w) > 1 and w not in self.cached_stop_words)
        ]

    def words_all_documents(self):
        tweet_lists = []
        for val in self.train_df["tweet"].values:
            tweet_lists += self.feature_extraction(val)

        return tweet_lists

    def conditional_probabilities(self, outcome, tweet_list):
        prob = dict(Counter(outcome))
        for key in list(set(tweet_list)):
            if key not in prob:
                n_word = 0
            else:
                n_word = prob[key]
            prob[key] = (n_word + self.alpha) / (
                len(outcome) + self.alpha * len(self.unique_tweet_lists)
            )
        return prob

    def predict(self):
        predicted_vals = []
        errors = 0
        print_top_five = True
        for index, row in self.test_df.iterrows():
            # Calculate prior probabilities
            tweet_feature = self.feature_extraction(row["tweet"])
            tweet_list = self.tweet_lists + tweet_feature

            likelihoods = {}
            for i in self.classes:
                txt = " ".join(self.train_df[self.train_df["location"] == i]["tweet"].values)
                feature = self.feature_extraction(txt)
                likelihoods[i] = self.conditional_probabilities(feature, tweet_list)

            if print_top_five:
                for key, val in likelihoods.items():
                    sorted_likelihoods = sorted(
                        val.items(), key=operator.itemgetter(1), reverse=True
                    )[0:10]
                    print(f"{key}: {', '.join([i[0] for i in sorted_likelihoods])}")
                print_top_five = False

            vals = {}
            for catg in self.classes:
                vals[catg] = self.class_probabilities[catg]
                for word in tweet_feature:
                    vals[catg] *= likelihoods[catg][word]

            pred_val = max(vals.items(), key=operator.itemgetter(1))[0]
            if pred_val != row["location"]:
                errors += 1
            predicted_vals.append(pred_val)

            print(index + 1)

        accuracy = 100 - errors / len(self.test_df) * 100
        self.test_df.insert(0, "predicted", predicted_vals)
        self.test_df.to_csv(self.output_file, header=False, index=False, sep=" ")
        print(f"Accuracy: {accuracy} %")

    def categories(self, all_=False):
        if not all_:
            classes = list(set(self.train_df["location"].values))
        else:
            classes = self.train_df["location"].values

        return classes


def main():
    start_time = time.time()
    train_file = "tweets_train.txt"
    test_file = "tweets_test1.txt"
    output_file = "output_file.txt"

    alpha = 1  # Smoothing parameter: alpha = 1 for Laplace smoothing
    TweetClassification(train_file, test_file, output_file, alpha).predict()
    text = f"Time taken: {time.time() - start_time} secs"
    print(text)


if __name__ == "__main__":
    main()
