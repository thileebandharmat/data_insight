import pandas as pd
import os

class InsightCreation:

    def create_summary(source, output_path):
        """This function gets a dataframe and output path as an input,
                Finds number of records, number of duplicate records, column names, data types and sample records.
                Writes those findings in a text file"""
        print("Started creating summary.,")
        src_cnt = "Number of records in Source is: " + str(len(source)) + "\n\n"
        src_dup_cnt = "Number of duplicate records in source is: " + str(
            len(source[source.duplicated(keep=False)])) + "\n\n"
        column_name = "Attribute names available in source is: " + str(list(source.columns)) + "\n\n"
        data_msg = "Data type of each attribute name is as below \n"
        data_types = str(source.dtypes) + "\n\n"
        header_msg = "Sample records from the source is as below \n"
        sample_records = source.sample(n=10)
        report = 'Summary.txt'
        summary_report = os.path.join(output_path, report)
        with open(summary_report, 'a') as fl:
            fl.writelines([src_cnt, src_dup_cnt, column_name, data_msg, data_types, header_msg, str(sample_records)])
        sample_file_nm = 'Sample_records.csv'
        sample_file_path = os.path.join(output_path, sample_file_nm)
        source.sample(n=1000).to_csv(sample_file_path)
        print("Completed creating summary.,")

    def find_complete_duplicates(source, output_path):
        """This function receives a dataframe and output path as an input.
        Finds the complete duplicate records in the dataframe.
        Writes those duplicate records in a csv file in the output path"""
        print("Started finding complete duplicate records.,")
        overall_dup_cnt = len(source[source.duplicated(keep=False)])
        report = 'Complete_Duplicate.csv'
        duplicate_report = os.path.join(output_path, report)
        if overall_dup_cnt > 1:
            dup_df = source[source.duplicated(keep=False)]
            dup_df.to_csv(duplicate_report)
        else:
            print("No duplicate records Available")
        print("Completed finding complete duplicate records.,")

    def find_pk_duplicates(source, output_path, primary_key):
        """This function receives a dataframe, output path and primary key of a dataframe as an input.
        Finds the duplicate records based on the primary key.
        Writes those duplicate records in a csv file in the output path"""
        print("Started finding duplicate records based on primary key.,")
        if primary_key[0] == '':
            primary_key = list(source.columns)
        report = 'Primary_Key_Duplicate.csv'
        primary_key_duplicate_report = os.path.join(output_path, report)
        pk_dup_df = source[source.duplicated(subset=primary_key, keep=False)]
        pk_dup_df.to_csv(primary_key_duplicate_report)
        print("Completed finding duplicate records based on primary key.,")

    def find_null_counts(source, output_path):
        """This function receives the dataframe and output path as an input.
        Finds the number of null records and not null records in each columns.
        Writes those count information in a csv file in the output path"""
        print("Started finding count of null and not null records in each column.,")
        null_records = source.isnull().sum()
        not_null_records = source.notnull().sum()
        null_and_not_null = pd.concat([not_null_records, null_records], axis=1)
        null_and_not_null.columns = ['Not_Null_count', 'Null_count']
        report = 'Null_not_null_records_counts.csv'
        report_name = os.path.join(output_path, report)
        null_and_not_null.to_csv(report_name)
        print("Completed finding count of null and not null records in each column.,")

    def find_unique_values(source, output_path):
        """This function receives dataframe and output path as an input.
        Finds the unique records and number of times it is repeated.
        Writes those details as a csv file in the output path"""
        print("Started finding unique values and its count in each column.,")
        report = 'Unique_values'
        os.mkdir(os.path.join(output_path, report))
        for col_nm in list(source.columns):
            report_col_name = 'Unique_values_in_column_' + str(col_nm) + '.csv'
            report_name = os.path.join(output_path, report, report_col_name)
            unique_value_df = source[col_nm].value_counts().to_frame()
            unique_value_df.index.name = col_nm
            unique_value_df.columns = ['count']
            unique_value_df.to_csv(report_name)
        print("Completed finding unique values and its count in each column.,")

    def find_stats(source, output_path):
        """This function receives dataframe and output path as an input.
        Find the following stats in each column count, min, max, std, 25%, 50% and 75%.
        Writes those information in a csv file in the output path"""
        print("Started finding the stats of each column.,")
        report = 'High_level_stats.csv'
        report_with_path = os.path.join(output_path, report)
        source.describe(include='all').transpose().to_csv(report_with_path)
        print("Completed finding the stats of each column.,")




