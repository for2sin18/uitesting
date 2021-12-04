##test_wrapper调用tmp，tmp1，tmp2，tmp0，1，2中都有hello goodbye是重复造轮子，所以把这些重复的操作放进装饰器中
def extend(fuc):
    def hello(*args,**kwargs):
        print("hello")
        fuc(*args,**kwargs)
        print("good bye")

    return hello

@extend
def tmp0(self,name,value):
    print("tmp0")
@extend
def tmp1():
    print("hello")
    print("tmp1")
    print("good bye")
#extend包裹住想要实现操作的方法名注意是方法名在这里充当参数，
def test_wrapper():
    # extend(tmp0)()
    # extend(tmp1)()
#在这里你发现还要写函数名extend，这很不爽，能不能把extend也省略直接写tmp1呢，答案是可以的只需要在不想造轮子的方法上加上@extend即可
    tmp0(self=1,name="x",value="akjhfkjdhvk")
