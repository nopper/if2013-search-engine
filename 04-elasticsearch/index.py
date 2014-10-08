import pycassa
from pycassa.pool import ConnectionPool

pool = ConnectionPool("demo", "127.0.0.1")
page = pycassa.ColumnFamily(pool, "page")

import pyes

es = pyes.ES()

for key, document in page.get_range():
    es.index(document, "document", "document")
