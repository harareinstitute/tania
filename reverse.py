def reverse_string(str1):
    if len(str1) % 4 == 0:
       return ''.join(reversed(str1))
    return str1

print(reverse_string('info'))
print(reverse_string('taniamag'))
print(reverse_string('lucy'))
print(reverse_string('informationsecurity'))
print(reverse_string('just'))
#not a multiple of 4 does not print
print(reverse_string('information'))

