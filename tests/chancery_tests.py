#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'fredrik.brannbacka'
from chancery import Catalog


def test_normal_name():
    catalog = Catalog("example.com")
    user = catalog.register("Fredrik Brännbacka")
    assert user.name == "Fredrik Brännbacka"
    assert user.short_name == "frbr"
    assert user.ascii_name == "Fredrik Brannbacka"
    assert user.login == "fredrik.brannbacka"
    assert user.email == "fredrik.brannbacka@example.com"
    assert user.id != ""
    #assert repr(user) == "<class 'chancery.user.User'>(Fredrik Brännbacka, fb, frbr, fredrik.brannbacka fredrik.brannbacka@example.com, f800499b-9128-522d-a7f5-b1f3610354e2)"


def test_short_name():
    catalog = Catalog(domain="example.com")
    user = catalog.register("Köngen")
    assert user.name == "Köngen"
    assert user.short_name == "kong"
    assert user.ascii_name == "Kongen"
    assert user.login == "kongen"
    assert user.email == "kongen@example.com"
    assert user.id != ""
    #assert repr(user) == "<class 'chancery.user.User'>(Köngen, k, kong, kongen kongen@example.com, bc61db0b-4a65-5274-9189-38bca4371c8c)"


def test_long_name():
    catalog = Catalog()
    catalog.domain = "example.com"
    user = catalog.register("Örjan Samuel Wärnström")
    assert user.name == "Örjan Samuel Wärnström"
    assert user.short_name == "orwa"
    assert user.ascii_name == "Orjan Samuel Warnstrom"
    assert user.login == "orjan.warnstrom"
    assert user.email == "orjan.warnstrom@example.com"
    assert user.id != ""
    #assert repr(user) == "<class 'chancery.user.User'>(Örjan Samuel Wärnström, osw, orwa, orjan.warnstrom orjan.warnstrom@example.com, 13eee80b-0e7e-5383-8d8c-a66da487c832)"


def test_multiple_names():
    catalog = Catalog()
    catalog.domain = "example.com"
    for user in catalog.register_users(["Fredrik Brännbacka", "Köngen", "Örjan Samuel Wärnström"]):
        print user.as_json()
