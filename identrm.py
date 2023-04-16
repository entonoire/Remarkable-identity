import os

labomep = True

calcul = input("\nWrite your calculations here: ")

option1 = "(a)²+2*a*b+(b)²"
option1_labomep = "(a)²+2\\times a\\times b+(b)²"

option2 = "(a)²-2*a*b+(b)²"
option2_labomep = "(a)²-2\\times a\\times b+(b)²"

option3 = "(a)²-(b)²"


def addToClipBoard(text): os.system(f"echo {text} | clip")


#(a+b)²
if "+" in calcul and not "-" in calcul:
	clean = calcul.replace("(", "").replace(")", "").replace("²", "").split("+")
	a = clean[0]
	b = clean[1]

	
	result = option1.replace("a", a).replace("b", b)

	if labomep:
		result_labomep = option1_labomep.replace("a", a).replace("b", b)
		print(f"\nresult: {result}\nlabomep (copied in clipboard): {result_labomep}\n")
		addToClipBoard(result_labomep)
		
	else:
		print(f"\nresult: {result}\n")


#(a-b)²
if "-" in calcul and not "+" in calcul:
	clean = calcul.replace("(", "").replace(")", "").replace("²", "").split("-")
	a = clean[0]
	b = clean[1]

	
	result = option2.replace("a", a).replace("b", b)

	if labomep:
		result_labomep = option2_labomep.replace("a", a).replace("b", b)
		print(f"\nresult: {result}\nlabomep (copied in clipboard): {result_labomep}\n")
		addToClipBoard(result_labomep)

	else:
		print(f"\nresult: {result}\n")


#(a-b)(a+b)
if "+" in calcul and "-" in calcul:
	clean = calcul.split(")(")[0].replace("(", "").split("-")
	a = clean[0]
	b = clean[1]

	
	result = option2.replace("a", a).replace("b", b)

	if labomep:
		print(f"\nresult (copied in clipboard): {result}\n")
		addToClipBoard(result_labomep)

	else:
		print(f"\nresult: {result}\n")
