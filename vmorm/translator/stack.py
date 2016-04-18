# -*- coding: utf-8 -*-

from vmorm.translator.ast import *


class Stack(list):
    """
    Stack revers
    """
    locals_ = {}
    globals_ = {}

    def __init__(self, locals_=None, globals_=None, *args, **kwargs):
        self.globals_ = globals_ or {}
        self.locals_ = locals_ or {}
        self.fast = {}
        self.val = None
        super(Stack, self).__init__(*args, **kwargs)

    def add(self, item):
        if item is not None:
            return super(Stack, self).append(item)

    def binary_add(self, _):
        self.add(Binary('+', left=self.pop(), right=self.pop()))

    def binary_multiply(self, _):
        self.add(Binary('*', left=self.pop(), right=self.pop()))

    def binary_true_divide(self, _):
        self.add(Binary('/', left=self.pop(), right=self.pop()))

    def binary_subtract(self, _):
        self.add(Binary('-', left=self.pop(), right=self.pop()))

    def binary_subscr(self, _):
        self.add(Binary('subscr', left=self.pop(), right=self.pop()))

    def binary_floor_divide(self, _):
        self.add(Binary('//', left=self.pop(), right=self.pop()))

    def binary_power(self, _):
        self.add(Binary('*', left=self.pop(), right=self.pop()))

    def load_const(self, const):

        self.add(Load(const, self.pop()))

    def pop_jump_if_false(self, _):
        self.add(Pop('if', self.list_(len(self))))

    def pop_top(self, _):
        self.add(Pop('top', self.list_(len(self))))

    def call_function(self, count):
        self.add(Function('call', self.list_(count)))

    def load_attr(self, attr):
        self.add(Load(attr, self.pop()))

    def compare_op(self, op):
        self.add(Compare(op, left=self.pop(), right=self.pop()))

    def load_global(self, glob):
        self.add(Load(glob, glob=self.globals_))

    def load_deref(self, fast):
        self.add(Load(fast, local=self.locals_))

    def store_fast(self, fast):
        top_item_stack = self.pop()
        self.fast[fast] = top_item_stack.context.pop(0)
        if any(top_item_stack.context):
            self.add(top_item_stack)

    def list_(self, count):
        return [self.pop() for _ in range(count)]

    def get_sql(self, driver):
        return driver(self.pop()).get_sql()

    def build_list(self, count):
        list_ = Build('list', self.list_(count))
        self.add(list_)

    def load_fast(self, fast):
        load = Load(fast, local=self.locals_)
        if load.context:
            self.add(load)
        else:
            self.add(Load(fast, fast=self.fast[fast]))
