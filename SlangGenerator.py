import subprocess
import datetime
from decimal import Decimal
options=str(subprocess.check_output(["ls ~/char-rnn/cv"],shell=True)).split("\\n")
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
word = input("Make up a word and enter it here: ")
temperature = input("Set your desired temperature (0-1, 0.5 reccomended): ")
response = str(subprocess.check_output(['''th ~/char-rnn/sample.lua ~/char-rnn/cv/%s -primetext "%s:" -temperature %s'''%(checkpoint,word,temperature)],shell=True))
response = response[response.rfind(word):]
response = response[:response.find("\\n")]
print(response)
make=input("Write this to html file? (y/n): ")
if "y" in make:
	with open("backgroundtools/urb.htm","r") as template:
		temp=template.read()
	temp=temp.replace("INPUTTERM123",word)
	temp=temp.replace("INPUTDEF123",response[response.find(":")+2:])
	now = datetime.datetime.now()
	short=now.strftime("%b %d")
	longd=now.strftime("%B %d, %Y")
	temp=temp.replace("INPUTSHORTDATE123",short)
	temp=temp.replace("INPUTDATE123",longd)
	with open("backgroundtools/%s.html"%(word),"w") as new:
		new.write(temp)