import unittest
from program import get_doc_owner_name, add_new_doc, delete_doc


class test_program(unittest.TestCase):

    def test_get_doc_owner_name(self):
        self.assertEqual('Василий Гупкин', get_doc_owner_name('2207 876234'), 'Записи нет')

    def test_delete_doc(self):
        self.assertEqual(('10006', True), delete_doc('10006'), 'Указанного документа нет')

    def test_add_new_doc(self):
        self.assertEqual('4', add_new_doc('007', 'invoise', 'Batman', '4'), 'Документ не создан')

if __name__ == '__main__':
    unittest.main()