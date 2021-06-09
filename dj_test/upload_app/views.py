from django.shortcuts import HttpResponse, render, reverse
from django.views import View


# Create your views here.
# def upload(request):
#     file = request.FILES
#     print(file)
#     return HttpResponse('ok')

class Upload(View):

    def get(slef, request):
        """
        处理get请求
        :param request:
        :return:
        """
        return render(request, "index.html")

    def post(self, request):
        """
        处理post请求
        :param request:
        :return:
        """
        file = request.FILES.get("f1")  # 通过request.FILES对象获取上传的文件
        print(file)
        with open(file.name, "wb") as f:  # 将文件通过文件名写入当前目录
            for data in file:
                f.write(data)
        return HttpResponse('ok')


def index(request):
    return render(request, "dd.html")


def go(request):
    return HttpResponse("go")


def go2(request):
    return HttpResponse("go2")


def go3(request, year=2021, month=5):
    strs = "".join(str(year)) + str(month)
    print(year)
    print(month)
    return HttpResponse(strs)


def index1(request):
    # url = reverse("main")
    url = reverse("do_it", args=(2009, 8))
    print(url)
    return render(request, "index1.html")
