#99乘法表-作法1
def table_1(a,b):
    print('\n'.join(['\t'.join(['%d x %d = %d' % (i,j,i*j) for i in range(a,b+1)]) for j in range(1,10)]))
    print('\n')





#三角形
def triangle(h):
    for i in range(h):
        print(" "*(h-i)+"*"*(i)*2+"*")



#菱形
def diamond(h):
    for i in range(h):
        print(" "*(h-i)+"*"*(i)*2+"*")
    for j in range(h-1):
        print(" "*(j+2)+"*"*(h-j-2)*2+"*")