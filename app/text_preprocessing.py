import string
import nltk
from nltk.stem import WordNetLemmatizer
from nltk.corpus import wordnet, stopwords
from nltk import pos_tag, word_tokenize

# Ensure all resources used in Colab are available
for resource in ['punkt', 'punkt_tab', 'wordnet', 'omw-1.4', 
                 'averaged_perceptron_tagger', 'averaged_perceptron_tagger_eng', 
                 'stopwords']:
    nltk.download(resource, quiet=True)

stop_words = set(stopwords.words('english'))
lemmatizer = WordNetLemmatizer()

def get_wordnet_pos(tag):
    if tag.startswith('J'): return wordnet.ADJ
    elif tag.startswith('V'): return wordnet.VERB
    elif tag.startswith('N'): return wordnet.NOUN
    elif tag.startswith('R'): return wordnet.ADV
    else: return wordnet.NOUN

def preprocess_text(text: str):
    # 1. Lowercase and strip
    text = text.lower().strip()
    # 2. Remove punctuation
    text = text.translate(str.maketrans('', '', string.punctuation))
    # 3. Tokenize
    words = word_tokenize(text)
    # 4. POS-aware lemmatization + Stopword removal
    cleaned_words = [
        lemmatizer.lemmatize(word, get_wordnet_pos(pos))
        for word, pos in pos_tag(words)
        if word not in stop_words
    ]
    return ' '.join(cleaned_words)