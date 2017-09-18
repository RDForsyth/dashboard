

from .models import Job






class ChartData(object):

    @classmethod
    def get_job_list(cls):

        data = {'name':[],'cost':[]}
        all_jobs = Job.objects.all()

        for job in all_jobs:
            data['name'].append(job.title)
            data['cost'].append(job.cost)

        return data
