import re
import curl

import mc_bin_client

import couchmigrator.migrator

class CouchbaseReader(couchmigrator.migrator.Reader):
    def __init__(self, source):
        # username:password@example.com:8091/bucket        
        m = re.match('^([^:]+):([^@]+)@([^:]+):([^/]+)/(.+)$', source)
        self.username = m.group(1)
        self.password = m.group(2)
        self.host = m.group(3)
        self.port = m.group(4)
        self.bucket = m.group(5)

        self.bucket_port = 11211
        self.bucket_password = ''

    def __iter__(self):
        return self

    def next(self):
#        data = self.reader.next()
#        if data:
#            record = {'id':data['id']}
#            record['value'] = dict((k,v) for (k,v) in json_data['value'].iteritems() if not k.startswith('_'))
#            return record
#        else:
#            raise StopIteration()
        raise StopIteration()


class CouchbaseWriter(couchmigrator.migrator.Writer):
    def __init__(self, destination):
        pass

    def write(self, record):
        pass
