# -*- coding: utf-8 -*-

from vmorm.translator.ast.ast import BaseAst

__all__ = ['Load']


class Load(BaseAst):
    def set(self, *args, **kwargs):

        if '.0' == self.val and kwargs.get('local'):
            return list(kwargs.get('local').get(self.val))
        elif kwargs.get('local'):
            return kwargs.get('local').get(self.val)
        elif kwargs.get('fast'):
            return kwargs.get('fast')
        elif kwargs.get('glob'):
            return kwargs.get('glob').get(self.val)
        else:
            return super(Load, self).set(*args, **kwargs)
