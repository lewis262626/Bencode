with open('ubuntu-19.10-desktop-amd64.iso.torrent', 'rb') as fp:
    read_data = fp.read()

def decode_int(data, pos):
    end = data[pos:].index(b'e')
    if data[pos+1] == ord('-'):
        return (int(data[pos + 2:pos + end]) * -1, end)
    else:
        return (int(data[pos + 1:pos + end]), end + pos)

# return data as raw bytes not decoded to ASCII
def decode_str(data, pos):
    index = data[pos:].find(b':')
    length = int(data[pos: pos+ index])
    return (data[pos + index + 1: pos + index + length+1], length + pos + index + 1)

def decode_lst(data):
    lst = []

    i = 1
    while data[i] != ord(b'e'):
        elem, newpos = decode_dic[bytes([data[i]])](data,  i)
        i = newpos
        lst.append(elem)

    return lst
    
decode_dic = {}

decode_dic[b'0'] = decode_str
decode_dic[b'1'] = decode_str
decode_dic[b'2'] = decode_str
decode_dic[b'3'] = decode_str
decode_dic[b'4'] = decode_str
decode_dic[b'5'] = decode_str
decode_dic[b'6'] = decode_str
decode_dic[b'7'] = decode_str
decode_dic[b'8'] = decode_str
decode_dic[b'9'] = decode_str

decode_dic[b'i'] = decode_int

print(decode_lst(b'l4:spam3:loli3ee'))
print(decode_lst(b'l4:spami42ee'))
