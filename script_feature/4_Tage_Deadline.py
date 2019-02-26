script = """               
            INT. CHURCH - DAY
                         
          We hear the Flash Gordon Wedding March as we ANGLE ON Sam
          J. Jones standing in robes at the altar. Ted, in a tux,
          stands in the best man's position. John stands on the
          steps smiling and looking out as we cut to...
                         
          ANGLE ON Lori, walking down the aisle in a wedding dress,
          smiling warmly. TIME CUT to shortly after, as Sam Jones
          addresses the two of them, standing at the altar.
                        
                          TEDDY
           Hug me.
                         
          John yelps and stumbles back, falling over. He stares at
          Teddy, breathing heavily.
                         
                          JOHN
           Did you... did you just talk?
                         
                          TEDDY
           You're my best friend, John.
                         
                          JOHN
                          (BEAT)
           You're alive?!
                         
                          TEDDY
           Uh-huh.
                         
                          JOHN
           Whoa...
                         
                          TEDDY
           Don't look so surprised. You're the one
           who wished for it, aren't you?
                         
                          JOHN
           Yeah, I... I did wish for it.
                         
                          TEDDY
           Well, here I am.
                         
                          JOHN
           You mean... we get to be best friends...
           for real?
                         
                          TEDDY
           For real.
                         
                          JOHN
           Forever and ever?
                         
                          (CONTINUED)
                          7
                         CONTINUED:
                         
                          TEDDY
           Sounds good to me.
           """

spoken_text = ""

for line in script.split('\n'):
    words = line.split()
    if not words:
        continue

    if len(words[0]) > 1 and all([i.isupper() for i in words[0]]):
        continue

    if len(line) - len(line.lstrip()) > 4:
        spoken_text += line.strip() + ' '

print(spoken_text)
