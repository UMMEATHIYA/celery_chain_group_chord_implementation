from celery import chain , signature, group
from tasks import add

res = group(add.s(i,i) for i in range(10))()
print(res.get(timeout=1))

job = group([
                add.s(2,2),
                add.s(4,4),
                add.s(8,8),
                add.s(16,16),
                add.s(32,32),
])

result = job.apply_async()

print(result.ready())

print(result.successful())

print(result.get())


g = group(add.s(2,2), add.s(4,4))
g.link(add.s())
res = g()
print(res)


