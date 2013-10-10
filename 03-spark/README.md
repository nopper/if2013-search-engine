# Requirements

You need to have [spark](http://spark.incubator.apache.org/) up and
running on your machine. I suggest you to use the binary distribution
(beware it is a 127M tgz file).

    $ wget http://spark-project.org/download/spark-0.8.0-incubating-bin-hadoop1.tgz
    $ tar xvfz spark-0.8.0-incubating-bin-hadoop1.tgz

To start a master:

    $ SPARK_MASTER_IP=127.0.0.1 ./bin/start-master.sh
    ...

You can now browse the [monitor web interface](http://localhost:8080) to
see the status of your spark cluster.

You can spawn multiple slaves and make them join on the cluste by
specifying the master URL:

    $ ./bin/start-slave.sh 1 spark://127.0.0.1:7077
    ...
    $ ./bin/start-slave.sh 2 spark://127.0.0.1:7077
    ...

# PageRank example

You can run the PageRank iterative algorithm on a simple graph by using:

    $ ./pyspark python/examples/pagerank.py spark://127.0.0.1:7077 pagerank_data.txt 10

# PageRank is broken

The correct version is called `pagerank-slow-correct.py`.

# Running approximate PageRank on the link graph

    $ pycassaShell -k demo

    In [10]: for key, columns in LINKS.get_range():
                 for url, text in columns.items():
                     print key, url, text
