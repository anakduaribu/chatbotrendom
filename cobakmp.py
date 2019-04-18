# NIM/Nama	: 13517065/Andrian Cedric
# 

def KMPSM(pola, teks): 
	M = len(pola) 
	N = len(teks) 
	arraytemp = []
	stopwords = 'itu'

	#array untuk prefiks/sufiks
	lps = [0]*M 
	j = 0 # index for pola[] 

	# Preprocess the polatern (calculate lps[] array) 
	computeLPSArray(pola, M, lps) 

	i = 0 #indeks untuk mencari pada teks
	while i < N: 
		if pola[j] == teks[i]: 
			arraytemp.append(teks[i])
			i += 1
			j += 1
			

		if j == M: 
			print("Found polatern at index " + str(i-j))
			j = lps[j-1] 
			#mencetak isi dari arraytemp
			" ".join(arraytemp) #menjadikan array char menjadi string
			print(len(arraytemp)) #panjang dari arraytemp
			print(len(teks)) #panjang dari teks yang diberikan
			sum = len(arraytemp)/len(teks) #untuk menghitung persentase dari kecocokan
			print(sum)																																											


		# mismatch after j matches 
		elif i < N and pola[j] != teks[i]: 
			# Do not match lps[0..lps[j-1]] characters, 
			# they will match anyway 
			if j != 0: 
				j = lps[j-1] 
			else: 
				i += 1

def computeLPSArray(pola, M, lps): 
	len = 0 # length of the previous longest prefix suffix 

	lps[0] # lps[0] is always 0 
	i = 1

	# the loop calculates lps[i] for i = 1 to M-1 
	while i < M: 
		if pola[i]== pola[len]: 
			len += 1
			lps[i] = len
			i += 1
		else: 
			# This is tricky. Consider the example. 
			# AAACAAAA and i = 7. The idea is similar 
			# to search step. 
			if len != 0: 
				len = lps[len-1] 

				# Also, note that we do not increment i here 
			else: 
				lps[i] = 0
				i += 1

def delstopword (teks):
	text2 = teks.replace(' itu', '')
	#print(text2)
	print("sucess")
	return text2

		
teks = str(input("Masukkan teks : "))
pola = str(input("Masukkan pola : "))
text2 = delstopword(teks)
#print(text2)
KMPSM(pola, text2) 

