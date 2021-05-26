from tkinter import *
import math
from tkinter import messagebox
from tkinter.messagebox import showinfo
from tkinter.simpledialog import askstring


# klasa liczby oraz dzialania dodawania odejmowania mnozenia dzielenia potegowania i pierwiastkowania

class Number:
    def __init__(self, x_axis, y_axis):
        self.real_part = x_axis
        self.imaginary_part = y_axis

    def module(self):
        return math.sqrt(self.real_part ** 2 + self.imaginary_part ** 2)

    def get_real_part(self):
        return self.real_part

    def get_imaginary_part(self):
        return self.imaginary_part

    def set_real_part(self, param):
        self.real_part = param

    def set_imaginary_part(self, param):
        self.imaginary_part = param

    def set_both_parts(self, param_x, param_y):
        self.set_real_part(param_x)
        self.set_imaginary_part(param_y)

    def get_angle(self):
        if self.module() != 0:
            return math.acos(self.real_part / self.module())
        else:
            return 0

    def set_angle_module(self, angle, module):
        self.real_part = math.cos(angle) * module
        self.imaginary_part = math.sin(angle) * module


class Operation:
    def __init__(self, number1, number2, mark):
        self.number_1 = number1
        self.number_2 = number2
        self.mark_ = mark  # typ char
        #   print()
        if mark == '+':
            self.result = Number(self.number_1.get_real_part() + self.number_2.get_real_part(),
                                 self.number_1.get_imaginary_part() + self.number_2.get_imaginary_part())
        elif mark == '-':
            self.result = Number(self.number_1.get_real_part() - self.number_2.get_real_part(),
                                 self.number_1.get_imaginary_part() - self.number_2.get_imaginary_part())
        elif mark == '*':
            self.result = Number((self.number_1.get_real_part() * self.number_2.get_real_part()) - (
                    self.number_1.get_imaginary_part() * self.number_2.get_imaginary_part()),
                                 (self.number_1.get_imaginary_part() * self.number_2.get_real_part()) + (
                                         self.number_1.get_real_part() * self.number_2.get_imaginary_part()))
        elif mark == '/':
            if self.number_2.module() != 0:
                self.result = Number(((self.number_1.get_real_part() * self.number_2.get_real_part()) + (
                        self.number_1.get_imaginary_part() * self.number_2.get_imaginary_part())) / (
                                             self.number_2.get_real_part() ** 2 + self.number_2.get_imaginary_part() ** 2),
                                     ((self.number_1.get_imaginary_part() * self.number_2.get_real_part()) + (
                                             self.number_1.get_real_part() * self.number_2.get_imaginary_part())) / (
                                             self.number_2.get_real_part() ** 2 + self.number_2.get_imaginary_part() ** 2))
            else:
                self.result = "ERROR"
        elif mark == '^':
            self.result = Number(0, 0)
            self.result.set_angle_module((self.number_1.get_angle()) * (self.number_2.get_real_part()),
                                         self.number_1.module() ** int(self.number_2.get_real_part()))
        elif mark == 'r':
            self.root = []
            self.angle_first = self.number_1.get_angle() / int(self.number_2.get_real_part())
            self.module_number = self.number_1.module() ** (1 / int(self.number_2.get_real_part()))
            for i in range(0, int(self.number_2.get_real_part())):
                self.root.append(Number(0, 0))
                self.root[i].set_angle_module(
                    self.angle_first + ((2 * math.pi) / int(self.number_2.get_real_part())) * i, self.module_number)
            self.result = self.root
        else:
            self.result = "ERROR"

    def get_number_1(self):
        return self.number_1

    def get_number_2(self):
        return self.number_2

    def get_operation(self):
        return self.mark_

    def get_result(self):
        return self.result


def add_to_memory(operation_obj):
    global memory
    memory.append(operation_obj)
    if len(memory) > 10:
        memory.pop(0)


def clear_memory():
    global memory
    memory = []


def show_memory(result_index: int):
    global memory
    global first_number
    global witch_number
    global expression
    if len(memory) > result_index:
        temp = memory[result_index]
        if temp.get_result() == "ERROR":
            return "ERROR"
        if temp.get_operation() == "r":
            info = ""
            for i in range(0, len(temp.get_result())):
                info = info + str(i) + ":  " + str(temp.get_result()[i].get_real_part()) + "+i" + str(
                    temp.get_result()[i].get_imaginary_part()) + "\n"

            numba = int(test_message_boxx_root_choice(info))
            if numba >= len(temp.get_result()):
                expression = "ERROR"
                input_text.set(expression)
            else:
                input_text.set(expression)
                x_part = temp.get_result()[numba].get_real_part()
                y_part = temp.get_result()[numba].get_imaginary_part()
                expression = str(x_part) + "+i" + str(y_part)
                input_text.set(expression)
        else:
            if temp.get_result().get_imaginary_part() == 0:
                expression = str(temp.get_result().get_real_part())
            else:
                expression = str(temp.get_result().get_real_part()) + '+i' + str(temp.get_result().get_imaginary_part())
            input_text.set(expression)
    else:
        expression = "ERROR"
        input_text.set(expression)


def number_str_to_number(str_number):  ##dziala
    numba = Number(0, 0)
    x_param = 0
    y_param = 0
    if str_number.find("+i", 0) > 0:
        x_param = float(str_number[0:str_number.find("+i", 0)])
        y_param = float(str_number[str_number.find("+i", 0) + 2:])
        numba.set_both_parts(x_param, y_param)
    elif str_number.find("e^i(", 0) > 0:
        x_param = float(str_number[0:str_number.find("e^i(", 0)])
        y_param = float(str_number[str_number.find("e^i(", 0) + 4:])
        numba.set_angle_module(y_param, x_param)
    else:
        numba.set_both_parts(float(str_number), 0.0)
    return numba


def interpretation(first, second, mark):  ####dostaje string daje wynik
    number__1 = number_str_to_number(first)
    number__2 = number_str_to_number(second)
    print(number__1.get_real_part())
    oper = Operation(number__1, number__2, mark)
    add_to_memory(oper)  # juz naprawione

    if oper.result == "ERROR":
        return "ERROR"
    if mark != 'r':
        if oper.result.get_imaginary_part() == 0:
            return str(oper.result.get_real_part())
        return str(oper.result.get_real_part()) + "+i" + str(oper.result.get_imaginary_part())
    if mark == 'r':
        string_stream_like_in_cpluspus = ""
        for i in range(0, len(oper.get_result())):
            if oper.result[i].get_imaginary_part() == 0:
                string_stream_like_in_cpluspus = string_stream_like_in_cpluspus + str(i) + ":  " + str(
                    oper.get_result()[i].get_real_part()) + "\n"
            else:
                string_stream_like_in_cpluspus = string_stream_like_in_cpluspus + str(i) + ":  " + str(
                    oper.get_result()[i].get_real_part()) + "+i" + str(oper.get_result()[i].get_imaginary_part()) + "\n"

        test_message_boxx(string_stream_like_in_cpluspus)
        if oper.get_result()[0].get_imaginary_part() == 0:
            return str(oper.get_result()[0].get_real_part())
        return str(oper.get_result()[0].get_real_part()) + "+i" + str(oper.get_result()[0].get_imaginary_part())
    return "ERROR"  # do poprawy


def result_normal(nummber):
    return str(nummber.get_real_part()) + "+i" + str(nummber.get_imaginary_part())


global memory
memory = []
global if_first_after_equal
if_first_after_equal = 0
# GUI

main_window = Tk()
# wyglad okna
main_window.geometry("700x400")
main_window.title("Calcualtor")


def btn_click(item):  ####add to input
    global expression
    global if_first_after_equal
    if if_first_after_equal:
        expression = ""
        if_first_after_equal = 0
    expression = expression + str(item)
    input_text.set(expression)


def btn_clear():  ####clear input
    global expression
    global witch_number
    witch_number = 1
    expression = ""
    input_text.set("0")


def btn_equal():
    global if_first_after_equal
    global expression
    global first_number
    global mark
    global second_number
    global witch_number
    global result_temp
    second_number = expression
    if second_number != "":
        result_temp = str(interpretation(first_number, second_number, mark))
        first_number = result_temp
        witch_number = 1
        second_number = ""
        mark = ""
        input_text.set(result_temp)
        expression = result_temp
        if_first_after_equal = 1


def iore():
    global expression
    num = number_str_to_number(expression)
    expression = str(num.module()) + "e^i(" + str(num.get_angle())
    input_text.set(expression)


def etoi():
    global expression
    num = number_str_to_number(expression)
    expression = str(num.get_real_part()) + "+i" + str(num.get_imaginary_part())
    input_text.set(expression)


def number_input(item):
    global first_number
    global second_number
    global witch_number
    global mark
    global expression
    global result_temp
    if witch_number == 2:
        second_number = expression
        btn_equal()
        first_number = result_temp
        mark = item
        witch_number = 2

    if witch_number == 1:
        first_number = expression
        witch_number = 2
        mark = item
        expression = ""
        result = str(expression)
        input_text.set(result)


def test_message_boxx(info):
    messagebox.showinfo("wynik pierwiastek", info)


def test_message_boxx_root_choice(info):
    number = askstring("jaki wynik?", info)
    return int(number)


input_text = StringVar()
btn_clear()

# output text as string
# input text
# output text as string
# input text
input_frame = Frame(main_window, width=400, height=50, bd=0, highlightbackground="black", highlightcolor="black",
                    highlightthickness=1)
input_frame.pack(side=TOP)
input_field = Entry(input_frame, font=('times', 20, 'bold'), textvariable=input_text, width=50, bg="#eee", bd=0,
                    justify=RIGHT)
input_field.grid(row=0, column=0)
input_field.pack(ipady=10)

# buttons

btns_frame = Frame(main_window, width=312, height=272.5, bg="grey")
btns_frame.pack(side=LEFT)
######
clear = Button(btns_frame, text="C", fg="black", width=10, height=3, bd=0, bg="SILVER", cursor="hand2", font="times",
               activebackground="silver",
               command=lambda: btn_clear()).grid(row=0, column=0, padx=1, pady=1)
I = Button(btns_frame, text="zamien na: \n a+ib", fg="black", width=10, height=3, bd=0, bg="#eee", cursor="hand2",
           font="times",
           command=lambda: etoi()).grid(row=3, column=3, padx=1, pady=1)
E = Button(btns_frame, text="zamien na: \n exp(i)", fg="black", width=10, height=3, bd=0, bg="#eee", cursor="hand2",
           font="times",
           command=lambda: iore()).grid(row=2, column=3, padx=1, pady=1)
divide = Button(btns_frame, text="÷", fg="black", width=10, height=3, bd=0, bg="#eee", cursor="hand2", font="times",
                activebackground="silver",
                command=lambda: number_input("/")).grid(row=0, column=3, padx=1, pady=1)
######
seven = Button(btns_frame, text="7", fg="black", width=10, height=3, bd=0, bg="white", cursor="hand2", font="times",
               command=lambda: btn_click(7)).grid(row=1, column=0, padx=1, pady=1)
eight = Button(btns_frame, text="8", fg="black", width=10, height=3, bd=0, bg="white", cursor="hand2", font="times",
               command=lambda: btn_click(8)).grid(row=1, column=1, padx=1, pady=1)
nine = Button(btns_frame, text="9", fg="black", width=10, height=3, bd=0, bg="white", cursor="hand2", font="times",
              command=lambda: btn_click(9)).grid(row=1, column=2, padx=1, pady=1)
multiply = Button(btns_frame, text="*", fg="black", width=10, height=3, bd=0, bg="#eee", cursor="hand2", font="times",
                  activebackground="silver",
                  command=lambda: number_input("*")).grid(row=1, column=3, padx=1, pady=1)
######
four = Button(btns_frame, text="4", fg="black", width=10, height=3, bd=0, bg="white", cursor="hand2", font="times",
              command=lambda: btn_click(4)).grid(row=2, column=0, padx=1, pady=1)
five = Button(btns_frame, text="5", fg="black", width=10, height=3, bd=0, bg="white", cursor="hand2", font="times",
              command=lambda: btn_click(5)).grid(row=2, column=1, padx=1, pady=1)
six = Button(btns_frame, text="6", fg="black", width=10, height=3, bd=0, bg="white", cursor="hand2", font="times",
             command=lambda: btn_click(6)).grid(row=2, column=2, padx=1, pady=1)
minus = Button(btns_frame, text="-", fg="black", width=10, height=3, bd=0, bg="#eee", cursor="hand2", font="times",
               activebackground="silver",
               command=lambda: number_input("-")).grid(row=0, column=2, padx=1, pady=1)
######
one = Button(btns_frame, text="1", fg="black", width=10, height=3, bd=0, bg="white", cursor="hand2", font="times",
             command=lambda: btn_click(1)).grid(row=3, column=0, padx=1, pady=1)
two = Button(btns_frame, text="2", fg="black", width=10, height=3, bd=0, bg="white", cursor="hand2", font="times",
             command=lambda: btn_click(2)).grid(row=3, column=1, padx=1, pady=1)
three = Button(btns_frame, text="3", fg="black", width=10, height=3, bd=0, bg="white", cursor="hand2", font="times",
               command=lambda: btn_click(3)).grid(row=3, column=2, padx=1, pady=1)
plus = Button(btns_frame, text="+", fg="black", width=10, height=3, bd=0, bg="#eee", cursor="hand2", font="times",
              activebackground="silver",
              command=lambda: number_input("+")).grid(row=0, column=1, padx=1, pady=1)
######
Clear = Button(btns_frame, text='clear \n memory', fg="black", width=10, height=3, bd=0, bg="#eee", cursor="hand2",
               font="times", activebackground="silver",
               command=lambda: clear_memory()).grid(row=4, column=4, padx=1, pady=1)
zero = Button(btns_frame, text="0", fg="black", width=10, height=3, bd=0, bg="white", cursor="hand2", font="times",
              command=lambda: btn_click(0)).grid(row=4, column=1, padx=1, pady=1)
point = Button(btns_frame, text=".", fg="black", width=10, height=3, bd=0, bg="#eee", cursor="hand2", font="times",
               activebackground="silver",
               command=lambda: btn_click(".")).grid(row=4, column=2, padx=1, pady=1)
equals = Button(btns_frame, text="=", fg="black", width=10, height=3, bd=0, bg="#eee", cursor="hand2", font="times",
                activebackground="silver",
                command=lambda: btn_equal()).grid(row=4, column=3, padx=1, pady=1)
####
root = Button(btns_frame, text="√", fg="black", width=10, height=3, bd=0, bg="#eee", cursor="hand2", font="times",
              activebackground="silver",
              command=lambda: number_input("r")).grid(row=0, column=4, padx=1, pady=1)
power = Button(btns_frame, text="xʸ", fg="black", width=10, height=3, bd=0, bg="#eee", cursor="hand2", font="times",
               activebackground="silver",
               command=lambda: number_input("^")).grid(row=1, column=4, padx=1, pady=1)
i_button = Button(btns_frame, text="+ i", fg="black", width=10, height=3, bd=0, bg="#eee", cursor="hand2", font="times",
                  activebackground="silver",
                  command=lambda: btn_click("+i")).grid(row=3, column=4, padx=1, pady=1)
i_to_e = Button(btns_frame, text="e\u2071\u1D43", fg="black", width=10, height=3, bd=0, bg="#eee", cursor="hand2",
                font="times", activebackground="silver",
                command=lambda: btn_click("e^i(")).grid(row=2, column=4, padx=1, pady=1)
plusminus = Button(btns_frame, text="+/-", fg="black", width=10, height=3, bd=0, bg="#eee", cursor="hand2",
                   font="times",
                   command=lambda: btn_click('-')).grid(row=4, column=0, padx=1, pady=1)
###memory
btng_frame = Frame(main_window, width=500, height=300, bg="grey")
btng_frame.pack(side=RIGHT)
M1 = Button(btng_frame, text="M1", fg="black", width=10, height=3, bd=0, bg="silver", cursor="hand2", font="times",
            command=lambda: show_memory(0)).grid(row=0, column=6, padx=1, pady=1)
M2 = Button(btng_frame, text="M2", fg="black", width=10, height=3, bd=0, bg="silver", cursor="hand2", font="times",
            command=lambda: show_memory(1)).grid(row=0, column=7, padx=1, pady=1)
M3 = Button(btng_frame, text="M3", fg="black", width=10, height=3, bd=0, bg="silver", cursor="hand2", font="times",
            command=lambda: show_memory(2)).grid(row=1, column=6, padx=1, pady=1)
M4 = Button(btng_frame, text="M4", fg="black", width=10, height=3, bd=0, bg="silver", cursor="hand2", font="times",
            command=lambda: show_memory(3)).grid(row=1, column=7, padx=1, pady=1)
M5 = Button(btng_frame, text="M5", fg="black", width=10, height=3, bd=0, bg="silver", cursor="hand2", font="times",
            command=lambda: show_memory(4)).grid(row=2, column=6, padx=1, pady=1)
M6 = Button(btng_frame, text="M6", fg="black", width=10, height=3, bd=0, bg="silver", cursor="hand2", font="times",
            command=lambda: show_memory(5)).grid(row=2, column=7, padx=1, pady=1)
M7 = Button(btng_frame, text="M7", fg="black", width=10, height=3, bd=0, bg="silver", cursor="hand2", font="times",
            command=lambda: show_memory(6)).grid(row=3, column=6, padx=1, pady=1)
M8 = Button(btng_frame, text="M8", fg="black", width=10, height=3, bd=0, bg="silver", cursor="hand2", font="times",
            command=lambda: show_memory(7)).grid(row=3, column=7, padx=1, pady=1)
M9 = Button(btng_frame, text="M9", fg="black", width=10, height=3, bd=0, bg="silver", cursor="hand2", font="times",
            command=lambda: show_memory(8)).grid(row=4, column=6, padx=1, pady=1)
M10 = Button(btng_frame, text="M10", fg="black", width=10, height=3, bd=0, bg="silver", cursor="hand2", font="times",
             command=lambda: show_memory(9)).grid(row=4, column=7, padx=1, pady=1)

main_window.mainloop()
# END GUI
