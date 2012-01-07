from argparse import ArgumentParser
from sphinx.websupport import WebSupport

def make_parser():
    parser = ArgumentParser()
    parser.add_argument('srcdir')
    parser.add_argument('builddir')
    return parser

def make_support(args):
    support = WebSupport(srcdir=args.srcdir,
        builddir=args.builddir)
    return support

def main():
    parser = make_parser()
    args = parser.parse_args()
    support = make_support(args)
    support.build()
