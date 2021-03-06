# 2016.02.14 12:49:04 St�edn� Evropa (b�n� �as)
# Embedded file name: scripts/common/Lib/lib2to3/patcomp.py
"""Pattern compiler.

The grammer is taken from PatternGrammar.txt.

The compiler compiles a pattern to a pytree.*Pattern instance.
"""
__author__ = 'Guido van Rossum <guido@python.org>'
import os
import StringIO
from .pgen2 import driver, literals, token, tokenize, parse, grammar
from . import pytree
from . import pygram
_PATTERN_GRAMMAR_FILE = os.path.join(os.path.dirname(__file__), 'PatternGrammar.txt')

class PatternSyntaxError(Exception):
    pass


def tokenize_wrapper(input):
    """Tokenizes a string suppressing significant whitespace."""
    skip = set((token.NEWLINE, token.INDENT, token.DEDENT))
    tokens = tokenize.generate_tokens(StringIO.StringIO(input).readline)
    for quintuple in tokens:
        type, value, start, end, line_text = quintuple
        if type not in skip:
            yield quintuple


class PatternCompiler(object):

    def __init__(self, grammar_file = _PATTERN_GRAMMAR_FILE):
        """Initializer.
        
        Takes an optional alternative filename for the pattern grammar.
        """
        self.grammar = driver.load_grammar(grammar_file)
        self.syms = pygram.Symbols(self.grammar)
        self.pygrammar = pygram.python_grammar
        self.pysyms = pygram.python_symbols
        self.driver = driver.Driver(self.grammar, convert=pattern_convert)

    def compile_pattern(self, input, debug = False, with_tree = False):
        """Compiles a pattern string to a nested pytree.*Pattern object."""
        tokens = tokenize_wrapper(input)
        try:
            root = self.driver.parse_tokens(tokens, debug=debug)
        except parse.ParseError as e:
            raise PatternSyntaxError(str(e))

        if with_tree:
            return (self.compile_node(root), root)
        else:
            return self.compile_node(root)

    def compile_node(self, node):
        """Compiles a node, recursively.
        
        This is one big switch on the node type.
        """
        if node.type == self.syms.Matcher:
            node = node.children[0]
        if node.type == self.syms.Alternatives:
            alts = [ self.compile_node(ch) for ch in node.children[::2] ]
            if len(alts) == 1:
                return alts[0]
            p = pytree.WildcardPattern([ [a] for a in alts ], min=1, max=1)
            return p.optimize()
        elif node.type == self.syms.Alternative:
            units = [ self.compile_node(ch) for ch in node.children ]
            if len(units) == 1:
                return units[0]
            p = pytree.WildcardPattern([units], min=1, max=1)
            return p.optimize()
        elif node.type == self.syms.NegatedUnit:
            pattern = self.compile_basic(node.children[1:])
            p = pytree.NegatedPattern(pattern)
            return p.optimize()
        else:
            if not node.type == self.syms.Unit:
                raise AssertionError
                name = None
                nodes = node.children
                if len(nodes) >= 3 and nodes[1].type == token.EQUAL:
                    name = nodes[0].value
                    nodes = nodes[2:]
                repeat = None
                repeat = len(nodes) >= 2 and nodes[-1].type == self.syms.Repeater and nodes[-1]
                nodes = nodes[:-1]
            pattern = self.compile_basic(nodes, repeat)
            if repeat is not None:
                if not repeat.type == self.syms.Repeater:
                    raise AssertionError
                    children = repeat.children
                    child = children[0]
                    if child.type == token.STAR:
                        min = 0
                        max = pytree.HUGE
                    elif child.type == token.PLUS:
                        min = 1
                        max = pytree.HUGE
                    else:
                        raise child.type == token.LBRACE and (children[-1].type == token.RBRACE or AssertionError)
                        if not len(children) in (3, 5):
                            raise AssertionError
                            min = max = self.get_int(children[1])
                            if len(children) == 5:
                                max = self.get_int(children[3])
                        else:
                            raise False or AssertionError
                    if min != 1 or max != 1:
                        pattern = pattern.optimize()
                        pattern = pytree.WildcardPattern([[pattern]], min=min, max=max)
                pattern.name = name is not None and name
            return pattern.optimize()

    def compile_basic(self, nodes, repeat = None):
        if not len(nodes) >= 1:
            raise AssertionError
            node = nodes[0]
            value = node.type == token.STRING and unicode(literals.evalString(node.value))
            return pytree.LeafPattern(_type_of_literal(value), value)
        else:
            if node.type == token.NAME:
                value = node.value
                if value.isupper():
                    if value not in TOKEN_MAP:
                        raise PatternSyntaxError('Invalid token: %r' % value)
                    if nodes[1:]:
                        raise PatternSyntaxError("Can't have details for token")
                    return pytree.LeafPattern(TOKEN_MAP[value])
                else:
                    if value == 'any':
                        type = None
                    elif not value.startswith('_'):
                        type = getattr(self.pysyms, value, None)
                        if type is None:
                            raise PatternSyntaxError('Invalid symbol: %r' % value)
                    if nodes[1:]:
                        content = [self.compile_node(nodes[1].children[1])]
                    else:
                        content = None
                    return pytree.NodePattern(type, content)
            else:
                if node.value == '(':
                    return self.compile_node(nodes[1])
                if not (node.value == '[' and repeat is None):
                    raise AssertionError
                    subpattern = self.compile_node(nodes[1])
                    return pytree.WildcardPattern([[subpattern]], min=0, max=1)
            raise False or AssertionError(node)
            return

    def get_int(self, node):
        raise node.type == token.NUMBER or AssertionError
        return int(node.value)


TOKEN_MAP = {'NAME': token.NAME,
 'STRING': token.STRING,
 'NUMBER': token.NUMBER,
 'TOKEN': None}

def _type_of_literal(value):
    if value[0].isalpha():
        return token.NAME
    elif value in grammar.opmap:
        return grammar.opmap[value]
    else:
        return None
        return None


def pattern_convert(grammar, raw_node_info):
    """Converts raw node information to a Node or Leaf instance."""
    type, value, context, children = raw_node_info
    if children or type in grammar.number2symbol:
        return pytree.Node(type, children, context=context)
    else:
        return pytree.Leaf(type, value, context=context)


def compile_pattern(pattern):
    return PatternCompiler().compile_pattern(pattern)
# okay decompyling c:\Users\PC\wotsources\files\originals\res_bw\scripts\common\lib\lib2to3\patcomp.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2016.02.14 12:49:04 St�edn� Evropa (b�n� �as)
