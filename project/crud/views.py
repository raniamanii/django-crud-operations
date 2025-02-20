from django.shortcuts import render, redirect, get_object_or_404  
from crud.forms import EmployeeForm  
from crud.models import Employee  

# Create your views here.  
def emp(request):  
    if request.method == "POST":  
        form = EmployeeForm(request.POST)  
        if form.is_valid():  
            form.save()  
            return redirect('show')  # Utilisation du nom défini dans urls.py
    else:  
        form = EmployeeForm()  
    return render(request, 'index.html', {'form': form})

def show(request):  
    employees = Employee.objects.all()  
    return render(request, "show.html", {'employees': employees})  

# Renommer la fonction update() en edit() dans views.py
def update(request, id):  
    employee = get_object_or_404(Employee, eid=id)  # Utiliser eid
    form = EmployeeForm(request.POST, instance=employee)  
    if form.is_valid():  
        form.save()  
        return redirect('show')  
    return render(request, 'edit.html', {'form': form, 'employee': employee})

def destroy(request, id):
    # Récupérer l'employé en fonction de `eid` (ou `id` selon ta config)
    employee = get_object_or_404(Employee, eid=id)  # Remplace `eid` par `id` si nécessaire
    employee.delete()  # Supprimer l'employé
    return redirect('show')  # Rediriger vers la page des employés après la suppression
