from re import match

f = open("/Users/Nils/MEGAsync/Dokumente/Uni/3. Semester/DH/IntroDH17/La_la_land_script.txt", "r")
script = f.read()

characters = ["MIA", "SEBASTIAN"]
prefix_speaker = True

out = speaker = ""
for line in input():
    # parse all lines beginning with at least one tab
    result = match(r"^(\t+)(\S.*?)\s*$", line)
    if not result:
        continue
    tabs = len(result.group(1))
    text = result.group(2)
    if tabs == 5:
        # dialogue header
        if speaker != text:
            # speaker changed, print what we've got and start over
            if len(out) > 0:
                if prefix_speaker:
                    print ("%s: %s" % (speaker, out))
                else:
                    print (out)
            out = ""
            speaker = text
    elif tabs == 3 and any(c in speaker for c in characters):
        # spoken line
        # append this line to the dialogue, with a space
        if len(out) > 0:
            out += " "
        out += text
    else:
        # ignore all other lines
        pass

# just in case the input ends in the middle of dialogue
if len(out) > 0:
    print (out)
f.close()