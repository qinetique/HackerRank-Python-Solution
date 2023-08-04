#Author: Tonmoy M
#URL: https://qinetique.github.io

regex_pattern = r"[.,]+"	# Do not delete 'r'.

import re
print("\n".join(re.split(regex_pattern, input())))
