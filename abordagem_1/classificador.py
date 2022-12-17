from sklearn import tree

arquivo = open('4.txt','w')

Defacement = 1
benign = 2
malware = 3
phishing = 4
spam = 5

caracteristicas = ['*** TREINAMENTO_4 ***']

classificacao = ['*** TREINAMENTO_R4 ***']

clf = tree.DecisionTreeClassifier()
clf = clf.fit (caracteristicas, classificacao)

lista = ['*** TESTE_4 ***']

for i in range(len(lista)):
	print(lista[i])   
	  
	todos = lista[i]

	URL_Type_obf_Type = clf.predict([todos])

	if URL_Type_obf_Type == 1:
		print("URL_Type_obf_Type :: Defacement")
		texto = '[Defacement],\n' 
		arquivo.write(texto)
	else:
		if URL_Type_obf_Type == 2:
			print("URL_Type_obf_Type :: benign")
			texto = '[benign],\n' 
			arquivo.write(texto)
		else:
			if URL_Type_obf_Type == 3:
				print("URL_Type_obf_Type :: malware")
				texto = '[malware],\n' 
				arquivo.write(texto)
			else:
				if URL_Type_obf_Type == 4:
					print("URL_Type_obf_Type :: phishing")
					texto = '[phishing],\n' 
					arquivo.write(texto)
				else:
					print("URL_Type_obf_Type :: spam")
					texto = '[spam],\n' 
					arquivo.write(texto)
					
			 
