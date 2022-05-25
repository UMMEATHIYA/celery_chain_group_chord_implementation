from celery import chain, signature, group

from tasks import add, mul

job1 = group([
                add.s(2,2),
                add.s(4,4),
                add.s(8,8),
                
])

job2 = group([
                mul.s(2,2),
                
])

final_job = chain(job1,job2, add.delay(2,2))
print(final_job)