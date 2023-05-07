import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
import sys
sys.path.append('/Users/ellington/dev/preprocessor/')  # nopep8
import preprocessor as p
from nltk.stem import SnowballStemmer


def tokenize_emojis_links_and_compare_counts(filename, data,):
    # Vectorize input
    input_vectorizer = CountVectorizer()
    input_vectorizer.fit_transform(data)
    print(
        f"Before tokenizing, total token count is: {len(input_vectorizer.get_feature_names_out())}")

    with open(filename, 'w') as f:
        data.to_json(f, orient='values')

    print("Cleaning file: removing numbers")
    p.api.set_options(p.OPT.NUMBER)
    cleaned_output = p.api.clean_file(filename)

    print("Cleaning file: tokenizing urls, emojis, mentions, hashtags, and smileys")
    p.api.set_options(p.OPT.URL, p.OPT.EMOJI, p.OPT.MENTION,
                      p.OPT.HASHTAG, p.OPT.SMILEY)
    tokenized_output = p.api.tokenize_file(cleaned_output)
    tokenized_data = pd.read_json(tokenized_output, typ='series')

    # Vectorize output
    output_vectorizer = CountVectorizer()
    output_vectorizer.fit_transform(tokenized_data)
    print(
        f"After tokenizing, total token count is: {len(output_vectorizer.get_feature_names_out())}"
    )

<<<<<<< HEAD
    # print("Applying Stemming")
    # stemmer = SnowballStemmer('english')
    # tokenized_data = tokenized_data.apply(
    #     lambda x: ' '.join([stemmer.stem(y) for y in x.split()]))
=======
    print("Applying Stemming")
    stemmer = SnowballStemmer('english')
    tokenized_data = tokenized_data.apply(
        lambda x: ' '.join([stemmer.stem(y) for y in x.split()]))
>>>>>>> ed0cabc (final code results)

    print("Removing stop words")
    stop_words = pd.read_json('../stop_words_english.json')[0].tolist()
    tokenized_data = tokenized_data.apply(lambda x: ' '.join(
<<<<<<< HEAD
        [word for word in x.split() if word.lower() not in (stop_words)]))
=======
        [word for word in x.split() if word not in (stop_words)]))
>>>>>>> ed0cabc (final code results)

    # Vectorize output
    output_vectorizer = CountVectorizer()
    output_vectorizer.fit_transform(tokenized_data)
    print(
        f"After stemming and removing stopwords, total token count is: {len(output_vectorizer.get_feature_names_out())}"
    )

    return tokenized_data


def confirm_veectorized_word_count(data):
    output_vectorizer = CountVectorizer()
    output_vectorizer.fit_transform(data)
    print(
        f"After cleaning, total token count is: {len(output_vectorizer.get_feature_names_out())}")
