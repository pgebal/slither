import glob
import subprocess

SOLC_PATH = '/home/pawel/Projects/solidity/build/solc/solc'
SOLC_OPTIONS = '--model-checker-targets all --model-checker-engine all --model-checker-bmc-loop-iterations 20 --model-checker-solvers z3'


def solc_call(file):
    return ' '.join([SOLC_PATH, SOLC_OPTIONS, file])

def slither_call(file):
    return ' '.join(['slither', '--solc', SOLC_PATH, file])


for file in glob.glob("*.sol"):
    with open(file + '_slither', 'w') as f:
        subprocess.Popen(['slither', '--solc', SOLC_PATH, file], stderr=f)
    
    with open(file + '_model_checker', 'w') as f:
        subprocess.Popen([SOLC_PATH, '--model-checker-targets', 'all', '--model-checker-engine', 'all', '--model-checker-bmc-loop-iterations', '20', '--model-checker-solvers', 'z3', file], stderr=f)

