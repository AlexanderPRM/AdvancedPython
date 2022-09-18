import unittest
from main import check_document_existance, get_doc_owner_name, \
    get_all_doc_owners_names, remove_doc_from_shelf, add_new_shelf, append_doc_to_shelf, \
    delete_doc, get_doc_shelf, move_doc_to_shelf, show_document_info, show_all_docs_info, add_new_doc
from parameterized import parameterized


class SecretaryProgramTest(unittest.TestCase):

    # Test function test_check_documents
    @parameterized.expand(
        [('10006', True),
         ('1444', False),
         ('3133', False),
         ('10006.', False),
         ('11-2', True)]
    )
    def test_check_document(self, doc_number, result):
        find = check_document_existance(doc_number)
        self.assertEqual(find, result)

    # Test function get_doc_ownername
    @parameterized.expand([
        ('Василий Гупкин', '2207 876234', True),
        ('Геннадий Покемонов', '11-2', True),
        ('Олег Волков', '11222', False)
    ])
    def test_get_doc_ownername(self, names, doc, excepted):
        owner_name, actual = get_doc_owner_name(doc)
        self.assertEqual(excepted, actual)


    # # Test function get_all_doc_owner_names
    @parameterized.expand([
        ('Василий Гупкин'),
        ('Геннадий Покемонов')
    ])
    def test_get_all_doc_owners_names(self, names):
        users_list = get_all_doc_owners_names()
        self.assertIn(names, users_list)

    # Test function remove_doc_from_shelf
    @parameterized.expand([
        ('10006', True),
        ('10006.', False),
        ('11-2', True)
    ])
    def test_remove_doc_from_shelf(self, doc_number, excepted):
        actually = remove_doc_from_shelf(doc_number)
        self.assertEqual(excepted, actually)

    # Test function add_new_shelf
    @parameterized.expand([
        ('5', True),
        ('10', True),
        ('1', False),
        ('1.', True)
    ])
    def test_add_new_shelf(self, shelf_number, excepted):
        shelf_number, actually = add_new_shelf(shelf_number)
        self.assertEqual(excepted, actually)

    # Test function append_doc_to_shelf
    @parameterized.expand([
        ('2', '10006', False),
        ('5', '112', True)
    ])
    def test_append_doc_to_shelf(self, shelf_number, doc_number, excepted):
        actually = append_doc_to_shelf(doc_number, shelf_number)
        self.assertEqual(excepted, actually)

    # Test function delete_doc
    @parameterized.expand([
        ('10006', True),
        ('11-2', True),
        ('11-2.', False)
    ])
    def test_delete_doc(self, doc_number, excepted):
        user_doc_number, actually = delete_doc(doc_number)
        self.assertEqual(excepted, actually)

    # Test function move_doc_to_shelf
    @parameterized.expand([
        ('10006', '5', True),
        ('11-2', '4', True),
        ('11-2.', '4', False)
    ])
    def test_move_doc_to_shelf(self, user_doc_number, user_shelf_number, expected):
        actual = move_doc_to_shelf(user_doc_number, user_shelf_number)
        self.assertEqual(expected, actual)

    # Test function get_doc_to_shelf
    @parameterized.expand([
        ('10006', True),
        ('11-2', True),
        ('11-2.', False)
    ])
    def test_get_doc_shelf(self, user_doc_number, excepted):
        shelf, actually = get_doc_shelf(user_doc_number)
        self.assertEqual(excepted, actually)

    # Test function show_document_info
    @parameterized.expand([
        ('11-2', True),
        ('10006', True),
        ('10006.', False)
    ])
    def test_show_document_info(self, doc_number, excepted):
        actually = show_document_info(doc_number)
        self.assertEqual(excepted, actually)

    # Test function add_new_doc
    @parameterized.expand([
        ('119-112', 'passport', 'Alexander', '10', True),
        ('10006', 'passport', 'Oleg', '2', False)
    ])
    def test_add_new_doc(self, doc_number, doc_type, owner_name, shelf, excepted):
        func = add_new_doc(doc_number, doc_type, owner_name, shelf)
        self.assertEqual(excepted, func)

if __name__ == '__main__':
    unittest.main()
