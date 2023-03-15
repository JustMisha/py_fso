from io import StringIO
import os
import sys

import unittest

import py_fso.folder

class FolderTestCase(unittest.TestCase):
    maxDiff = None
    common_init_dir = os.path.join(os.path.dirname(os.path.realpath(__file__)), "folder", "test_init")
    def test_process_print_all_files_and_subdirs(self):
        output = ''
        def just_lambda_func(entry):
            nonlocal output
            output += entry.path + '\n'

        result = py_fso.folder.process(self.common_init_dir, process_files=True, proc_file_function=just_lambda_func, process_dirs=True, proc_dir_function=just_lambda_func,
            go_into_subdirs=True, follow_symlinks=False)

        awaited_output = (
            os.path.join(self.common_init_dir, "test_1") +
            "\n" +
            os.path.join(self.common_init_dir, "test_2") +
            "\n" +
            os.path.join(self.common_init_dir, "test_3") +
            "\n" +
            os.path.join(self.common_init_dir, "test_file_0.txt") +
            "\n" +
            os.path.join(self.common_init_dir, "test_1", "test_file_1.txt") +
            "\n" +
            os.path.join(self.common_init_dir, "test_1", "test_file_2.txt") +
            "\n" +
            os.path.join(self.common_init_dir, "test_1", "test_file_3.txt") +
            "\n" +
            os.path.join(self.common_init_dir, "test_2", "test_file_4.txt") +
            "\n" +
            os.path.join(self.common_init_dir, "test_3", "test_file_5.txt") +
            "\n"
        )
        self.assertEqual(awaited_output, output)
        self.assertEqual(result, 0)

    def test_process_print_subdirs_only(self):
        output = ''
        def print_subdir(entry):
            nonlocal output
            if entry.is_dir:
                output += entry.path + '\n'

        result = py_fso.folder.process(self.common_init_dir, process_files=False, proc_file_function=None, process_dirs=True, proc_dir_function=print_subdir,
            go_into_subdirs=True, follow_symlinks=False)
        awaited_output = (
            os.path.join(self.common_init_dir, "test_1") +
            "\n" +
            os.path.join(self.common_init_dir, "test_2") +
            "\n" +
            os.path.join(self.common_init_dir, "test_3") +
            "\n"
        )

        self.assertEqual(awaited_output, output)
        self.assertEqual(result, 0)

    def test_process_print_files_only(self):
        output = ''
        def print_file(entry):
            nonlocal output
            output += entry.path + '\n'

        result = py_fso.folder.process(self.common_init_dir, process_files=True, proc_file_function=print_file, process_dirs=False, proc_dir_function=None,
            go_into_subdirs=True, follow_symlinks=False)
        awaited_output = (
            os.path.join(self.common_init_dir, "test_file_0.txt") +
            "\n" +
            os.path.join(self.common_init_dir, "test_1", "test_file_1.txt") +
            "\n" +
            os.path.join(self.common_init_dir, "test_1", "test_file_2.txt") +
            "\n" +
            os.path.join(self.common_init_dir, "test_1", "test_file_3.txt") +
            "\n" +
            os.path.join(self.common_init_dir, "test_2", "test_file_4.txt") +
            "\n" +
            os.path.join(self.common_init_dir, "test_3", "test_file_5.txt") +
            "\n"
        )

        self.assertEqual(awaited_output, output)
        self.assertEqual(result, 0)

    def test_process_print_files_only_without_subdirs(self):
        output = ''
        def print_file(entry):
            nonlocal output
            output += entry.path + '\n'

        result = py_fso.folder.process(self.common_init_dir, process_files=True, proc_file_function=print_file, process_dirs=False, proc_dir_function=None,
            go_into_subdirs=False, follow_symlinks=False)
        awaited_output = (
            os.path.join(self.common_init_dir, "test_file_0.txt") +
            "\n"
        )

        self.assertEqual(awaited_output, output)
        self.assertEqual(result, 0)

    def test_process_print_files_subdirs_in_init_dir_only(self):
        output = ''
        def print_entry(entry):
            nonlocal output
            output += entry.path + '\n'

        result = py_fso.folder.process(self.common_init_dir, process_files=True, proc_file_function=print_entry, process_dirs=True, proc_dir_function=print_entry,
            go_into_subdirs=False, follow_symlinks=False)

        awaited_output = (
            os.path.join(self.common_init_dir, "test_1") +
            "\n" +
            os.path.join(self.common_init_dir, "test_2") +
            "\n" +
            os.path.join(self.common_init_dir, "test_3") +
            "\n" +
            os.path.join(self.common_init_dir, "test_file_0.txt") +
            "\n"
        )
        self.assertEqual(awaited_output, output)
        self.assertEqual(result, 0)

    def test_process_run_without_proc_file_function(self):
        prev_stdout = sys.stdout

        result_output = StringIO()
        sys.stdout = result_output

        result = py_fso.folder.process(self.common_init_dir, process_files=True, proc_file_function=None, process_dirs=False, proc_dir_function=None,
            go_into_subdirs=False, follow_symlinks=False)

        self.assertEqual(result_output.getvalue(), "No function for files\n")
        self.assertEqual(result, -1)

        sys.stdout = prev_stdout

    def test_process_run_without_proc_dir_function(self):

        def print_entry(entry):
            pass

        prev_stdout = sys.stdout
        result_output = StringIO()
        sys.stdout = result_output

        result = py_fso.folder.process(self.common_init_dir, process_files=True, proc_file_function=print_entry, process_dirs=True, proc_dir_function=None,
            go_into_subdirs=False, follow_symlinks=False)

        self.assertEqual(result_output.getvalue(), "No function for dirs\n")
        self.assertEqual(result, -1)

        sys.stdout = prev_stdout

if __name__ == '__main__':
    unittest.main()
