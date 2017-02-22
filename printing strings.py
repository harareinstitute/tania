def string_both_ends(str):
  if len(str) < 2:
    return ''

  return str[0:2] + str[-2:]

print(string_both_ends('practicalsec'))
print(string_both_ends('iam'))
#print empty because it is less than 2
print(string_both_ends('t'))
print(string_both_ends('tania'))
