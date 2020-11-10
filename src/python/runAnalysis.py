import subprocess
import sys
import os

def execute_analysis(jalangi_path, analysis_path, source_path):
    """ This function executes node on a terminal
    """
    command = "node --no-deprecation " + jalangi_path + " --inlineIID --inlineSource --analysis " + analysis_path + " "+ source_path
    subprocess.call(command, shell=True, timeout=10)

    #os.system("node --no-deprecation " + jalangi_path + " --inlineIID --inlineSource --analysis " + analysis_path + " "+ source_path )
"""
if(len(sys.argv) < 4):
    print("Usage: $python runAnalysis.py [jalangi_path] [analysis_path] [source_path]")
    exit(0)

jalangi_path = sys.argv[1]
analysis_path = sys.argv[2]
source_path = sys.argv[3]

j_path = "../jalangi2/src/js/commands/jalangi.js"
s_path = "example/error_example.js"
a_path = "src/js/error_analysis.js"

execute_analysis(j_path, a_path, s_path)"""