# Lists are *objects*.

kallax1 = ['penna',
           'Think Python',
           'bärbar dator',
           'anteckningsblock']
kallax2 = kallax1

kallax1[0] = 'äpple'

# What do we expect here?
print(kallax2)

# (Sketch state diagram.)