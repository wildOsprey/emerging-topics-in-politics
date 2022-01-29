from transformers import AutoTokenizer, AutoModelForTokenClassification
from transformers import pipeline


class NERExtractor:
    def __init__(self):
        self.tokenizer = AutoTokenizer.from_pretrained("dslim/bert-base-NER")
        self.model = AutoModelForTokenClassification.from_pretrained("dslim/bert-base-NER")
        self.nlp = pipeline("ner", model=self.model, tokenizer=self.tokenizer)

    def extract_ner_words(self, text):
        '''Find list of Named Entity words in the text.'''
        ner_results = self.nlp(text)
        return [item['word'] for item in ner_results]
