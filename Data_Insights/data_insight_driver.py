from Source_To_Dataframe import SrcToDatafarme as sd
from insights import Insights as ist
import time
import os
import sys

class DataInsightDriver:
    """This class contains the driver functions, gets user input and calls others functions"""

    def data_insight_driver():
        print("Enter option from below based on your source data type")
        src_type = int(input(" 1. CSV \n 2. DB - SQL Server \n 3. MySQL \n 4. DB - Oracle \n 5. DB - MS Access  \n 6. DB - Netezza "
                             "\n 7. Simple JSON \n 8. Nested Json \n 9. Others \n   "))
        src_file_path = input("Enter the Absolute path of source file: ")

        try:
            if src_type == 1:
                source = sd.load_csv(src_file_path)
            elif src_type == 2:
                source = sd.load_sqlserver_data(src_file_path)
            elif src_type == 3:
                source = sd.load_mysql_data(src_file_path)
            elif src_type == 4:
                source = sd.load_oracle_data(src_file_path)
            elif src_type == 5:
                source = sd.load_msaccess_data(src_file_path)
            elif src_type == 6:
                source = sd.load_netezza_data(src_file_path)
            elif src_type == 7:
                source = sd.load_json(src_file_path)
            elif src_type == 8:
                source = sd.load_json_normalize(src_file_path)
            elif src_type == 9:
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

        print("Enter the primary key column name, if it is a combination of multiple columns, seperate it with comma")
        print("if you don't know primary key, please press enter key. We will be considering combination of all columns as primary key.")
        primary_key = (input()).split(",")
        output_root_folder = input("Please enter the absolute path of output, when you want results to be published: ")
        report = "Report_"+time.strftime("%Y%m%d_%H%M%S")
        output_path = output_root_folder+report
        try:
            os.mkdir(output_path)
        except Exception as err:
            print(err)
        try:
            ist.create_summary(source, output_path)
        except Exception as err:
            print(err)
        try:
            ist.find_complete_duplicates(source, output_path)
        except Exception as err:
            print(err)
        try:
            ist.find_pk_duplicates(source, output_path, primary_key)
        except Exception as err:
            print(err)
        try:
            ist.find_null_counts(source, output_path)
        except Exception as err:
            print(err)
        try:
            ist.find_unique_values(source, output_path)
        except Exception as err:
            print(err)
        try:
            ist.find_stats(source, output_path)
        except Exception as err:
            print(err)
        print("Output is available in: ", output_path)



