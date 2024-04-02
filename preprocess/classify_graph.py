import json
import os

if __name__=='__main__':
    folder_path = 'xxx/vector/'
    file_list = os.listdir(folder_path)
    sorted_file_list = sorted(file_list)
    data_list = []
    name2nodeNum_dict = {}
    for file_name in sorted_file_list:
        file_path = os.path.join(folder_path, file_name)
        with open(file_path, 'r') as f:
            nodeAttributeDict = json.load(f)
        num_keys = len(nodeAttributeDict.keys())
        processed_string = file_path.split("/vector/")[1]
        processed_string = processed_string.split("-000")[0] 
        if processed_string not in name2nodeNum_dict:
            name2nodeNum_dict[processed_string] = num_keys
    
    with open('xxx/name2nodeNum_dict.json', 'w') as f:
        json.dump(name2nodeNum_dict, f)
