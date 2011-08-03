#!/usr/bin/env python

import sys
import getopt

import couchmigrator

#sources: json, csv, sqlite, couchdb, couchbase, membase, memcached, membase-sqlite
#dest: json (chunked), couchbase


def usage(err=None):
    if err:
        print "Error: %s\n" % err
        r = 1
    else:
        r = 0

    print """\
Syntax: couchbase-migrator [options]

Options:
 -h, --help

 -s <source>, --source=<source>
     Data source that will be imported from

 -d <destination>, --destination=<destination>
     Data destination that will be exported to

 -o, --overwrite
     Overwrite any items that are in the destination

 --dry-run
     Do not write any data, just show what would be written

 -v, --verbose
     
 -q, --quiet

"""
    print "Sources:"
    for source in couchmigrator.sources:
        print " " + source['type'] + "(" + source['class'] + ")"
        print "     " + source['example']

    print

    print "Destinations:"
    for destination in couchmigrator.destinations:
        print " " + destination['type'] + "(" + destination['class'] + ")"
        print "     " + destination['example']

        """
Sources:
 json
     [json:]<filename>
 csv
     [csv:]<filename>
 sqlite
     [sqlite:]<filename>
 couchdb
     [couchdb:]example.com:5984/database
 couchbase
     [couchbase:]username:password@example.com:8091/bucket
 membase
     [membase:]username:password@example.com:8091/bucket
 membase-sqlite
     [membase-sqlite:]<dirname>
 memcached
     [memcached:]bucket:password@example.com:11211

Destinations:
 json
     [json:]<filename>
 couchbase
     [couchbase:]username:password@example.com:8091/bucket
"""

    sys.exit(r)

class Config(object):
    def __init__(self):
        self.source = ''
        self.destination = ''
        self.overwrite = False
        self.dryrun = False
        self.verbose = False
        self.quiet = False

def parse_args(argv):
    config = Config()
    try:
        opts, args = getopt.getopt(argv[1:],
                                     'hs:d:ovq', [
                'help',
                'source=',
                'destination=',
                'overwrite',
                'dry-run',
                'verbose',
                'quiet',
                ])
        for o, a in opts:
            if o == '-h' or o == '--help':
                usage()
            elif o == '-s' or o == '--source':
                config.source = a
            elif o == '-d' or o == '--destination':
                config.destination = a
            elif o == '-o' or o == '--overwrite':
                config.overwrite = True
            elif o == '--dry-run':
                config.dryrun = True
            elif o == '-v' or o == '--verbose':
                config.verbose = True
            elif o == '-q' or o == '--quiet':
                config.quiet = True

        msg = ""
        if not config.source or not config.destination:
            usage("missing source or destination")
        
    except IndexError:
        usage()
    except getopt.GetoptError, err:
        usage(err)

    return config


if __name__ == "__main__":
    config = parse_args(sys.argv)

    count = 0

    reader = couchmigrator.reader(config.source)
    writer = couchmigrator.writer(config.destination)
    for record in reader:
        writer.write(record)
        count += 1

    reader.close()
    writer.close()

    print 'migrated {0} items'.format(count)
