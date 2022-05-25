from celery import chain , signature, group, chord
from tasks import add 
from tasks import tsum

res = chord((add.s(i, i) for i in range(10)), tsum.s())()
print(res.get())

#The above example creates 10 tasks that all start in parallel, & when all of them are complete the return values #
#are comboned into a list and sent to the tsum task#