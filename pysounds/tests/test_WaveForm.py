import unittest
from ..WaveForm import WaveForm, FormatError, bytesEqual, WAV, AIFF


class Test_WaveForm(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.WAV = WaveForm("./pysounds/tests/test-sound.wav")
        cls.AIFF = WaveForm("./pysounds/tests/test-sound.aiff")

    def test_format(self):
        self.assertNotEqual(self.WAV.fileFormat, self.AIFF.fileFormat)

    def test_reading(self):
        with self.assertRaises(FormatError):
            WaveForm("./pysounds/tests/test-sound.mp3")

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
        self.assertEqual(bytesEqual(wav1, wav2), True)
        self.assertEqual(bytesEqual(wav1, wav1), True)
        self.assertEqual(bytesEqual(wav1, AIFF.magicNumber), False)

if __name__ == "__main__":
    unittest.main()