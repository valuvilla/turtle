import pickle


datos=["Rosa","Verde"]


ArchivoBinario=open("datos", "wb")

pickle.dump(datos, ArchivoBinario)

ArchivoBinario.close()



Archivo2=open("datos", "rb")

Lista2=pickle.load(Archivo2)

print(Lista2)