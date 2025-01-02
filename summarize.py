# Implements text summarization logic
import string
from scrape import fetchArticle
from collections import Counter
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
from collections import defaultdict


class Summarizer:
    def __init__(self):
        self.stop_words = set(stopwords.words('english'))
        self.puncuation = set(string.punctuation)

    def summarize_text(self, text, num_sentences):
        word_frequencies = defaultdict(int)
        sentences = sent_tokenize(text)
        words = word_tokenize(text.lower())
        for word in words:
            if word not in self.stop_words and word not in self.puncuation:
                word_frequencies[word] += 1


        max_frequency = max(word_frequencies.values(), default=1)
        #print(max_frequency)
        

        for word in word_frequencies:
            word_frequencies[word] /= max_frequency


        sentence_scores = {}
        for sentence in sentences:
            for word in word_tokenize(sentence.lower()):
                if word in word_frequencies:
                    sentence_scores[sentence] = sentence_scores.get(sentence, 0) + word_frequencies[word]

        ranked_sentences = sorted(sentence_scores, key=sentence_scores.get, reverse=True)
        summary = ' '.join(ranked_sentences[:num_sentences])
        return summary




