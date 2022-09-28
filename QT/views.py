from django.http import HttpResponse
from django.shortcuts import render, redirect

from .models import Developers, Managers, Report, AssignedWork


def Home(request):
    return render(request, 'Home.html')


def companyhome(request):
    return render(request, 'companyhome.html')


def Management(request):
    if request.method == 'POST':
        admin_id = request.POST.get('admin_id')
        password = request.POST.get('password')
        if admin_id == 'IAM' and password == 'qwer123':
            return redirect('manageuser.html')
        else:
            return HttpResponse('Invalid')
    return render(request, 'Management.html')


def manageusers(request):
    return render(request, 'manageuser.html')


def Dev_add(request):
    if request.method == 'POST':
        Name = request.POST.get('name')
        Email = request.POST.get('email')
        Dev_id = request.POST.get('dev_id')
        Password = request.POST.get('password')
        D = Developers()
        D.Name = Name
        D.Email = Email
        D.Dev_id = Dev_id
        D.Password = Password
        D.save()
    return render(request, 'Newdeveloper.html')


def TL_add(request):
    if request.method == 'POST':
        Name = request.POST.get('name')
        Email = request.POST.get('email')
        Manager_id = request.POST.get('manager_id')
        Password = request.POST.get('password')
        M = Managers()
        M.Name = Name
        M.Email = Email
        M.Manager_id = Manager_id
        M.Password = Password
        M.save()
    return render(request, 'Newteamlead.html')


def TL_space(request):
    return render(request, 'Teamleadspace.html')


def Assign_work(request):
    if request.method == 'POST':
        pro_name = request.POST.get('projectname')
        wtd = request.POST.get('work_to_do')
        a = AssignedWork()
        a.Project_Name = pro_name
        a.Work_To_Do = wtd
        a.save()
    return render(request, 'Assignwork.html')


def report(request):
    details = Report.objects.filter(Status=False)
    return render(request, 'viewreport.html', {'values': details})


def approve(request, id):
    data = Report.objects.get(id=id)
    data.Status = True
    data.save()
    return redirect('/viewreport')


def Manager_login(request):
    if request.method == 'POST':
        userid = request.POST.get('userid')
        password = request.POST.get('password')
        if userid == 'admin' and password == '1':
            return redirect('approvedreport.html')
        else:
            return HttpResponse('Invalid')
    return render(request, 'Manager.html')


def TL_login(request):
    if request.method == 'POST':
        m_id = request.POST.get('manager_id')
        pwd = request.POST.get('password')
        try:
            Managers.objects.get(Manager_id=m_id, Password=pwd)
            return redirect('Teamleadspace.html')
        except:
            return HttpResponse('Invalid')
    return render(request, 'Teamlead.html')


def Dev_login(request):
    if request.method == 'POST':
        dev_id = request.POST.get('dev_id')
        password = request.POST.get('password')
        try:
            Developers.objects.get(Dev_id=dev_id, Password=password)
            return redirect('Developermanu.html')
        except:
            return HttpResponse('Invalid')
    return render(request, 'Developer.html')


def the_report(request):
    if request.method == 'POST':
        Pname = request.POST.get('projectname')
        Dname = request.POST.get('dev_name')
        PR = request.POST.get('report')
        r = Report()
        r.Project_Name = Pname
        r.Dev_Name = Dname
        r.Project_Report = PR
        r.save()
    return render(request, 'report.html')


def approved_report(request):
    details = Report.objects.filter(Status=True)
    return render(request, 'approvedreport.html', {'values': details})


def Dev_home(request):
    return render(request, 'Developermanu.html')


def view_work(request):
    details = AssignedWork.objects.all()
    return render(request, 'viewwork.html', {'values': details})


def D_Update(request):
    details = Developers.objects.all()
    return render(request, 'DUpdate.html', {'values': details})


def edit(request, id):
    details = Developers.objects.all()
    D = Developers.objects.get(id=id)
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        D.Email = email
        D.Password = password
        D.save()
        return redirect('/DUpdate')
    return render(request, 'DUpdate.html', {'values': details, 'a': D})


def delete(request, id):
    data = Developers.objects.filter(id=id).delete()
    return redirect('/DUpdate')


def TL_Update(request):
    details = Managers.objects.all()
    return render(request, 'TLUpdate.html', {'values': details})


def ed(request, id):
    details = Managers.objects.all()
    M = Managers.objects.get(id=id)
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        M.Email = email
        M.Password = password
        M.save()
        return redirect('/TLUpdate')
    return render(request, 'TLUpdate.html', {'values': details, 'b': M})


def delt(request, id):
    data = Managers.objects.filter(id=id).delete()
    return redirect('/TLUpdate')
