#
import glob
import pandas as pd

from code.func import extract_from_csv, extract_from_json, extract_from_xml
from vars import raw_data_path 


def extract():

    # create an empty data frame to hold extracted data  
    extracted_data = pd.DataFrame(
        columns=['name','height','weight']
    ) 
     
    # process all csv files 
    for csvfile in glob.glob(raw_data_path + "*.csv"): 
        extracted_data = pd.concat(
            [extracted_data, pd.DataFrame(extract_from_csv(csvfile))], ignore_index=True
        ) 
         
    # process all json files 
    for jsonfile in glob.glob(raw_data_path + "*.json"): 
        extracted_data = pd.concat(
            [extracted_data, pd.DataFrame(extract_from_json(jsonfile))], ignore_index=True
        ) 
     
    # process all xml files 
    for xmlfile in glob.glob(raw_data_path + "*.xml"): 
        extracted_data = pd.concat(
            [extracted_data, pd.DataFrame(extract_from_xml(xmlfile))], ignore_index=True
        ) 
         
    return extracted_data  
