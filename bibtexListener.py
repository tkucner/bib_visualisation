# Generated from bibtex.g4 by ANTLR 4.5.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .bibtexParser import bibtexParser
else:
    from bibtexParser import bibtexParser

# This class defines a complete listener for a parse tree produced by bibtexParser.
class bibtexListener(ParseTreeListener):

    # Enter a parse tree produced by bibtexParser#parse.
    def enterParse(self, ctx:bibtexParser.ParseContext):
        pass

    # Exit a parse tree produced by bibtexParser#parse.
    def exitParse(self, ctx:bibtexParser.ParseContext):
        pass


    # Enter a parse tree produced by bibtexParser#entry.
    def enterEntry(self, ctx:bibtexParser.EntryContext):
        pass

    # Exit a parse tree produced by bibtexParser#entry.
    def exitEntry(self, ctx:bibtexParser.EntryContext):
        pass


    # Enter a parse tree produced by bibtexParser#tags.
    def enterTags(self, ctx:bibtexParser.TagsContext):
        pass

    # Exit a parse tree produced by bibtexParser#tags.
    def exitTags(self, ctx:bibtexParser.TagsContext):
        pass


    # Enter a parse tree produced by bibtexParser#tag.
    def enterTag(self, ctx:bibtexParser.TagContext):
        pass

    # Exit a parse tree produced by bibtexParser#tag.
    def exitTag(self, ctx:bibtexParser.TagContext):
        pass


    # Enter a parse tree produced by bibtexParser#content.
    def enterContent(self, ctx:bibtexParser.ContentContext):
        pass

    # Exit a parse tree produced by bibtexParser#content.
    def exitContent(self, ctx:bibtexParser.ContentContext):
        pass


    # Enter a parse tree produced by bibtexParser#concatable.
    def enterConcatable(self, ctx:bibtexParser.ConcatableContext):
        pass

    # Exit a parse tree produced by bibtexParser#concatable.
    def exitConcatable(self, ctx:bibtexParser.ConcatableContext):
        pass


