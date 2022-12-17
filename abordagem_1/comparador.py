Defacement = 1
benign = 2
malware = 3
phishing = 4
spam = 5

resultado_1 = ['*** 4 ***']

resultado_2 = ['*** TEST_R4 ***']

diferentes = 0
Defacement_erro = 0
benign_erro = 0
malware_erro = 0
phishing_erro = 0
spam_erro = 0
d_b = 0
d_m = 0
d_p = 0
d_s = 0
b_m = 0
b_p = 0
b_s = 0
m_p = 0
m_s = 0
p_s = 0

for i in range(len(resultado_1)):
	if resultado_1[i]!=resultado_2[i] :
		print("--------------- DIF: ", resultado_1[i] + resultado_2[i])
		diferentes = diferentes + 1
		if(resultado_1[i]==[1]): 
			Defacement_erro = Defacement_erro + 1
			if(resultado_2[i]==[2]): 
				d_b = d_b + 1
			if(resultado_2[i]==[3]): 
				d_m = d_m + 1
			if(resultado_2[i]==[4]): 
				d_p = d_p + 1	
			if(resultado_2[i]==[5]): 
				d_s = d_s + 1
		if(resultado_1[i]==[2]): 
			benign_erro = benign_erro + 1
			if(resultado_2[i]==[1]): 
				d_b = d_b + 1
			if(resultado_2[i]==[3]): 
				b_m = b_m + 1
			if(resultado_2[i]==[4]): 
				b_p = b_p + 1	
			if(resultado_2[i]==[5]): 
				b_s = b_s + 1
		if(resultado_1[i]==[3]): 
			malware_erro = malware_erro + 1
			if(resultado_2[i]==[1]): 
				d_m = d_m + 1
			if(resultado_2[i]==[2]): 
				b_m = b_m + 1
			if(resultado_2[i]==[4]): 
				m_p = m_p + 1	
			if(resultado_2[i]==[5]): 
				m_s = m_s + 1
		if(resultado_1[i]==[4]): 
			phishing_erro = phishing_erro + 1
			if(resultado_2[i]==[1]): 
				d_p = d_p + 1
			if(resultado_2[i]==[2]): 
				b_p = b_p + 1
			if(resultado_2[i]==[3]): 
				m_p = m_p + 1	
			if(resultado_2[i]==[5]): 
				p_s = p_s + 1
		if(resultado_1[i]==[5]): 
			spam_erro = spam_erro + 1
			if(resultado_2[i]==[1]): 
				d_s = d_s + 1
			if(resultado_2[i]==[2]): 
				b_s = b_s + 1
			if(resultado_2[i]==[3]): 
				m_s = m_s + 1	
			if(resultado_2[i]==[4]): 
				p_s = p_s + 1
	else:
		print("IGU: ", resultado_1[i] + resultado_2[i])

print()
print("----------------")
print("FIM")
print("----------------")		
print()
print("Estatísticas")
print()
print("Quantidade de Testes:", len(resultado_1), "")
print("Diferentes:", diferentes, "")
print()
print("Defacement_erro:", Defacement_erro, "")
print("benign_erro:", benign_erro, "")
print("malware_erro:", malware_erro, "")
print("phishing_erro:", phishing_erro, "")
print("spam_erro:", spam_erro, "")
print("	Defacement_erro e benign_erro:", d_b, "")
print("	Defacement_erro e malware_erro:", d_m, "")
print("	Defacement_erro e phishing_erro:", d_p, "")
print("	Defacement_erro e spam_erro:", d_s, "")
print("	benign_erro e malware_erro:", b_m, "")
print("	benign_erro e phishing_erro:", b_p, "")
print("	benign_erro e spam_erro:", b_s, "")
print("	malware_erro e phishing_erro:", m_p, "")
print("	malware_erro e spam_erro:", m_s, "")
print("	phishing_erro e spam_erro:", p_s, "")
