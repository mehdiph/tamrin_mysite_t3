from django.shortcuts import render 
blog=[
    {
        "id":1,
        "title":"jango",
        "description":"this is jango exercise"
    },
    {
        "id":2,
        "title":"jango",
        "description":"this is jango exercise"
    },
    {
        "id":3,
        "title":"jango",
        "description":"this is jango exercise"
    }
  
]

# Create your views here.
def home_view(request):
    return  render(request,"pages/home.html",{"posts":blog}) 

def about_view(request):
    return render(request, "pages/about.html", {"posts": blog})