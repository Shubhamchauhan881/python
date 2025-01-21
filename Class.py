class myClass():
    def method1 (self,name):
        print("My name is",name)

    def method2 (self,age):
        print("i am 22 year old",age)

def main():
    c = myClass()
    c.method1('Shubham')
    c.method2(22)

if __name__== "__main__":
    main()
