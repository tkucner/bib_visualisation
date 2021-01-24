# Generated from bibtex.g4 by ANTLR 4.5.1
# encoding: utf-8
from antlr4 import *
from io import StringIO

def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u0430\ud6d1\u8206\uad2d\u4417\uaef1\u8d80\uaadd\3\17")
        buf.write("Q\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\3\2")
        buf.write("\3\2\5\2\21\n\2\3\2\7\2\24\n\2\f\2\16\2\27\13\2\3\2\5")
        buf.write("\2\32\n\2\5\2\34\n\2\3\2\3\2\3\3\3\3\3\3\3\3\3\3\3\3\3")
        buf.write("\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\5\3\60\n\3\3\4")
        buf.write("\3\4\3\4\7\4\65\n\4\f\4\16\48\13\4\3\4\5\4;\n\4\5\4=\n")
        buf.write("\4\3\5\3\5\3\5\3\5\3\6\3\6\3\6\7\6F\n\6\f\6\16\6I\13\6")
        buf.write("\3\6\3\6\5\6M\n\6\3\7\3\7\3\7\2\2\b\2\4\6\b\n\f\2\3\4")
        buf.write("\2\7\7\16\16W\2\33\3\2\2\2\4/\3\2\2\2\6<\3\2\2\2\b>\3")
        buf.write("\2\2\2\nL\3\2\2\2\fN\3\2\2\2\16\25\5\4\3\2\17\21\7\5\2")
        buf.write("\2\20\17\3\2\2\2\20\21\3\2\2\2\21\22\3\2\2\2\22\24\5\4")
        buf.write("\3\2\23\20\3\2\2\2\24\27\3\2\2\2\25\23\3\2\2\2\25\26\3")
        buf.write("\2\2\2\26\31\3\2\2\2\27\25\3\2\2\2\30\32\7\5\2\2\31\30")
        buf.write("\3\2\2\2\31\32\3\2\2\2\32\34\3\2\2\2\33\16\3\2\2\2\33")
        buf.write("\34\3\2\2\2\34\35\3\2\2\2\35\36\7\2\2\3\36\3\3\2\2\2\37")
        buf.write(" \7\f\2\2 !\7\16\2\2!\"\7\5\2\2\"#\5\6\4\2#$\7\6\2\2$")
        buf.write("\60\3\2\2\2%&\7\t\2\2&\'\7\16\2\2\'(\7\3\2\2()\7\7\2\2")
        buf.write(")\60\7\6\2\2*+\7\n\2\2+,\5\n\6\2,-\7\6\2\2-\60\3\2\2\2")
        buf.write(".\60\7\13\2\2/\37\3\2\2\2/%\3\2\2\2/*\3\2\2\2/.\3\2\2")
        buf.write("\2\60\5\3\2\2\2\61\66\5\b\5\2\62\63\7\5\2\2\63\65\5\b")
        buf.write("\5\2\64\62\3\2\2\2\658\3\2\2\2\66\64\3\2\2\2\66\67\3\2")
        buf.write("\2\2\67:\3\2\2\28\66\3\2\2\29;\7\5\2\2:9\3\2\2\2:;\3\2")
        buf.write("\2\2;=\3\2\2\2<\61\3\2\2\2<=\3\2\2\2=\7\3\2\2\2>?\7\16")
        buf.write("\2\2?@\7\3\2\2@A\5\n\6\2A\t\3\2\2\2BG\5\f\7\2CD\7\4\2")
        buf.write("\2DF\5\f\7\2EC\3\2\2\2FI\3\2\2\2GE\3\2\2\2GH\3\2\2\2H")
        buf.write("M\3\2\2\2IG\3\2\2\2JM\7\r\2\2KM\7\b\2\2LB\3\2\2\2LJ\3")
        buf.write("\2\2\2LK\3\2\2\2M\13\3\2\2\2NO\t\2\2\2O\r\3\2\2\2\f\20")
        buf.write("\25\31\33/\66:<GL")
        return buf.getvalue()


class bibtexParser ( Parser ):

    grammarFileName = "bibtex.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'='", "'#'", "','", "'}'" ]

    symbolicNames = [ "<INVALID>", "Assign", "Concat", "Comma", "CloseBrace", 
                      "QuotedContent", "BracedContent", "StringType", "PreambleType", 
                      "CommentType", "Type", "Number", "Name", "Spaces" ]

    RULE_parse = 0
    RULE_entry = 1
    RULE_tags = 2
    RULE_tag = 3
    RULE_content = 4
    RULE_concatable = 5

    ruleNames =  [ "parse", "entry", "tags", "tag", "content", "concatable" ]

    EOF = Token.EOF
    Assign=1
    Concat=2
    Comma=3
    CloseBrace=4
    QuotedContent=5
    BracedContent=6
    StringType=7
    PreambleType=8
    CommentType=9
    Type=10
    Number=11
    Name=12
    Spaces=13

    def __init__(self, input:TokenStream):
        super().__init__(input)
        self.checkVersion("4.5.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None



    class ParseContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(bibtexParser.EOF, 0)

        def entry(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(bibtexParser.EntryContext)
            else:
                return self.getTypedRuleContext(bibtexParser.EntryContext,i)


        def Comma(self, i:int=None):
            if i is None:
                return self.getTokens(bibtexParser.Comma)
            else:
                return self.getToken(bibtexParser.Comma, i)

        def getRuleIndex(self):
            return bibtexParser.RULE_parse

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParse" ):
                listener.enterParse(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParse" ):
                listener.exitParse(self)




    def parse(self):

        localctx = bibtexParser.ParseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_parse)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 25
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << bibtexParser.StringType) | (1 << bibtexParser.PreambleType) | (1 << bibtexParser.CommentType) | (1 << bibtexParser.Type))) != 0):
                self.state = 12
                self.entry()
                self.state = 19
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,1,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 14
                        _la = self._input.LA(1)
                        if _la==bibtexParser.Comma:
                            self.state = 13
                            self.match(bibtexParser.Comma)


                        self.state = 16
                        self.entry() 
                    self.state = 21
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,1,self._ctx)

                self.state = 23
                _la = self._input.LA(1)
                if _la==bibtexParser.Comma:
                    self.state = 22
                    self.match(bibtexParser.Comma)




            self.state = 27
            self.match(bibtexParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class EntryContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Type(self):
            return self.getToken(bibtexParser.Type, 0)

        def Name(self):
            return self.getToken(bibtexParser.Name, 0)

        def Comma(self):
            return self.getToken(bibtexParser.Comma, 0)

        def tags(self):
            return self.getTypedRuleContext(bibtexParser.TagsContext,0)


        def CloseBrace(self):
            return self.getToken(bibtexParser.CloseBrace, 0)

        def StringType(self):
            return self.getToken(bibtexParser.StringType, 0)

        def Assign(self):
            return self.getToken(bibtexParser.Assign, 0)

        def QuotedContent(self):
            return self.getToken(bibtexParser.QuotedContent, 0)

        def PreambleType(self):
            return self.getToken(bibtexParser.PreambleType, 0)

        def content(self):
            return self.getTypedRuleContext(bibtexParser.ContentContext,0)


        def CommentType(self):
            return self.getToken(bibtexParser.CommentType, 0)

        def getRuleIndex(self):
            return bibtexParser.RULE_entry

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEntry" ):
                listener.enterEntry(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEntry" ):
                listener.exitEntry(self)




    def entry(self):

        localctx = bibtexParser.EntryContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_entry)
        try:
            self.state = 45
            token = self._input.LA(1)
            if token in [bibtexParser.Type]:
                self.enterOuterAlt(localctx, 1)
                self.state = 29
                self.match(bibtexParser.Type)
                self.state = 30
                self.match(bibtexParser.Name)
                self.state = 31
                self.match(bibtexParser.Comma)
                self.state = 32
                self.tags()
                self.state = 33
                self.match(bibtexParser.CloseBrace)

            elif token in [bibtexParser.StringType]:
                self.enterOuterAlt(localctx, 2)
                self.state = 35
                self.match(bibtexParser.StringType)
                self.state = 36
                self.match(bibtexParser.Name)
                self.state = 37
                self.match(bibtexParser.Assign)
                self.state = 38
                self.match(bibtexParser.QuotedContent)
                self.state = 39
                self.match(bibtexParser.CloseBrace)

            elif token in [bibtexParser.PreambleType]:
                self.enterOuterAlt(localctx, 3)
                self.state = 40
                self.match(bibtexParser.PreambleType)
                self.state = 41
                self.content()
                self.state = 42
                self.match(bibtexParser.CloseBrace)

            elif token in [bibtexParser.CommentType]:
                self.enterOuterAlt(localctx, 4)
                self.state = 44
                self.match(bibtexParser.CommentType)

            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class TagsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def tag(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(bibtexParser.TagContext)
            else:
                return self.getTypedRuleContext(bibtexParser.TagContext,i)


        def Comma(self, i:int=None):
            if i is None:
                return self.getTokens(bibtexParser.Comma)
            else:
                return self.getToken(bibtexParser.Comma, i)

        def getRuleIndex(self):
            return bibtexParser.RULE_tags

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTags" ):
                listener.enterTags(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTags" ):
                listener.exitTags(self)




    def tags(self):

        localctx = bibtexParser.TagsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_tags)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 58
            _la = self._input.LA(1)
            if _la==bibtexParser.Name:
                self.state = 47
                self.tag()
                self.state = 52
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,5,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 48
                        self.match(bibtexParser.Comma)
                        self.state = 49
                        self.tag() 
                    self.state = 54
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,5,self._ctx)

                self.state = 56
                _la = self._input.LA(1)
                if _la==bibtexParser.Comma:
                    self.state = 55
                    self.match(bibtexParser.Comma)




        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class TagContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Name(self):
            return self.getToken(bibtexParser.Name, 0)

        def Assign(self):
            return self.getToken(bibtexParser.Assign, 0)

        def content(self):
            return self.getTypedRuleContext(bibtexParser.ContentContext,0)


        def getRuleIndex(self):
            return bibtexParser.RULE_tag

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTag" ):
                listener.enterTag(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTag" ):
                listener.exitTag(self)




    def tag(self):

        localctx = bibtexParser.TagContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_tag)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 60
            self.match(bibtexParser.Name)
            self.state = 61
            self.match(bibtexParser.Assign)
            self.state = 62
            self.content()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ContentContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def concatable(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(bibtexParser.ConcatableContext)
            else:
                return self.getTypedRuleContext(bibtexParser.ConcatableContext,i)


        def Concat(self, i:int=None):
            if i is None:
                return self.getTokens(bibtexParser.Concat)
            else:
                return self.getToken(bibtexParser.Concat, i)

        def Number(self):
            return self.getToken(bibtexParser.Number, 0)

        def BracedContent(self):
            return self.getToken(bibtexParser.BracedContent, 0)

        def getRuleIndex(self):
            return bibtexParser.RULE_content

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterContent" ):
                listener.enterContent(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitContent" ):
                listener.exitContent(self)




    def content(self):

        localctx = bibtexParser.ContentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_content)
        self._la = 0 # Token type
        try:
            self.state = 74
            token = self._input.LA(1)
            if token in [bibtexParser.QuotedContent, bibtexParser.Name]:
                self.enterOuterAlt(localctx, 1)
                self.state = 64
                self.concatable()
                self.state = 69
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==bibtexParser.Concat:
                    self.state = 65
                    self.match(bibtexParser.Concat)
                    self.state = 66
                    self.concatable()
                    self.state = 71
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)


            elif token in [bibtexParser.Number]:
                self.enterOuterAlt(localctx, 2)
                self.state = 72
                self.match(bibtexParser.Number)

            elif token in [bibtexParser.BracedContent]:
                self.enterOuterAlt(localctx, 3)
                self.state = 73
                self.match(bibtexParser.BracedContent)

            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ConcatableContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def QuotedContent(self):
            return self.getToken(bibtexParser.QuotedContent, 0)

        def Name(self):
            return self.getToken(bibtexParser.Name, 0)

        def getRuleIndex(self):
            return bibtexParser.RULE_concatable

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterConcatable" ):
                listener.enterConcatable(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitConcatable" ):
                listener.exitConcatable(self)




    def concatable(self):

        localctx = bibtexParser.ConcatableContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_concatable)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 76
            _la = self._input.LA(1)
            if not(_la==bibtexParser.QuotedContent or _la==bibtexParser.Name):
                self._errHandler.recoverInline(self)
            else:
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





