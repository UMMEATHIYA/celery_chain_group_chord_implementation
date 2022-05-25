from tasks import add

res = add.chunks(zip(range(100), range(100)), 10)()
print(res.get())

#You can also convert chunks to a group#
group = add.chunks(zip(range(100), range(100)),10).group()
print(group)

group2 = group.skew(start=1, stop=10)()
print(group2)