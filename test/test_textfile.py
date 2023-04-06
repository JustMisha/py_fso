import os
import random

import unittest

import py_fso.folder
import py_fso.textfile


class TextfileTestCase(unittest.TestCase):

    test_dir = os.path.join(os.path.dirname(os.path.realpath(__file__)), "textfile")

    def test_convert_to_utf8(self):
        file_path = os.path.join(self.test_dir, "proba.txt")

        common_text = "Проба  Test"

        text = common_text.encode("cp1251")
        with open(file_path, "wb") as f1:
            f1.write(text)

        py_fso.textfile.convert_to_utf8(file_path, initial_encoding='cp1251')

        with open(file_path, "r", encoding="UTF-8") as f2:
            converted_text = f2.read()

        self.assertEqual(common_text, converted_text)

        os.remove(file_path)

    def test_convert_to_utf8_no_need(self):
        file_path = os.path.join(self.test_dir, "proba.txt")

        common_text = "Проба  Test"

        text = common_text.encode("UTF-8")
        with open(file_path, "wb") as f1:
            f1.write(text)

        py_fso.textfile.convert_to_utf8(file_path)

        with open(file_path, "r", encoding="UTF-8") as f2:
            converted_text = f2.read()

        self.assertEqual(common_text, converted_text)

        os.remove(file_path)

    def test_split_into_certain_parts_amount(self):

        parts_amount = 10

        d = 3
        n = 10000

        big_file_path = os.path.join(self.test_dir, "big_text_file.txt")

        f = open(big_file_path, 'w')

        for i in range(n):
            nums = [str(round(random.uniform(0, 1000), 3)) for j in range(d)]
            f.write(' '.join(nums))
            f.write('\n')

        f.close()

        output_files_path = os.path.join(self.test_dir, "big_text_file_chunks.txt")

        py_fso.textfile.split_into_certain_parts_amount(big_file_path, parts_amount, output_name=output_files_path, file_encode='utf8')

        file_size = 0
        real_parts_amount = 0
        def just_lambda_func(entry):
            nonlocal file_size
            nonlocal real_parts_amount
            if os.path.splitext(entry.path)[0] == output_files_path:
                file_size += os.path.getsize(entry.path)
                real_parts_amount += 1
                os.remove(entry.path)

        result = py_fso.folder.process(self.test_dir, process_files=True,
                                        proc_file_function=just_lambda_func, process_dirs=False,
                                        proc_dir_function=None,
                                        go_into_subdirs=False, follow_symlinks=False)

        self.assertEqual(result, 0)
        self.assertEqual(parts_amount, real_parts_amount)
        self.assertEqual(os.path.getsize(big_file_path), file_size)

        os.remove(big_file_path)

    def test_split_into_parts_certain_size(self):
        d = 3
        n = 10000

        big_file_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "textfile", "big_text_file.txt")

        f = open(big_file_path, 'w')

        for i in range(n):
            nums = [str(round(random.uniform(0, 1000), 3)) for j in range(d)]
            f.write(' '.join(nums))
            f.write('\n')

        f.close()

        output_files_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "textfile",
                                         "big_text_file_chunks.txt")

        part_size = int(round(os.path.getsize(big_file_path) / 10, 0))

        py_fso.textfile.split_into_parts_certain_size(big_file_path, part_size, output_name=output_files_path, file_encode='utf8')

        file_size = 0

        def just_lambda_func(entry):
            nonlocal file_size
            if os.path.splitext(entry.path)[0] == output_files_path:
                file_size += os.path.getsize(entry.path)
                os.remove(entry.path)

        result = py_fso.folder.process(self.test_dir, process_files=True,
                                       proc_file_function=just_lambda_func, process_dirs=False,
                                       proc_dir_function=None,
                                       go_into_subdirs=False, follow_symlinks=False)

        self.assertEqual(result, 0)
        self.assertEqual(os.path.getsize(big_file_path), file_size)

        os.remove(big_file_path)


if __name__ == '__main__':
    unittest.main()
