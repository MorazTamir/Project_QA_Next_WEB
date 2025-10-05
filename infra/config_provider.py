import json

class ConfigProvider:

    @staticmethod
    def load_config_file(file_path):
        try:
            with open(file_path,'r',encoding='utf-8') as file:
               return json.load(file)
        except FileNotFoundError:
            print(f"File {file_path} not found")