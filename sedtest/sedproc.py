import re
file='myfile'
out='myout'
with open(file, "r") as input:
    lines = input.readlines()
with open(out, "w") as output:
    for id, ln in enumerate(lines): 
        if id == 1:
            var=re.sub(r'^.*', 'components:', var)
        var=re.sub(r'^--', '#--', ln)
        var=re.sub(r'=', ': ', var)
        var=re.sub(r'} {', ': ', var)
        var=re.sub(r'^-', '', var)
        var=re.sub(r'^{', '', var)
        var=re.sub(r'}$', '', var)
        var=re.sub(r'^DB', '', var)
        var=re.sub(r'^db.', '', var)
        if id > 1: 
            var=re.sub(r'^', '  ', var)
        var=re.sub(r'  OVER', '- OVER', var)
        lines[id]=var
        
    output.write(''.join(lines))
