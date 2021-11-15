import json
import os

class Config:

    @staticmethod
    def get_config_file():
        root_path = os.path.dirname(os.path.abspath(__file__))
        config_file_name = root_path + r"\config.json"        
        with open(config_file_name) as f:
            config_file = json.load(f)
            return config_file
        
    @staticmethod
    def get_signin_id():
        return Config.get_config_file()["account_info"]["singin_id"]

    @staticmethod
    def get_signin_password():
        return Config.get_config_file()["account_info"]["password"]

    @staticmethod  
    def get_credit_card_info():
        return Config.get_config_file()["account_info"]["my_credit_card"]

    @staticmethod
    def get_pages():
        return Config.get_config_file()["pages"]

    @staticmethod
    def get_pages_for_signup_flow_test():
        return Config.get_pages()["signup_flow_test"]