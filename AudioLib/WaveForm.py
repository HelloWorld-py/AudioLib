# Author: Jacob Tsekrekos
# Date: June 29, 2018
# File: WaveForm.py
# Description: Loads an audio file into a Waveform object

import wave

from .Errors import FormatError


# https://docs.python.org/3/library/aifc.html
# https://docs.python.org/3/library/wave.html
# AIFF is currently broken: Problem with the library loading?
# todo: change AudioFormat/ Supported formats to be classes for creation?


class AudioFormat:
    """This class is used to increase readability in the code"""

    def __init__(self, magic_number, name, codec):
        self.magic_number = magic_number
        self.name = name
        self.codec = codec


WAV = AudioFormat([82, 73, 70, 70, -1, -1, -1, -1, 87, 65, 86, 69], "wav", wave)

supportedFormats = [WAV]


def bytes_equal(check, array):
    for i, j in enumerate(array):
        # accounts for wildcards
        if check[i] == -1 or array[i] == -1:
            continue

        if array[i] != check[i]:
            return False

    return True


def check_file_exists(filename):
    try:
        file = open(filename, "rb")
        return file
    except FileNotFoundError:
        return False


def determine_format(filename):
    """
    If the file is not found, FileNotFoundError is raised
    Compares the first 12 bytes to know magic numbers, if it is not know 'FormatError' is raised
    :type filename: str
    :returns: WaveFormABC or NoneType
    :raises FormatError, FileNotFoundError
    """
    file = check_file_exists(filename)

    if not file:
        raise FileNotFoundError

    magic_number = file.read(12)
    file.close()

    for audio_format in supportedFormats:
        if bytes_equal(audio_format.magic_number, magic_number):
            return audio_format
    else:
        return False


def load(filename):
    """Main method to create a Waveform"""
    file_format = determine_format(filename)

    if file_format in Chunk.supported:
        return Chunk(filename, file_format)
    else:
        raise FormatError


class WaveForm:
    codec = None

    def __init__(self, file_name, file_format):
        self.file_name = file_name
        self.file_format = file_format
        self.file = None
        self.codec = self.file_format.codec

        # ensures all constants are set
        info = self.get_info()
        self.framerate = info.get("frame rate", -1)
        self.frames = info.get("frames", -1)
        self.channels = info.get("channels", -1)
        self.sample_width = info.get("sample width", -1)

    def open(self):
        raise NotImplementedError

    def close(self):
        if self.isOpen:
            self.file.close()
            self.file = None
        return self

    def read(self, n):
        raise NotImplementedError

    def get_info(self):
        raise NotImplementedError

    @property
    def isOpen(self):
        return True if self.file is not None else False

    @property
    def position(self):
        raise NotImplementedError

    @position.setter
    def position(self, new):
        raise NotImplementedError


class Chunk(WaveForm):
    """The class for the built-in codecs using 'chunk'"""
    supported = [WAV]

    def __init__(self, file_name, file_format):
        super().__init__(file_name, file_format)

    def get_info(self):
        if not self.isOpen:
            self.open()

        info = {"frame rate": self.file.getframerate(),
                "frames": self.file.getnframes(),
                "channels": self.file.getnchannels(),
                "sample width": self.file.getsampwidth()}

        self.close()
        return info

    def open(self):
        self.file = self.codec.open(self.file_name)
        return self

    def read(self, n):
        if self.isOpen:
            return self.file.readframes(n)

    @property
    def position(self):
        return self.file.tell()

    @position.setter
    def position(self, new):
        self.file.setpos(new)
