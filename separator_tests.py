import unittest
import io, sys
from separator import wtfj

# Run this unittest file without passing any command-line arguments
# other than ones you want to pass to unittest such as -values

class Test_separator(unittest.TestCase):

    def setUp(self):
        # Add a spot to argv that we can use to pass command-line
        # arguments to the main function in the separator module
        sys.argv.append(None)

    def test_01(self):
        sys.argv[1] = 6  # Simulates passing 6 on the command line
        sys.stdout = student_output = io.StringIO()
        sys.stdin = io.StringIO("1 2 1.2 2.3\n3\n4\n7.8 garbage, 12\n")
        expected_out = "Integers: 1 2 3 4 \nFloats: 1.2 2.3 7.8"
        main()
        self.assertEqual(expected_out, student_output.getvalue().strip())


    def test_02(self):
        sys.argv[1] = 4 # Simulates passing 4 on the command line
        sys.stdout = student_output = io.StringIO()
        sys.stdin = io.StringIO(u"1 2 3\n4 5 6\n")
        expected_out = u"Integers: 1 2 3 4 \nFloats:"
        main()
        self.assertEqual(expected_out, student_output.getvalue().strip())

    def test_3(self):
        sys.argv[1] = 2
        sys.stdout = student_output = io.StringIO()
        sys.stdin = io.StringIO("\n")
        expected_out = "Integers: \nFloats: "
        self.assertEqual(expected_out, student_output.getvalue().strip())

    def test_4(self):
        sys.argv[1] = 3
        sys.stdout = student_output = io.StringIO()
        sys.stdin = io.StringIO("1 2 3.0 \n3 4 5")
        expected_out = "Integers: 1 2 3 \nFloats: 3.0"
        self.assertEqual(expected_out, student_output.getvalue().strip())

    def test_5(self):
        sys.argv[1] = 2
        sys.stdout = student_output = io.StringIO()
        sys.stdin = io.StringIO("1 \n1.0 2\n\n")
        expected_out = "Integers: 1 2 \nFloats: 1.0"
        self.assertEqual(expected_out, student_output.getvalue().strip())

    def test_6(self):
        sys.argv[1] = 5
        sys.stdout = student_output = io.StringIO()
        sys.stdin = io.StringIO("1 2.6\n1.0 2 3 4.5\n\n")
        expected_out = "Integers: 1 2 3 \nFloats: 2.6 1.0 4.5"
        self.assertEqual(expected_out, student_output.getvalue().strip())

    def test_7(self):
        sys.argv[1] = 2
        sys.stdout = student_output = io.StringIO()
        sys.stdin = io.StringIO("dog \n1.0 2\n\n")
        expected_out = "Integers: \nFloats:"
        self.assertEqual(expected_out, student_output.getvalue().strip())

    def test_8(self):
        sys.argv[1] = 4
        sys.stdout = student_output = io.StringIO()
        sys.stdin = io.StringIO("1 \n1 2\n\n")
        expected_out = "Integers: 1 1 2 \nFloats:"
        self.assertEqual(expected_out, student_output.getvalue().strip())

    def test_9(self):
        sys.argv[1] = 5
        sys.stdout = student_output = io.StringIO()
        sys.stdin = io.StringIO("1 \n1.0 2\n3 4.6 7 1.2\n6.2 dog 12")
        expected_out = "Integers: 1 2 3 7 \nFloats: 1.0 4.6 1.2 6.2"
        self.assertEqual(expected_out, student_output.getvalue().strip())

    def test_10(self):
        sys.argv[1] = 2
        sys.stdout = student_output = io.StringIO()
        sys.stdin = io.StringIO("dog \ncat hamster\nbird")
        expected_out = "Integers: \nFloats:"
        self.assertEqual(expected_out, student_output.getvalue().strip())



if __name__ == "__main__":
        unittest.main()