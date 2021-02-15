
"""# Fetch text"""


def fetchText(url):
    import urllib.request

    content = urllib.request.urlopen(url)

    read_content = content.read()
    from bs4 import BeautifulSoup
    soup = BeautifulSoup(read_content, 'html.parser')
    pAll = soup.find_all('p')

    text = ""

    for p in pAll:
        text += p.text

    text = text.strip()
    return text




"""# Summarize"""


def summarize(text):
    import spacy
    from spacy.lang.en.stop_words import STOP_WORDS
    from string import punctuation
    from heapq import nlargest
    print("Called")

    stopwords = list(STOP_WORDS)

    nlp = spacy.load('en_core_web_sm')
    doc = nlp(text)
    print(doc)
    tokens = [token.text for token in doc]

    punctuation = punctuation + '\n'

    word_frequencies = {}
    for word in doc:
        if word.text.lower() not in stopwords:
            if word.text.lower() not in punctuation:
                if word.text not in word_frequencies.keys():
                    word_frequencies[word.text] = 1
                else:
                    word_frequencies[word.text] += 1

   
    max_frequency = max(word_frequencies.values())
 

    for word in word_frequencies.keys():
        word_frequencies[word] = word_frequencies[word] / max_frequency


    sentence_tokens = [sent for sent in doc.sents]


    sentence_scores = {}
    for sent in sentence_tokens:
        for word in sent:
            if word.text.lower() in word_frequencies.keys():
                if sent not in sentence_scores.keys():
                    sentence_scores[sent] = word_frequencies[word.text.lower()]
                else:
                    sentence_scores[sent] += word_frequencies[word.text.lower()]

  

    select_length = min(int(len(sentence_tokens) * 0.2), 30)
    print(select_length)
    summary = nlargest(select_length, sentence_scores, key=sentence_scores.get)
    
    final_summary = [word.text for word in summary]
    summary = ' '.join(final_summary)

    return summary

