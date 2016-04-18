# -*- coding: utf-8 -*-
import dis
import sys

from byteplay3 import Code

from vmorm.translator import settings
from vmorm.translator.driver.db import DBDriverException, DBDriver
from vmorm.translator.stack import Stack


class Parser(object):
    def __get_local_and_global(self, generator, *, frame):
        locals_ = {}
        locals_.update(sys._getframe(frame).f_locals)
        globals_ = generator.gi_frame.f_globals
        locals_.update(generator.gi_frame.f_locals)
        return locals_, globals_

    def __visitor(self, generator, driver, locals_, globals_):
        stack = Stack(locals_=locals_, globals_=globals_)
        code = Code.from_code(generator.gi_frame.f_code)
        dis.dis(generator.gi_frame.f_code)
        for cmd, arg in code.code:
            cmd = cmd.__str__().lower()
            if hasattr(stack, cmd):
                cmd = getattr(stack, cmd)
                cmd(arg)
        return stack.get_sql(driver=driver)

    def find(self, generator, *, driver, frame):
        frame += 1
        return self.__visitor(
            generator,
            driver,
            *self.__get_local_and_global(generator, frame=frame)
        )

    @classmethod
    def select(cls, generator, *, driver=None):
        driver = driver or settings.DRIVER

        if DBDriver in driver.mro():
            return cls().find(generator, driver=driver, frame=1)
        else:
            raise DBDriverException


select = Parser.select
