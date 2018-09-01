import unittest
from ..WaveForm import load, FormatError, bytes_equal, WAV


class Test_WaveForm(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.WAV = load("test-sound.wav")

    def test_reading(self):
        with self.assertRaises(FormatError):
            load("test-sound.mp3")

        self.assertIs(self.WAV.isOpen, False)

        self.WAV.open()
        self.assertIs(self.WAV.isOpen, True)

        self.WAV.position = 10
        self.assertEqual(self.WAV.position, 10)

        self.WAV.close()
        self.assertIs(self.WAV.isOpen, False)


class Test_BytesEqual(unittest.TestCase):
    def test_bytes(self):
        wav1 = WAV.magicNumber[:]
        wav2 = wav1[:]
        wav2[4] = 13
        self.assertEqual(bytes_equal(wav1, wav2), True)
        self.assertEqual(bytes_equal(wav1, wav1), True)


if __name__ == "__main__":
    unittest.main()
