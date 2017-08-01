// csv2es 1.0.1   https://pypi.python.org/pypi/csv2es
// pip install csv2es


from elasticsearch import helpers, Elasticsearch
import csv

es = Elasticsearch()

with open('/tmp/x.csv') as f:
    reader = csv.DictReader(f)
    helpers.bulk(es, reader, index='my-index', doc_type='my-type')