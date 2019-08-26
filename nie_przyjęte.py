import re

input = r"""
#include <cctype>
#include "errno.h"
"""

pattern = r"#include *(<([a-z]+)(\.h)?>|\"([a-z]+)(\.h)?\")"
word = ""

for i in input:
    if i != '\n':
        word += i
    else:
        sword = re.search(pattern, word)
        if sword is not None:
            print(sword.group(2) or sword.group(4))
        word = ''
