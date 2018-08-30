# from django.http import HttpResponse
from django.shortcuts import render
import operator
# def mah(request):
#     return HttpResponse("<h1>hi welcome</h1>")
def wel(request):
    return render(request,'countwords.html')
def aboutus(request):
    return render(request,'aboutus.html')
# def good(request):
#     return render(request,'index.html',{"vlr":"9704620585"})
def count(request):
    get=request.GET['message']
    a=get.split()
    wcount={}
    for word in a:
        if word in wcount:
            wcount[word] +=1
        else:
            wcount[word]=1

    sort=sorted(wcount.items(),key=operator.itemgetter(1),reverse=True)


    return render(request,'count.html',{"data":get,"length":len(a),"abc":wcount,"dec":sort})