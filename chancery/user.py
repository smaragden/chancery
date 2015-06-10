#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'fredrik.brannbacka'
import uuid
import unicodedata
try:
    import simplejson as json
except:
    import json

class User(object):
    def __init__(self, name=u"", domain="example.com"):
        self.__name = name
        self.__domain = domain
        self.__uuid = uuid.uuid5(uuid.NAMESPACE_DNS, self.name+self.__domain)

    @property
    def id(self):
        return str(self.__uuid)

    @property
    def name(self):
        return self.__name.encode('utf-8')

    @property
    def ascii_name(self):
        return unicodedata.normalize('NFKD', self.__name).encode('ascii', 'ignore')

    @property
    def initials(self):
        return ''.join([token.lower()[0] for token in self.ascii_name.split(' ')])

    @property
    def short_name(self, num_chars=4):
        name_tokens = [token.lower() for token in self.ascii_name.split(' ')]
        if len(name_tokens) > 1:
            return name_tokens[0][:(num_chars/2)]+name_tokens[-1][:(num_chars/2)]
        else:
            return self.ascii_name[:num_chars].lower()

    @property
    def login(self):
        ascii_name = unicodedata.normalize('NFKD', self.__name).encode('ascii','ignore')
        name_tokens = [token.lower() for token in ascii_name.split(' ')]
        if len(name_tokens) > 2:
            return '.'.join([name_tokens[0], name_tokens[-1]])
        else:
            return '.'.join(name_tokens)

    @property
    def email(self):
        return "{user.login}@{domain}".format(user=self, domain=self.__domain)

    def as_json(self):
        return json.dumps({
            'name': self.name,
            'ascii_name': self.ascii_name,
            'id': self.id,
            'initials': self.initials,
            'short_name': self.short_name,
            'login': self.login,
            'email': self.email
        })

    def __repr__(self):
        return "%s(%r)" % (self.__class__, self.__dict__)

    def __str__(self):
        user_str = self.__name.encode('utf-8')
        return user_str

