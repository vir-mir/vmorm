# -*- coding: utf-8 -*-
from pprint import pprint

from vmorm.translator.ast import BaseAst

__all__ = ['DBDriver', 'DBDriverException']


class DBDriverException(Exception):
    pass


class Recursion(object):
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        result = self.func(*args, **kwargs)
        while callable(result):
            result = result()
        return result

    def call(self, *args, **kwargs):
        return lambda: self.func(*args, **kwargs)


class DBDriver(object):
    def __init__(self, ast):
        self.ast = ast

    def get_context(self, node, key=None):
        if hasattr(node, 'context'):
            context = getattr(node, 'context')
            if isinstance(context, BaseAst):
                return context.get_pre_sql(key)
            return context
        return node

    def tree_context(self, node):
        context = self.get_context(node)
        if type(context) in [tuple, list]:
            context = [self.tree_context(self.get_context(i)) for i in context]
        elif isinstance(context, BaseAst):
            context = self.tree_context(context)

        return context

    def get_sql(self):
        pprint(self.tree_context(self.ast))
