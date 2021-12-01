import chardet as chardet

with open(r'./clase5/catalogo_cf.csv', 'rb') as f:
    msg = f.read()
    result = chardet.detect(msg)
    print(result)

