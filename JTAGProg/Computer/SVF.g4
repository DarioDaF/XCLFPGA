grammar SVF;

/*

  SVF boundary scan subset parser
    Dario Fagotto, 2019

   Version: 1.0

*/

toggleCmd returns [name : str, state : bool]
	: TOGGLE_CMD (
		'ON' {$state = True} | 'OFF' {$state = False}
	) CMD_END {$name = $TOGGLE_CMD.text} ;

expnum : EXPNUM | NUM ;
freqCmd returns [freq : float]
	: 'FREQUENCY' expnum 'HZ' CMD_END {$freq = float($expnum.text)}
	| 'FREQUENCY' CMD_END {$freq = float('+inf')} ;

runtestCmd returns [ticks : int]
	: 'RUNTEST' NUM 'TCK' CMD_END {$ticks = $NUM.int} ;

stateCmd returns [name : str, state : str]
	: STATE_CMD STATE CMD_END {$name = $STATE_CMD.text} {$state = $STATE.text} ;

// Allow spaces between HEXes
hexLiteral : (HEX | NUM)+ ;
hexBlock returns [value : str]
	: '(' hexLiteral ')' {$value = $hexLiteral.text} ;

attr returns [name : str, value : str]
	: ATTR hexBlock {$name = $ATTR.text} {$value = $hexBlock.value} ;

dataCmd returns [name : str, len : int, attrs : dict = {}]
	: DATA_CMD NUM (
		attr {$attrs[$attr.name] = $attr.value}
	)* CMD_END {$name = $DATA_CMD.text} {$len = $NUM.int} ;

cmdShell : stateCmd | dataCmd | runtestCmd | freqCmd | toggleCmd ;

svf : cmdShell* ;

COMMENT : ('!' | '//') .*? '\n' -> skip ;
WS : [ \t\r\n]+ -> skip ;

NUM : [0-9]+ ;
HEX : [0-9a-f]+ ;
EXPNUM : NUM 'E' NUM ;
CMD_END : ';' ;

TOGGLE_CMD : 'TRST' ;

STATE_CMD : 'ENDIR' | 'ENDDR' | 'STATE' ;
STATE : 'IDLE' | 'RESET' ;

DATA_CMD : 'TIR' | 'HIR' | 'TDR' | 'HDR' | 'SIR' | 'SDR' ;
ATTR : 'TDI' | 'TDO' | 'SMASK' | 'MASK' ;
