"""blog/urls.py explained
        the urls config file here connects the users requests from the browser
        to python functions in your views.py file *see comments in views.py.
        breakdown:
        -import your shit
            -were using the path function *new with django 2.0.1
            -and of course we will be routing between views.py functions
        -declare your urlpatterns list
            -nothing but a list of urls
        -populating your list here's a breakdown of the arguments of path function
            path('route', view.argument, kwargs, name=urlname)
            -path of course calls the funtion,
            -route declares the url to route this url. using "" makes it a root url
             it can accept all sorts of data. in this case were making it use <int:pk>
             the pk "primary key" which is an integer from our model as a variable
             which will be called in our view.route variable is required.
            -view.argument calls a view to use this url with. the views is actually
             where the data is retrieved manipulated and supplied which is the whole
             point of django or any other "dynamic" web framework.
             its where the magic happens. views.argument is required
            -kwargs is optional and a place to set extra options for the url
            -name is the name we give the url so we can easily refer to it anywhere
             in our django application. name is required.
        And thats how django's url routing works. : )
        """

from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name='index'),
    path("post/<int:pk>", views.post, name='post'),

]
