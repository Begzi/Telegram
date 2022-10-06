from django.urls import path
from .views import *
#из этой же директории импортирую


urlpatterns = [
    # path('', MainHome.as_view(), name = 'work'),
    path('', main, name = 'main'),
    path('notmain', notmain, name = 'notmain'),
    path('wait', wait, name = 'wait'),
]
