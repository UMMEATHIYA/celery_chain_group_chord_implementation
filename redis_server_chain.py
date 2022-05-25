from celery import chain , signature
from tasks import add

res = chain(add.s(2,2),add.s(4),add.s(8))()
print(res.get())

######This can also be written using pipes####

print((add.s(2,2) | add.s(4) | add.s(8))().get())

###### IMMUTABLE SIGNATURES ##########
immut = add.signature((2,2), immutable=True)

print(add.si(2,2))

res = (add.si(2,2) | add.si(4,4) | add.si(8,8))()
print(res.get())

print(res.parent.get())

print(res.parent.parent.get())