from import_config import read_db_config  # Imports the function to import the config from the
# import_config module
from mysql.connector import MySQLConnection, Error  # Imports the connector and error functions from the MySQL


# library


# Defines a function called connect() which will attempt to connect to the database with the credential defined by the
# read_db_config function
def connect():
    our_config = read_db_config()  # places the config from the .ini file into our_config dictionary

    try:
        print("Connecting to database...")
        conn = MySQLConnection(**our_config)  # attempts to connect using the our_config dictionary (hence the **)

        if conn.is_connected():  # test the connection status and responds accordingly
            print("Connection established.")
        else:
            print("Connection failed.")

    except Error as error:  # if connection failed, return the error generated in the attempt
        print(error)

    finally:  # in all cases close the connection to prevent memory leak
        conn.close()
        print("Connection closed.")


if __name__ == "__main__":  # just a way of confirming the program is not being called by another
    connect()  # python script as a function for security.

# That last bit needs some clarification. So any .py file can call any other .py file and use it like an imported
# library. The test "if __name__ == "__main__" prevents this, because if the .py file has been imported into another .py
# file, then the __name__ variable will not be "__main__" so the connect() function will not run.

# One last consideration is the security aspect. The .ini file being used is in plain text - so can easily be viewed by
# anyone with a text editor and some simple knowledge - not good. In the real world the information is encrypted by an
# algorithm then written to the ini. When needed the function opening the .ini will decrypt it first and then use it
# thus ensuring secure storage of details.
