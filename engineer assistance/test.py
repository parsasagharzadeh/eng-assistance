import inspect

class MyClass:
    def method_one(self):
        return "Method One Called"

    def method_two(self):
        return "Method Two Called"

    def _private_method(self):
        return "Private Method Called"

def get_method_names(cls):
    # استخراج متدها و فیلتر کردن فقط متدهای عمومی
    return [name for name, obj in inspect.getmembers(cls, predicate=inspect.isfunction) if not name.startswith('_')]

# استفاده از تابع
method_names = get_method_names(MyClass)

# ایجاد یک شیء از کلاس
my_instance = MyClass()
listof=[]
# فراخوانی متدها و چاپ نتایج
for method_name in method_names:
    method = getattr(my_instance, method_name)
    listof.append(method)
    # print(f"{method_name}: {result}")
print(listof[0]())
