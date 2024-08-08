from configparser import ConfigParser

def get_config(category,key):
    con = ConfigParser()
    con.read("C:\\Users\\SM\\Desktop\\Suvetha_pytest(8-6)\\Pytest_OrangeHRM\\Configurations\\config.ini")
    return con.get(category,key)