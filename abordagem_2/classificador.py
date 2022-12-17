from sklearn import tree
from sklearn.model_selection import train_test_split

arquivo_Y_test = open('Y_test.txt','w')
arquivo = open('arquivo_saida.txt','w')

NaN = 0
Defacement = 1
benign = 2
malware = 3
phishing = 4
spam = 5

caracteristicas = ['*** caracteristicas ***']

classificacao = ['*** classificacao ***']

X_train, X_test, Y_train, Y_test = train_test_split(caracteristicas, classificacao, test_size = 0.2, random_state = 0)

clf = tree.DecisionTreeClassifier()
clf = clf.fit (caracteristicas, classificacao)

for i in range(len(Y_test)):
	if Y_test[i] == [1]:
		texto = '[Defacement],\n' 
		arquivo_Y_test.write(texto)
	else:
		if Y_test[i] == [2]:
			texto = '[benign],\n' 
			arquivo_Y_test.write(texto)
		else:
			if Y_test[i] == [3]:
				texto = '[malware],\n' 
				arquivo_Y_test.write(texto)
			else:
				if Y_test[i] == [4]:
					texto = '[phishing],\n' 
					arquivo_Y_test.write(texto)
				else:
					texto = '[spam],\n' 
					arquivo_Y_test.write(texto)
					
for i in range(len(X_test)):
	print(X_test[i])   
	  
	todos = X_test[i]

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
					
			 
			 
