from django.shortcuts import render , redirect

# request is dictionary : 
######## all below in request ########
## method ( GET,POST,PUT,DELETE)
## header
## body
## user
## context
######################################

 
context = {}

def root2(request):
    return render(request,'index.html')

def root(request):
    
    ## 
    name = None
    location = None
    comment = None
    checkbox= [] ## use append to add value
    if request.method == 'GET' :
        return render(request,"index.html")
    
    if request.method == 'POST' :
        ## Loop On All Input form in request
        for key , value in request.POST.items():
            if key == "name_person":
                name = value
            if key == "radio_location":
                location = value
            if key=="comment":
                comment=value
            if key =="language_python":
                checkbox.append(key)
            if key =="language_js":
                checkbox.append(key)
        context["name"] = name
        context["rl"] = location
        context["checkbox"] = checkbox
        context["comment"] = comment
        return redirect('/result')
    
def result_info(request):
    
    return render(request,'result.html',context)
