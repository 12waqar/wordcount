from django.http import HttpResponse
from django.shortcuts import render
import operator
def homepage(request):
    return render(request,'home.html')
def count(request):
    data=request.GET['fulltextarea']
    list_word=data.split()
    print(list_word)
    list_lenght=len(list_word)
    worddictionary={}
    for word in list_word:
        if word in worddictionary:
            worddictionary[word]+=1
        else:
            worddictionary[word]=1
        sorted_list=sorted(worddictionary.items(),key=operator.itemgetter(1),reverse=True)

    return render(request,'count.html',{'fulltext':data,'words':list_lenght,'worddictionary':sorted_list})
def aboutpage(request):
    return render(request,'about.html')