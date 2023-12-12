def msg(lang: str,line: int):
	with open(f"lang/{lang}.txt","r") as f:
		return f.readlines()[line].replace("\n","")