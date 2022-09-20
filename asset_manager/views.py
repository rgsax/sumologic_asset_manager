from ast import Delete
from django.shortcuts import render, redirect
from django.views import View
from django.http import HttpResponseNotFound, JsonResponse

from .sumo import verify_asset, get_assets
from .models import SumoInstance

class AssetView(View):
    def get(self, request, asset):
        if not verify_asset(asset):
            return HttpResponseNotFound("Asset not found.")
        
        instances = SumoInstance.objects.all()

        instances_assets = {}
        for instance in instances:
            instances_assets[instance.tag] = []

            data = get_assets(instance, asset)

            instances_assets[instance.tag].extend(data)

        return JsonResponse(instances_assets)

class InstanceView(View):
    def get(self, request, tag=''):
        return render(request, 'instances.html')

    def post(self, request, tag=''):
        if tag:
            instance = SumoInstance.objects.get(tag=tag)
            instance.delete()
        else:
            form_data = request.POST
            instance = SumoInstance.objects.get(tag=form_data['tag'])
            instance.url = form_data['url']
            instance.key = form_data['key']
            instance.save()

        return JsonResponse({"status": "Success"})

def homepage(request):
    return render(request, 'index.html')

def create_instance(request):
    if request.method =="POST":
        form_data = request.POST
        tag = tag=form_data['tag']
        url = form_data['url']
        key = form_data['key']
        
        instance = SumoInstance(tag=tag, url=url, key=key)
        instance.save()

        return redirect("/manage/instance")

def get_instances(request):
        instances = list(map(lambda i: {'tag': i.tag, 'url': i.url}, SumoInstance.objects.all()))
        return JsonResponse({'instances': instances})
