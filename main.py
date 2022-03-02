import re

password = 'ABd1234@1, a F1#, 2w3E*, 2We3345'
password_list = password.split(',')

strip_password = list(map(lambda x: x.strip(), password_list))

pattern = '[a-z0-9A-Z$#@]'

print(strip_password)

value = []

for p in strip_password:
  if len(p) < 6 or len(p) > 12:
    continue
  else:
    if not re.search('[a-z]', p):
      continue
    elif not re.search('[0-9]', p):
      continue
    elif not re.search('[A-Z]', p):
      continue
    elif not re.search('[$H@]', p):
      continue
    elif re.search('\s', p):
      continue
    else:
      pass
    value.append(p)

print(",".join(value))
