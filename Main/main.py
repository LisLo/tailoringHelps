import os
import sys
# find root dir
root_path = os.path.split((os.path.dirname(__file__)))[0]
# set root
sys.path.append(root_path)
from Source.Config.get_input import GetInput
from Source.Services.my_math_methods import MyMethods


class Main(GetInput):
    def execute_workflow(self):
        print("Addition:")
        print(MyMethods.addition(self.a, self.b))
        print("Substraction:")
        print(MyMethods.substraction(self.a, self.b))
        print("a hoch b")
        print(MyMethods.pows(self.a, self.b))
        print("Square")
        print(MyMethods.square(self.a))


my_code = Main(__file__)
my_code.execute_workflow()
