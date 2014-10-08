# Requirements

You need to have [elasticsearch](http://www.elasticsearch.org/) up and
running on your machine. You can install it by following the
instructions:

    $ wget https://download.elasticsearch.org/elasticsearch/elasticsearch/elasticsearch-1.3.4.zip
    $ unzip elasticsearch-1.3.4.zip

I highly suggest you to install the `head` plugin, by typing:

    $ bin/plugin -install mobz/elasticsearch-head
    ...

Now you can start your indexing server:

    $ bin/elasticsearch

Time to point your web browser on the [head plugin](http://localhost:9200/_plugin/head/).

# How to use it

You just send out REST HTTP request to the server and you should be fine
or you can just install a more high-level binding, like `pyes`:

    $ pip install pyes
    $ pyenv rehash
