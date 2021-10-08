# This code allows you to see the run time of your code 

import time

nemo = ['nemo']
everyone = ['dory', 'bruce', 'marlin', 'nemo', 'gill'
'bloat', 'nigel', 'squirt', 'darla', 'hank']
large = ['nemo' for i in range(10000)]

def findNemo(array):
  t0 = time.time()
  for i in range(len(array)):
    if (array[i] == 'nemo'):
      print ('Found Nemo')

  t1 = time.time()
  print (f'Call to find Nemo took {t1 -t0} milliseconds' )

findNemo(nemo)
