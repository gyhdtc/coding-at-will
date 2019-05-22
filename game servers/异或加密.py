def xor(s, k):
    return ''.join(chr(ord(i) ^ ord(j)) for i, j in zip(s,k))
s = 'gyhis108'
key = '12345678'
s2 = xor(s, key)
print ("[加密] :",s2)
print ("[解密] : ",xor(s2, key))