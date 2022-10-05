def make_bitseq(s: str) -> str:
  if not s.isascii():
  	raise ValueError("ASCII only allowed")
  	return " ".join(f"{ord(i):08b}" for i in s)