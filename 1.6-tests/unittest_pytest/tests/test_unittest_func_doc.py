import unittest
from func_doc import people, shelf, list_doc, add_doc, current_doc, finder_doc
from func_doc import move_doc, add_shelf, del_doc, documents, directories



class TestFunctions(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_people(self):
        self.assertEqual(people('11-2'), '\nВладелец документа №11-2 - Геннадий Покемонов.\n')

    def test_shelf(self):
        self.assertEqual(shelf('11-2'), '\nДокумент №11-2 находится на полке №1.\n')

    def test_current_doc(self):
        self.assertEqual(current_doc({"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"}),
                                     'invoice "11-2" "Геннадий Покемонов"')

# Я так и не понял как проверить такую функцию
    def test_list_doc(self):
        self.assertEqual(list_doc(documents), None)

    def test_add_doc_1(self):
        self.assertEqual(add_doc(doc_num='47', doc_type='id', doc_name='Джеффри Лебовски', doc_dir='3'),
                                "\nДокумент №47 добавлен на полку №3.\n")

    def test_add_doc_2(self):
        self.assertIn('47', directories['3'])

    def test_add_doc_3(self):
        new_doc = {"type": "id", "number": "47", "name": "Джеффри Лебовски"}
        self.assertIn(new_doc, documents)

    def test_finder_doc(self):
        self.assertTrue(finder_doc('11-2'))

    def test_del_doc_1(self):
        self.assertEqual(del_doc('10006'), "\nДокумент №10006 удалён.\n")

    def test_del_doc_2(self):
        d_doc = {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
        self.assertNotIn(d_doc, documents)

    def test_del_doc_3(self):
        self.assertNotIn('10006', directories['2'])

    def test_move_doc_1(self):
        self.assertEqual(move_doc('47', '2'),
                         "\nДокумент №47 перемещён с полки №3 на полку №2\n")

    def test_move_doc_2(self):
        self.assertNotIn('47', directories['3'])
        self.assertIn('47', directories['2'])

    def test_add_shelf_1(self):
        self.assertEqual(add_shelf('4'), "\nПолка №4 добавлена.\n")

    def test_add_shelf_2(self):
        self.assertIn('4', directories)
