import unittest
from atm_cli_tools.UseCase.GetSlugAction import GetSlugAction

class test_GetSlugAction(unittest.TestCase):
    def test_get_slug(self):
        atm_url = 'https://animethemes.moe/anime/hayate_no_gotoku'

        expected = 'hayate_no_gotoku'
        actual = GetSlugAction(atm_url)
        self.assertEqual(expected, actual)

        


if __name__ == '__main__':
    unittest.main()