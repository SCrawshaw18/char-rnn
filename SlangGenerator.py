import subprocess
options=str(subprocess.check_output(["ls cv"])).split("\n")
best=3.0
checkpoint=""
for option in options:
	error=float(option[option.rfind("_"):option.rfind(".")])
	if error < best:
		error=best
		checkpoint=option
word = input("Make up a word and enter it here: ")
temperature = input("Set your desired temperature (0-1): ")
response = str(subprocess.check_output(['''th sample.lua cv/%s -primetext "%s:" -temperature %s'''%(checkpoint,word,temperature)],shell=True))
print(response)