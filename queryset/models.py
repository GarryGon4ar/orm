from django.db import models


class Task(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    description = models.CharField(max_length=512)
    task_cost = models.DecimalField(max_digits=7, decimal_places=2)

class TaskStatuses(models.Model):
    CREATED = 0
    ASSIGNED = 1
    REISSUED = 2
    CHECKING = 3
    DONE = 4
    STATUS_TYPES = (
        (CREATED, 'Created'),
        (ASSIGNED, 'Assigned'),
        (REISSUED, 'Reissued'),
        (CHECKING, 'Checking'),
        (DONE, 'Done'),
    )
    created = models.DateTimeField(auto_now_add=True)
    task_id = models.IntegerField()
    status_type = models.PositiveSmallIntegerField(choices=STATUS_TYPES,max_length=5)
