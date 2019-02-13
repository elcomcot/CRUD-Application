from unittest import TestCase
import dataBase


class TestDataBaseClass(TestCase):
    def test_createTableWithDataInDataBase(self):
        result = dataBase.dataBaseClass.createTableWithDataInDataBase()
        self.assertEqual(result, 5)

    def test_selctRowFromMysql(self):
        result = dataBase.dataBaseClass.selctRowFromMysql(5)
        self.assertEqual(result.__len__(), 1)

    def test_deleteRowInDb(self):
        result = dataBase.dataBaseClass.deleteRowInDb(1)
        self.assertEqual(result, 5)

    def test_updateRowInDb(self):
        result = dataBase.dataBaseClass.updateRowInDb(1,"dfsd","dfsd","dfsd","dfsd","dfsd","dfsd","dfsd","dfsd","dfsd","dfsd","dfsd","dfsd","dfsd","dfsd","dfsd","dfsd")
        self.assertEqual(result, 5)

    def test_insertTheNewData(self):
        result = dataBase.dataBaseClass.insertTheNewData("fsdgvfs","dfsdf","dfsdf","dfsdf","dfsdf","dfsdf","dfsdf","dfsdf","dfsdf","dfsdf","dfsdf","dfsdf","dfsdf","dfsdf","dfsdf","dfsdf")
        self.assertEqual(result, 5)

    # def test_closeCursor(self):
    #     result = dataBase.dataBaseClass.closeCursor()
    #     self.assertEqual(result, 5)
