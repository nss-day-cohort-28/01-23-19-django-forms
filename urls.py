
app_name="myApp"
urlpatterns = [
    # ... other paths ...
    path('foo/newFoo', views.fooForm, name='fooForm'), #to load the page with your form
    path('foo/addFoo', views.addFoo, name='addFoo'), #to post the completed form to the db, then send the user to a new page
    path('foo', views.fooList, name='fooList'), # apage you could redirect to that shows the newly added foo in a list
    # ... other paths ...
]
