from django.shortcuts import render, HttpResponse, redirect


# Create your views here.
def login(request):
    from app01 import models

    if request.method == 'GET':
        return render(request, 'login.html')
    else:
        user = request.POST.get('user')
        pwd = request.POST.get('pwd')
        if models.User.objects.filter(user_name=user, pass_word=pwd):
            return redirect('/index/')
        else:
            # return Http404('404')
            # print('s')
            return render(request, 'login.html')



def index(request):
    # orm 测试
    from app01 import models
    # ret = models.User.objects.all()  # 获取表中所有的数据
    # print(ret)
    # for i in ret:
    #     print(i.user_name, i.pass_word)
    # ret = models.User.objects.get(user_name='alex', pass_word='456')  # 获取单条数据，如果没有或者返回多条数据则会报错
    # print(ret)
    ret = models.User.objects.filter(user_name='peiqi')  # 获取满足条件的多条数据，没有数据返回空列表
    print(ret.values())
    return render(request, 'index.html')

