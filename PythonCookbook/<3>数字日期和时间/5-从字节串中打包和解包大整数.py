'''

'''

import struct


data = b'\x00\x124V\x00x\x90\xab\x00\xcd\xef\x01\x00#\x004'

print(len(data))
print(int.from_bytes(data, 'little'))
print(int.from_bytes(data, 'big'))

x = 94522842520747284487117727783387188
print(x.to_bytes(16, 'big'))
print(x.to_bytes(16, 'little'))

# 这种功能在特定领域会有用，比如提取IPV6地址
hi, lo = struct.unpack('>QQ', data)
print((hi << 64) + lo)

x = 0x01020304
print(x.to_bytes(4, 'big'))
print(x.to_bytes(4, 'little'))