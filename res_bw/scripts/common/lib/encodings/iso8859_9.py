# 2016.02.13 15:10:35 St�edn� Evropa (b�n� �as)
# Embedded file name: scripts/common/Lib/encodings/iso8859_9.py
""" Python Character Mapping Codec iso8859_9 generated from 'MAPPINGS/ISO8859/8859-9.TXT' with gencodec.py.

"""
import codecs

class Codec(codecs.Codec):

    def encode(self, input, errors = 'strict'):
        return codecs.charmap_encode(input, errors, encoding_table)

    def decode(self, input, errors = 'strict'):
        return codecs.charmap_decode(input, errors, decoding_table)


class IncrementalEncoder(codecs.IncrementalEncoder):

    def encode(self, input, final = False):
        return codecs.charmap_encode(input, self.errors, encoding_table)[0]


class IncrementalDecoder(codecs.IncrementalDecoder):

    def decode(self, input, final = False):
        return codecs.charmap_decode(input, self.errors, decoding_table)[0]


class StreamWriter(Codec, codecs.StreamWriter):
    pass


class StreamReader(Codec, codecs.StreamReader):
    pass


def getregentry():
    return codecs.CodecInfo(name='iso8859-9', encode=Codec().encode, decode=Codec().decode, incrementalencoder=IncrementalEncoder, incrementaldecoder=IncrementalDecoder, streamreader=StreamReader, streamwriter=StreamWriter)


decoding_table = u'\x00\x01\x02\x03\x04\x05\x06\x07\x08\t\n\x0b\x0c\r\x0e\x0f\x10\x11\x12\x13\x14\x15\x16\x17\x18\x19\x1a\x1b\x1c\x1d\x1e\x1f !"#$%&\'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_`abcdefghijklmnopqrstuvwxyz{|}~\x7f\x80\x81\x82\x83\x84\x85\x86\x87\x88\x89\x8a\x8b\x8c\x8d\x8e\x8f\x90\x91\x92\x93\x94\x95\x96\x97\x98\x99\x9a\x9b\x9c\x9d\x9e\x9f\xa0\xa1\xa2\xa3\xa4\xa5\xa6\xa7\xa8\xa9\xaa\xab\xac\xad\xae\xaf\xb0\xb1\xb2\xb3\xb4\xb5\xb6\xb7\xb8\xb9\xba\xbb\xbc\xbd\xbe\xbf\xc0\xc1\xc2\xc3\xc4\xc5\xc6\xc7\xc8\xc9\xca\xcb\xcc\xcd\xce\xcf\u011e\xd1\xd2\xd3\xd4\xd5\xd6\xd7\xd8\xd9\xda\xdb\xdc\u0130\u015e\xdf\xe0\xe1\xe2\xe3\xe4\xe5\xe6\xe7\xe8\xe9\xea\xeb\xec\xed\xee\xef\u011f\xf1\xf2\xf3\xf4\xf5\xf6\xf7\xf8\xf9\xfa\xfb\xfc\u0131\u015f\xff'
encoding_table = codecs.charmap_build(decoding_table)
# okay decompyling c:\Users\PC\wotsources\files\originals\res_bw\scripts\common\lib\encodings\iso8859_9.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2016.02.13 15:10:35 St�edn� Evropa (b�n� �as)
