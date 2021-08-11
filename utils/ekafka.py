import os

from config import config
from pykafka import KafkaClient

flask_config = os.getenv('FLASK_CONFIG') or 'default'
kafka_uri = config[flask_config].KAFKA_URI


class Pkafka:
    def __init__(self):
        self.bootstrap_servers = kafka_uri

    def check_version(self):
        version = KafkaClient(
            bootstrap_servers=self.bootstrap_servers).check_version()
        return version


if __name__ == '__main__':
    print(kafka_uri)
