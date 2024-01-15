import configparser
from pymongo import MongoClient
import re

class LogParser:
    """
    Class for parsing logs and inserting data into MongoDB.
    """

    def __init__(self, config_file='config.ini'):
        """
        Initialize LogParser instance.

        Parameters:
            config_file (str): Path to the configuration file.
        """
        self.config = configparser.ConfigParser()
        self.config.read(config_file)

        self.mongo_client = MongoClient(
            self.config.get('MongoDB', 'host'),
            int(self.config.get('MongoDB', 'port'))
        )
        self.db = self.mongo_client[self.config.get('MongoDB', 'db')]
        self.collection = self.db[self.config.get('MongoDB', 'collection')]

        self.linux_pattern = self.config.get('Patterns', 'linux')
        self.mac_pattern = self.config.get('Patterns', 'mac')

    def parsing(self, filename):
        """
        Parse logs from the specified file and insert data into MongoDB.

        Parameters:
            filename (str): Path to the log file.
        """
        acount, exception_count, line_count, ncount = 0, 0, 0, 0
        doc_list = []
        linux, mac = 0, 0
        doc_dict = {}

        with open(filename, 'r') as logfile:
            lines = logfile.readlines()
            line_count += 1

            for l in lines:
                try:
                    matches1 = re.findall(self.linux_pattern, l)
                    matches2 = re.findall(self.mac_pattern, l)

                    if len(matches1):
                        doc_dict = {
                            'month': matches1[0][1],
                            'date': matches1[0][2] + matches1[0][3],
                            'time': matches1[0][4],
                            'hostname': matches1[0][5],
                            'severity': matches1[0][6],
                            'app_name': matches1[0][7],
                            'message': matches1[0][-1]
                        }
                        linux += 1
                    elif len(matches2):
                        doc_dict = {
                            'month': matches2[0][2],
                            'date': matches2[0][3] + matches2[0][4],
                            'time': matches2[0][5],
                            'hostname': matches2[0][10],
                            'severity': matches2[0][9],
                            'app_name': matches2[0][8],
                            'message': matches2[0][-1]
                        }
                        mac += 1

                    acount += 1
                    doc_list.append(doc_dict)

                    if acount == 5:
                        self.collection.insert_many(doc_list)
                        print(line_count, "-------------------")
                        acount = 0
                        doc_list.clear()

                    print("linux ", linux)
                    print("mac ", mac)
                    print("not", ncount)
                except Exception as e:
                    exception_count += 1
                    print(line_count, f"Lines processed ({e})")

        if len(doc_list) > 1:
            self.collection.insert_many(doc_list)
            print(line_count, "lines processed")
            doc_list.clear()

if __name__ == '__main__':
    log_parser = LogParser()
    file_name = "C:\\project\\data6.csv"  # Replace with your actual file path
    log_parser.parsing(file_name)
