import json
import subprocess
import sys

if __name__ == '__main__':
	# Read the json file, then call the asked generator with the given args, then call the asked solver
	if len(sys.argv) <= 1:
		print("Usage: python allCall.py <jsonDataFile.json>")
		exit(1)
	jsonDataFile = sys.argv[1]
	with open(jsonDataFile, 'r') as f:
		jsonData = json.load(f)
	subprocess.check_output("{} {}".format(jsonData["generatorWthArgs"], jsonData["tmpFile"]), shell=True)
	out=subprocess.check_output("python .\src\main.py {} {}".format(jsonData["algorithm"], jsonData["tmpFile"]))
	print(out.decode("utf-8"))