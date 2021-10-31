import matplotlib.pyplot as plt
import imageio
import pandas as pd
from wordcloud import WordCloud
from pathlib import Path
from operator import itemgetter
from textblob import TextBlob
import nltk
from nltk.corpus import stopwords
import wordcloud

#nltk.download('stopwords')
stops = stopwords.words("english")
#print(stops)

more_stops = ["thy", "ye", "verily", "thee", "hath", "say", "thou", "art", "shall", "thou hast", "saith unto"]
stops += more_stops
#print(stops)

blob = TextBlob(Path("book_of_John.txt").read_text())
words = blob.np_counts.items()

clean_words = [i for i in words if i[0] not in stops]
sorted_words = sorted(clean_words, key=itemgetter(1), reverse=True)
top15 = sorted_words[:15]
top15 = dict(top15)


wordcloud = WordCloud(colormap='Blues', max_font_size=80, background_color='grey').generate_from_frequencies(top15).to_file("BookofJohn.png")

#wordcloud = WordCloud(max_font_size=100, max_words=15, background_color="white").generate(noun_str).to_file("BookofJohn.png")
