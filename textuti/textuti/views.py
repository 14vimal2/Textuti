# I have created this file - Vimal Kumar
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request,'index.html')

def analyze(request):
    djtext = request.POST.get('text','default')
    removepunc = request.POST.get('removepunc','off')
    capitalize = request.POST.get('capitalize','off')
    newlineremove = request.POST.get('newlineremove','off')
    spaceremove = request.POST.get('spaceremove','off')
    charcount = request.POST.get('charcount','off')
    analyzed = ""
    purpose = ""
    punctuations = '''!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~'''
    if analyzed == djtext:
        return HttpResponse('''<h1>Error: You have not entered any text.</h1><a href = "/">Back</a>''')
    elif (removepunc == "off") & (capitalize == "off") & (newlineremove == "off") & (spaceremove == "off") & (charcount == "off"):
        return HttpResponse('''<h1>Error: You have not checked any box.</h1><a href = "/">Back</a>''')
    else:
        analyzed = djtext
        if removepunc == "on":
            temp = ""
            for char in analyzed:
                if char not in punctuations:
                    temp = temp + char
            analyzed = temp
            purpose = 'Punctuation removed\n'
        if capitalize == "on":
            temp = ""
            for char in analyzed:
                temp = temp + char.upper()
            analyzed = temp
            purpose = purpose + 'Capitalized\n'
        if newlineremove == "on":
            temp = ""
            for char in analyzed:
                if char != "\n" and char != "\r":
                    temp = temp + char
            analyzed = temp
            purpose = purpose + 'New lines removed\n'
        if spaceremove == "on":
            temp =""
            for char in analyzed:
                if char !=" ":
                    temp = temp + char
            analyzed = temp
            purpose = purpose + 'Space removed\n'
        if charcount == "on":
            i = 0
            for char in djtext:
                i = i + 1
            if i <2:
                verb = ' is ' + str(i) + '.'
            else:
                verb = 's are ' + str(i) + '.'
            purpose = purpose + 'Total character' + verb
        params = {'purpose': purpose, 'analyzed_text': analyzed}
        return render(request,'analyze.html',params)