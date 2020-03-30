from django.shortcuts import render

# Create your views here.

#여기서 홈페이지에 들어오면 실행시킨? 보여줄 HTML 페이지를 고름
def home(request):
    return render(request, 'home.html');
