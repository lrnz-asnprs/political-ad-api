    # merge all single files into one bigger!
import json
import os

  # helper function
def read_dataset(path_of_file: str): # returns file as python object
        with open(path_of_file) as json_file:
            return json.load(json_file)

def merge_files(directory: str):
        dir = r'single_files'
        final_list = []
        files = set() # iterate over files in that directory and put in set
        for filename in os.listdir(dir):
            print(filename)
                    # checking if it is a file
            if filename.endswith("txt"):
                    files.add(filename)
        while len(files) > 0:
            file = files.pop()
            try:
                print(dir + "\\" + file)
                joined_path = dir + "\\" + file
                data = read_dataset(joined_path)
                final_list.extend(data) # concatenate data to list
                print(len(final_list))
            except:
                files.add(file) # add file back
                print(f"There was an error with file {file}")

        jsonFile = open("data\\all_politicians_aggregated_final.txt", "w") # filepath and name specified here!
        final_file_str = json.dumps(final_list)
        jsonFile.write(final_file_str)
        jsonFile.close()

merge_files("single_files")
print("done")