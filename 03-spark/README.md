# Requirements

You need to have [spark](http://spark.incubator.apache.org/) up and
running on your machine. I suggest you to use the binary distribution
(beware it is a 169M tgz file).

    $ wget http://d3kbcqa49mib13.cloudfront.net/spark-1.1.0-bin-hadoop1.tgz
    $ tar xvfz spark-1.1.0-bin-hadoop1.tgz

To start a master:

    $ SPARK_MASTER_IP=127.0.0.1 ./sbin/start-master.sh
    ...

You can now browse the [monitor web interface](http://localhost:8080) to
see the status of your spark cluster.

You can spawn multiple slaves and make them join on the cluster by
specifying the master URL:

    $ ./bin/spark-class org.apache.spark.deploy.worker.Worker spark://127.0.0.1:7077
    ...
    $ ./bin/spark-class org.apache.spark.deploy.worker.Worker spark://127.0.0.1:7077
    ...

You can stop the master with:

    $ ./sbin/stop-master.sh

# PageRank example

You can run the PageRank iterative algorithm on a simple graph by using:

    $ ./bin/spark-submit --master spark://127.0.0.1:7077 --driver-class-path lib/spark-examples-1.1.0-hadoop1.0.4.jar examples/src/main/python/pagerank.py ../../graph.txt 2 > output.txt

# PageRank is broken

The correct version is called `pagerank-slow-correct.py`.

# Running approximate PageRank on the link graph

    $ pycassaShell -k demo

    In [10]: for key, columns in LINKS.get_range():
                 for url, text in columns.items():
                     print key, url, text
