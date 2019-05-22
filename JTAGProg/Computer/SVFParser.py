# Generated from SVF.g4 by ANTLR 4.7.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\25")
        buf.write("f\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b")
        buf.write("\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\3\2\3\2\3\2\3\2")
        buf.write("\3\2\5\2\36\n\2\3\2\3\2\3\2\3\3\3\3\3\4\3\4\3\4\3\4\3")
        buf.write("\4\3\4\3\4\3\4\3\4\5\4.\n\4\3\5\3\5\3\5\3\5\3\5\3\5\3")
        buf.write("\6\3\6\3\6\3\6\3\6\3\6\3\7\6\7=\n\7\r\7\16\7>\3\b\3\b")
        buf.write("\3\b\3\b\3\b\3\t\3\t\3\t\3\t\3\t\3\n\3\n\3\n\3\n\3\n\7")
        buf.write("\nP\n\n\f\n\16\nS\13\n\3\n\3\n\3\n\3\n\3\13\3\13\3\13")
        buf.write("\3\13\3\13\5\13^\n\13\3\f\7\fa\n\f\f\f\16\fd\13\f\3\f")
        buf.write("\2\2\r\2\4\6\b\n\f\16\20\22\24\26\2\4\4\2\r\r\17\17\3")
        buf.write("\2\r\16\2c\2\30\3\2\2\2\4\"\3\2\2\2\6-\3\2\2\2\b/\3\2")
        buf.write("\2\2\n\65\3\2\2\2\f<\3\2\2\2\16@\3\2\2\2\20E\3\2\2\2\22")
        buf.write("J\3\2\2\2\24]\3\2\2\2\26b\3\2\2\2\30\35\7\21\2\2\31\32")
        buf.write("\7\3\2\2\32\36\b\2\1\2\33\34\7\4\2\2\34\36\b\2\1\2\35")
        buf.write("\31\3\2\2\2\35\33\3\2\2\2\36\37\3\2\2\2\37 \7\20\2\2 ")
        buf.write("!\b\2\1\2!\3\3\2\2\2\"#\t\2\2\2#\5\3\2\2\2$%\7\5\2\2%")
        buf.write("&\5\4\3\2&\'\7\6\2\2\'(\7\20\2\2()\b\4\1\2).\3\2\2\2*")
        buf.write("+\7\5\2\2+,\7\20\2\2,.\b\4\1\2-$\3\2\2\2-*\3\2\2\2.\7")
        buf.write("\3\2\2\2/\60\7\7\2\2\60\61\7\r\2\2\61\62\7\b\2\2\62\63")
        buf.write("\7\20\2\2\63\64\b\5\1\2\64\t\3\2\2\2\65\66\7\22\2\2\66")
        buf.write("\67\7\23\2\2\678\7\20\2\289\b\6\1\29:\b\6\1\2:\13\3\2")
        buf.write("\2\2;=\t\3\2\2<;\3\2\2\2=>\3\2\2\2><\3\2\2\2>?\3\2\2\2")
        buf.write("?\r\3\2\2\2@A\7\t\2\2AB\5\f\7\2BC\7\n\2\2CD\b\b\1\2D\17")
        buf.write("\3\2\2\2EF\7\25\2\2FG\5\16\b\2GH\b\t\1\2HI\b\t\1\2I\21")
        buf.write("\3\2\2\2JK\7\24\2\2KQ\7\r\2\2LM\5\20\t\2MN\b\n\1\2NP\3")
        buf.write("\2\2\2OL\3\2\2\2PS\3\2\2\2QO\3\2\2\2QR\3\2\2\2RT\3\2\2")
        buf.write("\2SQ\3\2\2\2TU\7\20\2\2UV\b\n\1\2VW\b\n\1\2W\23\3\2\2")
        buf.write("\2X^\5\n\6\2Y^\5\22\n\2Z^\5\b\5\2[^\5\6\4\2\\^\5\2\2\2")
        buf.write("]X\3\2\2\2]Y\3\2\2\2]Z\3\2\2\2][\3\2\2\2]\\\3\2\2\2^\25")
        buf.write("\3\2\2\2_a\5\24\13\2`_\3\2\2\2ad\3\2\2\2b`\3\2\2\2bc\3")
        buf.write("\2\2\2c\27\3\2\2\2db\3\2\2\2\b\35->Q]b")
        return buf.getvalue()


class SVFParser ( Parser ):

    grammarFileName = "SVF.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'ON'", "'OFF'", "'FREQUENCY'", "'HZ'", 
                     "'RUNTEST'", "'TCK'", "'('", "')'", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "';'", "'TRST'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "COMMENT", "WS", "NUM", "HEX", "EXPNUM", 
                      "CMD_END", "TOGGLE_CMD", "STATE_CMD", "STATE", "DATA_CMD", 
                      "ATTR" ]

    RULE_toggleCmd = 0
    RULE_expnum = 1
    RULE_freqCmd = 2
    RULE_runtestCmd = 3
    RULE_stateCmd = 4
    RULE_hexLiteral = 5
    RULE_hexBlock = 6
    RULE_attr = 7
    RULE_dataCmd = 8
    RULE_cmdShell = 9
    RULE_svf = 10

    ruleNames =  [ "toggleCmd", "expnum", "freqCmd", "runtestCmd", "stateCmd", 
                   "hexLiteral", "hexBlock", "attr", "dataCmd", "cmdShell", 
                   "svf" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    COMMENT=9
    WS=10
    NUM=11
    HEX=12
    EXPNUM=13
    CMD_END=14
    TOGGLE_CMD=15
    STATE_CMD=16
    STATE=17
    DATA_CMD=18
    ATTR=19

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ToggleCmdContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.name = None
            self.state = None
            self._TOGGLE_CMD = None # Token

        def TOGGLE_CMD(self):
            return self.getToken(SVFParser.TOGGLE_CMD, 0)

        def CMD_END(self):
            return self.getToken(SVFParser.CMD_END, 0)

        def getRuleIndex(self):
            return SVFParser.RULE_toggleCmd

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterToggleCmd" ):
                listener.enterToggleCmd(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitToggleCmd" ):
                listener.exitToggleCmd(self)




    def toggleCmd(self):

        localctx = SVFParser.ToggleCmdContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_toggleCmd)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 22
            localctx._TOGGLE_CMD = self.match(SVFParser.TOGGLE_CMD)
            self.state = 27
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [SVFParser.T__0]:
                self.state = 23
                self.match(SVFParser.T__0)
                localctx.state = True
                pass
            elif token in [SVFParser.T__1]:
                self.state = 25
                self.match(SVFParser.T__1)
                localctx.state = False
                pass
            else:
                raise NoViableAltException(self)

            self.state = 29
            self.match(SVFParser.CMD_END)
            localctx.name = (None if localctx._TOGGLE_CMD is None else localctx._TOGGLE_CMD.text)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpnumContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EXPNUM(self):
            return self.getToken(SVFParser.EXPNUM, 0)

        def NUM(self):
            return self.getToken(SVFParser.NUM, 0)

        def getRuleIndex(self):
            return SVFParser.RULE_expnum

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpnum" ):
                listener.enterExpnum(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpnum" ):
                listener.exitExpnum(self)




    def expnum(self):

        localctx = SVFParser.ExpnumContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_expnum)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 32
            _la = self._input.LA(1)
            if not(_la==SVFParser.NUM or _la==SVFParser.EXPNUM):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FreqCmdContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.freq = None
            self._expnum = None # ExpnumContext

        def expnum(self):
            return self.getTypedRuleContext(SVFParser.ExpnumContext,0)


        def CMD_END(self):
            return self.getToken(SVFParser.CMD_END, 0)

        def getRuleIndex(self):
            return SVFParser.RULE_freqCmd

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFreqCmd" ):
                listener.enterFreqCmd(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFreqCmd" ):
                listener.exitFreqCmd(self)




    def freqCmd(self):

        localctx = SVFParser.FreqCmdContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_freqCmd)
        try:
            self.state = 43
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 34
                self.match(SVFParser.T__2)
                self.state = 35
                localctx._expnum = self.expnum()
                self.state = 36
                self.match(SVFParser.T__3)
                self.state = 37
                self.match(SVFParser.CMD_END)
                localctx.freq = float((None if localctx._expnum is None else self._input.getText((localctx._expnum.start,localctx._expnum.stop))))
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 40
                self.match(SVFParser.T__2)
                self.state = 41
                self.match(SVFParser.CMD_END)
                localctx.freq = float('+inf')
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RuntestCmdContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.ticks = None
            self._NUM = None # Token

        def NUM(self):
            return self.getToken(SVFParser.NUM, 0)

        def CMD_END(self):
            return self.getToken(SVFParser.CMD_END, 0)

        def getRuleIndex(self):
            return SVFParser.RULE_runtestCmd

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRuntestCmd" ):
                listener.enterRuntestCmd(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRuntestCmd" ):
                listener.exitRuntestCmd(self)




    def runtestCmd(self):

        localctx = SVFParser.RuntestCmdContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_runtestCmd)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 45
            self.match(SVFParser.T__4)
            self.state = 46
            localctx._NUM = self.match(SVFParser.NUM)
            self.state = 47
            self.match(SVFParser.T__5)
            self.state = 48
            self.match(SVFParser.CMD_END)
            localctx.ticks = (0 if localctx._NUM is None else int(localctx._NUM.text))
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StateCmdContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.name = None
            self.state = None
            self._STATE_CMD = None # Token
            self._STATE = None # Token

        def STATE_CMD(self):
            return self.getToken(SVFParser.STATE_CMD, 0)

        def STATE(self):
            return self.getToken(SVFParser.STATE, 0)

        def CMD_END(self):
            return self.getToken(SVFParser.CMD_END, 0)

        def getRuleIndex(self):
            return SVFParser.RULE_stateCmd

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStateCmd" ):
                listener.enterStateCmd(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStateCmd" ):
                listener.exitStateCmd(self)




    def stateCmd(self):

        localctx = SVFParser.StateCmdContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_stateCmd)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 51
            localctx._STATE_CMD = self.match(SVFParser.STATE_CMD)
            self.state = 52
            localctx._STATE = self.match(SVFParser.STATE)
            self.state = 53
            self.match(SVFParser.CMD_END)
            localctx.name = (None if localctx._STATE_CMD is None else localctx._STATE_CMD.text)
            localctx.state = (None if localctx._STATE is None else localctx._STATE.text)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class HexLiteralContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def HEX(self, i:int=None):
            if i is None:
                return self.getTokens(SVFParser.HEX)
            else:
                return self.getToken(SVFParser.HEX, i)

        def NUM(self, i:int=None):
            if i is None:
                return self.getTokens(SVFParser.NUM)
            else:
                return self.getToken(SVFParser.NUM, i)

        def getRuleIndex(self):
            return SVFParser.RULE_hexLiteral

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterHexLiteral" ):
                listener.enterHexLiteral(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitHexLiteral" ):
                listener.exitHexLiteral(self)




    def hexLiteral(self):

        localctx = SVFParser.HexLiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_hexLiteral)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 58 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 57
                _la = self._input.LA(1)
                if not(_la==SVFParser.NUM or _la==SVFParser.HEX):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 60 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==SVFParser.NUM or _la==SVFParser.HEX):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class HexBlockContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.value = None
            self._hexLiteral = None # HexLiteralContext

        def hexLiteral(self):
            return self.getTypedRuleContext(SVFParser.HexLiteralContext,0)


        def getRuleIndex(self):
            return SVFParser.RULE_hexBlock

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterHexBlock" ):
                listener.enterHexBlock(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitHexBlock" ):
                listener.exitHexBlock(self)




    def hexBlock(self):

        localctx = SVFParser.HexBlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_hexBlock)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 62
            self.match(SVFParser.T__6)
            self.state = 63
            localctx._hexLiteral = self.hexLiteral()
            self.state = 64
            self.match(SVFParser.T__7)
            localctx.value = (None if localctx._hexLiteral is None else self._input.getText((localctx._hexLiteral.start,localctx._hexLiteral.stop)))
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AttrContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.name = None
            self.value = None
            self._ATTR = None # Token
            self._hexBlock = None # HexBlockContext

        def ATTR(self):
            return self.getToken(SVFParser.ATTR, 0)

        def hexBlock(self):
            return self.getTypedRuleContext(SVFParser.HexBlockContext,0)


        def getRuleIndex(self):
            return SVFParser.RULE_attr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAttr" ):
                listener.enterAttr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAttr" ):
                listener.exitAttr(self)




    def attr(self):

        localctx = SVFParser.AttrContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_attr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 67
            localctx._ATTR = self.match(SVFParser.ATTR)
            self.state = 68
            localctx._hexBlock = self.hexBlock()
            localctx.name = (None if localctx._ATTR is None else localctx._ATTR.text)
            localctx.value = localctx._hexBlock.value
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DataCmdContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.name = None
            self.len = None
            self.attrs = {}
            self._DATA_CMD = None # Token
            self._NUM = None # Token
            self._attr = None # AttrContext

        def DATA_CMD(self):
            return self.getToken(SVFParser.DATA_CMD, 0)

        def NUM(self):
            return self.getToken(SVFParser.NUM, 0)

        def CMD_END(self):
            return self.getToken(SVFParser.CMD_END, 0)

        def attr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SVFParser.AttrContext)
            else:
                return self.getTypedRuleContext(SVFParser.AttrContext,i)


        def getRuleIndex(self):
            return SVFParser.RULE_dataCmd

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDataCmd" ):
                listener.enterDataCmd(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDataCmd" ):
                listener.exitDataCmd(self)




    def dataCmd(self):

        localctx = SVFParser.DataCmdContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_dataCmd)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 72
            localctx._DATA_CMD = self.match(SVFParser.DATA_CMD)
            self.state = 73
            localctx._NUM = self.match(SVFParser.NUM)
            self.state = 79
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==SVFParser.ATTR:
                self.state = 74
                localctx._attr = self.attr()
                localctx.attrs[localctx._attr.name] = localctx._attr.value
                self.state = 81
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 82
            self.match(SVFParser.CMD_END)
            localctx.name = (None if localctx._DATA_CMD is None else localctx._DATA_CMD.text)
            localctx.len = (0 if localctx._NUM is None else int(localctx._NUM.text))
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CmdShellContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def stateCmd(self):
            return self.getTypedRuleContext(SVFParser.StateCmdContext,0)


        def dataCmd(self):
            return self.getTypedRuleContext(SVFParser.DataCmdContext,0)


        def runtestCmd(self):
            return self.getTypedRuleContext(SVFParser.RuntestCmdContext,0)


        def freqCmd(self):
            return self.getTypedRuleContext(SVFParser.FreqCmdContext,0)


        def toggleCmd(self):
            return self.getTypedRuleContext(SVFParser.ToggleCmdContext,0)


        def getRuleIndex(self):
            return SVFParser.RULE_cmdShell

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCmdShell" ):
                listener.enterCmdShell(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCmdShell" ):
                listener.exitCmdShell(self)




    def cmdShell(self):

        localctx = SVFParser.CmdShellContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_cmdShell)
        try:
            self.state = 91
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [SVFParser.STATE_CMD]:
                self.enterOuterAlt(localctx, 1)
                self.state = 86
                self.stateCmd()
                pass
            elif token in [SVFParser.DATA_CMD]:
                self.enterOuterAlt(localctx, 2)
                self.state = 87
                self.dataCmd()
                pass
            elif token in [SVFParser.T__4]:
                self.enterOuterAlt(localctx, 3)
                self.state = 88
                self.runtestCmd()
                pass
            elif token in [SVFParser.T__2]:
                self.enterOuterAlt(localctx, 4)
                self.state = 89
                self.freqCmd()
                pass
            elif token in [SVFParser.TOGGLE_CMD]:
                self.enterOuterAlt(localctx, 5)
                self.state = 90
                self.toggleCmd()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SvfContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def cmdShell(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SVFParser.CmdShellContext)
            else:
                return self.getTypedRuleContext(SVFParser.CmdShellContext,i)


        def getRuleIndex(self):
            return SVFParser.RULE_svf

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSvf" ):
                listener.enterSvf(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSvf" ):
                listener.exitSvf(self)




    def svf(self):

        localctx = SVFParser.SvfContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_svf)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 96
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << SVFParser.T__2) | (1 << SVFParser.T__4) | (1 << SVFParser.TOGGLE_CMD) | (1 << SVFParser.STATE_CMD) | (1 << SVFParser.DATA_CMD))) != 0):
                self.state = 93
                self.cmdShell()
                self.state = 98
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





