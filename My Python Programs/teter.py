def getfilename(data):
          """C"""
          selfdata = data
          pos = selfdata.find("Name:")
          epos = selfdata.find("\n", pos)
          return selfdata[pos+5:epos]
          print(pos,epos)
out = """Name: treasure obisike\n Name: rex \n"""

print(getfilename(out))
getfilename(out)
