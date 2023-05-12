from django.urls import path
from .views import *

urlpatterns =[
    path('',index, name='index'),
    path('blog_one/',b_one, name='blog_one'),
    path('blog/', blog, name='blog'),
    path('about/', about, name='about'),
    path('contact/',contact, name='contact'),
    path('error/',error, name='error'),
    path('service/',service, name='service'),
    path('single/',single, name='single'),
    path('type/',type, name='type'),
    path('register/',register, name='rigster'),
    path('register_submit/',r_sub,name='register_submit'),
    path('otp/', otp_fun, name='otp'),
    path('login/', login, name='login'),
    path('logout/', logout, name='logout'),
    path('add_blog/',add_blog, name='add_blog'),
    path('my_blog/', my_blog, name='my_blog'),
    path('singleblog/<int:pk>', singleblog, name='singleblog'),
    path('add_comment/<int:bid>', add_comment, name='add_comment'),
    path('donate/<int:bid>', donate, name='donate'),
    path('donate/paymenthandler/', paymenthandler, name='paymenthandler' ),  
    path('search_blog/', search_blog, name='search_blog'),
    path('my_profile/', my_profile, name='my_profile')  
    
    
    
    
]