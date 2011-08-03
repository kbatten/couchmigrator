sources=[{'type':'csv','class':'CSVReader','example':'csv:<filename>'}]
destinations=[]

import csv

import couchmigrator.migrator

class CSVReader(couchmigrator.migrator.Reader):
    def __init__(self, source):
        self.reader = csv.DictReader(open(source, 'rb'))
        self.reader.fieldnames[0] = 'id'

    def __iter__(self):
        return self

    def next(self):
        data = self.reader.next()
        if data:
            record = {'id':data['id']}
            record['value'] = dict((k,v) for (k,v) in data.iteritems() if k != 'id' or not k.startswith('_'))
            return record
        else:
            raise StopIteration()


class CSVWriter(couchmigrator.migrator.Writer):
    pass
