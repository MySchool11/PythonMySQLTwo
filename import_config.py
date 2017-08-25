# This module uses the ConfigParser to import the settings for the MySQL connection from the file config.ini

from configparser import ConfigParser


def read_db_config(filename="config.ini", section="mysql"):
    parser = ConfigParser()
    parser.read(filename)

    db = {}
    if parser.has_section(section):
        items = parser.items(section)
        for item in items:
            db[item[0]] = item[1]
    else:
        raise Exception("{0} not found in the {1} file".format(section, filename))

    return db
