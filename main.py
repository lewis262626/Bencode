with open('ubuntu-19.10-desktop-amd64.iso.torrent', 'rb') as fp:
    read_data = fp.read()

def decode_int(data):
    if data[0].to_bytes(1, byteorder='big') == b'i':
        num = data[1:len(data)-1]
        return num.decode('ascii')
    else:
        raise TypeError('not valid bencode')

def decode_str(data):
    for i, byte in enumerate(data):
        if byte.to_bytes(1, byteorder='big') == b':':
            return data[i+1:len(data)]


print(decode_int(b'i42e'))
print(decode_str(b'4:spam'))
