#Author : Craig Clephane 

#Must remain the same order, do NOT change without authors permission 
TokenEOF, TokenMultiply, TokenDivide, TokenMod, TokenAdd,       \
TokenSubtract, TokenNegate, TokenNOT, TokenLss, TokenLeq,       \
TokenGTR, TokenGEQ, TokenEQ, TokenNeg, TokenAssign,             \
TokenAND, TokenOR, TokenIF, TokenELSE, TokenWHILE,              \
TokenPrint, TokenPutc, TokenLparen, TokenRparen, TokenLbrace,   \
TokenRbrace, TokenSemi, TokenComma, TokenIdent, TokenInteger,   \
TokenString = range(31)

#Must remain the same order, do NOT change without authors permission 
all_syms = ['End_of_File', 'OMulti', 'ODivide','OMod', 'OAdd', 
            'OSub', 'ONeg', 'ONot', 'OLess','OLessequal',
            'OGreater','OperationGreaterequal', 'OperationEqual', 'ONotequal', 'Oassign',
            'OAnd', 'Oor', 'KeywordIF', 'KeywordELSE', 'KeywordWHILE', 
            'KeywordPRINT', 'KeywordPutc', 'LeftParen', 'RightPaaren', 'LeftBrace', 
            'RightBrace', 'SemiColon', 'Comma', 'Identifier', 'Integer', 
            'String']

Symbols = { '{': TokenLbrace,
            '}': TokenRbrace,
            '(': TokenLparen,
            ')': TokenRparen,
            '+': TokenAdd,
            '-': TokenSubtract,
            '*': TokenMultiply,
            '%': TokenMod,
            ';': TokenSemi,
            ',': TokenComma }

#Keywords of the complier
keyWords = { 'if': TokenIF,
             'else':TokenELSE,
             'print': TokenPrint,
             'putc': TokenPutc,
             'while': TokenWHILE }
