// Source: https://stackoverflow.com/questions/7583982/bibtex-grammar-for-antlr
grammar bibtex;

//////////////////////////////// Parser rules ////////////////////////////////
parse
  :  (entry (Comma? entry)* Comma?)? EOF
  ;

entry
  :  Type Name Comma tags CloseBrace
  |  StringType Name Assign QuotedContent CloseBrace
  |  PreambleType content CloseBrace
  |  CommentType
  ;

tags
  :  (tag (Comma tag)* Comma?)?
  ;

tag
  :  Name Assign content
  ;

content
  :  concatable (Concat concatable)*
  |  Number
  |  BracedContent
  ;

concatable
  :  QuotedContent
  |  Name
  ;

//////////////////////////////// Lexer rules ////////////////////////////////
Assign
  :  '='
  ;

Concat
  :  '#'
  ;

Comma
  :  ','
  ;

CloseBrace
  :  '}'
  ;

QuotedContent
  :  '"' (~('\\' | '{' | '}' | '"') | '\\' . | BracedContent)* '"'
  ;

BracedContent
  :  '{' (~('\\' | '{' | '}') | '\\' . | BracedContent)* '}'
  ;

StringType
  :  '@' ('s'|'S') ('t'|'T') ('r'|'R') ('i'|'I') ('n'|'N') ('g'|'G') SP? '{'
  ;

PreambleType
  :  '@' ('p'|'P') ('r'|'R') ('e'|'E') ('a'|'A') ('m'|'M') ('b'|'B') ('l'|'L') ('e'|'E') SP? '{'
  ;

CommentType
  :  '@' ('c'|'C') ('o'|'O') ('m'|'M') ('m'|'M') ('e'|'E') ('n'|'N') ('t'|'T') SP? BracedContent
  |  '%' SP? ~('\r' | '\n')*
  ;

Type
  :  '@' Letter+ SP? '{'
  ;

Number
  :  Digit+
  ;

Name
  :  Letter (Letter | Digit | ':' | '-')*
  ;

Spaces
  :  SP -> skip
  ;

//////////////////////////////// Lexer fragments ////////////////////////////////
fragment Letter
  :  'a'..'z'
  |  'A'..'Z'
  ;

fragment Digit
  :  '0'..'9'
  ;

fragment SP
  :  (' ' | '\t' | '\r' | '\n' | '\f')+
  ;