import pymysql
from django.shortcuts import render, redirect, HttpResponse
from bookstore import models


# Create your views here.
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


def add_publisher(request):
    info = None
    if request.method == 'POST':
        pub_name = request.POST.get('pub_name')
        if not pub_name:
            info = '出版社名字不能为空'
            return render(request, 'publisher_add.html', {'info': info})
        if models.Publisher.objects.filter(name=pub_name):
            return render(request, 'publisher_add.html', {'info': '当前出版社已经存在'})
        # print(pub_name)
        models.Publisher.objects.create(name=pub_name)
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


# def book_list(request):
#     all_book = models.Book.objects.all()  # 查询book表中的所有数据
#     print(all_book)
#     for books in all_book:
#         print(books)
#         print(books.name)  # 获取表中的name属性
#         print(books.pk)  # 获取主键信息
#         print(books.publisher)  # 获取外键关联的出版社对象，可以直接操作该对象获取属性books.publisher.name
#         print(books.publisher_id)  # 获取外键id，也可以用books.publisher.id获得不过会更麻烦，会多查询一次
#
#     return HttpResponse('book')

def book_list(request):
    conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='1234', db='publisher',
                           charset='utf8')  # 通过pymysql连接mysql数据
    cursor = conn.cursor()  # 创建游标
    sql = 'select bookstore_book.id,bookstore_book.name,bp.name from bookstore_book left join ' \
          'bookstore_publisher bp on bp.id = bookstore_book.publisher_id;'  # 左连接查询书名和对应的出版社名称
    s = cursor.execute(sql)  # 查询到的结果数量
    all_book = cursor.fetchall()  # 获取所有数据，返回类型是元组，fetchone获取一条数据，
    cursor.close()
    conn.close()  # 关闭连接
    print(all_book)
    print(s)
    for book in all_book:
        print(type(book))
        print(book)
    return HttpResponse('book')
