
import re

ln = "LCNO-KAR-73-2015-0100"

res = re.search(r'LCNO-(KAR|KER|APN|TND|TLN|MAH)-([0-6][1-9]|[1-7][0-3])-([2-9][0-9]{3})-((?!0000)[0-9]{4})', ln)

if res:
    print("Match found....")
    print(res.group(0))
else:
    print("Match not found......")

#LCNO-(KAR|KER|APN|TND|TLN|MAH)-([0-6][1-9]|[1-7][0-3])-([2-9][0-9]{3})-((?!0000)[0-9]{4})