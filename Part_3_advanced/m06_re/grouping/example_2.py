import re

text = "N1: +48 123 456 789, N2: +123 (98)7 654 321, N3: 987 654 321, N4: 987654321"
pattern = re.compile(r"(?:\+(\d{2,3})[-\s])?\(?(\d{2})\)?(\d[-\s]\d{3}[-\s]\d{3})")
