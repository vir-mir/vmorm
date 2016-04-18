# -*- coding: utf-8 -*-
from vmorm.translator.parser import select


class AMeta(type):
    def __iter__(self):
        s = [self]
        return iter(s)


class Slots(metaclass=AMeta):
    slot = 15
    year = 2016
    fio = 'Firsov'

    def __iter__(self):
        return [self]


class Slots1(metaclass=AMeta):
    slot = 15
    year = 2016
    fio = 'Firsov'

    def __iter__(self):
        return [self]


class Slots3(metaclass=AMeta):
    slot = 15
    year = 2016
    fio = 'Firsov'

    def __iter__(self):
        return [self]


year = 2014


def ddd(sl=203):
    fio = 'He'
    select([slot_obj, slot_obj2, slo] for slot_obj, slot_obj2, slo in [Slots, Slots1, Slots3]
           if slot_obj.year == year
           and slot_obj.fio.startswith(fio)
           and slot_obj.fio.startswith('He')
           and slot_obj.fio.startswith('He')
           or slot_obj.year in [year, 130, slot_obj2.year]
           or slot_obj.slot is False
           or slot_obj.slot is not None
           or slot_obj.slot > sl
           or slot_obj.slot == (slot_obj.slot+slot_obj.slot)
           or slot_obj.slot == (fio*23)
           or slot_obj.slot == (fio+fio)
           or slot_obj.slot == (''.join([[fio]][0]+[fio]))
           or slot_obj.slot == (slot_obj.slot/slot_obj.slot)
           or slot_obj.slot == (slot_obj.slot-slot_obj.slot)
           or slot_obj.slot == (slot_obj.slot//slot_obj.slot)
           or slot_obj.slot == (slot_obj.slot**slot_obj.slot)
           or slot_obj.slot == (round(slot_obj.slot*slot_obj.slot, 5))
           or slot_obj.slot >= sl
           )


if __name__ == '__main__':
    ddd()
