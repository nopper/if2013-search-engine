# Requirements

You need to have [cassandra](http://cassandra.apache.org/) possibly the
`2.1.0` release up and running on your box. To do so:

    $ wget http://apache.fastbull.org/cassandra/2.1.0/apache-cassandra-2.1.0-bin.tar.gz
    $ tar xvfz apache-cassandra-2.1.0-bin.tar.gz

You need to create some directories that will be used to hold your data:

    $ cd apache-cassandra-2.1.0
    $ mkdir -p data/{data,commitlog,saved_caches}

After that you can start your server with:

    $ bin/cassandra -f

# Python requirements

Python binding are availabe in `pycassa`. Install it with:

    $ pip install pycassa
    $ pyenv rehash

# Simple Keyspace setup

    $ bin/cassandra-cli
    ...
    [default@unknown] create keyspace demo;
    52d926b4-c9bf-369b-92a7-28d5e9935bc4
    [default@unknown] use demo;
    Authenticated to keyspace: demo
    [default@unknown] create column family page with
                      comparator = UTF8Type and
                      default_validation_class = UTF8Type and
                      key_validation_class = UTF8Type;
    ...
    [default@unknown] create column family links with
                      comparator = UTF8Type and
                      default_validation_class = UTF8Type and
                      key_validation_class = UTF8Type;

You can easily insert data with `set` and retrieve it with `get`:

    [default@unknown] set page['it.repubblica.www:80:/']['url'] = 'http://ww.repubblica.it';
    ...
    [default@unknown] set page['it.repubblica.www:80:/berlusconi']['url'] = 'http://ww.repubblica.it/berlusconi';
    ...
    [default@demo] get page['it.repubblica.www:80:/berlusconi']['url'];
    => (name=url, value=http://ww.repubblica.it/berlusconi, timestamp=1381398759998000)

Delete is supported with the insertion of tombstones:

    [default@demo] del page['it.repubblica.www:80:/'];
    ...
    [default@demo] del page['it.repubblica.www:80:/berlusconi'];
    ...
    [default@demo] list page;
    Using default limit of 100
    Using default cell limit of 100
    -------------------
    RowKey: it.repubblica.www:80:/
    -------------------
    RowKey: it.repubblica.www:80:/berlusconi

# Exploit cassandra for data storage in scrapy

Now you can go back to the scrapy project and enable the
`CassandraPipeline` I have prepared in the `settings.py` file by
uncommenting the `ITEM_PIPELINES` directive.
