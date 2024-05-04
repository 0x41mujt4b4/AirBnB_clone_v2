import unittest
import MySQLdb
import os


host = os.getenv('HBNB_MYSQL_HOST')
user = os.getenv('HBNB_MYSQL_USER')
password = os.getenv('HBNB_MYSQL_PWD')
database = os.getenv('HBNB_MYSQL_DB')


class TestDatabase(unittest.TestCase):
    """ Test the database connection """
    def setUp(self):
        """ Set up the database connection """
        self.db = MySQLdb.connect(
            host=host,
            user=user,
            password=password,
            database=database
            )
        self.cursor = self.db.cursor()

    def test_connection(self):
        """ Test the database connection """
        self.assertTrue(self.db.is_connected())

    def test_insert_state(self):
        # Get the number of records in the states table
        self.cursor.execute("SELECT COUNT(*) FROM states")
        count_before = self.cursor.fetchone()[0]
        # Execute the console command (insert a new state)
        os.system("./console.py -c 'create State name=\"California\"'")
        # Get the number of records in the states table
        self.cursor.execute("SELECT COUNT(*) FROM states")
        count_after = self.cursor.fetchone()[0]
        # Check the number of records in states table has increased by 1
        self.assertEqual(count_after, count_before + 1)

    def tearDown(self):
        """ Close the database connection """
        self.cursor.close()
        self.db.close()


if __name__ == '__main__':
    unittest.main()
