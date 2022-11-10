import pandas as pd

articles_pd = pd.read_csv('wikispeedia_paths-and-graph/articles.tsv', delimiter='\t')
print(articles_pd.head())