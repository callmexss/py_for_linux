from __future__ import print_function

import fileinput

for line in fileinput.input():
    # meta = [fileinput.filename(), fileinput.fileno(),
    #        fileinput.isfirstline(), fileinput.isstdin()]
    meta = [fileinput.lineno()]
    print(*meta, end=' ')
    print(line, end=" ")
