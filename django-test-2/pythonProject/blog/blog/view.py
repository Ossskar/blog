from django.shortcuts import render

MENU = {'�������':'/','����':'/post','� �����':'/about'}

def main_page(request):
    title = '������� ��������'
    data = {"menu":MENU,"title":title}
    return render(request, './index.html', context=data)

def post_page(request):
    title = '�������� �����'
    data = {"menu":MENU,"title":title}
    return render(request, './post.html', context=data)

def about_page(request):
    title = 'C������� � �����'
    data = {"menu":MENU,"title":title}
    return render(request, './about.html', context=data)