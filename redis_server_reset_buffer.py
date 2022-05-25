# celery -A tasks worker --loglevel=info

from celery import signature
from tasks import add

#####Any options added will be merged with the options in the signature, with new options taking precedence ###3

s = add.signature((2,2), countdown = 10)
print("Changed option - countdown value: ", s.apply_async(countdown=1))     # countdown is now 1


#####You can also clone signatures to create derivatives#######

s = add.s(2)
print("clone result 1",s)

clone_result = s.clone(args=(4,), kwargs={'debug': True})
print('Clone result:', clone_result)

#####Immutability########
#Sometimes you want to specify a callback that doesn't take additional arguments, and in that case ou can set the signature to be immutable###

imm = add.apply_async((2,2), link=reset_buffers.signature(immutable=True))
print(imm)
