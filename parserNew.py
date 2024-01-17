import re
import configparser
from pymongo import MongoClient

config = configparser.ConfigParser()
config.read('config.ini')


class LogParser:
    def __init__(self, config_file='config.ini'):
        self.config = configparser.ConfigParser()
        self.config.read(config_file)

        self.mongo_client = MongoClient(
            self.config.get('MongoDB', 'host'),
            int(self.config.get('MongoDB', 'port'))
        )
        self.db = self.mongo_client[self.config.get('MongoDB', 'db')]
        self.collection = self.db[self.config.get('MongoDB', 'collection')]

        self.linux_pattern = self.config.get('Patterns', 'linux')
        self.windows_pattern = self.config.get('Patterns', 'windows')
        self.mac_pattern = self.config.get('Patterns', 'mac')

    def parse_and_insert(self, log_entry):
        linux_matches = re.findall(self.linux_pattern, log_entry)
        windows_matches = re.findall(self.windows_pattern, log_entry)
        mac_matches = re.findall(self.mac_pattern, log_entry)

        if linux_matches:
            self.insert_to_db(linux_matches[0])
        elif windows_matches:
            self.insert_to_db(windows_matches[0])
        elif mac_matches:
            self.insert_to_db(mac_matches[0])

    def insert_to_db(self, matches):
        doc_dict = {
            'month': matches[1],
            'date': matches[2] + matches[3],
            'time': matches[4],
            'severity': matches[9],
            'message': matches[-1]
        }
        self.collection.insert_one(doc_dict)


if __name__ == '__main__':
    log_parser = LogParser()
    log_entry = "<1>Jan 1 00:00:00 localhost app_name[123]: Log message example"
    log_parser.parse_and_insert(log_entry)
