# Strings can be accessed like arrays:

name = 'Think Python'

# This is OK:
print(name[1])

# But strings are immutable!
name[0] = 'x'
name[6] = 'x'

print(name)