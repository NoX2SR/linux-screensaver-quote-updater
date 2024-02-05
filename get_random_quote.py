import sys
import json
import random

f = open('./quotes.json')
data = json.load(f)
quotes_count = len(data['quotes'])
random_quote_index = random.randint(0, quotes_count-1)
random_quote = data['quotes'][random_quote_index]
f.close()
print('{}\n{}'.format(random_quote['quote'], random_quote['author']))
