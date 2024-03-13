class IndentPrinter:

    def __init__(self, *args, spaces=4):
        self.args = args
        self._spaces = spaces
        self._start = 0

    def __call__(self, *args, sep=' ', end='\n'):
        print(' '*self._start*self._spaces, end='')
        print(*args, sep=sep, end=end)

    def __enter__(self):
        self._start += 1
        return self

    def __exit__(self, exc_type, exc_name, traceback):
        self._start -= 1


indent_print = IndentPrinter()
indent_print('No indentation')
with indent_print:
    indent_print('A')
    with indent_print:
        indent_print('B')
        indent_print('C')
    indent_print('D')
    indent_print('E')
indent_print('F')

with IndentPrinter(spaces=2) as indent_print:
    indent_print('A')
    with indent_print:
        indent_print('B')
        indent_print('C', 'D', 'E', sep='$')
    indent_print('F')
    indent_print('G')
