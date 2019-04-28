import re
import configparser

#
# check = '010100000111101000101'
# character_regex = re.compile(r'[0-1]')
# check = character_regex.search(check)
# print(bool(check))
#
# if len(a) > 8:
#     re.match("12345677890", r'[1, 2}]' / g);
# a = configparser.ConfigParser()
# a.read('config.ini')
# print(a['DEFAULT']['Password'])

import math
import binascii

a = '00110100010000010011101000101100000000100100100100'

d = (math.ceil(len(a) / 8) * 8) - len(a)
a = d * '0' + a

c = 0
output = ''

# print(binascii.b2a_uu('0011010001000001001110100010110000000010'.encode()))
# print(binascii.b2a_uu('0100100100'.encode()))
for byte in a:
    if not (c % 8):
        output += output.join(':')

    output += output.join(byte)
    c += 1

print(output)
output = output.split(':')
output.remove('')

for key, val in enumerate(output):
    output[key] = binascii.b2a_uu(val.encode())
    output[key] = str(output[key]).replace(r'\n', '').replace('b', '')

print(output)