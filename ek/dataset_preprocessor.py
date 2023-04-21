import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
import sys
sys.path.append('/Users/ellington/dev/preprocessor/')
import preprocessor as p

def tokenize_emojis_links_and_compare_counts(filename, data,):
    # Vectorize input
    input_vectorizer = CountVectorizer()
    input_vectorizer.fit_transform(data)
    print(f"Before tokenizing, total token count is: {len(input_vectorizer.get_feature_names_out())}")

    with open(filename, 'w') as f:
        data.to_json(f, orient='values')
    
    p.api.set_options(p.OPT.URL, p.OPT.EMOJI, p.OPT.MENTION, p.OPT.HASHTAG, p.OPT.SMILEY, p.OPT.NUMBER)
    cleaned_output = p.api.tokenize_file(filename)
    cleaned_data = pd.read_json(cleaned_output, typ='series')

    # Vectorize output
    output_vectorizer = CountVectorizer()
    output_vectorizer.fit_transform(cleaned_data)
    print(f"After tokenizing, total token count is: {len(output_vectorizer.get_feature_names_out())}")

    return cleaned_data

def confirm_veectorized_word_count(data):
    output_vectorizer = CountVectorizer()
    output_vectorizer.fit_transform(data)
    print(f"After cleaning, total token count is: {len(output_vectorizer.get_feature_names_out())}")
