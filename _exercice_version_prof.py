#!/usr/bin/env python
# -*- coding: utf-8 -*-

from turtle import *
import re


def valide(saisie):
    """
    if len(saisie) != 0:
        return set(saisie).issubset("atgc")

    return False
    """

    return bool(re.match("^[atgc]+$", saisie))


def saisie(type):
    value = input(f"Entrez une {type} d'ADN valide: ")

    if valide(value):
        return value

    print(f"La {type} n'est pas valide")
    return saisie(type)


def proportion(chain, sequence):

    return chain.count(sequence) / len(chain)


def check_dna():
    chain = saisie("chaine")
    sequence = saisie("sequence")

    prop = proportion(chain, sequence)
    print("Il y a {0:.2f} % de {1}.".format(prop*100, sequence))


def draw_branch(branch_len, pen_size, angle):
    if branch_len > 0 and pen_size > 0:
        pensize(pen_size)
        forward(branch_len)
        right(angle)
        draw_branch(branch_len - 10, pen_size - 1, angle - 5)
        left(angle * 2)
        draw_branch(branch_len - 10, pen_size - 1, angle - 5)
        right(angle)
        backward(branch_len)


def draw_tree():
    setheading(90)
    color("green")
    draw_branch(70, 7, 35)
    done()


if __name__ == '__main__':
    # TODO: Appelez vos fonctions ici
    check_dna()
    draw_tree()


