import os
import sys
from pathlib import Path

home_dir = str(Path.home())
aliases_path = f"{home_dir}/aliases/aliases.sh"

assert len(sys.argv) == 2, "one required argument : alias_name "
alias_name = sys.argv[1];

curr_dir = os.getcwd()
with open(aliases_path, 'a') as aliases_file:
    aliases_file.write(f"\nalias {alias_name}=\"cd {curr_dir}\"")

