import chardet

# pip install chardet
# with open('test.log', 'r', encoding='utf-8') as f:
#     lines = f.read()
#
# print(lines)

# rb  odczyt binarny
with open('test.log', 'rb') as f:
    raw_data = f.read()

print(raw_data)  # b'Nadpisane\r\nDopisane\r\nDopisane\r\nDodane\r\nDodane\r\nDo\xc5\x9bdane\r\n'

result = chardet.detect(raw_data)
print(result)
# {'encoding': 'Windows-1254', 'confidence': 0.6565429274104, 'language': 'Turkish'}
# po dodoaniu większej ilości polskich znaków
# {'encoding': 'utf-8', 'confidence': 0.99, 'language': ''}
encoding = result['encoding']
confidence = result['confidence']
print("kodowanie:", encoding)
print("pewnośc:", confidence)
print(raw_data.decode(encoding=encoding))
# {'encoding': 'utf-8', 'confidence': 0.99, 'language': ''}
# kodowanie: utf-8
# pewnośc: 0.99
# Nadpisane
# Dopisane
# Dopisane
# Dodane
# Dodane
# Dośddane
# Dośdąźćdane
