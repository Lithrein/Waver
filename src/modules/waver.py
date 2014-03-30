#!/usr/bin/python2.7
# -*- coding: utf-8 -*-


class Waver:
    def __init__(self, pieces, properties, tracker, pieces_sz):
        self.pieces = pieces
        self.properties = properties
        self.tracker = tracker
        self.hashes = pieces.extract_hashes()
        self.nb_pieces = self.hashes
        self.pieces_sz = pieces_sz

    def __str__(self):
        ret = "\n"

        ret += ":begin properties\n"
        for const, value in self.properties:
            ret += str(const) + '=' + str(value) + '\n'
        ret += ":end properties\n"

        ret += "\n:begin tracker\n"
        for ip in self.tracker:
            ret += str(ip) + '\n'
        ret += ":end tracker\n"

        ret += "\n:begin pieces\n"
        ret += self.pieces.pretty_print() + '\n'
        ret += ":end pieces\n"

        ret += "\n:begin hash\n"
        for md5hash in self.hashes:
            ret += str(md5hash) + '\n'
        ret += ":end hash"

        return ret
