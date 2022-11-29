from bertopic import BERTopic
from sklearn.datasets import fetch_20newsgroups

docs = fetch_20newsgroups(subset='all',  remove=(
    'headers', 'footers', 'quotes'))['data'][0:100]


topic_model = BERTopic(language="multilingual", nr_topics=20)
topics, probs = topic_model.fit_transform(docs)


print(docs[2])
topic_model.fit_transform(docs)
print(topic_model.get_topic_info())
print(topic_model.get_topic(0))
