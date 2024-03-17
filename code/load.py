#
from vars import transformed_data_path


def load_data(target_file, transformed_data): 
    transformed_data.to_csv(transformed_data_path + target_file) 