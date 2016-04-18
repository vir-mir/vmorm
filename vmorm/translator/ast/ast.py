# -*- coding: utf-8 -*-

__all__ = ['BaseAst', 'Build', 'Function']


class Node(object):
    def __init__(self, ast):
        self.ast = ast


class BaseAst(object):
    def __init__(self, val, *args, **kwargs):
        self.val = val
        self.context = self.set(*args, **kwargs)

    def set(self, *args, **kwargs):
        return Node(kwargs) if not any(args) else args[0]

    def get_pre_sql(self, key):
        return self

    def __str__(self):
        return self.val


class Build(BaseAst):
    pass


class Function(BaseAst):
    pass
