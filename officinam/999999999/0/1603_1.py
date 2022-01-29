#!/usr/bin/env python3
# ==============================================================================
#
#          FILE:  1603_1.py
#
#         USAGE:  ./999999999/0/1603_1.py
#                 ./999999999/0/1603_1.py --help
#                 NUMERORDINATIO_BASIM="/dir/ndata" ./999999999/0/1603_1.py
#
#   DESCRIPTION:  ---
#
#       OPTIONS:  ---
#
#  REQUIREMENTS:  - python3
#          BUGS:  ---
#         NOTES:  ---
#       AUTHORS:  Emerson Rocha <rocha[at]ieee.org>
# COLLABORATORS:
#                 <@TODO: put additional non-anonymous names here>
#
#       COMPANY:  EticaAI
#       LICENSE:  Public Domain dedication or Zero-Clause BSD
#                 SPDX-License-Identifier: Unlicense OR 0BSD
#       VERSION:  v0.5.0
#       CREATED:  2022-01-27 17:07 UTC created. Based on 1603_3_12.py
#      REVISION:  ---
# ==============================================================================

# pytest
#    python3 -m doctest ./999999999/0/1603_1.py

__EPILOGUM__ = """
Exemplōrum gratiā:
    printf "#item+conceptum+codicem,#item+rem+i_qcc+is_zxxx+ix_wikiq" | \
{0} --de-archivum
    cat 1603/1/1/1603_1_1.no1.tm.hxl.csv | \
{0} --de-archivum
    {0} --de-archivum 1603/1/1/1603_1_1.no1.tm.hxl.csv

    {0} ./999999999/0/1603_1.py --dictionaria-numerordinatio

    {0} ./999999999/0/1603_1.py --codex-de 1603_25_1

""".format(__file__)


import os
import sys
import argparse
# from pathlib import Path
from typing import (
    Type,
    Union
)

import urllib.parse
import requests

# from itertools import permutations
from itertools import product
# valueee = list(itertools.permutations([1, 2, 3]))
import csv

NUMERORDINATIO_BASIM = os.getenv('NUMERORDINATIO_BASIM', os.getcwd())
NUMERORDINATIO_DEFALLO = int(os.getenv('NUMERORDINATIO_DEFALLO', '60'))  # �
NUMERORDINATIO_MISSING = "�"
DESCRIPTION = """
Explain the dictionaries
"""

# In Python2, sys.stdin is a byte stream; in Python3, it's a text stream
STDIN = sys.stdin.buffer

# print('getcwd:      ', os.getcwd())
# print('oi', NUMERORDINATIO_BASIM)


# def quod_1613_2_60_datum():
#     datum = {}
#     with open(NUMERORDINATIO_BASIM + "/1613/1603.2.60.no1.tm.hxl.tsv") as file:
#         tsv_file = csv.DictReader(file, delimiter="\t")
#         return list(tsv_file)

# a b aa bb
# printf "30160\n31161\n1830260\n1891267\n" | ./999999999/0/2600.py --actionem-decifram

# a aa aaa
# printf "30160\n1830260\n109830360\n" | ./999999999/0/2600.py --actionem-decifram
# ./999999999/0/1603_1.py --actionem-quod-sparql


# SELECT ?item ?itemLabel
# WHERE {
#   # A. Einstein or J.S. Bach
#   VALUES ?item { wd:Q1065 wd:Q82151 wd:Q125761 wd:Q7809}
#   # mother of
#   OPTIONAL { ?item wdt:P25 ?pseudoquery. }
#   SERVICE wikibase:label { bd:serviceParam wikibase:language "[AUTO_LANGUAGE],en". }
# }

class Codex:
    def __init__(self, de_codex: str):

        self.de_codex = de_codex
        self.dictionaria_linguarum = DictionariaLinguarum()


class DictionariaLinguarum:
    def __init__(self, fontem_archivum: str = None):
        if fontem_archivum:
            self.D1613_1_51_fontem = self._init_1613_1_51_datum(
                fontem_archivum)
        else:
            self.D1613_1_51_fontem = NUMERORDINATIO_BASIM + \
                "/1603/1/51/1603_1_51.no1.tm.hxl.csv"

        self.dictionaria_codex = self._init_dictionaria()

    def _init_dictionaria(self):

        datum = {}
        with open(self.D1613_1_51_fontem) as file:
            csv_file = csv.DictReader(file)
            # return list(tsv_file)
            for conceptum in csv_file:
                # print('conceptum', conceptum)
                int_clavem = int(conceptum['#item+conceptum+codicem'])
                datum[int_clavem] = {}
                for clavem, rem in conceptum.items():
                    if not clavem.startswith('#item+conceptum+codicem'):
                        datum[int_clavem][clavem] = rem
        return datum

    def quod(self, terminum: str,
             #  factum: str = '#item+rem+i_lat+is_latn',
             clavem: str = None):
        clavem_defallo = [
            '#item+rem+i_qcc+is_zxxx+ix_hxla',
            '#item+rem+i_qcc+is_zxxx+ix_csvsffxm'
        ]
        _clavem = clavem_defallo if clavem is None else [clavem]
        # _clavem = clavem_defallo

        for item in _clavem:
            # print('item', item)
            for _k, linguam in self.dictionaria_codex.items():
                # print('linguam', linguam)
                if terminum.find(linguam[item]) > -1:
                    # return linguam[factum]
                    return linguam

        return None


class DictionariaNumerordinatio:
    def __init__(self):
        self.dictionaria_linguarum = DictionariaLinguarum()

    def _basim(self) -> list:
        resultatum = []
        # ix_regexc | ix_regexvdc | ix_hxlt | ix_hxla | i_mul+is_zyyy
        resultatum.append([
            '{{1603_13_1_2}}',  # hxlhashtag
            '',
            '',
            '',
            '',
            '',
            '',
            '',
            '[Rēgula expressiōnī cōnstrūctae (HXL Standard Tag)]',
            ''
        ])
        resultatum.append([
            '{{1603_13_1_3}}',  # HXL Standard attributes
            '',
            '',
            '',
            '',
            '',
            '',
            '',
            '[Rēgula expressiōnī cōnstrūctae (HXL Standard attributes)]',
            ''
        ])
        resultatum.append([
            '{{1603_13_1_23}}',  # Trivia: ('2' + '3')
            '',
            '',
            '',
            '',
            '',
            '',
            '',
            '[Rēgula expressiōnī cōnstrūctae (HXL Standard composed prefix, Hashtag + attributes)]',
            ''
        ])
        resultatum.append([
            '{{1603_13_1_3_9}}',  # i_ attribute; Trivia: [9] I = 9
            '{{1603_13_1_3}}',  # HXL Standard attributes
            '',
            '',
            '',
            '',
            '',
            '',
            '[Rēgula expressiōnī cōnstrūctae (HXL Standard attributes, language +i_)]',
            ''
        ])
        resultatum.append([
            '{{1603_13_1_3_19}}',  # is_ attribute; Trivia: [19] S = 19
            '{{1603_13_1_3}}',  # HXL Standard attributes
            '',
            '',
            '',
            '',
            '',
            '',
            '[Rēgula expressiōnī cōnstrūctae (HXL Standard attributes, writting system +is_)]',
            ''
        ])
        resultatum.append([
            '{{1603_13_1_3_24}}',  # ix_ attribute; Trivia: [24] X = 24
            '{{1603_13_1_3}}',  # HXL Standard attributes
            '',
            '',
            '',
            '',
            '',
            '',
            '[Rēgula expressiōnī cōnstrūctae (HXL Standard attributes, +ix_)]',
            ''
        ])
        resultatum.append([
            # i_zzz + ix_zzzz attribute; [919] I(9) + S(19)
            '{{1603_13_1_3_919}}',
            '{{1603_13_1_3}}',  # HXL Standard attributes
            '',
            '',
            '',
            '',
            '',
            '',
            '[Rēgula expressiōnī cōnstrūctae (HXL Standard attributes, +i_zzz+is_zzzz)]',
            ''
        ])
        resultatum.append([
            # i_zzz + ix_zzzz attribute; [91924] I(9) + S(19) + X (24)
            '{{1603_13_1_23_91924}}',
            '{{1603_13_1_23}}',
            '',  # '1',
            '',  # '1',
            '',
            '',
            '',
            '',
            '[Rēgula expressiōnī cōnstrūctae (HXL Standard composed prefix #hashtag+rem+i_zzz+is_zzzz+ix_zzzzzzz)]',
            ''
        ])
        resultatum.append([
            '',
            '{{1603_13_1_2}}',
            '',
            '',
            '',
            '#item',
            '',
            '',
            '[Factum ad Rēgula expressiōnī cōnstrūctae (HXL Standard Tag)]',
            ''
        ])
        resultatum.append([
            '',
            '{{1603_13_1_2}}',
            '',
            '',
            '',
            '#status',
            '',
            '',
            '[Status ad Rēgula expressiōnī cōnstrūctae (HXL Standard Tag)]',
            ''
        ])
        resultatum.append([
            '',
            '{{1603_13_1_2}}',
            '',
            '',
            '',
            '#meta',
            '',
            '',
            '[Meta ad Rēgula expressiōnī cōnstrūctae (HXL Standard Tag)]',
            ''
        ])

        # resultatum.append([
        #     '{{1603_13_1_23}}',  # hxlhashtag + attribute, specific with ix_*
        #     '',
        #     '',
        #     '',
        #     '',
        #     '',
        #     '',
        #     '',
        #     '[Rēgula expressiōnī cōnstrūctae (HXL Standard composed prefix, Hashtag + attributes)]',
        # ])
        resultatum.append([
            '{{1603_13_1_23_3}}',  # [3] C (concept)
            '{{1603_13_1_23}}',
            '1',
            '',
            '',
            '',
            '',
            '',
            '/Concept level information/',
            ''
        ])
        resultatum.append([
            '{{1603_13_1_23_3_10}}',  # 10 local identifier (1), no variant (0)
            '{{1603_13_1_23_3}}',
            '1',
            '',
            '',
            '#item',
            'conceptum+codicem',
            '#item+conceptum+codicem',
            '/Concept level information, local identifier/',
            ''
        ])
        resultatum.append([
            '{{1603_13_1_23_3_11}}',  # [11] local identifier (1), status (1)
            '{{1603_13_1_23_3}}',
            '1',
            '',
            '',
            '#status',
            'conceptum+codicem',
            '#status+conceptum+codicem',
            '/Educated guess on stability (1-100) of local identifier/',
            ''
        ])
        resultatum.append([
            '{{1603_13_1_23_3_18}}',  # [11] local identifier (1), metadata (8)
            '{{1603_13_1_23_3}}',
            '1',
            '',
            '',
            '#meta',
            'conceptum+codicem',
            '#meta+conceptum+codicem',
            '/Concept level information, local identifier, metadata/',
            ''
        ])
        resultatum.append([
            '{{1603_13_1_23_3_21}}',
            '{{1603_13_1_23_3}}',
            '1',
            '',
            '',
            '#status',
            'conceptum+definitionem',
            '#status+conceptum+definitionem',
            '/Educated guess on comprehensibility (1-100) of concept/',
            ''
        ])
        resultatum.append([
            '{{1603_13_1_23_91924_26}}',  # [26] Z, external, end of alphabet
            '{{1603_13_1_23_91924}}',
            '1',
            '',
            '',
            '#item',
            'rem+i_qcc+is_zxxx+{{1603_13_1_3_24}}',
            '#item+rem+i_qcc+is_zxxx+{{1603_13_1_3_24}}',
            '/Concept level information, external identifier/',
            ''
        ])
        resultatum.append([
            '{{1603_13_1_23_919}}',
            '{{1603_13_1_23}}',
            '0',
            '1',
            '1',
            '',
            'rem+{{1603_13_1_3_919}}',
            '',
            '/Language and term level information, any type/',
            ''
        ])
        resultatum.append([
            '{{1603_13_1_23_919_1}}',
            '{{1603_13_1_23_919}}',
            '0',
            '0',
            '1',
            '#item',
            'rem+{{1603_13_1_3_919}}',
            '#item+rem+{{1603_13_1_3_919}}',
            '/Language level information, local human label/',
            ''
        ])
        resultatum.append([
            '{{1603_13_1_23_919_13}}',  # [13] M
            '{{1603_13_1_23_919}}',
            '0',
            '0',
            '1',
            '#meta',
            'rem+{{1603_13_1_3_919}}',
            '#meta+rem+{{1603_13_1_3_919}}',
            '/Metadata about the local human label/',
            ''
        ])
        resultatum.append([
            '{{1603_13_1_23_919_19}}',  # Trivia: [19] S, status
            '{{1603_13_1_23_919}}',
            '0',
            '0',
            '1',
            '#status',
            'rem+{{1603_13_1_3_919}}',
            '#status+rem+{{1603_13_1_3_919}}',
            '/Educated guess on reliability (1-100) of the local human label/',
            ''
        ])
        return resultatum

    def _basim_extras(self) -> list:
        resultatum = []
        resultatum.append([
            # https://www.wikidata.org/wiki/Wikidata:Glossary#QID
            # 13_12 is used for Community knowledge/Wikidata
            # 13_12_16 : [16] P
            '{{1603_13_1_23_91924_26_13_12_16}}',
            '{{1603_13_1_23_91924_26}}',
            '1',
            '0',
            '0',
            '#item',
            'rem+i_qcc+is_zxxx+ix_wikiq',
            '#item+rem+i_qcc+is_zxxx+ix_wikiq',
            '/Wikidata, QID/',
            'https://www.wikidata.org/wiki/$1'
        ])
        resultatum.append([
            # https://www.wikidata.org/wiki/Wikidata:Glossary#QID
            # 13_12 is used for Community knowledge/Wikidata
            # 13_12_17 : [17] Q
            '{{1603_13_1_23_91924_26_13_12_17}}',
            '{{1603_13_1_23_91924_26}}',
            '1',
            '0',
            '0',
            '#item',
            'rem+i_qcc+is_zxxx+ix_wikip',
            '#item+rem+i_qcc+is_zxxx+ix_wikip',
            '/Wikidata, P; Property (also attribute)/',
            'https://www.wikidata.org/wiki/Property:$1'
        ])
        return resultatum

    def exportatum(self) -> list:
        resultatum = []
        resultatum.append([
            '#item+conceptum+codicem',
            '#item+rem+i_qcc+is_zxxx+ix_regexc',  # regex constructor
            '#item+rem+i_qcc+is_zxxx+ix_regexvdc',  # value de regex constructor
            '#item+rem+i_qcc+is_zxxx+ix_tconceptuae',  # if is conceptual
            '#item+rem+i_qcc+is_zxxx+ix_tlinguae',  # if is linguistic
            '#item+rem+i_qcc+is_zxxx+ix_tterminum',  # if varies at term level
            '#item+rem+i_qcc+is_zxxx+ix_hxlt',
            '#item+rem+i_qcc+is_zxxx+ix_hxla',
            '#item+rem+i_qcc+is_zxxx+ix_exemplum',
            '#item+rem+i_mul+is_zyyy',
            '#item+rem+i_qcc+is_zxxx+ix_wikip1630',  # formatter URL
            # '#meta',
        ])

        index = 0
        for item in self._basim():
            # print('item', item)
            index = index + 1
            item.insert(0, str(index))
            resultatum.append(item)

        for item in self._basim_extras():
            # print('item', item)
            index = index + 1
            item.insert(0, str(index))
            resultatum.append(item)

        return resultatum


class A1603z1:
    """1603_1 Main class to load boostrapping tables and explain headers

    [extended_summary]
    """

    def __init__(self):
        # self.D1613_1_51 = self._init_1613_1_51_datum()
        self.dictionaria_codex = DictionariaLinguarum()

        self.ix_csv = []  # Not really used
        self.ix_hxlhstg = []

        self.fontem_separato = ","
        self.resultatum_separato = "\t"

    def _init_1613_1_51_datum(self):
        archivum = NUMERORDINATIO_BASIM + "/1603/1/51/1603_1_51.no1.tm.hxl.csv"
        datum = {}
        with open(archivum) as file:
            # tsv_file = csv.DictReader(file, delimiter="\t")
            csv_file = csv.DictReader(file)
            # return list(tsv_file)
            for conceptum in csv_file:
                # print('conceptum', conceptum)
                int_clavem = int(conceptum['#item+conceptum+codicem'])
                datum[int_clavem] = {}
                for clavem, rem in conceptum.items():
                    if not clavem.startswith('#item+conceptum+codicem'):
                        datum[int_clavem][clavem] = rem

        return datum

    def est_resultatum_separato(self, resultatum_separato: str):
        self.resultatum_separato = resultatum_separato
        return self

    def est_fontem_separato(self, fontem_separato: str):
        self.fontem_separato = fontem_separato
        return self

    def est_lineam(self, lineam):
        # @TODO: this would not work when parsing files strictly not
        #        Numerordinatio
        if self.is_ready():
            return self

        if isinstance(lineam, list):
            self.ix_hxlhstg = lineam
        else:
            self.ix_hxlhstg = lineam.split(self.fontem_separato)
        return self

    # temporary name
    def is_ready(self):
        return len(self.ix_hxlhstg) > 0

    def exportatum(self):
        resultatum = []
        resultatum.append([
            '#item+conceptum+codicem',
            '#item+rem+i_qcc+is_zxxx+ix_hxlhstg',
            '#item+rem+i_qcc+is_zxxx+ix_hxlt',
            '#item+rem+i_qcc+is_zxxx+ix_hxla',
            '#meta',
        ])

        index = 0
        for item in self.ix_hxlhstg:
            # print('item', item)
            index = index + 1
            rem = NumerordinatioItem(
                item, dictionaria_codex=self.dictionaria_codex)

            meta = rem.quod_meta()
            meta_nomen = '' if meta is None else meta['#item+rem+i_lat+is_latn']
            resultatum.append([
                str(index),
                rem.quod_ix_hxlhstg(),
                rem.quod_ix_hxlt(),
                rem.quod_ix_hxla(),
                meta_nomen
            ])
        return resultatum


class NumerordinatioItem:
    """Numerordĭnātĭo item

    _[eng-Latn]
    For an HXL full hashtag, explain what it means
    [eng-Latn]_
    """

    def __init__(self, ix_hxlhstg: str, dictionaria_codex: Type['DictionariaLinguarum']):
        self.ix_hxlhstg = ix_hxlhstg
        self.dictionaria_codex = dictionaria_codex

    def quod_ix_hxlhstg(self):
        return self.ix_hxlhstg

    def quod_ix_hxla(self):
        return self.ix_hxlhstg.replace(self.quod_ix_hxlt(), '')

    def quod_ix_hxlt(self):
        return self.ix_hxlhstg.split('+')[0]

    def quod_meta(self):
        return self.dictionaria_codex.quod(self.quod_ix_hxla())


class CLI_2600:
    def __init__(self):
        """
        Constructs all the necessary attributes for the Cli object.
        """
        self.pyargs = None
        # self.args = self.make_args()
        # Posix exit codes
        self.EXIT_OK = 0
        self.EXIT_ERROR = 1
        self.EXIT_SYNTAX = 2

    def make_args(self, hxl_output=True):
        parser = argparse.ArgumentParser(
            prog="1603_1",
            description=DESCRIPTION,
            formatter_class=argparse.RawDescriptionHelpFormatter,
            epilog=__EPILOGUM__
        )

        # https://en.wikipedia.org/wiki/Code_word
        # https://en.wikipedia.org/wiki/Coded_set

        # cōdex verbum tabulae
        # parser.add_argument(
        #     '--actionem',
        #     help='Action to execute. Defaults to codex.',
        #     # choices=['rock', 'paper', 'scissors'],
        #     choices=[
        #         'codex',
        #         'fontem-verbum-tabulae',
        #         'neo-scripturam',
        #     ],
        #     dest='actionem',
        #     required=True,
        #     default='codex',
        #     const='codex',
        #     type=str,
        #     nargs='?'
        # )

        parser.add_argument(
            'infile',
            help='HXL file to read (if omitted, use standard input).',
            nargs='?'
        )

        parser.add_argument(
            '--punctum-separato-de-resultatum',
            help='Character(s) used as separator for generate output. ' +
            'Used only for tabular results. ' +
            'Defaults to tab "\t"',
            dest='resultatum_separato',
            default="\t",
            nargs='?'
        )

        parser.add_argument(
            '--punctum-separato-de-fontem',
            help='Character(s) used as separator from input file ' +
            'Used only for tabular results. ' +
            'Defaults to comma ","',
            dest='fontem_separato',
            default=",",
            nargs='?'
        )

        archivum = parser.add_argument_group(
            "archivum",
            "(DEFAULT USE) Use archive as source (directory not ready yet)")

        archivum.add_argument(
            '--de-archivum',
            help='Parse single archive',
            # metavar='',
            dest='de_archivum',
            # const=True,
            action='store_true',
            # nargs='?'
        )

        dictionaria = parser.add_argument_group(
            "dictionaria",
            "Generate dictionaries. No input required (uses disk 1603 and "
            "999999999/1603 data files)")

        dictionaria.add_argument(
            '--dictionaria-numerordinatio',
            help='Dictionary of all possible values on stricter '
            ' Numerordĭnātĭo (HXLStantad container)',
            # metavar='',
            dest='dictionaria_numerordinatio',
            # const=True,
            action='store_true',
            # nargs='?'
        )

        # https://en.wiktionary.org/wiki/codex#Latin
        codex = parser.add_argument_group(
            "codex",
            "Book/manual creation")

        codex.add_argument(
            '--codex-de',
            help='Generate documentation of dictionaries',
            # metavar='',
            dest='codex_de',
            # const=True,
            nargs='?'
        )

        return parser.parse_args()

    # def execute_cli(self, args, stdin=STDIN, stdout=sys.stdout,
    #                 stderr=sys.stderr):
    def execute_cli(self, pyargs, stdin=STDIN, stdout=sys.stdout,
                    stderr=sys.stderr):
        # print('TODO')

        self.pyargs = pyargs

        a1603z1 = A1603z1()

        # cs1603_1 = cs1603_1()

        # print('self.pyargs', self.pyargs)

        # cs1603_1.est_verbum_limiti(args.verbum_limiti)
        a1603z1.est_resultatum_separato(args.resultatum_separato)
        a1603z1.est_fontem_separato(args.fontem_separato)

        # if self.pyargs.actionem_sparql:
        if self.pyargs.codex_de:
            dictionaria_numerordinatio = DictionariaNumerordinatio()
            # data = ['TODO']
            return self.output(dictionaria_numerordinatio.exportatum())

        if self.pyargs.dictionaria_numerordinatio:
            dictionaria_numerordinatio = DictionariaNumerordinatio()
            # data = ['TODO']
            return self.output(dictionaria_numerordinatio.exportatum())

        if self.pyargs.de_archivum:

            if stdin.isatty():

                with open(self.pyargs.infile) as csv_file:
                    csv_reader = csv.reader(
                        csv_file, delimiter=args.fontem_separato)
                    line_count = 0
                    for row in csv_reader:
                        if a1603z1.is_ready():
                            break
                        a1603z1.est_lineam(row)

                quod_query = a1603z1.exportatum()
                return self.output(quod_query)

            for line in sys.stdin:
                if a1603z1.is_ready():
                    break
                crudum_lineam = line.replace('\n', ' ').replace('\r', '')
                # TODO: deal with cases were have more than Qcode
                # a1603z1.est_wikidata_q(codicem)
                a1603z1.est_lineam(crudum_lineam)

            quod_query = a1603z1.exportatum()
            # tabulam_numerae = ['TODO']
            # return self.output(tabulam_numerae)
            return self.output(quod_query)

        print('unknow option.')
        return self.EXIT_ERROR

    def output(self, output_collectiom):

        spamwriter = csv.writer(
            sys.stdout, delimiter=self.pyargs.resultatum_separato)
        for item in output_collectiom:
            # TODO: check if result is a file instead of print

            # print(type(item))
            if isinstance(item, int) or isinstance(item, str):
                print(item)
            else:
                spamwriter.writerow(item)

        return self.EXIT_OK


if __name__ == "__main__":

    cli_2600 = CLI_2600()
    args = cli_2600.make_args()
    # pyargs.print_help()

    # args.execute_cli(args)
    cli_2600.execute_cli(args)
