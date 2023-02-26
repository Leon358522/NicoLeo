from automata.pda.dpda import DPDA

'''Paar Tests mit dem Modul'''
# DPDA which which matches zero or more 'a's, followed by the same
# number of 'b's (accepting by final state)
dpda = DPDA(
    states={'q0', 'q1', 'q2', 'q3'},
    input_symbols={'a', 'b'},
    stack_symbols={'0', '1'},
    transitions={
        'q0': {
            'a': {'0': ('q1', ('1', '0'))}  # push '1' to stack
        },
        'q1': {
            'a': {'1': ('q1', ('1', '1'))},  # push '1' to stack
            'b': {'1': ('q2', '')}  # pop from stack
        },
        'q2': {
            'b': {'1': ('q2', '')},  # pop from stack
            '': {'0': ('q3', ('0',))}  # no change to stack
        }
    },
    initial_state='q0',
    initial_stack_symbol='0',
    final_states={'q3'},
    acceptance_mode='final_state'
)

dpda.read_input('ab')  # returns PDAConfiguration('q3', '', PDAStack(('0',)))

dpda.read_input('aab')  # raises RejectionException


dpda.read_input_stepwise('ab')
# yields:
# PDAConfiguration('q0', 'ab', PDAStack(('0',)))
# PDAConfiguration('q1', 'a', PDAStack(('0', '1')))
# PDAConfiguration('q3', '', PDAStack(('0',)))

if dpda.accepts_input(my_input_str):
    print('accepted')
else:
    print('rejected')
    
dpda.copy()  # returns deep copy of dpda
