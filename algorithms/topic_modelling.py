import gensim
from gensim.parsing.preprocessing import remove_stopwords


EXCEPTIONS = ['good', 'bad', 'horrible', 'like']


class LDATopicModeller:
    def __init__(self, num_topics, minimum_probability):
        self.minimum_probability = minimum_probability
        self.num_topics = num_topics

    def create_topic_model(self, texts):
        processed_docs = [remove_stopwords(text).split() for text in texts]
        processed_docs = [[t for t in text if len(t) > 3] for text in processed_docs]

        self.dictionary = gensim.corpora.Dictionary(processed_docs)
        bow_corpus = [self.dictionary.doc2bow(doc) for doc in processed_docs]

        self.lda_model = gensim.models.LdaMulticore(
            bow_corpus,
            num_topics=self.num_topics,
            id2word=(self.dictionary),
            passes=10,
            workers=2,
            minimum_probability=self.minimum_probability,
        )

    def get_topic_from_model(self, doc):
        bow_vector = self.dictionary.doc2bow(doc.split())

        try:
            index, score = sorted(
                (self.lda_model[bow_vector]), key=(lambda tup: -1 * tup[1])
            )[0]
        except:
            return None

        topic_probs = self.lda_model.show_topic(index)
        most_prob = [topic for topic, prob in topic_probs if prob > 0.06]

        if most_prob:
            return ' '.join((f for f in most_prob if f not in EXCEPTIONS))

