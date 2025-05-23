import math
import re

class TfIdfCalculator:
    """
    Класс для вычисления TF, IDF и TF-IDF по коллекции документов.
    """

    stopwords = {
        "и", "в", "во", "не", "что", "он", "на", "я", "с", "со", "как", "а", "то",
        "все", "она", "так", "его", "но", "да", "ты", "к", "у", "же", "вы", "за",
        "бы", "по", "только", "ее", "мне", "было", "вот", "от", "меня", "еще", "нет",
        "о", "из", "ему", "теперь", "когда", "даже", "ну", "вдруг", "ли", "если", "уже",
        "или", "ни", "быть", "был", "него", "до", "вас", "нибудь", "опять", "уж", "вам",
        "ведь", "там", "потом", "себя", "ничего", "ей", "может", "они", "тут", "где",
        "есть", "надо", "ней", "для", "мы", "тебя", "их", "чем", "была", "сам", "чтоб",
        "без", "будто", "человек", "чего", "раз", "тоже", "себе", "под", "будет",
        "ж", "тогда", "кто", "этот", "того", "потому", "этого", "какой", "совсем",
        "ним", "здесь", "этом", "один", "почти", "мой", "тем", "чтобы", "нее", "сейчас",
        "были", "куда", "зачем", "всех", "никогда", "можно", "при", "наконец",
        "два", "об", "другой", "хоть", "после", "над", "больше", "тот", "через",
        "эти", "нас", "про", "всего", "них", "какая", "много", "разве", "три",
        "эту", "моя", "впрочем", "хорошо", "свою", "этой", "перед", "иногда",
        "лучше", "чуть", "том", "нельзя", "такой", "им", "более", "всегда", "конечно",
        "всю", "между"
    }

    def __init__(self, texts):
        """
        texts: список строк (документов)
        """
        self.texts = texts
        self.N = len(texts)
        self.docs_words = [self._tokenize(text) for text in texts]

    def _tokenize(self, text):
        return re.findall(r'\b\w+\b', text.lower())

    def get_tf(self, word, doc_number):
        """
        Возвращает TF (частота слова в документе).
        """
        word = word.lower()
        words = self.docs_words[doc_number]
        count_word = words.count(word)
        total_words = len(words)
        return count_word / total_words if total_words > 0 else 0

    def get_idf(self, word, doc_number=None):
        """
        Возвращает IDF (обратная частота документа).
        """
        word = word.lower()
        docs_with_word = sum(1 for doc in self.docs_words if word in doc)
        return math.log((self.N + 1) / (docs_with_word + 1)) + 1

    def get_tf_idf(self, word, doc_number, ignore_stopwords=True):
        """
        Возвращает TF-IDF. По умолчанию стоп-слова игнорируются.
        """
        word_l = word.lower()
        if ignore_stopwords and word_l in self.stopwords:
            return 0.0
        tf = self.get_tf(word_l, doc_number)
        idf = self.get_idf(word_l)
        return tf * idf
