destino = "/home/gouvea/Documentos/Programing/Python/JogoPalavrasNV/palavras.txt"
arquivo = open(destino, "r")
conteudo_arquivo = arquivo.read()

conteudo_arquivo2 = "".join(conteudo_arquivo.replace("\n", ",").replace(" ", ""))
conteudo_tup = conteudo_arquivo2.split(",")


print(conteudo_tup)
