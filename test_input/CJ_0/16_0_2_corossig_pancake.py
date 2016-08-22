#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys

for caseno, line in enumerate(open("test.in", "r").readlines()[1:]) :
    pancakes=line.strip()

    # Add + at end to force flip on last - if any
    pancakes = pancakes + "+"

    prec = None
    nb = 0
    for p in pancakes :
        if p != prec :
            nb += 1
            prec = p

    print("Case #%d: %s" % (caseno+1, nb-1))
