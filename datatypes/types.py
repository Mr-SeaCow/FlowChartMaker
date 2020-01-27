datatypes = [
    {'key': 'int'},
    {'key': 'float'},
    {'key': 'double'},
    {'key': 'char'},
    {'key': 'string'},
    {'key': 'bool'}
    ]
reg = ['DATATYPE VARIABLENAME;',
       'DATATYPE VARIABLENAME = VALUE;',
       'DATATYPE VARIABLENAME, VARIABLENAME2;', 
       'DATATYPE VARIABLENAME, VARIABLENAME2 = VALUE;'
       ] # GO UNTIL ;