import pycassa
from pycassa.pool import ConnectionPool

from urlparse import urlparse

class CassandraPipeline(object):
    def __init__(self):
        self.pool = ConnectionPool("demo", "127.0.0.1")
        self.links = pycassa.ColumnFamily(self.pool, "links")
        self.page = pycassa.ColumnFamily(self.pool, "page")

    def encode_url(self, url):
        parse_result = urlparse(url)

        port = parse_result.port
        location = parse_result.netloc
        protocol = parse_result.scheme
        path = parse_result.path

        if not protocol.startswith("http"):
            return None

        if port:
            location = location.replace(":%s" % port, "")
            protocol = port

        if protocol == "http":
            protocol = "80"
        elif protocol == "https":
            protocol = "443"

        location = '.'.join(reversed(location.split(".")))

        # The output is something like this: it.ilpost.www:80:/
        return "%s:%s:%s" % (location, protocol, path)

    def process_item(self, item, spider):
        url = self.encode_url(item['url'])

        self.page.insert(url, {
            'url': item['url'],
            'title': item['title'],
            'desc': item['desc'],
        })

        columns = {}

        for link in item['links']:
            link_text = link['text']
            link_url_encoded = self.encode_url(link['url'])

            if link_url_encoded:
                columns[link_url_encoded] = link_text

        if columns:
            self.links.insert(url, columns)
