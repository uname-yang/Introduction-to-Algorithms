#python
#coding=utf-8
from Stack import Stack
from Queue import Queue


class RailExpress():
    def __init__(self, express):
        self.fontExpress = express
        self.railExpress = []
        self.size = len(express)
        self.stack = Stack()
        self.queue = Queue()

        self.level = {'+': 1, '-':  1, '*': 2, '/': 2, '(': 3, ')': 3}
        self.operators = ['+', '-', '*', '/', '(', ')']

        self.makeRailExpress()

    def makeRailExpress(self):
        for i in self.fontExpress:
            if i in self.operators:
                if i is self.operators[-1]:
                    ele = self.stack.pop()

                    while ele is not self.operators[-2]:
                        self.queue.push(ele)
                        ele = self.stack.pop()

                        if self.stack.isEmpty():
                            break

                elif i is self.operators[-2]:
                    self.stack.push(i)

                else:
                    if not self.stack.isEmpty():
                        while self.stack.returnFristEle() is not self.operators[-2] and self.level[self.stack.returnFristEle()] >= self.level[i]:
                            ele = self.stack.pop()
                            self.queue.push(ele)

                            if self.stack.isEmpty():
                                break

                    self.stack.push(i)
            else:
                self.queue.push(i)

        if not self.stack.isEmpty():
            stack = self.stack.returnStack()
            stack.reverse()
            self.queue.returnQueue().extend(stack)


class CheckExpress():
    def __init__(self, express):
        if len(express) > 10000:
            sys.exit(0)
        self.express = express

    def checkExpress(self):
        express = []
        count = -1

        for each in self.express:
            if (each >= '0') and (each <= '9') or (each == '.'):
                length = len(express)
                if length == 0:
                    express.append(each)
                    count += 1

                elif (express[count] >= '0') and (express[count] <= '999999') or (each == '.'):
                    length = len(express)
                    express[length - 1] = express[length - 1] + each
                else:
                    express.append(each)
                    count += 1
            else:
                if each == '+' or each == '-' or each == '*' or each == '/' or each == '(' or each == ')':
                    express.append(each)
                    count += 1

        return express


class Calculator():
    def __init__(self, express):
        self.express = express
        size = len(express)
        self.stack = Stack(size)
        self.result = None

        self.operatorRailExpress()

    def operatorRailExpress(self):
        for each in self.express:
            if (each >= '0') and (each <= '999999'):
                self.stack.push(each)

            else:
                twoOperator = self.stack.pop()
                oneOperator = self.stack.pop()
                temp = self.calculator(oneOperator, twoOperator, each)

                self.stack.push(temp)

        self.result = self.stack.returnFristEle()

    def calculator(self, one, two, operator):
        operatorDict = {'+': self.plus, '-': self.reduction, '*': self.multiplicate, '/': self.devision}
        temp = operatorDict[operator](one, two)

        return temp

    def plus(self, one, two):
        return float(one)+float(two)

    def reduction(self, one, two):
        return float(one)-float(two)

    def multiplicate(self, one, two):
        return float(one)*float(two)

    def devision(self, one, two):
        return float(one)/float(two)


class ConnectView():
    def __init__(self, model):
        self._model = model

    def calculator(self):
        express = CheckExpress(self._model.result).checkExpress()
        if len(express) == 1:
            sys.exit(0)

        rail = RailExpress(express)
        queue = rail.queue.returnQueue()
        if len(queue) == 1:

            sys.exit(0)
        calculate = Calculator(queue)
        self._model.result = str(calculate.result)

import sys
if __name__ == '__main__':
    express = raw_input('输入表达式：')

    express = CheckExpress(express).checkExpress()
    if len(express) == 1:
        sys.exit(0)

    rail = RailExpress(express)
    queue = rail.queue.returnQueue()
    if len(queue) == 1:
        print int(queue[0])
        sys.exit(0)
    calculate = Calculator(queue)
    print calculate.result