from django.http import JsonResponse
from .models import Manager, Driver
import json
from .forms import ManagerRegistrationForm, DriverRegistrationForm

from django.shortcuts import render

#TODO: write the functions down



def get_manager(request, manager_id):
    return JsonResponse({"hello": "world"})
    try:
        manager = Manager.objects.get(id=manager_id)
        data = {
            'id': manager.id,
            'name': manager.name,
            'email': manager.email,
            # add other fields as needed
        }
        return JsonResponse(data)
    except Manager.DoesNotExist:
        return JsonResponse({'error': 'Manager not found'}, status=404)



def get_driver(request, driver_id):
    try:
        driver = Driver.objects.get(id=driver_id)
        data = {
            'id': driver.id,
            'name': driver.name,
            'email': driver.email,
            # add other fields as needed
        }
        return JsonResponse(data)
    except Driver.DoesNotExist:
        return JsonResponse({'error': 'Driver not found'}, status=404)



def update_manager(request, manager_id):
    if request.method == 'POST':
        try:
            manager = Manager.objects.get(id=manager_id)
            data = json.loads(request.body)
            manager.name = data.get('name', manager.name)
            manager.email = data.get('email', manager.email)
            # update other fields as needed
            manager.save()
            return JsonResponse({'message': 'Manager profile updated successfully'})
        except Manager.DoesNotExist:
            return JsonResponse({'error': 'Manager not found'}, status=404)
    return JsonResponse({'error': 'Invalid HTTP method'}, status=405)



def update_driver(request, driver_id):
    if request.method == 'POST':
        try:
            driver = Driver.objects.get(id=driver_id)
            data = json.loads(request.body)
            driver.name = data.get('name', driver.name)
            driver.email = data.get('email', driver.email)
            # update other fields as needed
            driver.save()
            return JsonResponse({'message': 'Driver profile updated successfully'})
        except Driver.DoesNotExist:
            return JsonResponse({'error': 'Driver not found'}, status=404)
    return JsonResponse({'error': 'Invalid HTTP method'}, status=405)



# DONE: 


def register_manager(request):
    if request.method == 'POST':
        form = ManagerRegistrationForm(request.POST, request.FILES)
        if form.is_valid():
            manager = form.save(commit=False)
            manager.set_password(form.cleaned_data['password'])
            manager.save()  # now save to DB
            return JsonResponse({'message': 'Manager registered successfully'})
    else:
        form = ManagerRegistrationForm()
    return render(request, 'register.html', {'form': form})





def register_driver(request):
    if request.method == 'POST':
        form = DriverRegistrationForm(request.POST, request.FILES)
        if form.is_valid():
            driver = form.save(commit=False)
            driver.set_password(form.cleaned_data['password'])
            driver.save()  # now save to DB
            return JsonResponse({'message': 'Driver registered successfully'})
    else:
        form = DriverRegistrationForm()
    return render(request, 'register.html', {'form': form})

