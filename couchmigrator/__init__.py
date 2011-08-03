__version__ = '1.0.0'
__all__ = [
    'reader', 'writer',
]

from migrator_csv import CSVReader, CSVWriter
from migrator_json import JSONReader, JSONWriter
#from migrator_couchdb import CouchdbReader, CouchdbWriter
from migrator_couchbase import CouchbaseReader, CouchbaseWriter

def reader(loc):
    kind, fp = loc.split(':', 1)
    if kind.lower() == 'csv':
        return CSVReader(fp)
    elif kind.lower() == 'json':
        return JSONReader(fp)
#    elif kind.lower() == 'couchdb':
#        return CouchdbReader(fp)
    elif kind.lower() == 'couchbase':
        return CouchbaseReader(fp)

def writer(loc):
    kind, fp = loc.split(':', 1)
    if kind.lower() == 'csv':
        return CSVWriter(fp)
    elif kind.lower() == 'json':
        return JSONWriter(fp)
#    elif kind.lower() == 'couchdb':
#        return CouchdbWriter(fp)
    elif kind.lower() == 'couchbase':
        return CouchbaseWriter(fp)
