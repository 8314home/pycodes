import unittest
import Python_codes.guessing_game as guessing_game


class GuessGame(unittest.TestCase):

    def test_1(self):
        print("Test-1")
        par_num = 8
        par_ans = 8
        result = guessing_game.guess_integer(par_num,par_ans)
        self.assertEqual(result, True)

    def test_2(self):
        print("Test-2")
        par_num = 9
        par_ans = 8
        result = guessing_game.guess_integer(par_num,par_ans)
        self.assertEqual(result, False)

    def test_3(self):
        print("Test-3")
        par_num = None
        par_ans = 8
        result = guessing_game.guess_integer(par_num,par_ans)
        self.assertEqual(result, False)

    def test_4(self):
        print("Test-4")
        par_num = 12
        par_ans = 8
        result = guessing_game.guess_integer(par_num,par_ans)
        self.assertEqual(result, False)


if __name__ == "__main__":
    unittest.main()
