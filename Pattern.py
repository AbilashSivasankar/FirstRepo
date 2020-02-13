def pattern(a):
    for x in range(a):
        print('  '*(a-x-1)+'*'*(2*x+1))

pattern(5)        
