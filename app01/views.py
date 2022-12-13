from django.shortcuts import render, HttpResponse


def index(response):
    return HttpResponse("helloman")


def login(request):  # 参数具体是啥无所谓，习惯是request，即接收到的用户的发送的请求
    if request.method == "GET":
        return render(request, '登录.html')
    else:  # post
        # 获取用户提交的数据
        print(request.POST)
        
        user = request.POST.get("user")
        pwd = request.POST.get("pwd")
        
        if user == "whatcarp" and pwd == "lab20010119":
            return HttpResponse("Login succeeded")
        else:
            return render(request, '登录.html', {'error_msg':"Incorrect username or password 😢"})
