#variable scope= where a variable is visible and acessible
# scope resolution =(LEGB) Local -> enclosed->global->built_in very important

def func1():
    x=1
    print(x)

def func2():
    x=2
    print(x)
x=3

func1()
func2()