# Perguntar ao utilizador o tipo do ficheiro - pedir um "input"
# Lista: .gif; .jpg; .jpeg; .png; .pdf; .txt; .zip

file_name = input('File_name:')
file_name = file_name.lower().strip()


# Escrever o tipo de ficheiro e a sua extensão, p.e. "image/.jpeg"
# Se não for um tipo que esteja na lista, escrever "application/octet-stream"

if file_name.endswith ('.gif'):
    print ('image/gif')
elif file_name.endswith ('.jpg'):
    print ('image/jpeg')
elif file_name.endswith ('.jpeg'):
    print ('image/jpeg')
elif file_name.endswith ('.png'):
    print ('image/png')
elif file_name.endswith ('.pdf'):
    print ('application/pdf')
elif file_name.endswith ('.txt'):
    print ('text/plain')
elif file_name.endswith ('.zip'):
    print ('application/zip')
else:
    print ('application/octet-stream')
