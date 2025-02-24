import spacy

# Load the SpaCy English model
nlp = spacy.load("en_core_web_sm")

# Function to process the text
def text_processor(texto):
    doc = nlp(texto)
    # Remove stopwords and lemmatize
    text_processed = " ".join([token.lemma_ for token in doc if not token.is_stop and token.is_alpha])
    return text_processed
