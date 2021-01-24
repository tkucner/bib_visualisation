import antlr4
from antlr4.InputStream import InputStream
from bibtexLexer import bibtexLexer, FileStream
from bibtexParser import bibtexParser
import sys


def clean_type(bibtype):
    bibtype = bibtype.replace('@', '')
    bibtype = bibtype.replace('{', '')
    return bibtype


def remove_brackets(text):
    text = text.replace('{', '')
    text = text.replace('}', '')
    return text


def handle_bibliogrpahy(expr):
    bibliography = []
    for child in expr.getChildren():
        entry = {}
        if isinstance(child, antlr4.tree.Tree.TerminalNode) or child.CommentType() is not None:
            pass
        else:
            entry['bibtype'] = clean_type(child.Type().symbol.text)
            entry['bibkey'] = child.Name().symbol.text
            entry['fields'] = {}
            for t in child.tags().getChildren():
                if isinstance(t, antlr4.tree.Tree.TerminalNode):
                    pass
                else:
                    entry['fields'][t.Name().symbol.text] = remove_brackets(t.content().BracedContent().symbol.text)
            bibliography.append(entry)
    return bibliography


def main():
    input_stream = None
    if len(sys.argv) > 1:
        input_stream = FileStream(sys.argv[1])
    else:
        input_stream = InputStream(sys.stdin.readline())
    lexer = bibtexLexer(input_stream)
    stream = antlr4.CommonTokenStream(lexer)
    parser = bibtexParser(stream)
    tree = parser.parse()
    bib = handle_bibliogrpahy(tree)


if __name__ == '__main__':
    main()
