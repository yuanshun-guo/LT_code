def byte_size(string):
  print(len(string.encode('utf-8')))

byte_size('😀') # 4
byte_size('Hello World') # 11
