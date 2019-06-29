class comp:
    def run(self):
        print('running')
class lap:
    def work(self,ih,il):
        ih.run()
        il.stop()
class te:
    def stop(self):
        print('stopping')
#il=te()
#ih=comp()
#a=lap()
#a.work(ih,il)
x=int(input('enter the number'))
if x==1:
    print('1')
if x==2:
    print('2')
if x==3:
    print('3')
if x==4:
    print('4')
else:
    print('5')