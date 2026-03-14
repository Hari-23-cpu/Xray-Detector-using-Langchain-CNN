from django.shortcuts import render
from .forms import Scanform
from .ai_logic.processor import chain

def upload_scan(request):

    report = None

    if request.method == "POST":
        form = Scanform(request.POST,request.FILES)
        if form.is_valid():
            scan=form.save()

            report = chain.invoke({
                "image_path": scan.image.path,
                "patient_name": scan.patient_name  
            })
            scan.ai_report =report
            scan.save()

    else:
        form = Scanform()

    return render(request,"index.html",{
        "form":form,
        "report":report
    })