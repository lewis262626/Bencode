import pytest

from bencode import decode_int, decode_str, decode_lst

class TestClass:
    def test_int(self):
        bencode = [b'i42e', b'i-42e', b'i238327832e']
        real    = [42,      -42,      238327832]
        for (bencode, real) in list(zip(bencode, real)):
            assert decode_int(bencode, 0)[0] == real

    def test_str(self):
        bencode = [b'13:parrot sketch', b'6:github']
        real    = [b'parrot sketch',    b'github']
        for (bencode, real) in list(zip(bencode, real)):
            assert decode_str(bencode, 0)[0] == real

    # TODO: more tests
    def test_lst(self):
        bencode = b'l13:parrot sketchi42ee'
        real    = [b'parrot sketch', 42]
        print(decode_lst(bencode)[0])
        assert decode_lst(bencode) == real

