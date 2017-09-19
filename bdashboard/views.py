from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Job
import json
from django.http import HttpResponse
from .filters import JobFilter
from django.core import serializers
from .reports import ChartData
from .forms import JobForm
from django.shortcuts import redirect

def post_list(request):
    jobs = Job.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'bdashboard/post_list.html', {'jobs': jobs})

def post_detail(request, pk):
    job = get_object_or_404(Job, pk=pk)
    return render(request, 'bdashboard/post_detail.html', {'job': job})

def add_job(request):
    return render(request, 'bdashboard/add_job.html')


def get_jobs(request):
    if request.is_ajax():
        q = request.GET.get('term', '')
        jobs = Job.objects.filter(text__icontains = q )[:20]
        results = []
        for job in jobs:
            job_json = {}
            job_json['id'] = job.pk
            job_json['label'] = job.text
            job_json['value'] = job.title
            results.append(job_json)
        data = json.dumps(results)
        print(data)
    else:
        data = 'fail'
    mimetype = 'application/json'
    return HttpResponse(data, mimetype)


def search(request):
    job_list = Job.objects.all()
    job_filter = JobFilter(request.GET, queryset=job_list)
    return render(request, 'bdashboard/job_list.html', {'filter': job_filter})


def get_chart(request):
    data = {}
    data['chart_data'] = ChartData.get_job_list()
    print(data)
    return HttpResponse(json.dumps(data), content_type='application/json')

def add_job(request):

    if request.method == "POST":
        form = JobForm(request.POST)
        if form.is_valid():
            job = form.save(commit=False)
            #job.creator = request.user
            job.published_date = timezone.now()
            job.save()
            return redirect('job_list')
    else:
        form = JobForm()
    return render(request, 'bdashboard/add_job.html', {'form': form})

def job_edit(request, pk):
    job = get_object_or_404(Job, pk=pk)
    if request.method == "POST":
        form = JobForm(request.POST, instance=job)
        if form.is_valid():
            job = form.save(commit=False)
            #job.author = request.user
            job.published_date = timezone.now()
            job.save()
            return redirect('job_list')
    else:
        form = JobForm(instance=job)
    return render(request, 'bdashboard/add_job.html', {'form': form})

def job_remove(request, pk):
    job = get_object_or_404(Job, pk=pk)
    job.delete()
    return redirect('job_list')
