import pickle


datos=["Rosa","Verde"]


ArchivoBinario=open("ArchivoLista", "wb")

pickle.dump(datos, ArchivoBinario)

ArchivoBinario.close()

del (ArchivoBinario)

Archivo2=open("ArchivoLista", "rb")

Lista2=pickle.load(Archivo2)

print(Lista2)