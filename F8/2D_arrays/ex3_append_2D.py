# Example showing append on a 2D array.


arr = [['📚','☕'],
       ['💡','⏰'],
       ['💻','🥄'],
       ['📦','🧺']]

# Append a whole row, to the outer list
arr.append(['xx', 'yy'])

# Append a single element to the first 'row'
arr[0].append('zx')


print(arr)
# (copy code from slides)