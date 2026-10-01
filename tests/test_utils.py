import unittest

from utils import to_utf8


class TestToUtf8(unittest.TestCase):
    def test_utf8_content_is_unchanged(self):
        content = "def f():\n    return 'ação'\n".encode('utf-8')

        self.assertEqual(to_utf8(content), content)

    def test_uses_pep263_coding_declaration(self):
        source = "# -*- coding: iso-8859-1 -*-\ndef f():\n    return 'Straße'\n"

        actual = to_utf8(source.encode('iso-8859-1'))

        self.assertEqual(actual.decode('utf-8'), source)

    def test_invalid_bytes_without_declaration_are_replaced(self):
        content = b"def f():\n    return '\xdf'\n"

        actual = to_utf8(content)

        self.assertEqual(actual.decode('utf-8'), "def f():\n    return '�'\n")


if __name__ == '__main__':
    unittest.main()
