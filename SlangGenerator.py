import subprocess
from decimal import Decimal
options=str(subprocess.check_output(["ls cv"],shell=True)).split("\\n")
del options[-1]
options[0]=options[0][2:]
best=3.0
checkpoint=""
for option in options:
	error=Decimal(option[option.rfind("_")+1:option.rfind(".")])
	if error < best:
		error=best
		checkpoint=option
print("Checkpoint chosen: %s"%(checkpoint))
word = input("Make up a word and enter it here: ") + ":"
temperature = input("Set your desired temperature (0-1, 0.5 reccomended): ")
response = str(subprocess.check_output(['''th sample.lua cv/%s -primetext "%s" -temperature %s'''%(checkpoint,word,temperature)],shell=True))
response = response[response.rfind(word):]
response = response[:response.find("\\n")]
print(response)