## Описание

В этом проекте реализованы:
- Функции для загрузки и анализа текста первой главы романа "Улисс" Джеймса Джойса с сайта Project Gutenberg, поиска употреблений слова в контексте.
- Класс для вычисления TF, IDF и TF-IDF по коллекции текстов с поддержкой стоп-слов.

## Структура проекта

- **ulysses.py** - функции для загрузки главы, поиска слова в контексте, подсчёта частоты слов.
- **tf_idf.py** - класс для вычисления TF, IDF, TF-IDF по списку документов.
- **examples.ipynb** - примеры использования функций и класса.
- **README.md** - описание проекта.

## Быстрый старт

1. Скачайте или клонируйте репозиторий:

   ```bash
   git clone https://github.com/yourusername/yourrepo.git
   ```

2. Установите необходимые библиотеки (если работаете локально):

   ```bash
   pip install requests beautifulsoup4
   ```

3. Импортируйте модули в вашем Python-скрипте или Jupyter Notebook:

   ```python
   from ulysses import load_chapter_text, find_word_context
   from tf_idf import TFIDF
   ```

4. Пример использования:

   ```python
   # Загрузка текста главы
   url = 'https://www.gutenberg.org/files/4300/4300-h/4300-h.htm'
   chapter_text = load_chapter_text(url, chapter_id='chap01')

   # Поиск слова в контексте
   find_word_context(chapter_text, word='ulysses', left_context=5, right_context=5, cut_length=True)

   # Работа с TF-IDF
   docs = ["This is the first doc.", "This is the second doc."]
   tfidf = TFIDF(docs)
   print(tfidf.get_tf('this', 0))
   print(tfidf.get_idf('this', 0))
   print(tfidf.get_tf_idf('this', 0))
   ```

## Примечания

- Для корректной работы функций требуется интернет-соединение (для загрузки главы с сайта).
- Все примеры приведены в файле `examples.ipynb`.

## Авторы

- Ваше имя, 2025

---

**Совет:**  
Можете добавить/убрать пункты по желанию. После выставления оценки доступ к репозиторию можно ограничить.

Если хотите, я могу подстроить README под ваши пожелания или добавить больше примеров!

Citations:
[1] https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/attachments/65695691/b133ba49-3c7c-4887-a8a3-15d0b766ee8b/ulysses.py

---
Answer from Perplexity: pplx.ai/share
