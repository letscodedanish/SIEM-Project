from pymongo import MongoClient
import re

class WindowsLogParser:
    def __init__(self):
        self.mongo_client = MongoClient('localhost', 27017)
        self.db = self.mongo_client['project_db']
        self.collection = self.db['win2_log']
        self.win2_pattern = r"(\d{2}.\d{2}.\d{3}.\d{2}) <(\d+)>(\d+) (\d{4})-(\d{2})-(\d{2})[T](\d{2}:\d{2}:\d{2})[+](\d{2}:\d{2}) (\d{2}.\d{2}.\d{3}.\d{2}) ([A-Z]*) - (\w*) - %([A-Z]*)-
