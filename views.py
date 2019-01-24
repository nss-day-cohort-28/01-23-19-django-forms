# All the imports of classes, etc would be up here


def addFoo(request):

  # Access the values from the form data that has been attached to the request object
  fooName = request.POST["foo_name"] #foo_name is the name we gave to the input in the template
  fooAddress = request.POST["address"]

  # If a 'foo' instance has a foreign key value, you'll need to fetch the item you're relating to foo from the db. The information about that item ( its id or name, etc) will need to be provided in the POST request or via the URL. In this example, we've sent it in with the form data.
  bar = get_object_or_404(Bar, pk=request.POST["id_of_related_thing"])

  # Now make an instance of foo that we can add as a new row in the foo table
  newFoo = Foo(name=fooName, address=fooAddress, bar=bar)
  newFoo.save()

  # You can ALSO take a shortcut by instantiating and saving the mew object at the same time, using create()
  # Note that create just takes comma-separated keyword arguments, not a dict as I showed in class. Oops
  newFoo = Foo.objects.create(name=fooName, address=fooAddress, bar=bar)

  # Always return an HttpResponseRedirect after successfully dealing
  # with POST data. This prevents data from being posted twice if a
  # user hits the Back button.
  return HttpResponseRedirect(reverse('myApp:some_landing_page', args=(newFoo.id,))) #args is optional. Only needed if the route you're heading to needs some data to build the url, like an id


# NEW NEW NEW! Here's another way to handle all of this POST route stuff that we didn't even talk about yet.
# You can use just one route/view for all HTTP requests and simply check for what kind of request it is in the view to decide what to do. In this case, you could have a single route for both viewing the form page and for posting to it
# -- for example 'foo/addFoo'. In that case, your urlpattern list in urls.py would not have a separate url pattern for both the form page and the POST. The 'action' in the form would be the same as the page you're on. You can even use a '.' to represent it!' Like this:
<form action="." method='POST'>


# Then, in the view, all of the above stuff would be in the body of the function, but it would be wrapped in a conditional so you can either render the form or handle adding the POSTed form data to the db. Like so:

def addFoo(request):

  if request.method == "POST":
    # Do all the stuff from above example

  if request.method == "GET":
    #render the form page
    return render(request, 'myApp/foo_form.html')

# Please ask an instructor if you need any clarity on this!
