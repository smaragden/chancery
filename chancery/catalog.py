#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'fredrik.brannbacka'
from user import User


class Catalog(object):
    __domain = ""

    def __init__(self, domain=""):
        self.__domain = domain

    @property
    def domain(self):
        return self.__domain

    @domain.setter
    def domain(self, domain):
        self.__domain = domain

    def register(self, name=u"John Doe"):
        user = User(name.decode('utf-8'), self.domain)
        return user

    def register_users(self, names=[]):
        for name in names:
            user = User(name.decode('utf-8'), self.domain)
            yield user

