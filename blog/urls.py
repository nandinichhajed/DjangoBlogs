from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new/', views.post_new, name='post_new'),
]


# This part post/<int:pk>/ specifies a URL pattern – we will explain it for you:

# post/ means that the URL should begin with the word post followed by a /. So far so good.
# <int:pk> – this part is trickier. 

# It means that Django expects an integer value and will transfer it to 
# a view as a variable called pk.

# / – then we need a / again before finishing the URL.
# That means if you enter http://127.0.0.1:8000/post/5/ into your browser, 
# Django will understand that you are looking for a view called post_detail and 
# transfer the information that pk equals 5 to that view.