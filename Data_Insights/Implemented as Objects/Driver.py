import time
import os
from datetime import datetime
import sys

from Src_to_Dataframe import SrcToDataframe as sd
from Insight_Creation import InsightCreation as ic

class Driver:

    def __init__(self, src_type, src_file_path, output_root_folder, primary_key):
        self.src_type = src_type
        self.src_file_path = src_file_path
        self.output_root_folder = output_root_folder
        self.primary_key = primary_key
        self.source = 0
        self.output_path = 0
        self.start_insight()

    def start_insight(self):
        try:
            if self.src_type == 1:
                self.source = sd.load_csv(self.src_file_path)
            elif self.src_type == 2:
                self.source = sd.load_sqlserver_data(self.src_file_path)
            elif self.src_type == 3:
                self.source = sd.load_mysql_data(self.src_file_path)
            elif self.src_type == 4:
                self.source = sd.load_oracle_data(self.src_file_path)
            elif self.src_type == 5:
                self.source = sd.load_msaccess_data(self.src_file_path)
            elif self.src_type == 6:
                self.source = sd.load_netezza_data(self.src_file_path)
            elif self.src_type == 7:
                self.source = sd.load_json(self.src_file_path)
            elif self.src_type == 8:
                self.source = sd.load_json_normalize(self.src_file_path)
            elif self.src_type == 9:
                print("Other sources are not supported now. Kindly contact Admin.")
                time.sleep(30)
                sys.exit()
            else:
                print("Choosen Invalid option, kindly choose correct option.")
                time.sleep(30)
                sys.exit()
        except Exception as err:
            print(str(err))
            sys.exit()
        report = "Report_" + datetime.now().strftime("%Y%m%d_%H%M%S%f")
        self.output_path = self.output_root_folder + report
        try:
            os.mkdir(self.output_path)
        except Exception as err:
            print(err)
        try:
            ic.create_summary(self.source, self.output_path)
        except Exception as err:
            print(err)
        try:
            ic.find_complete_duplicates(self.source, self.output_path)
        except Exception as err:
            print(err)
        try:
            ic.find_pk_duplicates(self.source, self.output_path, self.primary_key)
        except Exception as err:
            print(err)
        try:
            ic.find_null_counts(self.source, self.output_path)
        except Exception as err:
            print(err)
        try:
            ic.find_unique_values(self.source, self.output_path)
        except Exception as err:
            print(err)
        try:
            ic.find_stats(self.source, self.output_path)
        except Exception as err:
            print(err)
        print("Output is available in: ", self.output_path)





