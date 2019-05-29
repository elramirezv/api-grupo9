import os
from celery import Celery


#  https://djangopy.org/how-to/handle-asynchronous-tasks-with-celery-and-django


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'api_config.settings')

app = Celery('api_config')
app.config_from_object('django.conf:settings', namespace='CELERY')

app.conf.beat_schedule = {
    'thread_check': {  #name of the scheduler
        'task': 'thread_check',  # task name which we have created in tasks.py
        'schedule': 600.0,   # set the period of running
                            # set the args
    },

    'thread_check_10000': {  #name of the scheduler
    'task': 'thread-check-10000',  # task name which we have created in tasks.py
    'schedule': 1200.0,   # set the period of running
                        # set the args
    },
    'watch_server': {  #name of the scheduler
    'task': 'watch_server',  # task name which we have created in tasks.py
    'schedule': 900.0,   # set the period of running
                        # set the args
    },
    'check_not_finished': {  #name of the scheduler
        'task': 'check_not_finished',  # task name which we have created in tasks.py
        'schedule': 700.0,   # set the period of running
                            # set the args
    },
    'create_base_products': {  #name of the scheduler
        'task': 'base_products',  # task name which we have created in tasks.py
        'schedule': 1200.0,   # set the period of running
                            # set the args
    },
        'get_base_products': {  #name of the scheduler
        'task': 'get_base_products',  # task name which we have created in tasks.py
        'schedule': 1200.0,   # set the period of running
                            # set the args
    }

    
}

app.autodiscover_tasks()

@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request)) 
