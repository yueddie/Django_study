import pymysql
from django.shortcuts import render, redirect
from bookstore import models
from django.views import View
from django.utils.decorators import method_decorator

# Create your views here.
import time


# 统计时间的装饰器
def timer(func):
    def inner(request, *args, **kwargs):
        start = time.time()
        ret = func(request, *args, **kwargs)
        print("执行时间{}".format(time.time() - start))
        return ret

    return inner


@timer
def publisher(request):
    """
    展示数据
    :param request:
    :return:
    """
    # 逻辑处理
    all_info = models.Publisher.objects.all().order_by('id')  # 通过orm获取数据库中Publisher表中的所有信息

    # 返回页面
    return render(request, 'publisher_list.html', context={'all_info': all_info})
    # context将信息替换到html模板进行渲染，是字典类型，key是前端识别的值,values是需要用到的后台信息


# FBV添加出版社
# def add_publisher(request):
#     info = ''
#     if request.method == 'POST':
#         pub_name = request.POST.get('pub_name')
#         if not pub_name:
#             info = '出版社名字不能为空'
#             return render(request, 'publisher_add.html', {'info': info})
#         if models.Publisher.objects.filter(name=pub_name):
#             return render(request, 'publisher_add.html', {'info': '当前出版社已经存在'})
#         # print(pub_name)
#         models.Publisher.objects.create(name=pub_name)
#         info = '新增成功'
#
#     return render(request, 'publisher_add.html', {'info': info})


# CBV 添加出版社

@method_decorator(timer, name='dispatch')
class AddPublisher(View):

    @method_decorator(timer)  # 让get和post都实现装饰器，应为post get执行之前都会执行该函数
    def dispatch(self, request, *args, **kwargs):
        ret = super().dispatch(request, *args, **kwargs)
        return ret

    def get(self, request):
        print('get')
        return render(request, 'publisher_add.html')

    def post(self, request):
        print('post')
        pub_names = request.POST.get('pub_name')
        if not pub_names:
            info = '出版社名字不能为空'
            return render(request, 'publisher_add.html', {'info': info})
        if models.Publisher.objects.filter(name=pub_names):
            return render(request, 'publisher_add.html', {'info': '当前出版社已经存在'})
        # print(pub_name)
        models.Publisher.objects.create(name=pub_names)
        info = '新增成功'
        return render(request, 'publisher_add.html', {'info': info})


def del_publisher(request):
    """
    删除出版社
    :param request:
    :return:
    """
    # 获取从前端传过来的信息
    pk = request.GET.get('pk')
    # 通过model查询到该id并通过delete方法删除
    models.Publisher.objects.filter(pk=pk).delete()
    return redirect('/publisher/')


# def edit_publisher(request):
#     pk = request.GET.get('pk')  # 获取前台传递get传递过来的pk信息
#     edit_obj = models.Publisher.objects.get(pk=pk)
#     if request.method == 'GET':
#         return render(request, 'publisher_edit.html', {'edit_obj': edit_obj})
#     else:
#         edit_name = request.POST.get('pub_name')  # 获取post传递过来的name值
#         edit_obj.name = edit_name  # 内存中修改要该的名字
#         print(edit_obj.id)
#         edit_obj.save()  # 提交到数据库
#         return redirect('/publisher')

def edit_publisher(request):
    pk = request.GET.get('pk')  # 获取从页面穿过来要删除的出版社id
    if request.method == 'GET':  # get请求
        conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='1234', db='publisher',
                               charset='utf8')  # 通过pymysql连接mysql数据
        cursor = conn.cursor()  # 创建游标
        sql = "select name from bookstore_publisher where id = %s"  # sql语句
        cursor.execute(sql, [pk, ])  # 执行sql语句
        ret = cursor.fetchone()  # 只取执行后的一条数据，fetchall()则是取多条数据
        cursor.close()  # 关闭游标连接
        conn.close()  # 关闭数据连接
        return render(request, 'publisher_edit.html', {'edit_object': ret})  # 返回结果
    else:  # post 请求
        conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='1234', db='publisher',
                               charset='utf8')
        cursor = conn.cursor()
        name = request.POST.get('pub_name')
        sql = "update bookstore_publisher set name=%s where id=%s"
        cursor.execute(sql, [name, pk, ])
        conn.commit()
        cursor.close()
        conn.close()
        return redirect('/publisher')


def book_list(request):
    all_book = models.Book.objects.all()  # 查询book表中的所有数据
    # print(all_book)
    # for books in all_book:
    #     print(books)
    #     print(books.name)  # 获取表中的name属性
    #     print(books.pk)  # 获取主键信息
    #     print(books.publisher)  # 获取外键关联的出版社对象，可以直接操作该对象获取属性books.publisher.name
    #     print(books.publisher_id)  # 获取外键id，也可以用books.publisher.id获得不过会更麻烦，会多查询一次
    return render(request, 'book_list.html', {'all_book': all_book})


# def book_list(request):
#     conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='1234', db='publisher',
#                            charset='utf8')  # 通过pymysql连接mysql数据
#     cursor = conn.cursor()  # 创建游标
#     sql = 'select bookstore_book.id,bookstore_book.name,bp.name from bookstore_book left join ' \
#           'bookstore_publisher bp on bp.id = bookstore_book.publisher_id;'  # 左连接查询书名和对应的出版社名称
#     s = cursor.execute(sql)  # 查询到的结果数量
#     all_book = cursor.fetchall()  # 获取所有数据，返回类型是元组，fetchone获取一条数据，
#     cursor.close()
#     conn.close()  # 关闭连接
#     # print(all_book)
#     # print(s)
#     # for book in all_book:
#     #     print(type(book))
#     #     print(book)
#     # return HttpResponse('book')
#     return render(request, 'book_list.html', {'all_book': all_book})


# def book_add(request):
#     errors = ''
#     if request.method == 'POST':
#         book_name = request.POST.get('book_name')
#         pub_id = request.POST.get('publisher')  # 获取前端提交的post数据中的book_name和pub_id
#         if not book_name:  # 验证用户输入不能为空，返回错误信息
#             errors = '书名不能为空'
#         elif models.Book.objects.filter(name=book_name):  # 验证用户输入信息不能重复，并给出错误提示
#             errors = '书名重复请重新输入'
#         else:  # 执行正确的新增操作
#             models.Book.objects.create(name=book_name, publisher_id=pub_id)  # 将获取的到数据通过orm在数据库中新建数据
#             return redirect('/book_list/')  # 重定向到book_list界面
#     # 直接get请求或者出现错误时会返回当前界面和错误信息
#     all_publishers = models.Publisher.objects.all()  # 获取所有的出版社,让用户只能选择已有的出版社
#     return render(request, 'book_add.html', {'all_publishers': all_publishers, 'errors': errors})
#     # 返回值必须带有all_publishers不然前端无法获取出版社的值，进行更新


def book_add(request):
    errors = ''
    conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='1234', db='publisher',
                           charset='utf8')  # 通过pymysql连接mysql数据
    cursor = conn.cursor()  # 创建游标
    if request.method == 'POST':
        book_name = request.POST.get('book_name')
        pub_id = request.POST.get('publisher')  # 获取前端提交的post数据中的book_name和pub_id
        sql = 'select * from bookstore_book where name=%s;'  # 查询是否存在该书的sql语句
        cursor.execute(sql, [book_name, ])  # 执行sql语句
        if not book_name:  # 验证用户输入不能为空，返回错误信息
            errors = '书名不能为空'
        elif cursor.fetchone():  # 验证用户输入信息不能重复，并给出错误提示
            errors = '书名重复请重新输入'
        else:  # 执行正确的新增操作
            sql = 'insert into bookstore_book(name, publisher_id) values (%s,%s);'  # 新增数据到数据库表中
            cursor.execute(sql, [book_name, pub_id, ])
            conn.commit()  # 一定要提交不然不会保存到数据库
            cursor.close()
            conn.close()
            return redirect('/book_list/')  # 重定向到book_list界面
    sql = 'select bookstore_publisher.id,bookstore_publisher.name from bookstore_publisher;'  # 查询得到所有的出版社信息
    cursor.execute(sql)
    all_publishers = cursor.fetchall()
    cursor.close()
    conn.close()
    return render(request, 'book_add.html', {'all_publishers': all_publishers, 'errors': errors})


def book_del(request):
    pk = request.GET.get('id')  # 获取id
    print(pk)
    del_obj = models.Book.objects.filter(id=pk)  # 通过orm获取删除对象
    del_obj.delete()  # 通过orm对象进行删除
    return redirect('/book_list/')


def book_edit(request):
    pk = request.GET.get('id')
    book_obj = models.Book.objects.get(id=pk)
    publisher_obj = models.Publisher.objects.all()
    if request.method == 'POST':
        book_name = request.POST.get('book_name')
        publisher_id = request.POST.get('publisher_id')
        # 编辑对象做出修改
        # 方法1
        # book_obj.name = book_name
        # book_obj.publisher_id = publisher_id
        # book_obj.save()
        # 方法2
        models.Book.objects.filter(pk=pk).update(name=book_name, publisher_id=publisher_id)
        return redirect('/book_list/')
    return render(request, 'book_edit.html', {'book_obj': book_obj, 'publisher_obj': publisher_obj})


def author_list(request):
    """
    展示作者
    :param request:
    :return:
    """
    # 查询所有的作者然后返回一个页面
    all_author = models.Author.objects.all()
    # for author in all_author:
    #     print(author)
    #     print(author.name)
    #     print(author.books, type(author.books))  # 是一个关系管理对象，会获取到当前作者关联的所有对象
    #     print(author.books.all(), type(author.books.all()))  # 关联的所有对象
    return render(request, 'author_list.html', {'all_author': all_author})


def author_add(request):
    """
    新增作者
    :param request:
    :return:
    """
    # get 返回页面包含form表单，让用户输入作者，选择作评
    all_books = models.Book.objects.all()
    # post
    if request.method == 'POST':
        # 获取用户提交数据
        author_name = request.POST.get('author_name')
        # book_ids = request.POST.get('book_id') # 如果传入的值有多个只能获取最后一个值
        book_ids = request.POST.getlist('book_id')  # 获取多个数据
        # print(request.POST)
        # print(author_name)
        # print(book_ids)
        # 向数据库中插入对象
        author_obj = models.Author.objects.create(name=author_name)
        # 将作者绑定书籍对象
        author_obj.books.set(book_ids)  # 设置多对多关系
        # 返回展示页面
        return redirect('/author_list/')
        pass

    return render(request, 'author_add.html', {'all_books': all_books})


# 删除作者
def author_del(request):
    pk = request.GET.get('pk')  # 通过前端获取需要删除的id
    models.Author.objects.filter(pk=pk).delete()  # 查询到对象进行删除
    # 也会删除与书籍相关的对应关系,并没有删除书籍
    return redirect('/author_list/')


# 编辑作者
def author_edit(request):
    pk = request.GET.get('pk')  # 获取get请求中的id
    author_obj = models.Author.objects.get(pk=pk)  # 获取所有的书籍用于修改
    if request.method == 'POST':
        name = request.POST.get('author_name')  # 获取post中修改的作者名字
        book_ids = request.POST.getlist('book_id')  # 获取修改的后书籍id
        author_obj.name = name  # 修改作者名字
        author_obj.save()  # 将修改保存到数据库
        author_obj.books.set(book_ids)  # 设置作者与书籍的对应关系
        return redirect('/author_list/')  # 重定向到到作者列表界面
    book_objs = models.Book.objects.all()  # 查询出所有书籍方便编辑界面
    return render(request, 'author_edit.html', {'author_obj': author_obj, 'book_objs': book_objs})  # 返回修改界面
