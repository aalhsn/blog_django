"""blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from articles.views import ArticlesListView

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('home/',views.homepage_view, name="home"),
    path('list/',ArticlesListView.as_view(), name="articles-list"),
    # path('details/<int:article_id>',views.article_detail, name="article-detials"),
    # path('create/',views.create_view, name="create"),
    # path('update/<int:article_id>',views.update_view, name="update"),
    # path('delete/<int:article_id>',views.delete_article, name="delete"),

]

urlpatterns+=static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)