keywords = [
    {'key': 'if', 'container': False, 'reg': 'if ( CONDITION ) CODE;' },
    {'key': 'if', 'container': True, 'reg': 'if ( CONDITION ) { CODE; }' },
    {'key': 'ifelse', 'container': False, 'reg': 'if (CONDITION) CODE; else CODE; ' },
    {'key': 'ifelse', 'container': True, 'reg': 'if (CONDITION) { CODE; } else CODE; ' },
    {'key': 'ifelse', 'container': True, 'reg': 'if (CONDITION) { CODE; } else { CODE; } ' },
    {'key': 'switch', 'container': True, 'reg': 'switch (STATEMENT) { case CONDITION: case CONDITION: break; default: CODE;}'}
]