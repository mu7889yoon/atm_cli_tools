import unittest
from atm_cli_tools.UseCase.Theme.FindSimilarIdAction import FindSimilarIdAction

class FindSimilarActionTest(unittest.TestCase):
        
    themes_params = [
            {'songname': 'HAYATE NO GOTOKU!', 'id': '/song/15510'},
            {'songname': 'SHICHI-TEN HAKKI SHIJOU SHUGI!', 'id': '/song/15515'},
            {'songname': 'PROOF', 'id': '/song/568'},
            {'songname': 'GET MY WAY!', 'id': '/song/8650'},
            {'songname': 'CHASSE', 'id': '/song/2488'},
        ]
    
    def test_find_exist_songname(self):
        en_songname = 'Shichiten Hakki ☆Shijou Shugi!'

        expected = 'https://anidb.net/song/15515'
        actual = FindSimilarIdAction(en_songname, self.themes_params)
        self.assertEqual(expected, actual)
        
    def test_find_not_exist_songname(self):
        en_songname = ''
        expected = None
        actual = FindSimilarIdAction(en_songname, self.themes_params)
        self.assertEqual(expected, actual)
        
    def test_not_find_exist_songname(self):
        en_songname = 'Daily-Daily Dream'
        
        expected = None
        actual = FindSimilarIdAction(en_songname, self.themes_params)
        self.assertEqual(expected, actual)
        


if __name__ == '__main__':
    unittest.main()