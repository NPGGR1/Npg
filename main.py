import math
#klasa liczby oraz dzialania dodawania odejmowania mnozenia dzielenia potegowania i pierwiastkowania
class number:
    def __init__(self,x_axis , y_axis):
        self.real_part=x_axis;
        self.imaginary_part=y_axis;
    def module(self):
        return math.sqrt( self.real_part**2 + self.imaginary_part**2 );
    def get_real_part(self):
        return self.real_part;
    def get_imaginary_part(self):
        return self.imaginary_part;
    def set_real_part(self, param):
        self.real_part = param;
    def set_imaginary_part(self, param):
        self.imaginary_part = param;
    def set_both_parts(self, param_x, param_y):
        self.set_real_part(param_x);
        self.set_imaginary_part(param_y);
    def get_angle(self):
        if(self.module() != 0):
            return math.acos((self.real_part) / self.module());
        else:
            return 0;
    def set_angle_module(self, angle, module):
        self.real_part=math.cos(angle)*module;
        self.imaginary_part=math.sin(angle)*module;
def plus(number_1, number_2):
    return number(number_1.get_real_part()+number_2.get_real_part(),number_1.get_imaginary_part()+number_2.get_imaginary_part())
def minus(number_1, number_2):
    return number(number_1.get_real_part() - number_2.get_real_part(),
                  number_1.get_imaginary_part() - number_2.get_imaginary_part())
def multiply(number_1, number_2):
    return number((number_1.get_real_part() * number_2.get_real_part()) - (number_1.get_imaginary_part() * number_2.get_imaginary_part()),
                  (number_1.get_imaginary_part() * number_2.get_real_part()) + (number_1.get_real_part() * number_2.get_imaginary_part()))
def divide(number_1, number_2):
    if (number_2.module()!=0):
        return number(((number_1.get_real_part() * number_2.get_real_part()) + (
                    number_1.get_imaginary_part() * number_2.get_imaginary_part())) / (
                                  number_2.get_real_part() ** 2 + number_2.get_imaginary_part() ** 2),
                      ((number_1.get_imaginary_part() * number_2.get_real_part()) + (
                                  number_1.get_real_part() * number_2.get_imaginary_part())) / (
                                  number_2.get_real_part() ** 2 + number_2.get_imaginary_part() ** 2))
    else:
        return "ERROR";
def root_normal(number_1 , n):
    list = []
    angle_first = number_1.get_angle()/n
    module_number = number_1.module()**(1/n)
    for i in range(0,n):
        list.append(number(0,0));
        list[i].set_angle_module(angle_first+(2*math.pi)/n,module_number)
    return list
def power_normal(number_1 , n):
    number_1_copy= number_1
    number_1_copy.set_angle_module(number_1.get_angle()*n, number_1.module()**n)
    return number_1_copy;
#pamiec ostatnich 10 zad
class operation:
    def __init__(self,number1, number2, mark):
        self.number_1=number1;
        self.number_2=number2;
        self.mark_=mark; #typ char
        if(mark=='+'):
            self.result = plus(number1, number2)
        elif(mark=='-'):
            self.result = minus(number1 , number2)
        elif(mark=='*'):
            self.result = multiply(number1, number2)
        elif(mark=='/'):
            self.result = divide(number1 , number2)
        elif(mark=='^'):
            self.result = power_normal(number1 , number2)
        elif(mark=='r'):
            self.result= root_normal(number1 , number2)
        else:
            self.result="ERROR"
    def get_number_1(self):
        return self.number_1
    def get_number_2(self):
        return self.number_2
    def get_operation(self):
        return self.mark_
    def get_result(self):
        return self.result

def add_to_memory (list , operation1):
    list.append(operation1)
    if(len(list)>10):
        list.pop(0)
    return list
def clear_memory ():
    return []
memory = []


#test:
first = number(1,1);
first.set_both_parts(3,4);
first.set_angle_module(math.pi, 1)
second=number(0,0);
second.set_angle_module(0, 1)
plus(second,first)
third=number(-1,0)
print( first.get_real_part())
print( first.module())
print(plus(second,first).get_angle())
lis=root_normal(second,2)
print("root test: ")
print(lis[0].get_real_part(),"+", lis[0].get_imaginary_part(), "i\n", lis[1].get_real_part(),"+", lis[1].get_imaginary_part(), "i")
print("normal power test: ")
print(power_normal(third, 2).get_real_part(),"+", power_normal(third, 2).get_imaginary_part() ,"i")