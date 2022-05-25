# celery -A tasks worker --loglevel=info

from celery import signature
from tasks import add


result = signature('tasks.add', args=(2,2), countdown=10)
print(result)
print(add.signature((2,2), countdown=10))
print(add.s(2,2,debug=True))

s = add.signature((2,2), {'debug': True}, countdown=10)
print(s.args)

####################
print(s.kwargs)

#####################
print(s.options)

#print(add.apply_async(args, kwargs, **options))
#res = add.signature(args, kwargs, **options).apply_async()

res = add.apply_async((2,2),countdown=1)
print(res)

res2 = add.signature((2,2), countdown=1).apply_async()
print(res2)

##############PARTIALS##############################
###########With a signature, you can execute the task in a worker#############

r1 = add.s(2,2).delay()
print("This is r1 result" ,r1)

r2 = add.s(2,2).apply_async(countdown=1)
print("This is r2 result" ,r2)

###########PARTIALS###########################
print("Partials 1:" ,add.s(2,2).delay())
print("Partials 2:" ,add.s(2,2).apply_async(countdown=1))
print("Partials 3:" ,add.s(2,2)())


#####################################################
#Specifying additional args,kwargs, or options to apply_async/delay creates partials####
#Any arguments added will be prepended to the args in the signature##

partial = add.s(2)      # incomplete signature 
print("Partial delay result:" ,partial.delay(4))        # 4 + 2
print("Partial apply async result:", partial.apply_async((4,)))     #same - remember async is a method which takes arguments and then pass the values like tuple values 
test = partial.apply_async((4,))
print("(4,) result",test.get())

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

imm = add.apply_async((2,2), lin=reset_buffers.signature(immutable=True))
print(imm)

