import json
from django.urls import reverse
from django.shortcuts import render,redirect,HttpResponse
from django.core.paginator import Paginator
from django.core.paginator import Paginator,EmptyPage   #EmptyPage:一个错误类型
from library.models import Book,Publish,Author

# Create your views here.

def  books(request):
    book_list = Book.objects.all()
    paginator = Paginator(book_list, 10)
    try:   #如果取超过页码的页面会报错
        current_page_num=request.GET.get('page',1) #如果取不到数据，就取第一页的#取值page是多少
        current_page=paginator.page(current_page_num)#显示第几页数据
    except EmptyPage as e:
        current_page_num=1
        current_page = paginator.page(1)


    return render(request, 'books.html', {'current_page': current_page,'paginator':paginator,'current_page_num':int(current_page_num),'book_list':book_list,})

def  add(request):
    if request.method == 'GET':
        publish_list = Publish.objects.all()
        author_list = Author.objects.all()
        return render(request,'add.html',{'publish_list':publish_list,'author_list':author_list})
    else:
        title = request.POST.get('title')
        price = request.POST.get('price')
        pub_date = request.POST.get('pub_date')
        publish_id = request.POST.get('publish_id')
        author = request.POST.getlist('author')  # 获取的是列表
        book = Book.objects.create(title=title, price=price, pub_date=pub_date, publish_id=publish_id)
        book.authors.add(*author)
        return redirect(reverse('books'))



def delete(request,delete_id):
    Book.objects.filter(pk=delete_id).delete()
    return redirect(reverse('books'))


def edit(request,edit_id):
    edit_list = Book.objects.filter(pk=edit_id).first()
    if request.method=='GET':

        publish_list = Publish.objects.all()
        author_list = Author.objects.all()
        return render(request,'edit.html',{'edit_list':edit_list,'publish_list':publish_list,'author_list':author_list})
    else:
        title = request.POST.get('title')
        price = request.POST.get('price')
        pub_date = request.POST.get('pub_date')
        publish_id = request.POST.get('publish_id')
        author = request.POST.getlist('author')
        Book.objects.filter(pk=edit_id).update(title=title, price=price, pub_date=pub_date, publish_id=publish_id)
        edit_list.authors.set(author)
        return redirect(reverse('books'))



def ajax_delete(request,ajax_del_id):
    response = {'state': True}
    try:
        Book.objects.filter(pk=ajax_del_id).delete()
    except Exception as e:
        response = {'state': False}

    return HttpResponse(json.dumps(response))



