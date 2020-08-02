
from django.shortcuts import render


def home(request):
	return render(request,'home.html')

def reverse(request):
	user_text=request.GET['messange']
	reverse_text=user_text[::-1]
	# count_word=0
	# for i in user_text:
	# 	if i==' ' :
	# 		count_word = count_word+1
	# count_word +=1
	words=user_text.split()
	number=len(words)
	
	return render(request,'reverse.html',{'usertext':user_text,
		'reversetext':reverse_text,'count':number})

