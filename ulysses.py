import requests
from bs4 import BeautifulSoup
from collections import Counter
import re

def load_chapter_text(url, chapter_id='chap01'):
    """
    Загружает текст главы по id из HTML-страницы.
    url: ссылка на страницу
    chapter_id: id главы (например, 'chap01')
    Возвращает текст главы как одну строку.
    """
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    start_tag = soup.find(id=chapter_id)
    if not start_tag:
        raise ValueError(f"Chapter id '{chapter_id}' not found")
    texts = []
    for sibling in start_tag.find_next_siblings():
        if sibling.name and sibling.name.startswith('h'):
            break
        texts.append(sibling.get_text(separator=' ', strip=True))
    chapter_text = ' '.join(texts)
    return chapter_text

def word_frequency(text):
    """
    Подсчитывает частоту слов в тексте.
    text: строка с текстом
    Возвращает Counter с частотами слов.
    """
    words = re.findall(r'\b\w+\b', text.lower())
    return Counter(words)

def find_word_context(text, word, left_context=5, right_context=5, cut_length=False, output_file='contexts.txt'):
    """
    Находит все вхождения слова с указанным контекстом.
    text: строка с текстом
    word: искомое слово (без учёта регистра)
    left_context: количество слов слева
    right_context: количество слов справа
    cut_length: если True, контекст ограничивается рамками предложения
    output_file: имя файла для записи результатов
    Возвращает список строк-контекстов.
    """
    word = word.lower()
    results = []

    if cut_length:
        # По предложениям
        sentences = re.split(r'(?<=[.!?])\s+', text)
        for sentence in sentences:
            sent_words = re.findall(r'\b\w+\b', sentence.lower())
            indices = [i for i, w in enumerate(sent_words) if w == word]
            for idx in indices:
                left_start = max(0, idx - left_context)
                right_end = min(len(sent_words), idx + right_context + 1)
                context_words = sent_words[left_start:idx] + [sent_words[idx]] + sent_words[idx+1:right_end]
                context_str = ' '.join(context_words)
                results.append(context_str)
    else:
        # По всему тексту
        all_words = re.findall(r'\b\w+\b', text.lower())
        indices = [i for i, w in enumerate(all_words) if w == word]
        for idx in indices:
            left_start = max(0, idx - left_context)
            right_end = min(len(all_words), idx + right_context + 1)
            context_words = all_words[left_start:idx] + [all_words[idx]] + all_words[idx+1:right_end]
            context_str = ' '.join(context_words)
            results.append(context_str)

    with open(output_file, 'w', encoding='utf-8') as f:
        for line in results:
            print(line)
            f.write(line + '\n')
    return results
