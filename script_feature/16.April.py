import re
import codecs
from nltk import word_tokenize
from collections import Counter, defaultdict
from pprint import pprint
import matplotlib.pyplot as plt


#Liest Script ein
#f = open("/Users/Nils/women-in-movies/script_feature/Test files/Ted_script.txt", "r")
script = '''
TED


                         
                                   Written by

                  Seth Macfarlane, Alec Sulkin & Wellesley Wild




          EXT. SPACE - X
                         
          As the Universal logo completes itself, we begin to
          slowly push in on the East Coast of the United States.
          The camera glides down through the atmosphere, through
          the clouds, closer and closer, until we begin to see
          large patches of snow covering the upper coastline. It's
          winter. We continue to push in, until we arrive at one
          small suburban neighborhood. Over the push-in, we hear
          the following narration, delivered by Patrick Stewart.
                         
           NARRATOR (V.O.)
           It has been said that magic vanished from
           our world a long time ago. And that
           humanity can no longer fulfill its
           desires through the power of wishes.
           To those who have lost the wondrous
           vision of childhood eyes, submitted here
           is the story of a little boy, and a
           magical Christmas wish that changed his
           life forever.
                         
                         
          EXT./ESTAB. A SUBURBAN NEIGHBORHOOD - MORNING
                         
           NARRATOR (V.O.)
           It began in 1985, in a town just outside
           Boston.
                         
          We see a GROUP OF KIDS laughing and tossing snowballs at
          each other in the street.
                         
           NARRATOR (V.O.)
           It was Christmas Eve, and all the
           children were in high spirits. That
           special time of year when Boston children
           gather together and beat up the Jewish
           kids.
                         
          Another little kid walks out of his house with a sled,
          and starts walking up the street. One of the snowball-
          throwing kids points at the sled kid.
                         
                          KID #1
           Hey, Greenbaum!
                         
                          GREENBAUM
           Uh oh.
                         
                          KID #1
           It's Jesus' birthday tomorrow! You know
           what I'm gonna get him?
                         
                          GREENBAUM
           W...what?
                          (CONTINUED)
                          2
                         CONTINUED:
                         
                          KID #1
           My fist in your fuckin' face!
                         
                          GREENBAUM
           Why would Jesus want that?
                         
                          KID #2
           Get him!
                         
          The kids all chase Greenbaum up the street, and tackle
          him. Another boy, JOHN BENNETT (about 8 years old, shy
          and innocent-looking) approaches the melee.
                         
           NARRATOR (V.O.)
           But there was one child who wasn't in
           such good spirits. Little John Bennett.
           That one boy in every neighborhood who
           just has a tough time making friends.
                         
                          JOHN
           Hey guys, can I play?
                         
          The kids all look at him.
                         
                          KID #1/#2/#3
           Get outta here! / Get outta here,
           Bennett! / Get lost, Bennett!
                         
          The Jewish kid, his face bloodied, looks angrily at John.
                         
                          GREENBAUM
           Yeah, Bennett, get outta here!
                         
          The kids go back to beating up Greenbaum, as John sadly
          walks back toward his house.
                         
          INT. JOHN'S BEDROOM - SHORTLY AFTER
                         
           NARRATOR (V.O.)
           John longed with all his heart for that
           one true friend that he could call his
           own. And he knew that if he ever found
           that friend, he would never let him go.
                         
          John sadly sits by his window with his chin in his hands,
          looking outside. John'S POV - We see the other kids all
          playing in the snow: building snowmen, throwing
          snowballs, etc. At one point, a BLACK KID IN A
          WHEELCHAIR wheels up. The other kids welcome him with
          open arms, and he immediately joins in the fun.
                         
           NARRATOR (V.O.)
           Well, as it does every year, Christmas
           morning finally came.
                          (MORE)
                          (CONTINUED)
                          3
                         CONTINUED:
           NARRATOR (V.O.) (CONT'D)
           All the children were opening their gifts
           with holiday glee.
                         
                         
          INT. A SUBURBAN HOUSE - MORNING
                         
          A LITTLE GIRL opens a present as her parents look on,
          smiling. Inside is a My Little Pony. She smiles with
          delight.
                         
                         
          INT. ANOTHER SUBURBAN HOUSE - MORNING
                         
          A LITTLE BOY opens a present as HIS PARENTS look on,
          smiling. Inside is a G.I. Joe Hovercraft. The boy is
          overjoyed.
                         
          INT. A THIRD SUBURBAN HOUSE - MORNING
                         
          ANOTHER LITTLE BOY opens a present as his parents look on,
          smiling. Inside is a "Darth Vader head" action figure case.
          The boy opens it up, revealing that it's full of "Star Wars"
          action figures. The boy jumps around ecstatically.
                         
                         
          EXT./ESTAB. A FOURTH SUBURBAN HOUSE - MORNING
                         
                         
          INT. A FOURTH SUBURBAN HOUSE - SAME
                         
           NARRATOR (V.O.)
           And for little John Bennett, Christmas
           Day brought a very special new arrival.
                         
          John sits amidst unwrapped gifts. We see him opening a
          present. Inside is a plush, adorable-looking teddy bear.
          The boy holds it with delight.
                         
                          JOHN
           Wow!
                         
          HIS MOM AND DAD hug him.
                         
                          JOHN'S DAD
           I guess Santa paid attention to how good
           you were this year, huh?
                         
                          JOHN'S MOM
                          (KISSING HIM)
           Merry Christmas, John.
                         
          John hugs the teddy bear. It makes a cutesy, high-
          pitched "I wuv you" sound. John gasps with delight.
                         
                          (CONTINUED)
                          4
                         CONTINUED:
                         
                          JOHN
           He talks!
                         
          John giggles happily, squeezing the bear to make it talk,
          as his mom and dad exchange a smile.
                         
                          JOHN (CONT'D)
           I'm gonna name you Teddy.
                         
                         
          INT. JOHN'S HOUSE - LIVING ROOM - DAY
                         
          John sits on the floor watching the 1980 film "Flash
          Gordon" on TV. He eats Twizzlers with Ted sitting next
          to him. Occasionally he gives Ted a "bite."
                         
           NARRATOR (V.O.)
           John became instantly attached to Teddy.
           There was something about that bear that
           made him feel as if he finally had a
           friend with whom he could share his
           deepest secrets.
                         
                         
          INT. JOHN'S ROOM - NIGHT
                         
                          JOHN
           Hey Teddy... can I tell you something
           nobody knows?
                         
          Teddy looks back at him, expressionless.
                         
                          JOHN (CONT'D)
           Last week, my mom and dad took me to the
           park for a picnic. And they have this
           duck pond there, and... when nobody was
           looking, I pooped in my hand and threw it
           at a duck. Was that mean?
                         
          He squeezes Ted, who once again makes the "I wuv you"
          sound.
                         
                          JOHN (CONT'D)
                          (HUGGING HIM)
           I love you too, Teddy!
                         
          John gets into bed with the teddy bear, and snuggles with
          it.
                         
                          JOHN (CONT'D)
           You know... I wish you could really talk
           to me. Because then we could be best
           friends forever and ever.
                         
                         
                          (CONTINUED)
                          5
                         CONTINUED:
                         
          John drifts off to sleep. The camera moves toward the
          window, and drifts outside. It pulls back from the house
          slowly.
                         
           NARRATOR (V.O.)
           Now, if there's one thing you can be sure
           of... it's that nothing is more powerful
           than a young boy's wish.
                          (BEAT)
           Except an Apache helicopter. An Apache
           helicopter has machine guns and missiles.
           It is an unbelievably impressive
           complement of weaponry. An absolute
           death machine. Well, as it turned out,
           John picked the perfect night to make a
           wish.
                         
          EXT. JOHN'S HOUSE - CONTINUOUS
                         
          The camera pivots around to face the sky. We see the
          snow falling from moonlit clouds. At the center of the
          clouds, there is a small patch of open air through which
          we can see stars. Suddenly, a shooting star whizzes by
          through the opening.
                         
                         
          INT. JOHN'S BEDROOM - CONTINUOUS
                         
          SLOWLY PUSH IN on the teddy bear's face as John lies
          sleeping next to it.
                         
                          DISSOLVE TO:
                         
                         
          EXT. NEIGHBORHOOD - NEXT MORNING
          The house and yard are covered with snow.
                         
                         
          INT. JOHN'S BEDROOM - SAME
                         
          John slowly opens his eyes. He turns over to face Teddy,
          but we see that Teddy is no longer next to him. John
          bolts upright and looks around, frantically.
                         
                          JOHN
           Teddy?
           (beat, a bit more concerned)
           Teddy?!
                         
                         
                         
                         
                          (CONTINUED)
                          6
                         CONTINUED:
                         
          John looks under the covers, but the bear is not there.
          He jumps out of bed and looks around the bed's perimeter,
          assuming that Teddy must have fallen off during the
          night. Finally, he checks underneath the bed. ANGLE
          FROM UNDERNEATH THE BED we see John looking around.
                         
                          JOHN (CONT'D)
           Teddy?
                         
          John sits up again and freezes, looking right into the
          camera, wide eyed. ANGLE ON JOHN'S P.O.V.: We see the
          face of Teddy staring right at him. Teddy blinks once.
                         
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
                         
          A huge grin spreads across John's face. He gets up, runs
          to Teddy and hugs him.
                         
           NARRATOR (V.O.)
           John was just about the happiest boy in
           the world. And he couldn't wait to tell
           everyone the good news.
                         
                         
          INT. KITCHEN - SHORTLY AFTER
                         
          John's Dad sits at the breakfast table, reading the paper
          as John's Mom prepares eggs and bacon, putting it on
          their plates.
                          JOHN'S MOM
           Well, I think we had a wonderful
           Christmas this year.
                         
                          JOHN'S DAD
           One of the best.
                          (SLYLY)
           And I particularly enjoyed the gift you
           gave me last night.
                         
          John runs into the kitchen.
                         
                          JOHN
           Mom! Dad! Guess what?! My teddy bear's
           alive!
                         
          John's Mom and Dad look at each other and smile.
                          JOHN'S MOM
                          (PLAYING ALONG)
           Really, sweetie? Well, that's exciting.
                         
                          JOHN
           No mom, he's alive! For real! Look!
                         
          Teddy walks in and stands next to John.
                         
                          TEDDY
           Merry Christmas, everybody!
                         
          John's Dad scrambles to his feet, knocking plates off the
          table. John's mom screams.
                         
                          JOHN'S DAD
           Jesus H. Fuck!
                         
                         
                          (CONTINUED)
                          8
                         CONTINUED:
                         
                          TEDDY
           Let's all be best friends!
                         
                          JOHN'S MOM
           Oh my god...
                         
                          JOHN'S DAD
           John, get away from that thing! Come
           over here, right now!
                         
                          JOHN
                          BUT DAD--
                         
                          JOHN'S DAD
           GET OVER HERE!
                         
          John reluctantly walks over to his dad, who grabs him and
          protectively pulls him aside.
                         
           JOHN'S DAD (CONT'D)
           Helen, get my gun.
                         
                          JOHN
           Dad, no!
                         
                          TEDDY
           Is it a hugging gun?
                         
                          JOHN'S DAD
           Helen, get my gun, and call the police!
                         
                          TEDDY
           I'm sorry, Mr. Bennett. I didn't mean to
           scare anybody. I just wanted John and I
           to be friends.
                          JOHN
           Yeah, Dad! I made a wish last night that
           Teddy was alive, and my wish came true!
                         
                          JOHN'S MOM
                          (ASTONISHED WHISPER)
           My god, Steve... it's a miracle. A
           Christmas miracle.
                         
          They stare at Teddy for a beat.
                         
           NARRATOR (V.O.)
           Well, it wasn't long before the story of
           John's little miracle was sweeping the
           nation.
                          9
                         
                         
           INT. NEWSROOM - DAY (ON TV)
                         
           We see an 80's NEWSCASTER behind the news desk. A
           graphic of the bear is over his left shoulder.
                         
                          NEWSCASTER
           Out of a Boston suburb comes what is,
           without a doubt, the most incredible
           story in the history of broadcast news...
                         
                          DISSOLVE TO:
                         
                         
           INT. DIFFERENT NEWSROOM - DAY (ON TV)
                         
           We see an 80's FEMALE NEWSCASTER. A graphic of the bear
           is over her left shoulder.
                          FEMALE NEWSCASTER
           ...young boy's stuffed animal has
           magically come to life for as yet unknown
           reasons. Scientists are stumped as to
           how...
                         
          AA18 INT. ANOTHER NEWSROOM - DAY (ON TV) AA18
                         
           We see a `70S SOUTHERN NEWSCASTER with a CHYRON that says
           "ACTION NEWS GEORGIA". He points manically at the
           graphic of the bear above his left shoulder.
                         
                          SOUTHERN NEWSCASTER
           Look what Jesus did! Look what Jesus
           did! Look what Jesus did!
                         
                         
           INT. JAPANESE NEWSROOM - DAY (ON TV)
           A MALE JAPANESE NEWSCASTER and FEMALE JAPANESE NEWSCASTER
           sit behind the desk. Between them, at the top of the
           screen, is a picture of the bear.
                         
                          FEMALE NEWSCASTER
           (SPEAKS JAPANESE FOR A FEW MOMENTS)
                         
           The male newscaster turns sharply to her.
                         
                          MALE NEWSCASTER
           (ADDRESSES HER ANGRILY IN JAPANESE)
                         
           He strikes her for an unclear reason. She buries her
           head in her hands, in shame.
                          10
                         
                         
          INT. TONIGHT SHOW - DAY (ON TV)
                         
           NARRATOR (V.O.)
           Before long, Teddy had become a huge
           celebrity in his own right.
                         
          We see REAL FOOTAGE of "The Tonight Show" from the `80's,
          with Johnny Carson talking to Teddy, who is sitting in
          the guest chair (If appropriate footage is accessible,
          will include Teddy walking out on stage, shaking hands
          with Johnny and sitting down.)
                         
          REST OF CARSON SCENE TBD BASED ON ARCHIVE FOOTAGE
                         
                         
          INT. A SHITTY APARTMENT - NIGHT
                         
          INT. JOHN'S BEDROOM - NIGHT
                         
          John and Teddy are in bed, under the covers with a
          flashlight.
                         
           NARRATOR (V.O.)
           But through all the fame, Teddy never
           forgot his very best friend, John.
                         
           JOHN (O.S., UNDER COVERS)
           The thunder can't get us, right?
                         
           TEDDY (O.S., UNDER COVERS)
           Nope. We're thunder buddies. And the
           thunder knows it. We're totally safe.
                         
          ANGLE UNDER THE COVERS - we now see them.
                          JOHN
           Teddy?
                         
                          TEDDY
           Yeah, John?
                         
                          JOHN
           Do you promise we'll always be together?
                         
                          TEDDY
           I promise.
                         
          Another thunder clap.
                         
                          TEDDY (CONT'D)
           Thunder buddies for life.
                         
                          JOHN
           Thunder buddies for life.
                          (CONTINUED)
                          11
                         CONTINUED:
                         
          They hug as we PULL BACK SLOWLY, dissolving through the
          covers.
                         
           NARRATOR (V.O.)
           And that was a promise that neither one
           of them ever forgot.
                         
          Over the following, we continue to pull back from the
          room to the outside of the moonlit house...
                         
           NARRATOR (V.O.)
           So where are John and Teddy today? Well,
           let me put it this way: no matter how big
           a splash you make in this world, whether
           you're Corey Feldman, Frankie Muniz,
           Justin Bieber, or a talking teddy bear,
           eventually nobody gives a shit.
           SMASH CUT TO:
                         
                         
          EXT. BOSTON SKYLINE - MORNING
                         
          We PAN ACROSS the Boston skyline as the opening titles
          roll. CUT TO various shots of the city throughout.
                         
          PAN DOWN to the streets below: several shots of the
          everyday bustle of the city, then we CUT TO:
                         
                         
          INT. YOUNG JOHN'S HOUSE - DAY (PHOTO)
                         
          Young John and Ted lie on the floor as they both grin at
          the camera, chins resting on their hands.
                         
          EXT. BACKYARD - DAY (PHOTO)
                         
          Young John and Ted wave to the camera from up in a
          treehouse.
                         
          A NEWSWEEK MAGAZINE COVER SLIDES BY - It shows Ted
          shaking hands with Reagan. The headline reads:
          "America's Little Miracle". Smaller headlines read,
          "Goodbye Heart Disease, Here Comes Oat Bran!" and "The
          Future of Entertainment: The Laserdisc."
                         
          A US NEWS COVER SLIDES BY - It shows Ted standing in
          front of an American flag. The headline reads, "Ted,
          White, and Blue". Smaller headlines read, "Oliver North
          Draws the Heat" and "Will Your Town Soon Have Its Own
          `Robocop'?"
                          12
                         
                         
          EXT. SUBURBAN STREET - DAY (EXISTING FOOTAGE)
                         
          (Insert existing soapbox racer bit here)
                         
                         
          EXT. PARK (PHOTO)
                         
          Ted and young John blow out the candles on a birthday
          cake at John's ninth birthday party.
                         
                         
          INT. LOCKER ROOM - DAY (PHOTO)
                         
          Larry Bird stands with young John, who has Ted standing
          on the top of his head. They are still nowhere near as
          tall as Larry.
          A TV GUIDE COVER SLIDES BY: It shows a smiling Ted with
          the headline "TV'S NEW FAVORITE GUEST STAR!" Smaller
          headlines read, "Inside: The Best Show You're Not
          Watching!" and "The Unstoppable Phil Hartman!"
                         
          WE CUT TO TBD FOOTAGE OF "WHO'S THE BOSS?" INTO WHICH
          TED HAS BEEN INSERTED.
                         
                         
          INT. YOUNG JOHN'S HOUSE - NIGHT
                         
          Young John and Ted sit on the couch smiling and laughing
          as they watch the show.
                         
                         
          EXT. STREET - NIGHT (PHOTO)
                         
          Young John wears a hooded sweatshirt as he pedals his
          bike up the street. Ted sits in the front basket, like
          E.T.
                         
          ANGLE ON a People magazine from 1992 that reads, "UP
          CLOSE AND PERSONAL WITH `TERMINATOR 2's ARNOLD
          SCHWARZENEGGER!" Down below in smaller print it says
          "Plus, we talk to Ted the bear".
                         
                         
          EXT. STREET - DAY (PHOTO)
                         
          Teenage John and Ted lean against a car. Teenage John
          looks indifferent and a bit jaded now.
                         
                         
          EXT. SCHOOL - DAY (PHOTO)
                         
          John's high school graduation.
                         
                         
                          (CONTINUED)
                          13
                         CONTINUED:
                         
          ANGLE ON A TV - The nightly news is in progress. A news
          anchor addresses the camera. A graphic next to her reads
          "FORMER CELEBRITY BUSTED AT AIRPORT", with an
          unflattering photo of Ted.
                         
                         
          INT. AIRPORT - DAY (VIDEO)
                         
          We see Ted getting hauled away by security. A caption
          below reads "Ted caught with mushrooms at airport
          security". He's putting up a bit of a fight, and gives
          the "finger" to the camera (the finger is pixilated).
                         
                         
          INT. JOHN'S ROOM - NIGHT (EXISTING FOOTAGE)
                         
          We see 20 year-old John sitting on his bed, laughing.
          Ted sits by his side, also laughing at the incident.
                         
                         
                         
                         
          EXT. A MOVIE THEATER - NIGHT (EXISTING FOOTAGE)
                         
          (Insert existing "Phantom Menace" bit)
                         
                         
          INT. CHUCK E. CHEESE - DAY (EXISTING FOOTAGE)
                         
          (Insert existing Chuck E. Cheese bit)
                         
          ANGLE ON A FACEBOOK PAGE FOR JOHN BENNETT: PAN DOWN to
          the status indicator. It reads, "In a Relationship With
          Lori Collins." An arrow clicks on her name, going to her
          page. On her wall, it reads "Lori has added 3 new photos
          in the album Mobile Uploads".
                         
                         
          EXT. OUTDOOR FAIR - DAY (PHOTO)
                         
          Lori and John smile as Lori holds a big stuffed bear that
          John has won for her at a booth. Ted stands nearby, arms
          crossed, with a deep, disapproving scowl.
                         
                         
          EXT. PARK - DAY (PHOTO)
                         
          In the photo, presumably taken by John, Lori stands
          laughing as Ted stands behind her (standing on something)
          covering her eyes with his paws.
                          14
                         
                         
          EXT. STABLES - DAY (PHOTO)
                         
          John and Lori are set for a trail ride. They are both on
          horses, wearing helmets. WIDEN TO REVEAL Ted, who also
          wears a helmet, but rides a smiling golden retriever.
                         
                         
          EXT. MINIATURE GOLF COURSE - NIGHT (EXISTING FOOTAGE)
                         
          John, Lori, and Ted play miniature golf. Lori putts the
          ball, which rolls to the lip of the cup. She reacts,
          disappointed. Ted makes a graceful leg sweep, pushing
          the ball into the cup "accidentally". Lori smiles. John
          smiles back at her. Ted winks.
                         
                         
          EXT. BASEBALL GAME - DAY (EXISTING FOOTAGE)
          (Insert "Jeter sucks" bit)
                         
                         
          EXT. LAKE - DAY (EXISTING PHOTO)
                         
                         
          EXT. ICE CREAM SHOP - DAY
                         
          John, Lori and Ted sit outside at a table, each holding
          an ice cream cone. They stare deadpan at the camera,
          each with a dab of ice cream on their noses, and a dab of
          ice cream on their upper lips.
                         
                         
          EXT./ESTAB. - JOHN AND LORI'S APARTMENT - DAY
                         
                         
          INT. JOHN AND LORI'S APARTMENT - DAY
          John and Lori paint the apartment walls. Lori sneaks up
          behind John, and paints his back. John turns around and
          grabs her. They scuffle playfully, and then kiss. We
          ANGLE ON Ted, who stands on a little stepladder hammering
          a "Home Sweet Home" picture into the wall. He steps
          back, but realizes he has nailed his hand to the wall.
          He tugs, slips, and the ladder falls. Ted hangs there
          like an idiot.
                         
                         
          INT. JOHN AND LORI'S APARTMENT - NIGHT (PHOTO)
                         
          John, Lori, and Ted sit on the couch. All three sit with
          their legs crossed, faux-pretentiously raising glasses of
          Jorian Hill Syrah to camera in identical poses, the wine
          bottle on the table in front of them.
                          15
                         
                         
          INT. JOHN AND LORI'S APARTMENT - NIGHT (PHOTO)
                         
          We see a photo Ted has taken of himself. In the
          background are John and Lori, playing Scrabble. Ted is
          in the foreground, smiling at the camera as he holds up
          his letters. He has spelled out the word "DOUCHE", with
          an extra B and G to spare.
                         
                         
          INT. JOHN AND LORI'S APARTMENT - NIGHT
                         
          John, Ted, and Lori watch a horror movie on the couch.
                         
                         
          EXT. BOSTON COMMON - DAY (EXISTING FOOTAGE)
                         
          (Insert existing John/Lori swan boat footage.)
                         
          EXT./ ESTAB. JOHN AND LORI'S APARTMENT - MORNING
                         
                         
          INT. JOHN AND LORI'S APARTMENT - SAME
                         
          CLOSE ON a bong. PULL OUT TO REVEAL Ted, who inhales,
          his snout inside the tube. Ted sits on the sofa, and for
          the first time, we see Ted in his present day form: he is
          ratty, patched-up, and worn-looking. He has a couple
          stains, some small spots of exposed stuffing, and there's
          evidence of some half-assed sewing. It's obvious he's
          been around for three decades. He and John, who sits
          next to him, are both clearly stoned as we join them.
          John, for his part, looks far too comfortable in the too-
          worn Red Sox T-shirt he wears. He eats directly from a
          box of Fruity Pebbles. Reaching in for a last handful,
          he finds the box almost empty. He raises it to empty the
          remainder into his mouth, and accidentally pours Fruity
          Pebbles all over his face. It doesn't faze him much,
          though, as he brushes them off. It's quite obvious that
          this is a guy who has never really given up his
          childhood... and has never given up his teddy bear. Ted
          passes the bong to John.
                         
                          TED
           All I'm sayin' is Boston women are are,
           on the whole, a paler, uglier sort than
           women from the elsewheres of life.
                         
                          JOHN
           That's bullshit, what about Lori? She's
           hot.
                         
                          TED
           Lori's from Pennsylvania, not a Boston
           girl.
                          (CONTINUED)
                          16
                         CONTINUED:
                         
                          JOHN
           They're not that bad.
                         
          John takes a hit from the bong over Ted's next line.
                         
                          TED
           The fact that you have to say they're not
           that bad means that they are that bad.
           They turn into drunk, half-white, half-
           pink monsters after 2 hours at any beach.
                         
          Ted takes a hit from the bong.
                         
                          TED (CONT'D)
                          (COUGHS)
           Jesus, this is weak. It's not even
           gettin' me high. I gotta have a talk
           with my weed guy.
                         
                          JOHN
           I-- It's workin' for me.
                         
                          TED
           I think it sucks, I'm gonna have a talk
           with him.
                         
                          JOHN
           Yeah, I don't know that you wanna go to a
           drug dealer with complaints.
                         
                          TED
           No, I know this guy a long time. I've
           known him since 9/11. Remember, I was
           like, "Aw, shit. 9/11. I gotta get
           high."
                          JOHN
           (looks at his watch)
           Oh fuck, is it nine-thirty? Shit, I
           gotta get to work.
                         
          John gets up, and hurries into the other room to get
          dressed.
                         
                          TED
           Hey, you mind pickin' up a bird feeder on
           the way home? I wanna start enjoying the
           beauty of birds.
                         
           JOHN (O.S.)
           Jesus, I don't know if I can drive.
                         
                          TED
           I'll drive you, I feel fine.
                          17
                         
                         
          EXT. BOSTON STREETS - CONTINUOUS
                         
          We see two shots of John's car driving through the city:
          We see John in the passenger's seat putting Visine into
          his eyes, with only Ted's ears and eyes showing as he
          drives (his paws grip the wheel). We then cut to an
          overhead pull-back shot as we move away from the car to
          reveal it crossing Boston's huge suspension bridge.
                         
                         
          EXT. LIBERTY RENT-A-CAR - MORNING
                         
          John's car pulls up the street and into the parking lot,
          scraping its side against the corner headlight of one of
          the rental cars.
                         
                          JOHN/TED
           Aw, Jesus. / Fuck.
                         
          ANGLE ON Ted's feet. There are wooden blocks attached to
          the pedals so that his feet can reach them. He slams on
          the brakes. ANGLE OUTSIDE THE CAR. John gets out, and
          looks at the damage.
                         
                          JOHN
           Aw, man.
                         
                          TED
           Is it bad?
                         
                          JOHN
           It's not good.
                         
          ANGLE ON THE RENT-A-CAR OFFICE - THOMAS, the branch
          manager, an intense, middle-aged man, is standing in the
          doorway.
                          THOMAS
           John! May I speak with you, please?
                         
                          JOHN
           Shit.
                         
                          TED
           It's okay, go, go, I'll pull outta here.
                          (WAVING)
           Hi, Thomas! How are ya?
                         
          Thomas dryly waves back. Ted pulls forward, scraping the
          car again. He abruptly pulls out into traffic, and
          another car swerves a bit to get around him, honking.
                         
                          OTHER DRIVER
           Asshole!
                         
                          (CONTINUED)
                          18
                         CONTINUED:
                         
                          TED
                          (OVERLAPPING)
           Easy, Jersey license!
                         
          Ted drives away.
                         
                         
          INT. THOMAS' OFFICE - SHORTLY AFTER
                         
          Thomas sits at his desk facing John.
                         
                          THOMAS
           John, it's almost ten o'clock.
                         
                          JOHN
           I know, I'm sorry, it wasn't my fault.
                          THOMAS
           What do you mean?
                         
                          JOHN
                          (BEAT)
           I guess I... wasn't really prepared for a
           follow-up question.
                         
                          THOMAS
           John, all you have to do is not fuck up,
           and you get my job when I go to corporate
           next month. You will be the new branch
           manager. All you have to do is not fuck
           up, and all you're doing is fucking up.
           Not that I don't think you're too fucked
           up to handle not fucking up my job, but
           you happen to be the least fucked-up
           person in the whole office. The next
           least fucked-up is Alix, and you've been
           here three fucking years longer than him.
           But I'm telling you, I will promote the
           fuck out of him if you fuck up one more
           time. That is all. Fuck.
                         
                          JOHN
           Sir, I promise, you're not gonna regret
           promoting the fuck out of me.
                         
                          THOMAS
           Good. I like hearing that. Because in a
           month my life now could be your life: a
           cushy $38,000-a-year branch manager who's
           personal friends with Tom Skerritt. It's
           not a bad life, is it?
                         
                          JOHN
           N--no.
                         
                          (CONTINUED)
                          19
                         CONTINUED:
                         
                          THOMAS
           Did you know I'm friends with Tom
           Skerritt?
                         
                          JOHN
           No.
                         
                          THOMAS
           I'll show you something I don't show too
           many people, because I don't want anyone
           treating me differently.
                         
          Thomas takes out a framed picture of himself with Tom
          Skerritt.
                         
                          THOMAS (CONT'D)
           That's me and Tom Skerritt.
                          JOHN
                          (SLIGHTLY OVERDONE)
           Wowwww.
                         
                          THOMAS
           Goddamn right, wow. Now get outta here.
           I'm gonna dock you for being late, and
           for the scratch on that car. Try and be
           a little more responsible tomorrow.
                         
                          JOHN
           I will, sir. Thank you. I won't let you
           down, Goose.
                         
                          THOMAS
           What?
                         
                          JOHN
           Top Gun.
                         
                          THOMAS
           So?
                         
                          JOHN
           Tom Skerritt.
                         
                          THOMAS
           Oh.
                         
          John exits.
                         
                         
          INT. LIBERTY RENT-A-CAR FRONT OFFICE - MOMENTS LATER
                         
          John emerges from Thomas' office, and walks out into the
          front desk area.
                         
                          (CONTINUED)
                          20
                         CONTINUED:
                         
          We see his coworker, Guy (a burly Patrick-Warburton
          type), handing a car key and a rental envelope to a
          pleasant-looking couple. He looks tired, disheveled, and
          a little bruised.
                         
                          GUY
           There you go, here's your key and rental
           agreement, and a complimentary map of
           Boston. Thanks for choosing Liberty,
           drive safely.
                         
                          HUSBAND/WIFE
           Thank you./Thanks so much.
                         
          The couple exits. Guy turns to face John.
                         
                          GUY
           Hey, heard you got busted.
                         
                          JOHN
           Jesus, Guy, you look like shit, what
           happened?
                         
                          GUY
           I don't know, man. I got fuckin' wasted
           last night, and my phone says I texted
           somebody at 3:15 asking them to beat me
           up. And then at 4:30 I texted the same
           person saying thanks.
                         
                          JOHN
           And you don't remember it?
                         
                          GUY
           No. Same as last time.
                          JOHN
           It... it just seems gay, doesn't it?
                         
                          GUY
           I don't know. Maybe, yeah.
                         
                          JOHN
           Do you think you're part of some, like,
           gay beat-up underworld? Like one of
           those gay beat-up clubs?
                         
                          GUY
           I don't know. I dig chicks. I don't
           remember any of it, I was so fucked up.
           I might be gay, I don't know. You mind
           covering for me for a bit? I'm gonna go
           lay down in the john.
                         
                         
                          (CONTINUED)
                          21
                         CONTINUED:
                         
          Guy starts to leave, when ALIX, a foreign guy with a
          vague European accent, long dark hair, and a great tan
          walks up.
                         
                          ALIX
           Hey you buddies. Where's it hanging?
                         
                          GUY/JOHN
           Hey Alix. / Hey, how was the club last
           night?
                         
                          ALIX
           Ah, I didn't get in because the bouncer
           was doucheface, but I made friends in the
           line.
                         
                          GUY
           Oh, well, that's good I guess.
                         
          We see TANYA, an unbelievably gorgeous salesgirl, enter
          from the back with a set of keys.
                         
                          TANYA
           Hi you guys.
                         
          Over the following, Tanya puts the keys away, walks over
          to her station and sits.
                         
                          ALIX
           You look so pretty today.
                         
                          TANYA
           Aw, thanks Alix, I worked out this
           morning.
                         
                          ALIX
           I can tell, you are less fat than you
           have been.
                         
                          JOHN
           Hey guys, does anybody know a nice
           restaurant? Like something where the
           napkins are cloth?
                         
                          GUY
           For what?
                         
                          JOHN
           Lori and I have been dating four years
           tomorrow, and I wanted to take her
           someplace nice.
                         
                          TANYA
           Oh wow, congratulations, John.
                         
                          (CONTINUED)
                          22
                         CONTINUED:
                         
                          GUY
           You guys`ve been goin' out for four
           years?
                         
                          JOHN
           Yeah.
                         
                          GUY
                          THAT'S IN--
                          (HIGH-PITCHED)
           --saaaane, my longest relationship was
           like six months, and then she farted in
           her sleep. I'm like, I am outta here,
           man. Was gone before she woke up.
                         
                          JOHN
           Wow, you're... not very tolerant, huh.
                          GUY
           Lori ever fart in front of you?
                         
                          JOHN
           Yes.
                         
                          GUY
           Really.
                         
                          JOHN
           Yes. Many times.
                         
                          GUY
           You Italian?
                         
                          JOHN
           No.
                          GUY
           Oh.
                         
                          JOHN
           Why?
                         
                          GUY
           I dunno, just seems like-- never mind,
           take her to Benihana.
                         
                          TANYA
           Don't you think after four years, maybe
           she's probably hoping for something more
           than dinner?
                         
                          JOHN
           Like what?
                         
                         
                          (CONTINUED)
                          23
                         CONTINUED:
                         
                          TANYA
           Well, if I were her, I'd be expecting a
           proposal.
                         
                          JOHN
           Oh come on, nobody's expecting anybody to
           propose. Marriage isn't... I mean, isn't
           love enough? I submit that love is
           enough.
                         
                          GUY
           You could put the ring in her ass and let
           her fart it out.
                         
                         
          EXT./ ESTAB. JOHN AND LORI'S APARTMENT - LATE AFTERNOON
                         
          INT. JOHN AND LORI'S APARTMENT - SAME
                         
          John and Ted sit on the couch, in the same exact spots we
          saw them earlier, bookending the day. John drinks a beer
          as they watch TV. Ted lights up a bong and inhales. The
          TV blares the opening titles of the 1980 film "Flash
          Gordon." As "Flash's Theme" plays:
                         
                          JOHN
           So bad, but so good.
                         
                          TED
           Yes, a study in contrasts.
                         
                          JOHN
           Oh, I love this part.
                          (SINGING ALONG)
           HE'S FOR EVERY ONE OF US!
                          TED
                          (SINGING ALONG)
           STAND FOR EVERY ONE OF US!
                         
                          JOHN
                          (SINGING ALONG)
           HE'LL SAVE WITH A MIGHTY HAND/EVERY MAN
           EVERY WOMAN EVERY CHILD WITH A MIGHTY
           FLASH!
                         
                          TED
           Fuck yeah, Flash! (then) Hey, before I
           forget, let's nail down a plan for the
           Bruins game tomorrow night.
                         
                          JOHN
           I can't, I'm taking Lori to dinner.
                         
                          (CONTINUED)
                          24
                         CONTINUED:
                         
                          TED
           For what?
                         
                          JOHN
           Well, we've been dating four years
           tomorrow.
                         
                          TED
           Oh, fuck me. Nice.
                         
                          JOHN
           Lemme ask you something... you don't
           think she's gonna be expecting
           something... big, do you?
                         
                          TED
                          (BEAT)
           What, like anal?
                         
                          JOHN
           No, like... a circular gold thing on the
           finger.
                         
                          TED
           Oh, fuck that! It's four years! You and
           I have been together 27 years!
                         
          Ted jumps on John, and starts playfully punching him in
          the face.
                         
                          TED (CONT'D)
           Where's my ring, Johnny? Where's my
           ring, asshole?
                         
                          JOHN
           Stop it! Jesus Christ, knock it off!
          He throws Ted off of him.
                         
                          JOHN (CONT'D)
           I mean, do you think she might be
           expecting me to make that kinda move?
                         
                          TED
           No, John. It's a bad idea. And it's the
           wrong time. What with the economy and...
           the credit bubble... the Supreme Court...
           I mean, look at Haiti.
                         
                          JOHN
           I guess I didn't think about that.
                         
          ANGLE ON TV - We see Flash Gordon facing Ming the
          Merciless.
                         
                          (CONTINUED)
                          25
                         CONTINUED:
                         
           KLYTUS (ON TV)
           Who are you?
                         
           FLASH (ON TV)
           Flash Gordon. Quarterback. New York
           Jets.
                         
                          JOHN
           This is the American fantasy, right here.
           A professional NFL player is called upon
           to save the world.
                         
                          TED
           Tom Brady could do that.
                         
                          JOHN
           Tom Brady could do that.
          The front door opens and LORI, an attractive girl in her
          mid to late 20's, enters holding several grocery bags.
                         
                          LORI
           Hi guys.
                         
                          JOHN
           Hey, sweetie.
                         
                          TED
           Hey, Lori.
                         
          John gets up and gives Lori a kiss.
                         
                          LORI
           Ooh. I think you just got me stoned.
                         
                          JOHN
                          (RE: GROCERIES)
           What do we got there?
                         
                          LORI
           Turkey burgers.
                         
                          TED
           Oh. Okay. Are we having homos over for
           dinner or something?
                         
                          LORI
                          (WISEASS)
           No, just you homos.
                         
                          TED/JOHN
           Whoa!!!
                         
                         
                         
                          (CONTINUED)
                          26
                         CONTINUED:
                         
                          TED
           She's funny, John. You got yourself a
           regular Toni Collette.
                         
                          LORI
           Wait, who's that? Is that good?
                         
                          JOHN
           She's a comedienne.
                         
                          LORI
           Oh nice. Is she pretty?
                         
                          JOHN
           She's as pretty as she is funny. How was
           work?
                          LORI
           Good.
                         
                          JOHN
           How's your dickhead boss?
                         
                          LORI
           Rex is fine. He only hit on me once
           today, so that's good.
                         
                          JOHN
           I'm not saying this to be mean, but I
           really hope that fucker gets leukemia.
                         
                          LORI
           He's harmless, I can handle it.
                         
                          TED
           Hey Johnny, while you're up, grab me a
           beer, huh?
                         
                          JOHN
           (crossing to fridge)
           Oh yeah, a coupla' Charles Brew-Kowskis?
                         
                          TED
           Yes, a Brew-stoy-ovski would be nice
           right about now.
                         
          We see Lori roll her eyes. She's heard this before.
                         
                          LORI
           Jesus.
                         
                          JOHN
           Maybe a Mike Brew-ga-slow-ski?
                         
                         
                          (CONTINUED)
                          27
                         CONTINUED:
                         
                          TED
           Perhaps a Ted Kazyn-brewski?
                         
                          LORI
           Y'know, I think I might also have a
           Martina Navra-ti-brewski.
                         
                          JOHN/TED
           Ohhhh, that doesn't work!/Come on, don't
           ruin it, yeah, that doesn't work.
                         
                          LORI
           Bullshit, what do you mean?
                         
                          JOHN
           It doesn't work, the name has to have a
           "ski" at the end of it. You just put
           "brewski" on the end of Martina
           Navratolova.
                         
                          LORI
           I thought we were just doing funny names.
                         
                          TED
           No, it's gotta have a "ski" at the end.
           Otherwise where's the challenge? If
           there's no "ski" at the end of the root
           word, then we would just be idiots saying
           nonsense.
                         
                         
          EXT./ ESTAB. JOHN AND LORI'S APARTMENT - NIGHT
                         
          It's raining, with an occasional roll of thunder.
                         
          INT. JOHN AND LORI'S APARTMENT - SAME
                         
          Lori lies in bed holding an iPad, reading a gossip news
          site, with the TV on. John comes out of the bathroom,
          and cozies up next to her.
                         
                          LORI
                          (OFF IPAD)
           Oh, look, they found those missing
           hikers.
                         
                          JOHN
           They did? What happened?
                         
                          LORI
           It says they got separated and one of
           them had his foot trapped under a rock
           for five days.
                         
                          (CONTINUED)
                          28
                         CONTINUED:
                         
                          JOHN
           You know, if your leg got trapped under a
           rock, I'd chew it off to get you free.
                         
                          LORI
                          (SWEETLY)
           You would?
                         
                          JOHN
           I sure would.
                          (BEAT)
           Is that cannibalism?
                         
                          LORI
           No, I think it's only cannibalism if you
           swallow.
                          JOHN
           Oh yeah, no, I don't swallow.
                         
          She laughs.
                         
                          LORI
           Really? That's not what I heard about
           you.
                         
                          JOHN
           It's not true, I'm a fuckin' classy
           broad.
                         
                          LORI
                          (LAUGHS AGAIN)
           I can see that.
                          (THEN)
           Y'know, speaking of classy, Ciao Bella's
           a really expensive restaurant. If you
           want, we can go somewhere else tomorrow
           night. I don't care, as long as we're
           together.
                         
                          JOHN
           You kiddin' me? Four years we been going
           out, I'm takin' you to the best place in
           town. I been crappin' out room for it
           for two days, I know exactly what I'm
           gonna order.
                         
                          LORI
           (leaning in to kiss him)
           You're disgusting.
                         
                          JOHN
           And you get to pick any bottle of wine.
                         
                         
                          (CONTINUED)
                          29
                         CONTINUED:
                         
                          LORI
           Ooh.
                         
                          JOHN
           Any bottle of 2012 wine.
                         
                          LORI
           Oh, are the new wines in?
                         
                          JOHN
           They are in and they. Are. Fresh.
                         
                         
          She leans over and kisses him again. He kisses her back.
                         
                          JOHN (CONT'D)
           I love you.
                          LORI
           I love you, too.
                         
          They continue to kiss, becoming more and more intimate.
          She starts to pull his T-shirt off, when there is a
          thunder clap from outside.
                         
                          JOHN
           Ah, come on!
                         
                          LORI
           (shaking her head)
           I don't understand it, 35 years old, and
           you're still scared of a little thunder.
                         
                          JOHN
           I am not.
          We hear another thunderclap. Ted runs into the room with
          no warning and leaps into bed, right between Lori and
          John.
                         
                          TED
           Thunder buddies for life, right Johnny?
           C'mon, let's sing the thunder song!
                         
                          JOHN/TED
                          (SINGING)
           WHEN YOU HEAR THE SOUND OF THUNDER, DON'T
           YOU GET TOO SCARED / JUST GRAB YOUR
           THUNDER BUDDY AND SAY THESE MAGIC WORDS:
           FUCK YOU THUNDER, YOU CAN EAT MY ASS /
           YOU CAN'T GET ME THUNDER, `CAUSE YOU'RE
           JUST GOD'S FARTS.
                         
                          TED
           Boomp.
                          (CONTINUED)
                          30
                         CONTINUED:
                         
          Lori rolls over and goes to sleep with a groan.
                         
                         
          EXT./ ESTAB. BOSTON HIGH RISE - DAY
                         
          Lori enters the building.
                         
                         
          INT. OFFICE - MOMENTS LATER
                         
          Lori gets off the elevator, where we see several signs
          that read "PLYMOUTH PUBLIC RELATIONS." Lori goes to her
          desk, looking exhausted. Lori's office friends, GINA,
          MICHELLE, and TRACY approach.
                         
                          GINA
           Wow...Baby, I'm not saying this to be
           nasty, but you look really tired.
                         
                          LORI
           Oh, I'm okay... except I didn't have time
           for breakfast, the garage was full, I
           spilled coffee on my leg, and I have a
           boyfriend who can't sleep through a storm
           without his teddy bear.
                         
                          GINA
           I don't understand why you keep putting
           up with him.
                         
                          TRACY
           Yeah, I mean, the guy's thirty-five years
           old and he's working for a rental car
           service.
                         
                          LORI
           No, it's not that, I don't care about
           that. I'd love him even if he was a
           janitor. I mean, he's got a huge heart,
           we laugh together all the time, and it's
           just a bonus that he's like the hottest
           guy in Boston.
                         
                          GINA
           Yeah but the hottest guy in Boston is
           like being the classiest Kardashian.
                         
                          LORI
           I just wish he could get his life
           together, you know? Our life. And he
           can't, and I swear to god, it's all
           because of that bear.
                         
                         
                         
                          (CONTINUED)
                          31
                         CONTINUED:
                         
                          MICHELLE
           You should give him an ultimatum: it's
           you or the bear.
                         
                          LORI
           I can't do that, he'd be devastated. And
           I mean... what if he chose Ted?
                         
                          MICHELLE
           Oh come on, you don't really think that.
                         
                          LORI
           Not really, but what if?
                         
                          MICHELLE
           Well then... things happen for a reason.
                          TRACY
           No they don't. That's just something
           girls say when something bad happens to
           them that they don't understand.
                         
                          GINA
           Fuck off, Tracy.
                         
                         
          INT. OFFICE ENTRYWAY - CONTINUOUS
                         
          Lori's boss REX (asshole handsome, mid-30's, expensive
          suit) walks into the office, and approaches the gathering
          of female employees.
                         
                          REX
           Well hello there. Sorry if I'm
           interrupting any private girl talk about
           Channing Tatum's index finger but Lori I
           need to see you in my office.
                         
                          LORI
           Actually Rex, I have a lot of work I need
           to get to--
                         
                          REX
           Oh, this is work, I swear.
                         
                          LORI
                          (SIGH)
           Okay, fine.
                         
          Lori follows Rex and gives the girls a "help!" look.
                         
                          MICHELLE
           He's such an asshole.
                         
                         
                          (CONTINUED)
                          32
                         CONTINUED:
                         
                          GINA
           Out of control. Such a sleaze.
                         
                          TRACY
           You guys are so pathetic. You're
           shitting on Rex, and you both had sex
           with him.
                         
          Short beat.
                         
                          GINA/MICHELLE
           Like once./I was drunk.
                         
                          GINA
           And so did you.
                         
                          TRACY
           Well, I didn't want one of you whores
           getting promoted before me.
                         
                         
          INT. REX'S OFFICE - MOMENTS LATER
                         
          Lori sits across from Rex, who sits at a large desk.
                         
                          LORI
           So... what do you need to talk to me
           about, Rex?
                         
          Rex takes a framed picture out of a drawer, and shows it
          to her.
                         
                          REX
           See that? That's me on the diving team
           in high school. We dove the shit outta
           that pool that year. If you look close,
           you can see the outline of my root.
                         
                          LORI
                          (ANNOYED)
           You promised this was about work.
                         
                          REX
           Lori, what is wrong with you? Why don't
           you like me? I'm rich, I'm good-looking,
           my dad owns the company--
                         
                          LORI
           I have a boyfriend, Rex. I think you
           know this.
                         
                          REX
           Yeah, the guy with the teddy bear, that's
           a cute relationship, but I'm talking
           about being with a real man, Lori.
                          (MORE)
                          (CONTINUED)
                          33
                         CONTINUED:
                          REX (CONT'D)
           Someone who wears a blazer on an
           airplane.
                         
                          LORI
                          (STANDING UP)
           I'm very busy.
                         
                          REX
           Well then, how do you have all that time
           to be in my head?
                         
                          LORI
           Goodbye, Rex.
                         
          Lori exits Rex's office. Rex casually gets up, strolls
          over to her chair, nonchalantly brushes his hand on the
          cushion where she was sitting, and nonchalantly smells
          his hand.
                         
                         
          INT./ ESTAB. CIAO BELLA RESTAURANT, NEWBURY STREET -
                         NIGHT
                         
                         
          INT. RESTAURANT - CONTINUOUS
                         
          John and Lori sit across from each other at a
          romantically set table. They've just finished their
          meal. John has the remains of a lobster shell on his
          plate.
                         
                          LORI
                          (SATISFIED SIGH)
           That was perfect.
                         
          A WAITRESS approaches.
                          WAITRESS
           Would you like me to wrap up your
           leftovers?
                         
                          LORI
           Oh no, I'm fine, thanks.
                         
          John holds up the front portion of the lobster shell,
          which has the face and eyes on it.
                         
                          JOHN
           Actually, could you wrap just this up for
           me? I wanna scare the shit outta
           somebody.
                         
                          WAITRESS
                          (BEAT)
           Sure.
                          (CONTINUED)
                          34
                         CONTINUED:
                         
          The waitress walks away.
                         
                          LORI
                          (MILDLY AMUSED)
           What are you, five years old?
                         
                          JOHN
           Yeah, but I read at a six year-old level.
                         
          Another WAITER approaches with a bottle of champagne, two
          glasses, and some chocolate-covered strawberries.
                         
                          WAITER
           Senor. Senora, here is your dessert and
           champagne.
                         
                          LORI
           Ooh, Cristal.
                         
                          JOHN
           It's a special night. We've been dating
           for four years.
                          (TAKING BOTTLE)
           And hey, all those rich black people
           can't be wrong, right?
                         
                          LORI
           It doesn't seem like four years, does it?
                         
                          JOHN
           (affectionately taking her
                          HAND)
           No, it doesn't.
                         
                          LORI
           You had no business being out on that
           dance floor, but I'm glad you were.
                         
                         
          INT. CLUB - NIGHT (FLASHBACK)
                         
          We see Lori out on the dance floor, amidst a sea of
          dancing clubgoers. Nearby, we see John dancing with a
          girl, and doing it very badly. He's putting too much
          into it, obviously trying to impress her. The girl is
          gamely tolerating it, but is clearly not digging the
          moves. John thrusts his butt back in one move,
          accidentally bumping a girl behind him with enough force
          to send her sprawling on the floor. As the crowd reacts
          to this, we see that it is Lori. She starts to get up,
          when John turns and rushes to help her to her feet.
                         
                          JOHN
           Oh my god, are you okay? Oh god, I'm so
           sorry!
                          (CONTINUED)
                          35
                         CONTINUED:
                         
                          LORI
           (a little stunned)
           Yeah, I'm... I'm fine.
                         
                          JOHN
           Oh Jesus, I'm so so sorry! I didn't see
           you! It was an accident!
                         
                          LORI
           Well, yeah, I... I would hope it was an
           accident.
                         
                          JOHN
           Did you hurt your head?
                         
                          LORI
           Um, yes. My head hurts a lot.
                          JOHN
           Oh, man. Here, let me get you some ice.
                         
          She sits down. He reaches into a nearby glass, pulls out
          a handful of ice, and wraps it in a napkin. He puts it
          against her head. She inhales sharply for a moment.
                         
                          JOHN (CONT'D)
           Sorry. Does it hurt?
                         
                          LORI
           (beat, noticing him for the
                          FIRST TIME)
           N... No. No it's okay.
                         
                          JOHN
           (beat, noticing too)
           I'm... I'm John.
                          LORI
           I'm Lori.
                         
          They smile at each other...
                         
                         
          INT. RESTAURANT - NIGHT (BACK TO SCENE)
                         
                          LORI
           Okay, here's a question that'll show how
           much you actually care about me. You
           remember we stayed and talked until the
           place closed, and then we went for late
           night eggs and waffles, and we stayed
           there til 5 a.m. watching a movie on the
           little TV in the diner. Name the movie.
                         
                         
                          (CONTINUED)
                          36
                         CONTINUED:
                         
                          JOHN
           Octopussy.
                         
                          LORI
           Gold star.
                         
                          JOHN
           But does that show that I care about you,
           or I care about Roger Moore?
                         
                          LORI
           I'm gonna give you the benefit of the
           doubt.
                         
                          JOHN
           Thank you. And by the way, my dancing
           was not that bad.
                          LORI
                          (LAUGHING)
           Your dancing was bad.
                         
                          JOHN
           I had some cool moves.
                         
                          LORI
           So do people with Parkinson's.
                         
                          JOHN
           That's not how I remember it.
                         
                          LORI
           Yeah, how do you remember it?
                         
                         
          INT. SMOKY TAVERN - NIGHT (FLASHBACK)
          We see John leaning against the bar, wearing a white Navy
          officer's uniform, a la Ted Stryker in "Airplane!" as
          "Stayin' Alive" blasts from the jukebox. ANGLE ON LORI,
          who is up on the dance floor, done up like Julie Hagerty.
          John takes his hat off, and tosses it O.S. coolly. He
          struts up to the dance floor, locks eyes with Lori. They
          circle one another for a beat. John suavely takes off
          his jacket, twirls it in the air a few times, and tosses
          it O.S. He then strikes a "finger up" disco pose, with a
          bullet SFX. He and Lori begin disco dancing
          simultaneously. He jumps up, locking his legs around
          Lori, who spins him around in circles, as we cut back to:
                         
                         
          INT. CIAO BELLA RESTAURANT - NIGHT (BACK TO SCENE)
                         
                          LORI
           Whatever you say, baby.
                          (CONTINUED)
                          37
                         CONTINUED:
                         
                          JOHN
           Hey, here's to four more years, huh?
                         
          They clink glasses, and take a sip.
                         
                          JOHN (CONT'D)
           Now I know we said no gifts, but--
                         
                          LORI
           No, we didn't.
                         
                          JOHN
           --But, I got you something anyway, in
           clear violation of the "no gift" rule.
                         
                          LORI
           There was no such rule.
          John reaches into his jacket pocket and pulls out a small
          box. Lori looks excited.
                         
                          JOHN
           Lori, I've wanted to give this to you for
           a long time.
                         
          John slides the box over to Lori. She picks it up.
                         
                          LORI
           Oh, John.
                         
          Lori unwraps the box and opens it. Inside is a pair of
          nice, but not-super-expensive-looking earrings.
                         
                          JOHN
           Those are the ones you liked, right?
           From that kiosk at the mall?
                          LORI
           Oh. Yeah.
                         
                          JOHN
           Check out the card.
                         
          She opens up the card, which we see as John describes it.
          It says, "Happy 4 year anniversary! Love you."
                         
                          JOHN (CONT'D)
           See, I even wrote the words with
           different colored markers so you wouldn't
           get bored while you were reading it.
                         
                          LORI
                          (UNENTHUSED)
           Great. Thanks. Well, um, here. This is
           for you.
                          (CONTINUED)
                          38
                         CONTINUED:
                         
          Lori hands John a small box. He opens it up, revealing a
          very nice watch.
                         
                          JOHN
                          (OPENS BOX)
           Oh wow, a Hamilton!
                         
          He puts it on his wrist.
                         
                          LORI
           I remember you liked it when you saw Tom
           Brady wearing one in GQ.
                         
                          JOHN
           Yeah, I mean his was analog, but this is
           so awesome, I love it!
          She reacts a bit to this.
                         
                          JOHN (CONT'D)
           Y'know, Lori...
                          (INDICATING BOX)
           Someday, there's gonna be a ring in
           there. But I wanna wait `til I can get
           you something really special, y'know? I
           just don't have the money right now.
                         
                          LORI
           John, I don't need the Hope diamond, all
           I want is--
                         
                          JOHN
           I know, but it's important to me that you
           have the engagement ring you deserve.
           And what with the credit bubble... the
           Supreme Court... I mean, look at Haiti.
                          LORI
           Look, I'm only saying this because I love
           you, but that's not realistic. You're
           never gonna have any kind of a career if
           you're always partying and wasting time
           with Ted.
                         
                          JOHN
           Oh, Jesus, here we go--
                         
                          LORI
           John, please get him to find his own
           place, so we can get on with our lives.
                         
                          JOHN
           Look, can we talk about this another
           time, and just enjoy our anniversary
           dinner?
                          (CONTINUED)
                          39
                         CONTINUED:
                         
                          LORI
           Yeah. Fine. Let's talk about it ten
           years from now.
                         
                          JOHN
           (rolling his eyes with a
                          SIGH)
           Lori, we can't talk about this every time
           we go out. Look, he's been my best
           friend since I was eight. And I was not
           a popular child. You have to understand,
           I had no friends before he came along.
           He's the only reason I ever gained any
           fucking confidence. I coulda wound up
           like that Asian kid at Virginia Tech, but
           I didn't. `Cause of him. So, y'know,
           I'm not that psyched to just, like, kick
           him out.
                         
                          LORI
           Well, it's good to know that a talking
           teddy bear is the only thing that kept
           you from gunning down your classmates,
           but John, you're not eight. You're
           thirty-five. And unless you're too blind
           to notice, he's not your only friend
           anymore. You have me. And I love you.
                         
                          JOHN
           I love you, too. You know that.
                         
                          LORI
           Look, I've put the best physical years of
           my life into this. I mean, I'm cute now,
           but in a few years my body's gonna fall
           off a fucking cliff. Things'll be
           hanging and stretching in ways that might
           scare a man. I need to feel secure in
           the fact that you won't leave me when
           that happens.
                         
                          JOHN
           Not only will I not leave you, it's gonna
           be even better. `Cause I can have sex
           with you, and press your arm fat against
           a comic book so I can see it backwards.
                         
          She laughs. So does he.
                         
                          LORI
           And, my boobs and vagina will all be in
           the same place, so that's a lot less
           movin' around for you.
                         
                         
                          (CONTINUED)
                          40
                         CONTINUED:
                         
                          JOHN
           I can do it all with one hand.
                         
                          LORI
           Exactly, and you can do whatever you want
           with the other hand.
                         
                          JOHN
           I can write a novel. Maybe a bestseller.
                         
                          LORI
           We can achieve critical acclaim and
           become rich just by screwing each other.
                         
          They both laugh hard.
                         
                          JOHN
           Well, I hope these jokes have distracted
           you from the actual problems in our
           relationship.
                         
                          LORI
                          (SIGH)
           We can't put the real conversation off
           forever, John.
                         
                          JOHN
           I dunno, I got a lotta fuckin' jokes.
                         
                         
                         
          EXT. JOHN AND LORI'S APARTMENT BUILDING - NIGHT
                         
          Their car pulls up. They start to get out.
                         
                          JOHN
                          (NOTICING)
           Ah shit, hang on, my phone fell under the
           seat somewhere. Can you call it?
                         
          Lori punches his number on her cellphone. After a beat,
          we hear The Imperial March from "The Empire Strikes
          Back."
                         
                          LORI
           That's my ringtone?
                         
                          JOHN
           (laughs, embarrassed)
           Oh, yeah...
                         
                          LORI
           What is it? It sounds negative.
                         
                         
                          (CONTINUED)
                          41
                         CONTINUED:
                         
                          JOHN
           No, it's from The Notebook.
                         
          He reaches under the seat, fishing for the phone, as she
          goes inside.
                         
                          JOHN (CONT'D)
                          (STRAINING)
           This is gonna take some doin'.
                         
                          LORI
           All right, well I'll see you upstairs.
                         
          He continues digging for the phone, as she walks inside.
                         
                         
          INT. UPSTAIRS HALLWAY - MOMENTS LATER
          Lori walks toward the apartment, but stops as she hears
          loud music coming from inside. She approaches the door
          cautiously and opens it, revealing...
                         
                         
          INT. JOHN AND LORI'S APARTMENT - CONTINUOUS
                         
          Lori enters a haze of pot smoke, and a very much trashed
          apartment (empty bottles, wrappers, etc.). Ted sits on
          the sofa with a small group of trashy-looking women.
          They're watching "Romancing the Stone," which plays very
          loudly on the TV.
                         
                          LORI
           What the hell is all this?!
                         
                          TED
           Lori! Hey, you're home early! The
           ladies and I were just watching
           "Romancing the Stone." Got it on Blu-
           Ray. Came in a two-pack with "Jewel of
           the Nile," but I don't know that we'll
           end up watchin' that one.
                         
                          LORI
           This place is a wreck! Who are these
           girls?
                         
                          TED
           Oh, where are my manners? Lori, this is
           Angelique, Heavenly, Cherene, and
           Sauvignon Blanc. I love you girls.
           Y'know, somewhere out there are four
           terrible fathers I wish I could thank for
           this great night.
                         
          The girls ad-lib "Hello," "Nice to meet you," etc.
                          (CONTINUED)
                          42
                         CONTINUED:
                         
          Lori glances around the room, then SCREAMS as she sees
          something in the corner.
                         
                          LORI
           What is that?!!!
                         
                          TED
           What's what?
                         
                          LORI
           There is... a shit in the corner! On the
           floor! There's a shit!
                         
                          TED
                          (LOOKING OVER)
           Oh man, that's what Dierdre was doin'
           over there in the corner for so long.
           Remember, she was crouched over there and
           I thought she was just makin' a call or
                          SOMETHIN'--
                         
                          LORI
           There is a shit!! On my floor!!
                         
                          TED
           Yeah, she's passed out in the bathroom
           now, she seemed like she was hopped up on
           somethin'. I mean, mystery solved, I
                          GUESS--
                         
                          LORI
           What the fuck!!!!
                         
                          TED
           Lori, if I can-- now this is just
           speculation, but... is it possible that
           this is not so much about the stool in
           the corner, and more about maybe
           tonight's dinner not measuring up to your
           expectations?
                         
                          LORI
           What!!! The fuck!!!
                         
          Lori is speechless with rage. At that moment, we see the
          lobster head poke in aggressively from behind the door.
                         
           JOHN (V.O.)
           RAAARRRR!!
                         
                          TED
                          (POINTING)
           Ahaaaaa!
                         
                         
                          (CONTINUED)
                          43
                         CONTINUED:
                         
           JOHN (V.O., AS LOBSTER)
           Who lives here? I'm comin' to get
           whoever lives here! You owe me lobster
           money!
                         
                          TED
                          (TO GIRL)
           Hahaaa! That's my friend John. Not the
           lobster, the guy runnin' it.
                         
          At that moment, John enters, holding his cell phone.
                         
                          JOHN
           Found my phone.
                         
          He stops, seeing everyone there.
                          JOHN (CONT'D)
           What's goin' on?
           (then, noticing)
           Is that a shit?
                         
                         
          INT./ESTAB. NEW ENGLAND AQUARIUM - AFTERNOON
                         
                         
          INT. NEW ENGLAND AQUARIUM - SAME
                         
          Ted and John walk slowly down the ramp circling the
          massive see-through tank, occasionally stopping to
          observe some of the more bizarre varieties of fish. John
          is oddly restrained. Something is on his mind. As they
          stroll, we see a nearby man keeping an eye on them. He
          seems much more interested in them than in the fish.
          This, we will find out later, is DONNY...
                          TED
           God, there are some fucked up fish out
           there.
                         
                          JOHN
           Yeah.
                         
                          TED
           Jesus, look at that one. Mister tough
           guy fish.
           (tough guy voice:)
           "Hey! Whatsa big idea? Cold fusion?
           Well that is a big idea, I beg pardon!"
           Look at that guy. WASP-y white guy fish.
           (tight-ass white guy voice:)
           "I don't care for some of Conan O'Brien's
           humor. I don't like Irish humor. And
           this food is too flavorful. I don't care
           for flavor in my food."
                          (MORE)
                          (CONTINUED)
                          44
                         CONTINUED:
                          TED (CONT'D)
           (switching to goofy voice as
           a bottle-nosed fish swims
                          BY)
           "Oh hey, sorry I'm late, guys. Hey,
           where's everybody goin'? Any of you guys
           got a tissue? I'm allergic to water."
                         
                          JOHN
           Ted... you gotta move out.
                         
          Ted turns and stares at John for a beat.
                         
                          TED
           Wh... what?
                         
                          JOHN
           It's... it's gotta happen.
          Ted sits down on a bench, a little stunned and dazed.
                         
                          TED
           What...what did I do?
                         
          John looks heartbroken at this response.
                         
                         
          INT. NEW ENGLAND AQUARIUM - MOMENTS LATER
                         
          Ted and John sit side-by-side on a bench next to the
          penguin habitat.
                         
                          JOHN
           Ted, my relationship is at a very
           delicate stage, and, y'know, Lori and I
           may just need a little space right now.
           Plus a hooker took a shit in our
           apartment.
                         
                          TED
           Hey, look, that was a tough night for all
           of us.
                         
                         
          INT. JOHN AND LORI'S APARTMENT - NIGHT - FLASHBACK
                         
          Lori is staring at the O.S. poop in the corner. She is
          trying to pick it up with a shoebox. In the background,
          we can see an almost panicky, grossed-out John peering
          out from behind the bathroom door.
                         
                          LORI
                          (BEYOND DISGUSTED)
           Oh, god!!
                         
                         
                          (CONTINUED)
                          45
                         CONTINUED:
                         
                          JOHN
           Aaaa, what?!
                         
                          LORI
           It's so gross!!
                         
                          JOHN
           Don't tell me, I don't wanna hear about
           it! Did you get it?
                         
                          LORI
           No! Oh my god!
                         
                          JOHN
           Tell me when you get it!
                         
                          LORI
           AAAA, I got some on my thumb!
                         
                          JOHN
           AAAAA! You can never cook with that hand
           again! I'm serious, learn to cook other-
           handed!
                         
                          LORI
           Shit!
                         
                          JOHN
           I'll get the next one, okay?
                         
                         
          INT. NEW ENGLAND AQUARIUM - DAY
                         
                          TED
           She's makin' you do it, isn't she?
                          JOHN
           (giving up the bullshit)
           Yes. But, that doesn't mean we can't
           hang out. We'll hang out all the time!
                         
                          TED
           What about... thunder buddies for life,
           Johnny?
                         
                          JOHN
           I know. Fuck. I just don't know what to
           do here. I know it sucks, but otherwise
           I'm gonna lose her. And I do love her,
           Ted.
                         
                          TED
                          (SIGH)
           I know you do, Johnny.
                         
                          (CONTINUED)
                          46
                         CONTINUED:
                         
                          JOHN
           I'll help you get on your feet out there,
           I promise.
                         
                          TED
           And we'll hang out a lot, right?
                         
                          JOHN
           Fuck, all the time.
                         
                          TED
           (arms wide for a hug)
           Bring it over here.
                         
          John hugs Ted. Ted hugs him back. We hear a squeak, and
          a high-pitched recorded voice saying "I wuv you." John
          and Ted pull away from each other uncomfortably.
           TED (CONT'D) JOHN
          That was the-- the thing-- The old-- Yeah-- no, I know-
          that doesn't mean-- I'm not -
          gay.
                         
                          JOHN
           We've got to get you a job.
                         
                         
          EXT./ ESTAB. GROCERY STORE - LATE AFTERNOON
                         
                         
          EXT. GROCERY STORE - SAME
                         
          John and Ted head toward the store. Ted is dressed in a
          coat and tie, and looks very uncomfortable.
                         
                          TED
           I look stupid.
                         
                          JOHN
           No, you don't. You look dapper.
                         
                          TED
           I look like Snuggles' accountant. 
                         
          They pause as John straightens Ted's tie.
                         
                          JOHN
           Look, I know it sucks, but you gotta make
           some money so you can pay for an
           apartment.
                         
                          TED
           I don't wanna work at a grocery store.
                         
                         
                          (CONTINUED)
                          47
                         CONTINUED:
                         
                          JOHN
           Well, you have no skills.
                         
                          TED
           I told you, I can totally be a lawyer.
                         
                          JOHN
           As I said, you would need a law degree
           from a law school.
                         
                          TED
           I'm a special case. I'm a fucking
           talking bear. They might make an
           exception `cause they're all like, "Aaa!
           This bear can talk and do stuff! Let's
           give him a job and maybe he'll give us a
           few laughs," but then they're surprised
           at what a stellar performance I'm turnin'
           in. And then they practically have to
           give me the Anderson case.
                         
                          JOHN
           Look, you get the job, and we'll
           celebrate after.
                         
          John discreetly pulls out a baggie of weed.
                         
                          TED
           And if I don't get the job will we still
           smoke that pot?
                         
                          JOHN
           Probably, yes.
                         
                          TED
           (patting John on the leg)
           Yeah. Okay, good speech, coach.
                         
                         
          INT. GROCERY STORE MANAGER'S OFFICE - SHORTLY AFTER
                         
          Ted sits opposite FRANK, the grocery store manager. We
          see his name and title on a desk nameplate. Frank sits at
          the desk, staring at Ted.
                         
                          FRANK
           So. You think you got what it takes?
                         
                          TED
           Nope.
                         
                          FRANK
           (a beat, then)
           No one's ever talked to me like that
           before. You're hired.
                          (CONTINUED)
                          48
                         CONTINUED:
                         
                          TED
           Shit.
                         
                         
          EXT. BOSTON COMMON - LATE AFTERNOON
                         
          (Over music:) John and Ted walk across the Common,
          passing various park-goers. The occasional person
          notices and points with a "Hey, isn't that..." sort of
          look. They passes three cute girls who flag Ted down.
          Two pose with him as the third takes their picture with
          her cellphone. Ted poses for the photo with one hand on
          the girl's breast. She laughs hard. Ted waves goodbye,
          and he and John make their way over to a park bench.
          They sit. John takes out the weed, looks around for a
          beat, then starts to discreetly roll a joint.
                          TED
           Well, I'm a former celebrity with a
           minimum wage job. This must be what the
           cast of Different Strokes feels like.
                         
           O.S. VOICE
           Excuse me.
                         
          John and Ted react, startled. John stuffs the weed in
          his pocket, accidentally dropping the buds in the rolling
          papers on the ground.
                         
          ANGLE ON a creepy-looking man glancing at them
          repeatedly. This is Donny, the fat kid we saw in the
          prologue. He has grown up into a thinner but no less
          creepy man.
                         
                          DONNY
           I'm sorry to bother you, but my son and I
           couldn't help but admire your teddy bear.
                         
          ADJUST TO REVEAL his son, who looks exactly like fat
          young Donny from earlier.
                         
                          JOHN
           (a little uncomfortable)
           Oh. Um, thank you.
                         
                          DONNY
           I'm Donny. And this is my boy, Robert.
           I have to tell you, I've been fascinated
           by your story ever since I was a boy. I
           remember seeing you on the Carson show.
           You were just wonderful.
                         
          BRIEF ANGLE ON the ground, where a pigeon is pecking at
          the dropped weed.
                         
                          (CONTINUED)
                          49
                         CONTINUED:
                         
                          TED
           Yeah, that was ah... that was a good
           time.
                         
                          DONNY
                          (TO JOHN)
           I wonder, is there any chance I could
           purchase the bear from you? For my son?
                         
                          JOHN/TED
           Huh? / Excuse me?
                         
                          ROBERT
                          (CALM)
           I want it.
                         
                          TED
           Hey, I'm not an "it", pal. I'm a "he."
                         
                          JOHN
           (leaning down to his level)
           I'm sorry, little guy, but my bear isn't
           for sale. I've had him since I was about
           your age. He's very special to me.
                         
                          ROBERT
           Sit up straight when you talk to me.
                         
                          JOHN
                          (RECOILING)
           Ew, why the fuck did he say that?
                         
                          DONNY
           Don't swear in front of my child. Now.
           We are very interested in the bear. If
           you'd like to work out some sort of
           arrangement, here's my address and phone
           number.
                         
          He writes on a slip of paper and hands it to John. John
          smiles awkwardly and puts it in his wallet.
                         
                          JOHN
           Okay. Will do. Here it goes, in the
           really important pocket for really
           important stuff.
                         
          Donny and Robert walk off. Donny turns and steals a
          glance back at Ted as they move off.
                         
                          TED
           Wow. Can you imagine what that little
           shit would do to me?
                         
                         
                          (CONTINUED)
                          50
                         CONTINUED:
                         
                          JOHN
           Oh man, I can totally see him just taking
           you down to the basement and really
           slowly de-limbing you while singing some
           creepy Victorian nursery rhyme.
                         
          John tugs on one of Ted's arms trying to creep him out.
          He then breaks into a creepy falsetto.
                         
                          JOHN (CONT'D)
           OH, MY LITTLE SIXPENCE/MY PRETTY LITTLE
           SIXPENCE/I LOVE MY SIXPENCE BETTER THAN
           MY LIFE.
                         
                          TED
           Fuck you. Why do you have to take it so
           far? Now it's real. Fuck you again for
           that. C'mon, let's go find a better
           place to get stoned.
                         
          They exit. After a beat, the pigeon flies into frame,
          slamming right into a fucking tree.
                         
                         
          EXT. ESTAB. A SHITTY APARTMENT BUILDING - NIGHT
                         
          John and Ted walk into the building. John carries two
          cardboard boxes, and Ted carries one smaller one.
                         
                         
          INT. AN ALMOST EMPTY APARTMENT - SAME
                         
          There's a couch, a coffee table, and a couple of boxes.
          John and Ted put down their boxes, and stand just inside
          the doorway.
                          JOHN
           Well... I guess this is it, huh?
                         
                          TED
           Yeah, sure is.
                         
                          JOHN
           First night on your own.
                         
                          TED
           Yeah. First night in my beautiful new
           apartment. They say they're ain't hardly
           been no murders here.
                         
          They awkwardly nod to each other, both knowing that John
          must leave soon.
                         
                          JOHN
           Okay... so... if you need anything...
                          (CONTINUED)
                          51
                         CONTINUED:
                         
                          TED
           I know.
                         
                          JOHN
           Seriously, anything...
                         
                          TED
           I know. I'll be fine, Johnny.
                         
                          JOHN
                          (BEAT)
           I know you will, buddy.
                         
          They regard each other for a moment, then John slowly
          turns and walks off down the hall. He turns back to
          smile and wave. From John's POV, we see a diminutive-
          looking Ted give a wan wave back. He looks very alone as
          the camera recedes.
                         
          INT. JOHN AND LORI'S LIVING ROOM - DAY
                         
          John sits on the couch, putting his tie on as he watches
          TV. Lori comes over and sits down next to him.
                         
                          LORI
           Hey there.
                         
                          JOHN
           Hey.
                         
                          LORI
           Listen... I just wanna say thank you.
           What you did with Ted was a big step, and
           I know it wasn't easy, but I just want
           you to know that I love you for it. And,
           I think this a new beginning for our
           relationship.
                         
                          JOHN
           Hey, anything for you. This is all part
           of the new grown up, adult John Bennett.
           So, get used to him.
                         
          She gives him a kiss, and starts to undo his tie.
                         
                          LORI
           Y'know, I don't have to be at work for
           another twenty minutes...
                         
                          JOHN
           (guiding her down onto the
                          COUCH)
           Ooh, that's perfect, I'm only gonna need
           one.
                         
                          (CONTINUED)
                          52
                         CONTINUED:
                         
          She laughs, and they kiss.
                         
                          LORI
           You know what my favorite thing about you
           is? After four years, you can still
           surprise me. To step up and change such
           a big part of your life just to make your
           girlfriend happier... I dunno, I bet you
           most guys couldn't do it.
                         
                          JOHN
           Most guys don't have you to motivate `em.
                         
                          LORI
           I'm sorry if I was pushy about it...
                         
                          JOHN
           No, you were right! Look, the reason I
           love you so much is the same reason I
           guess I take you for granted sometimes.
           It's `cause you're... inevitable.
                         
                          LORI
           (huh?)
           Inevitable. Well, that's... romantic? I
           think?
                         
                          JOHN
           No, what I mean is, there's just no
           version of this universe where you and I
           don't end up together. You're
           inevitable.
                         
                          LORI
           That sounds like something Stephen
           Hawking would say to his girlfriend.
                          JOHN
           But do you get what I'm saying?
                         
                          LORI
           Yeah, I do. And I feel exactly the same
           way about you.
                         
          They kiss.
                         
                          LORI (CONT'D)
           (smiling coyly, as she
                          NOTICES)
           Ooh. Is that a Flash Gordon ray gun in
           your pocket or are you glad to see me?
                         
          John pulls the Flash Gordon gun out of his pocket and
          shows it to her. She cracks up.
                          53
                         
                         
          EXT./ESTAB. GROCERY STORE - DAY
                         
                         
          INT. GROCERY STORE - SAME
                         
          Ted is at his station, finishing checking out a customer.
                         
                          TED
           Thank you, please come again, we have a
           lot more groceries.
                         
          The customer exits. Ted sighs with boredom. He turns to
          ELLEN, the large African-American woman at the next
          station.
                         
                          TED (CONT'D)
           Hey Ellen?
                          ELLEN
           Yeah?
                         
                          TED
           Who's that over there?
                         
          ANGLE ON A VERY ATTRACTIVE blonde girl bagging groceries
          a few aisles away (This is TAMI-LYNN).
                         
                          ELLEN
           That's the new bag girl. I don't know
           her name, but she seems cute.
                         
                          TED
           Yeah. Very cute. You know what I'd like
           to do to her? Somethin' I call a Dirty
           Fozzie.
          Ted waves to the girl. She waves back. He makes a kissy
          face at her. She giggles and blows him a kiss back. He
          pantomimes hard, thrusting, standing-up sex. Her eyes
          widen for a beat, as she stares, then smiles. He grabs
          an Oh Henry bar, and pantomimes fellatio. The girl
          laughs hysterically. CLOSE ANGLE on Ted, as white liquid
          sprays all over his face from one side, then from the
          other. WIDEN to reveal he's squirting two bottles of
          pump hand soap on either side of him. The girl laughs
          and shakes her head "no."
                         
                          TED (CONT'D)
                          (TO HIMSELF)
           Okay, so that's where we'll draw the
           line.
                         
                         
          EXT. ESTAB./ LIBERTY RENT-A-CAR - DAY
                          54
                         
                         
          INT. LIBERTY RENT-A-CAR - SAME
                         
          John sits at his workstation, playing a TBD video game on
          his iPhone. Tanya approaches.
                         
                          TANYA
           Hey. How you holding up?
                         
                          JOHN
           Oh, I'm all right. Just... getting used
           to things, that's all.
                         
                          TANYA
           It's gonna be all right. Y'know, I went
           through something like this with my last
           boyfriend.
                          JOHN
           Really?
                         
                          TANYA
           Yeah, we were dating for eight months,
           and I was really in love with him, and
           then he was deported back to Iran. So, I
           get it.
                         
                          JOHN
           Oh... yeah. So... I guess we both lost
           our furry little guy.
                         
                          TANYA
           Yeah.
                         
          John's phone rings the theme from "Knight Rider." He
          sees Ted's name pop up, with a photo of Ted smiling open-
          mouthed at the camera, with his arms outstretched and a
          bra on his head. John picks up.
                         
                          JOHN
           Hey, Ted.
                         
           TED (V.O.)
           Johnny. What are you doin'? You wanna
           come over and catch a buzz?
                         
                          JOHN
           I could probably swing by after work.
                         
           TED (V.O.)
           Fuck that, I traded off yesterday, so I
           got the night shift. C'mon, I'm bored as
           crap over here, just swing by for a bit.
                         
                         
                         
                          (CONTINUED)
                          55
                         CONTINUED:
                         
                          JOHN
           I can't just ditch work, man. Look, I'm
           trying to get my shit together and be an
           adult here, y'know? For Lori's sake.
                         
                         
          INT. TED'S BATHROOM - DAY
                         
          Ted sits in the tub, talking on the phone. He has suds
          in his hair, and there are a couple of little toy boats
          in the water. From here, we intercut back and forth from
          him and John.
                         
                          TED
           John. Five minutes. And then I'll kick
           you out, I promise. C'mon, I picked up
           the "Cheers" DVD box set, and supposedly
           everybody talks shit about each other in
           the interviews.
                         
                          JOHN
           Really?
                         
                          TED
           Yeah, and apparently George Wendt
           confesses to a rape.
                         
                          JOHN
                          (BEAT)
           Sometimes adults get high.
                         
                          TED
           They do, John. Sometimes they do.
                         
                          JOHN
           You'll kick me out in five.
           TED (V.O.)
           John, I have to kick you out. I am
           extraordinarily busy today, I have so
           much teddy bear paperwork to get through,
           it is retarded. Five minutes and you're
           outta here.
                         
          John turns and looks back at Thomas in his office.
                         
                          JOHN
           What do I tell Thomas?
                         
                          TED
           Just tell him you don't feel well.
                          56
                         
                         
          INT. THOMAS' OFFICE - MOMENTS LATER
                         
          John stands in front of Thomas, who sits at his desk.
                         
                          JOHN
           I gotta duck out for a bit. Lori tried
           to break up a dog fight, and I guess she
           got hurt pretty bad.
                         
                          THOMAS
           Oh my god.
                         
                          JOHN
           Yeah, she's-- that's the way she is, she
           sees trouble, she tries to help out, and
           I guess one of these dogs clamped his
           jaws on her forearm, and he wouldn't let
           go until the fireman showed up and had to
           stick his finger in his ass.
                         
                          THOMAS
           Jesus, John.
                         
                          JOHN
           Yeah, she's pretty shook up.
                         
                          THOMAS
           Oh my god.
                          (BEAT)
           Up the dog's ass, right?
                         
                          JOHN
           Yeah, that's how they--
                         
                          THOMAS
           That's how they get `em to stop biting,
           sure.
                         
                          JOHN
           Yeah.
                         
                          THOMAS
           Go go go, take care of it, let me know
           how she is.
                         
                          JOHN
           Oh gosh, thank you, sir. I owe you one.
                         
                          THOMAS
           You don't owe me anything, go.
                         
          John smiles wanly, and exits.
                         
                         
                         
                          (CONTINUED)
                          57
                         CONTINUED:
                         
                          THOMAS (CONT'D)
           (looking at his own finger)
           Jesus.
                         
                         
          EXT./ ESTAB. TED'S NEW APARTMENT - DAY
                         
                         
          INT. TED'S NEW APARTMENT - SAME
                         
          ANGLE ON THE TV - Ted Danson sits in a chair, being
          interviewed.
                         
                          TED DANSON
           Was there cocaine on the set of "Cheers"?
           Hm. Lemme figure out the best way to
           answer that. Um...are there naked dicks
           in gay porn?
                          (LAUGHS WARMLY)
           Yes, there was quite a lot of cocaine. I
           mean, it was the eighties. And I was
           king. I was king of the eighties. I was
           Ted fucking Danson. And not only that, I
           was Sam fucking Mayday Malone. Was I
           popular? Gee, lemme think: are there
           naked dicks in gay porn?
                          (LAUGHS WARMLY)
           Yes, I was quite beloved.
                         
          ANGLE ON Ted and John watching. They have a bong.
                         
                          JOHN
           You know, he's exactly who you want him
           to be.
                         
                          TED
           He is. He is. Someone the likes of
           which we should all aspire to become.
                         
          ANGLE BACK ON TV -
                         
                          TED DANSON
           Woody Harrelson. Smallest dick I've ever
           seen on a man.
                         
          ANGLE BACK ON John and Ted -
                         
                          TED
           (passing him bong)
           Here, try this stuff. I told my guy to
           step it up, and he gave me this.
                         
                          JOHN
           What is it?
                         
                          (CONTINUED)
                          58
                         CONTINUED:
                         
                          TED
           It's called Kennedy's Head. It's
           actually pretty mellow.
                         
                          JOHN
           That doesn't sound very mellow.
                         
                          TED
           No, it's-- it makes you cerebral. Like
           Kennedy. Kennedy was smart. That's what
           it refers to. Decisions under pressure.
           Cuban missile crisis. Go on, spark it
           up.
                         
          John takes a hit off the bong, then glances around.
                         
                          JOHN
           Y'know, this place looks great.
                         
                          TED
           Yeah, it's all Ikea. Did the whole
           apartment for 47 dollars.
                         
                          JOHN
           How are the neighbors?
                         
                          TED
           There's an Asian family next door, but
           they don't have a gong or nothin', so
           it's fine.
                         
                          JOHN
           That's lucky.
                         
                          TED
           How's work?
                          JOHN
           Sucks.
                         
                          TED
           Ah.
                         
                          JOHN
           You?
                         
                          TED
           It's actualy not bad. Met a girl. She's
           a bagger.
                         
                          JOHN
           No way, that's awesome. We should double
           date, you, me Lori and, what's her name?
                         
                         
                          (CONTINUED)
                          59
                         CONTINUED:
                         
                          TED
           White trash name. Guess.
                         
                          JOHN
           Uh, Mandy?
                         
                          TED
           Nope.
                         
                          JOHN
           Madison?
                         
                          TED
           Nope.
                         
                          JOHN
           Britney, Tiffany, Candice?
                          TED
           Nope.
                         
                          JOHN
           Don't fuck with me on this. I know this
           shit.
                         
                          TED
           I know you do, and I am not fucking with
           you.
                         
                          JOHN
           Okay, Brandi, Heather, Channing, Breanna,
           Amber, Sabrina, Melody, Dakota, Sierra,
           Bambi, Crystal, Samantha, Autumn, Ruby,
           Taylor, Tara, Tamra, Tami, Lauren,
           Charlene, Chantel, Courtney, Misty,
           Jenna, Krista, Mindy, Noelle, Shelby,
           Trina, Reba, Cassandra, Nikki, Kelsey,
           Shawna, Jolene, Earline, Claudine,
           Savannah, Kasey, Dolly, Kendra, Carla,
           Chloe, Devon, Emmylou, Becky?
                         
                          TED
           Nope.
                         
                          JOHN
           Okay, was it any one of those names with
           a Lynn after it?
                         
                          TED
           Yep.
                         
                          JOHN
           Okay. Brandi-Lynn, Heather-Lynn--
                         
                         
                          (CONTINUED)
                          60
                         CONTINUED:
                         
                          TED
           Tami-Lynn.
                         
                          JOHN
           Fuck!
                         
                         
          EXT. ESTAB. RESTAURANT - NIGHT
                         
                         
          INT. RESTAURANT - SAME
                         
          John, Ted, Lori and Ted's dolled-up and sort of trashy
          date Tami-Lynn (the bag girl from the grocery store) eat
          dinner.
                         
                          TAMI-LYNN
           See, I was all pissed off `cause me and
           my friend Danielle were supposed to go
           skydiving last year, but then she got
           pregnant from this asshole guy, and so we
           couldn't go and I was all upset, but then
           she had a miscarriage, and so we ended up
           getting to go skydiving, and it was so
           scary but it was so much fun.
                         
                          JOHN
           Hey, well... it sounds like everything
           worked out then.
                         
                          TAMI-LYNN
           I guess god wanted me to go skydiving,
           y'know?
                         
                          LORI
           Jesus.
                          TAMI-LYNN
           Or Jesus, yeah, but whatever.
                         
                          TED
           Hey, isn't this great? The four of us
           here, having dinner together? Lori,
           how've you been? Haven't seen you in
           forever.
                         
                          LORI
           Um, I've been good. Not much going on.
           My company's 20th anniversary is next
           week, that's something.
                         
                          JOHN
           (proud, to Tami-Lynn)
           Lori's a senior VP at a big PR firm.
                         
                          (CONTINUED)
                          61
                         CONTINUED:
                         
                          LORI
           It's not that big a deal.
                         
                          TED
           Company's turnin' 20, eh? So you can
           bang it but you can't get it drunk.
                         
          Tami-Lynn laughs heartily at this, as does John. Lori
          isn't quite as delighted.
                         
                          LORI
                          (VISIBLY ANNOYED)
           I'm surprised John didn't tell you
           already. Seems like you guys have seen
           each other every day since you moved out.
                         
                          TED
           Well, it's funny, usually the first item
           on our agenda is "what's goin' on with
           Lori?" So I'm surprised that one slipped
           through the cracks.
                         
                          JOHN
           We do, we talk about you all the time.
                         
                          TED
           Right?
                         
                          JOHN
           Oh my god, remember, Ted, last week we
           were talking about... how... neat all of
           Lori's shoes are?
                         
                          TED
           That was a lengthy conversation.
                          JOHN
           And we were saying like, a lot of women
           look like unsteady horses when they wear
           high heels, but Lori has a sort of...
           regal... trot.
                         
                          TED
           A canter.
                         
                          JOHN
           Oh my god yes. You canter.
                         
          Lori stares at him for a beat, then:
                         
                          LORI
           So, Tami, where are you from? Tell us
           about yourself. I'm always... fascinated
           to meet Ted's girlfriends.
                         
                          (CONTINUED)
                          62
                         CONTINUED:
                         
                          TAMI-LYNN
           What do you mean girlfriends?
                          (TO TED)
           Is there like a lot of `em or somethin'?
                         
                          TED
           No, no, that's not what she's sayin' at
           all, right Lori?
                         
                          LORI
           No, right, I was-- all I was doing was
           asking. Ted's very... attractive, I'm
           just always interested in the... type of
           girl that can snatch him up.
                         
                          TAMI-LYNN
           Did you just call me a whore?
                          LORI
           What? No, I--
                         
                          TAMI-LYNN
           You just worry about your own snatch, how
           `bout that, honey?
                         
                          TED/JOHN
           Whoa! Whoa! Whoa! / What the hell
           happened? We're havin' a friendly meal
           here!
                         
                          TAMI-LYNN
           Don't talk shit to me!
                         
                          LORI
           I was just asking a question.
                          TAMI-LYNN
           You're a friggin' snob! You think you're
           all cool cause you work at some fancy
           shit place!
                         
                          TED
           It's okay, Tami.
                          (TO LORI)
           Nice, Lori. Real nice.
                         
                          LORI
           What?! It's not my fault she can't speak
           English.
                         
                          TAMI-LYNN
           Fuck you! Just `cause you're all in the
           business world and shit, you think
           everyone's supposed to like, suck your
           asshole!
                          (CONTINUED)
                          63
                         CONTINUED:
                         
                          TED
           Baby! Baby! Baby. Baby. Let's get outta
           here. We'll go back to my place for a
           couple vodka and strawberry Quiks. Okay?
           See ya, John.
                         
          Ted and Tami Lynn exit leaving John and Lori at the
          table.
                         
                          LORI
           What a cunt.
                         
                          JOHN
           (covering ears in pain)
           Ooh! I hate that word.
                         
                          LORI
           Huh?
                         
                          JOHN
           That word is so sharp. It's like an
           electric sword, slashing everything in
           its path.
                         
                          LORI
           Well, you didn't exactly stick up for me.
                         
                          JOHN
           I... I'm trying to walk a line here, I
           want to be fair to you and to him,
           y'know?
                         
                          LORI
           Yeah, well, I think you're being a little
           more fair to him.
                          JOHN
                          (SCOFFING)
           Come on.
                         
                          LORI
           Y'know, your boss called this morning and
           asked me how my arm was.
                         
                          JOHN
                          (CAUGHT)
           Oh?
                         
                          LORI
           Yeah. Because of the dog fight I tried
           to break up.
                         
                          JOHN
           Ohh...
                         
                          (CONTINUED)
                          64
                         CONTINUED:
                         
                          LORI
           If I had to hazard a guess, I'd say that
           was some bullshit lie you made up so you
           could take off work and go to Ted's. Am
           I right?
                         
                          JOHN
                          (BEAT)
           I... I made you out to be a hero.
                         
                          LORI
           John, Ted moved out so we could give
           ourselves a chance without him. You're
           not really giving anything a chance if
           you're blowing off work to get high with
           your teddy bear.
                          JOHN
           It won't happen again, I promise.
                         
                          LORI
           (with a bit of anger)
           Yes. It will.
                         
          A beat. She sighs.
                         
                          LORI (CONT'D)
           I wanna break up.
                         
                          JOHN
                          (THROWN)
           W... What?
                         
                          LORI
           I'm just... I'm done. This isn't gonna
           work. We're in two different places.
                          JOHN
           Lori, look, I know--
                         
                          LORI
           You promised me you were gonna grow up
           and take our life together seriously.
                         
                          JOHN
           Hey, Ted moved out, didn't he? I did
           that for you-- for us! And it wasn't
           easy.
                         
                          LORI
           Jesus, he might as well still be living
           with us, John. You spend more time with
           him than you do with me.
                         
                         
                          (CONTINUED)
                          65
                         CONTINUED:
                         
                          JOHN
           Okay, look. I've been getting stoned too
           much. I know that. I've been bumming
           around with Ted too much, I know that,
           too. Give me one more chance, I promise
           I can fix it. Lori, I love you too much,
           please give me one more chance.
                         
                          LORI
                          (BEAT)
           I need a man, John. Not a boy with a
           teddy bear.
                         
                          JOHN
           I know. Done. Man, right here in front
           of you. Look at these pecs. Man pecs.
           Look at the hair on my upper lip. Man
           hair. I just farted. Man fart.
                         
          Lori can't help but let a small laugh escape. She
          softens a bit...
                         
                          LORI
           John... this really is your last chance.
           I can't do this anymore.
                         
                          JOHN
           You won't have to. Trust me. I love
           you.
                         
          He kisses her.
                         
                          LORI
                          (BEAT)
           Okay.
                          JOHN
           Aw, sweetie, I love you so much! You
           won't be sorry, I swear.
                         
          She smiles at him, then:
                         
                          LORI
           Did you really just fart?
                         
                          JOHN
           Yeah, but I pushed it that way with my
           hand.
                         
                          LORI
           Oh. Wonder where it'll hit first.
                         
          WIDER ANGLE on the restaurant. For a moment, nothing
          happens.
                         
                          (CONTINUED)
                          66
                         CONTINUED:
                         
          Then, a guy at a table on the right (sitting with a
          couple other men and women) screams into his napkin,
          followed by his dining companions.
                         
           GUY AT TABLE
                          (FURIOUS)
           Who did this to us?!
                         
           GUY #2 AT TABLE
                          (FURIOUS)
           God dammit! I'm here on business!
                         
                         
          EXT./ESTAB. GROCERY STORE - DAY
                         
                         
          INT. GROCERY STORE - DAY
          Ted's boss, Frank, emerges from the back, writing on a
          clipboard. He looks up, and his expression turns to
          confused anger as he sees an unusually long line at
          Ellen's register.
                         
                          FRANK
           What the hell?
                         
          He walks over to the line. A GUY IN LINE turns and
          notices him.
                         
           GUY IN LINE
           Hey, dude, you think you could open more
           than one register? There's like a
           thousand people here!
                         
                          FRANK
           There's supposed to be three registers
           open, for god's sake!
                         
          He looks around, aggravated, for a moment, then storms
          off toward the back. He looks around the butcher's
          counter and produce area, then walk into the back
          storeroom.
                         
                         
          INT. STOREROOM - MOMENTS LATER
                         
          Frank opens the door, and reacts with shock. REVERSE
          ANGLE where we see Ted on top of Tami Lynn, who is almost
          naked. He is doing a very close approximation of banging
          her wildly. We see his furry bear butt pumping away,
          with its little tail on the end. Frank screams in shock
          and horror.
                          67
                         
                         
          INT. FRANK'S OFFICE - SHORTLY AFTER
                         
          Frank sits at his desk, addressing Ted.
                         
                          FRANK
           You had sexual intercourse with a
           coworker in a storeroom filled with
           produce that we sell to the public.
                         
                          TED
           Yes.
                         
                          FRANK
                          (BEAT)
           That took guts. We need guts. I'm
           promoting you.
                          TED
           Oh.
                         
                         
          EXT. GROCERY STORE - LATER THAT NIGHT
                         
          We see the "CLOSED" sign on the door. Ted exits,
          finishing off a bottle of beer. He walks around to the
          dumpster alley, and lines up for a Kareem-style sky hook
          shot into a trash can. He takes the shot:
                         
                          TED
           Kareem!
                         
          The bottle smashes off the side of the can, and shatters.
                         
                          TED (CONT'D)
           You suck, Kareem.
          We hear a soft footstep somewhere O.S. Ted turns and
          looks around. There appears to be no one in the
          darkness.
                         
                          TED (CONT'D)
           Hello?
                         
          No answer. He looks around for a beat, and finds
          nothing. He turns... and finds himself facing Donny, who
          stands eerily lit by a single outdoor wall bulb.
                         
                          DONNY
           Hello, Ted.
                         
                          TED
           Gah! Uh... hi there.
                         
                          DONNY
           Are you all alone out here?
                          (CONTINUED)
                          68
                         CONTINUED:
                         
                          TED
           Uh... no. No I'm not. I'm... you know,
           you're never alone when you're with
           Christ.
                         
                          DONNY
           You know, Robert and I could give you a
           very, very good home.
                         
                          TED
           I'm... I'm pretty happy where I am. I
           just got a shitty new apartment--
                         
                          DONNY
           I can offer you six thousand dollars in
           railroad bonds. They were left to me by
           my father.
                          TED
           Well, gosh, you know, since I just
           returned from active duty in the Civil
           War, that sounds really appealing. Oh
           wait, no, that was a hundred and fifty
           years ago, and I don't give a shit.
                         
          Tami-Lynn approaches.
                         
                          TAMI-LYNN
           Teddy, come on-- we're gonna have pop
           tarts and cigarettes with my mom before
           she goes to work.
                         
                          TED
           Yeah, I'm comin', sweetheart.
                          (TO DONNY)
           Yeah, my dance card is quite full, so I'm
           gonna have to decline.
                         
                          DONNY
           I really wish you wouldn't...
                         
                          TED
           Yeah, sorry. But, ah... you know, I'd
           like to thank you for creepin' up my
           night, and... Jesus be with you. In
           Christ.
                         
          Ted hurries off. ANGLE ON DONNY, who looks eerily
          determined.
                          69
                         
                         
          EXT./ ESTAB. REX'S HOUSE - NIGHT
                         
          John and Lori walk up to the fabulously expansive house
          in Cambridge. It's a very impressive estate with no
          expense spared.
                         
                          LORI
           (smiling at him warmly)
           I'm glad you're here.
                         
                          JOHN
           Yeah, me too. Is it cool if I kick your
           boss' ass? That won't affect your
           workplace chemistry, will it?
                         
                          LORI
           Play nice. Please.
          Rex throws open the door.
                         
                          REX
           There she is! I was worried you weren't
           coming!
                          (TO JOHN)
           Hi kiddo, how ya doin'? Where's your
           bunny rabbit?
                         
                          JOHN
           He's a bear.
                         
                          REX
           (ushering them in)
           Got it. "Hey, this house is fucking
           huge!" I know guys, try not to get lost.
                         
          INT. REX'S HOUSE - CONTINUOUS
                         
          The party is a very costly-looking event: uniformed
          servers walking around with trays of cocktails and hors
          d'ouvres, tables laden with lavish-looking food displays
          and floral arrangements, a 20-piece big band, and
          hundreds of guests. A large banner reads "Happy 20th
          Anniversary, Plymouth Public Relations."
                         
                          REX
           Oh, here come the ladies.
                         
          Gina, Michelle, and Tracy approach. Everyone adlibs
          their hellos to John and Lori. A waiter walks by with a
          tray of champagne. Lori and the girls each take a glass.
                         
                         
                         
                         
                          (CONTINUED)
                          70
                         CONTINUED:
                         
                          REX (CONT'D)
           Say listen, why don't John and I give you
           gals a chance to talk tampax while we go
           grab a drink at the bar, huh?
                         
                          LORI
           Sure.
                         
                         
          INT. REX'S HOUSE - CONTINUOUS - STAIRS AND UPSTAIRS
                         
          Rex and John are walking up the stairs to the second
          floor of his house. Rex points out various items bought
          at auction. John is visibly unenthused. He does not
          like this guy, and definitely does not trust him.
                         
                          REX
           ...and that's a Wade Boggs autographed
           bat. Just barely outbid Phil Donahue for
           that at auction.
                         
                          JOHN
           Wow, cool.
                         
                          REX
           Yeah, cool. And those boxing gloves were
           worn by Joe Louis in his first fight.
           (passing an abstract
                          PAINTING)
           This is art. Do you get it?
           (passing wall mounted pair of
                          GLASSES) )
           These were John Lennon's glasses. Worth
           about two million dollars.
           (passing photo on wall) )
           That's me and Tom Skerritt. Oh, and
           check this out.
                         
          Rex indicates a small, bronze-colored item on a stand.
                         
                          REX (CONT'D)
           See that? Know what that is?
                         
                          JOHN
                          (TOUCHING IT)
           No.
                         
                          REX
           That's Lance Armstrong's nut.
                         
          John quickly pulls his hand away.
                         
                          REX (CONT'D)
           Something, isn't it? Had it freeze-dried
           and bronzed.
                          (MORE)
                          (CONTINUED)
                          71
                         CONTINUED:
                          REX (CONT'D)
           Every now and then, when I feel like my
           life's gettin' me down and things are
           tough, I just come in here and look at
           it, and it reminds me that things aren't
           so bad. That some people have it worse
           than me. I mean, he's only got one ball,
           and I have three. One of them, of
           course, being his.
                         
                          JOHN
           That's inspiring. You've led a rich
           life.
                         
                          REX
           I've fucked the shit outta life.
                          (THEN)
           So talk to me, Goose. How are things
           with you and Lori?
                         
                          JOHN
           Things are great, actually.
                         
                          REX
           That's good, that's good.
                         
                          JOHN
           You know... Lori would hate me for saying
           this, but... she's told me how you are at
           the office, and... as one gentleman to
           another, I just wanna say I really hope
           you fucking get Lou Gehrig's disease.
                         
                          REX
           Whoa, whoa, okay, look, I think I oughtta
           just clear the air here a little. I...
           just want you to know that... I mean,
           yeah, I'm kind of a "fun-time boss" and
           whatnot, but... look man, I do that with
           everybody at the office! I'm just a
           kook! I have no designs on your
           girlfriend. We work together, and that's
           it. I think you're a great guy and she's
           very lucky.
                         
          John is a bit surprised, not unpleasantly so, to hear
          this.
                         
                          JOHN
           Well... that's good to hear.
                         
                          REX
           Well, that's how it is, so...there we go.
                         
                          JOHN
           Okay.
                          (CONTINUED)
                          72
                         CONTINUED:
                         
                          REX
           Yeah.
                         
          They stand there for a beat, looking at Lance Armstrong's
          nut. John's phone rings the "Knight Rider" theme. John
          answers it.
                         
                          JOHN
           Hey, Ted.
                         
          INTERCUT PERIODICALLY BETWEEN JOHN AND TED, who stands in
          the foreground with one finger in his ear. In the
          background, we see a party in full swing.
                         
           TED (V.O.)
           Johnny! You gotta get over here, man!
                          JOHN
           Why? What's going on?
                         
           TED (V.O.)
           I'm havin' a little impromptu thing with
           some people, and John... Sam Jones is
           here.
                         
                          JOHN
           What?!
                         
           TED (V.O.)
           Sam Jones. Flash fucking Gordon. Is
           here.
                         
                          JOHN
           Holy shit! How?
                         
          INT. TED'S APARTMENT - CONTINUOUS
                         
                          TED
           Remember I said, my buddy's cousin is
           friends with Sam Jones? My buddy's in
           town with his cousin and who's with `em?
           Sam Jones!!
                         
                         
          INT. REX'S HOUSE - CONTINUOUS
                         
           TED (V.O.)
           Sam Jones is here, and John...
           (softly, into phone)
           ...his hair is parted down the middle.
                         
                          JOHN
                          (EQUALLY SOFTLY)
           Just like in the movie.
                          (CONTINUED)
                          73
                         CONTINUED:
                         
                          TED
           Get over here.
                         
                          JOHN
           Fuck! I can't... I'm with Lori. I'm
           already on probation here.
                         
          John looks down at the main area of the party, and sees
          Lori happily chatting with her co-workers.
                         
                          JOHN (CONT'D)
                          (AGONIZED)
           I just... I can't.
                         
                         
          INT. TED'S APARTMENT - CONTINUOUS
                          TED
           John. There are moments in a man's life:
           Nathan Hale, "I regret that I have but
           one life to give for my country." Alan
           Hale, "Yes, I accept the role of the
           Skipper on `Gilligan's Island.'"
                         
                         
          INT. REX'S HOUSE - CONTINUOUS
                         
           TED (V.O.)
           John, this is your Alan Hale moment. For
           god's sake, come share this with me.
                         
                          JOHN
           (beat, then:)
           I'm coming.
                         
          John hangs up.
                          JOHN (CONT'D)
           Rex. I gotta go. I'll be back in thirty
           minutes tops, but Lori cannot find out.
           She absolutely cannot know I was gone.
           If you can cover for me... we're cool on
           all that other stuff.
                         
                          REX
           I got your back, my friend. Been there.
           She'll never know.
                         
                          JOHN
           This is one man to another. I don't
           really know you, but I'm trusting you.
           As a man. This is serious. Can I trust
           you?
                         
                         
                          (CONTINUED)
                          74
                         CONTINUED:
                         
                          REX
           Dude. One man to another. I got you on
           this.
                         
                          JOHN
                          (RELAXING SOMEWHAT)
           Okay. Thank you.
                         
          John races O.S.... and Rex raises his scotch glass to his
          mouth.
                         
                          REX
                          (SMILING)
           I'm gonna make traditional to your
           girlfriend. And then fuck her in the
           ass. All right. We have a game plan.
                         
          EXT. REX'S HOUSE - MOMENTS LATER
                         
          The "Football Fight" music from "Flash Gordon" starts
          playing, as John bolts O.S.
                         
                         
          EXT. REX'S HOUSE - MOMENTS LATER
                         
          John sprints out of the house and runs down the walkway.
          He leaps over a hedge toward the parking area. He slides
          across the hood of Lori's car, gets in, quickly starts
          the car, and backs out.
                         
                         
          EXT. BOSTON (VARIOUS) - NIGHT
                         
          CUT TO various shots of John racing through the city on
          his way to Ted's. Finally, he pulls up to Ted's
          apartment.
                         
                         
          INT. TED'S APARTMENT - MOMENTS LATER
                         
          John throws open the door. The place is as lively as it
          can be. The party is packed with people, including Alix
          and Tanya, John's co-workers from Liberty. There are
          also a large number of booze-swilling guys and hot
          chicks. Ted runs up, wearing a blazer.
                         
                          TED
           Johnny! Thank Christ you made it!
                         
                          JOHN
                          (QUICKLY)
           I got ten minutes, where's Flash Gordon?
                         
                         
                          (CONTINUED)
                          75
                         CONTINUED:
                         
                          TED
           Okay, get ready, man.
           (to someone O.S.)
           Hey, Sam! This is the guy I was tellin'
           you about!
                         
          John turns to look in the direction Ted is indicating.
          The shot slows down into slo-mo as John's eyes widen, and
          he sees...
                         
          OPPOSITE ANGLE - Across the room, SAM J. JONES turns in
          slo-mo to face John. He is inexplicably still sporting
          the same hairstyle he had in the "Flash Gordon" movie.
          We hear the theme from "Flash Gordon." We INTERCUT back
          and forth from him to John:
                         
          ON JOHN - He stands frozen in awe.
          ON SAM - He smiles as he begins to walk toward the
          camera, in John's POV.
                         
          ON JOHN - He continues to stare in frozen awe.
                         
          ON SAM - Still slowly walking toward camera in John's
          POV, but he is now dressed in the Flash Gordon costume.
                         
          ON JOHN - He continues to stare in frozen awe.
                         
                         
          EXT. MONGO SKY - DAY - FANTASY
                         
          Sam J. Jones flies on the flying Jetski from the movie.
          John stands behind him on the back, with his arms around
          Sam's chest, as if on the back seat of a motorcycle.
          John has a huge, elated smile on his face.
                         
          INT. TED'S APARTMENT - BACK TO SCENE
                         
          ON John - He still stares in awe.
                         
          ON SAM - He smiles and offers an outstretched hand for a
          handshake.
                         
          BACK TO NORMAL SPEED - Sam walks up to John with Ted by
          his side.
                         
                          TED
           John, this is Sam Jones. Sam, this is my
           best friend in the whole world, John.
                         
                          SAM
           Hi there. Good to meet you.
                         
                         
                          (CONTINUED)
                          76
                         CONTINUED:
                         
                          JOHN
           (in absolute fucking awe)
           I... thank you for saving every one of
           us.
                         
                          SAM
           You're welcome. Hey, let's do some
           shots, huh?
                         
                          JOHN
           With you? Yes. Oh my god, yes.
                         
          Sam passes out shots of Southern Comfort.
                         
                          SAM
           (raising his glass)
           Death to Ming!
          John and Ted look at each other, squealing with delight.
          Everyone then does their shots.
                         
                          SAM (CONT'D)
           Hey, you guys seem pretty cool.
                          (SIGNIFICANTLY)
           You like to party?
                         
          John and Ted don't answer for a beat. They look at each
          other nervously. It's clear neither one has any
          experience with this sort of thing.
                         
                          SAM (CONT'D)
           Aw, come on dudes. Don't tell me you've
           never done it before.
                         
                          JOHN
           (a little scared)
           Not... recently, no.
                         
                          SAM
           You fellas better come with me.
                         
                         
          INT. TED'S APARTMENT - SHORTLY AFTER
                         
          John, Ted, and Sam emerge from the bathroom. John's eyes
          are wide and enthusiastic. Ted has a little bit of
          powder on his nose, and his ears are flattened back. And
          Sam is just playing it cool.
                         
                          TED
           Wow.
                         
                          SAM
           Let's party like the `80's huh?
                         
                          (CONTINUED)
                          77
                         CONTINUED:
                         
                          TED
                          (REVERENTIAL)
           Show us how, Flash.
                         
                          SAM
           It's easy. We just gotta bang a lotta
           girls named Stephanie.
                         
                          JOHN
           Holy shit.
           (looking around intensely)
           All these people need to be talked to.
                         
                         
          INT. TED'S APARTMENT - LATER
                         
          John and Ted sit staring at each other intensely across
          the table.
                         
                          TED
           Look Johnny, if we're ever gonna get
           serious about openin' a restaurant we
           gotta start plannin' it now.
                         
                          JOHN
           Italian.
                         
                          TED
           Italian, yes.
                         
                          JOHN
           What's the special on Tuesdays?
                         
                          TED
           Eggplant parm.
                          JOHN
           Chopped salad half price.
                         
                          TED
           And it's a non-restricted place.
                         
                          JOHN
           Yeah--wait, whaddaya mean?
                         
                          TED
           Anybody can come.
                         
                          JOHN
           Of course.
                         
                          TED
           Mormons are welcome.
                         
                         
                          (CONTINUED)
                          78
                         CONTINUED:
                         
                          JOHN
           Well yeah--why wouldn't they be?
                         
                          TED
           Exactly, that's what I'm saying.
                         
                          JOHN
           But why even bring that up--
                         
                          TED
           You don't bring it up. You just let `em
           in.
                         
                          JOHN
           Yeah, but why mention it?
                         
                          TED
           No one will.
                         
                          JOHN
           So why are we talking about it?
                         
                          TED
           You're talkin' about it, I'm just sayin'
           let `em in.
                         
                          JOHN
           Yes, let `em in.
                         
                          TED
           Exactly.
                         
                          JOHN
           Right.
                         
                          TED
           Good.
                         
                          JOHN
           Okay.
                         
                          TED
           No Catholics, though.
                         
                         
          INT. TED'S APARTMENT - SAME
                         
          Ted stands opposite a group of party guests who sit on
          the couch. He holds a knife.
                         
                          TED
           No see, I can do this.
                         
                          GUY #1
           Shut up.
                          (CONTINUED)
                          79
                         CONTINUED:
                         
                          TED
           My teddy bear biology gives me superhuman
           reflexes.
                         
                          GUY #2
           Let him try it, man.
                         
                          GUY #1
           Fuck it, all right.
                         
          Guy #1 puts his hand down on the coffee table and Ted
          starts doing the knife trick from "Aliens". He gets it
          right for a few seconds, then stabs the guy right through
          the hand. The guy screams in pain.
                         
                          TED
           Well, you never shoulda trusted me, I'm
           on drugs!
                         
                         
          INT. TED'S APARTMENT - LATER
                         
          John stands with a pair of fake bear ears on his head,
          doing an impression of Ted as a small group of partygoers
          (Ted included) watches, laughing hysterically.
                         
                          JOHN
                          (AS TED)
           Hey Johnny, I just had a great idea--
           let's go get drunk and puke on cars from
           the overpass!
                         
                          TED
           Oh god, that was a fun day.
                         
                          JOHN
                          (AS TED)
           Johnny, you gotta get over here man, I
           just tried this DMT all the kids are
           talkin' about, and I'm in trouble! I
           think I got sucked inside my chair!
                         
                          TED
           I do not sound that much like Peter
           Griffin.
                         
                         
          INT. TED'S APARTMENT - LATER
                         
          Ted sits on the couch drawing a pair of Garfield eyes on
          a topless girl. Below the eyes he has drawn the muzzle
          and the mouth, and above them the ears.
                         
                         
                         
                          (CONTINUED)
                          80
                         CONTINUED:
                         
                          TED
           See? There. Proof. Garfield's eyes
           look like a pair of tits.
                         
                          TAMI-LYNN
           Okay, you were right.
                         
                         
          INT. TED'S APARTMENT - LATER
                         
          Ted stands by the TV, singing a karaoke version of "I
          Only Want to be with You" by Hootie and the Blowfish.
                         
                          TED
           Okay, Johnny, c'mon up here and do this
           with me!
                          JOHN
           No no.
                         
                          TED
           Come on!
                         
                          JOHN
           No, I don't sing in front of people!
                         
                          TED
           YOU AND ME, WE COME FROM DIFFERENT
           WORLDS. YOU LIKE TO LAUGH AT ME WHEN I
           LOOK AT OTHER GIRLS. SOMETIMES YOU'RE
           CRAZY AND YOU WONDER WHY I'M SUCH A BABY
           `CAUSE DOLPHINS MAKE CRY. WELL THERE'S
           NOTHING I CAN DO I'VE BEEN LOOKING FOR A
           GIRL LIKE YOU. YOU LOOK AT ME YOU'VE GOT
           NOTHING LEFT TO SAY. I'LL ONLY POUT AT
           YOU UNTIL I GET MY WAY. I WON'T DANCE.
           YOU WON'T SING. I JUST WANT TO LOVE YOU
           BUT YOU WANT TO WEAR MY RING. WELL
           THERE'S NOTHING I CAN DO. I ONLY WANNA BE
           WITH YOU. YOU CAN CALL ME YOUR FOOL, I
           ONLY WANNA BE WITH YOU.
                         
                         
          INT. TED'S BEDROOM - LATER
                         
          Sam, John and Ted stand by the wall.
                         
                          TED
           See there's this one part of the wall
           that's really soft, you could punch
           through it wicked easy.
                         
          Sam punches the wall a couple times, and his fist goes
          right through.
                         
                          (CONTINUED)
                          81
                         CONTINUED:
                         
           SAM/TED/JOHN
           Holy shit! / Ha! / Wow! / Etc.
                         
          Immediately we see half an Asian face dart into frame
          through the hole. He screams in Cantonese, then,
                         
                          ASIAN MAN
           What the hell you problem!! You break my
           wall! You break my wall I break you
           wall!
                         
          The neighbor sticks a knife through the hole. John, Ted,
          and Sam scream. Sam and John jump around and scream as
          they frantically try to get the knife.
                         
                          JOHN
           AAA! AAA!! Break his arm, Flash! Cut
           his arm off!!
                         
          Sam grabs the arm, and it darts back inside.
                         
                         
          INT. TED'S APARTMENT - MOMENTS LATER
                         
          There's an angry pounding on the door. One of the party
          guests opens it, and the Asian guy runs in, screaming in
          Cantonese. He holds a wooden spoon in one hand, and a
          live duck in the other. John, Sam, and Ted run back out
          into the living room. The Asian guy runs toward them,
          screaming first in Cantonese, then:
                         
                          ASIAN MAN
           You break my wall! This my home long
           time! You break my wall! You bastard
           men!
                          JOHN/TED
           Dude, we're sorry! We're sorry!
                         
                          ASIAN MAN
           You bastard men! I try to make duck
           dinner, now plaster everywhere!
                         
                          TED
           Chill out okay? We'll pay for it! Let's
           talk this out okay? What's your name?
           I'm John!
                         
                          ASIAN MAN
                          (CAUTIOUSLY)
           My name Wan Ming.
                         
                          FLASH
                          (NARROWING EYES)
           Ming!
                          (CONTINUED)
                          82
                         CONTINUED:
                         
          SAM'S POV - We see the Asian man dressed as Ming the
          Merciless.
                         
                          ASIAN MAN
           You pay many dollar for wall! This
           bullshit! This all bullshit!
                         
                          SAM
           DEATH TO MING!!!
                         
          Sam charges the Asian man, tackling him. They both
          tumble over the back of the couch, nearly knocking it
          over. The duck flies out of his arms, landing on the
          floor. It immediately goes after Ted, who screams.
          ANGLE ON SAM, who chokes the Asian man on the floor.
          John struggles to pull him off.
                          JOHN
           Sam, no! Get off him!
                         
          ANGLE ON TED - who circles confrontationally with the
          duck, as in an Irish bar fight. ANGLE BACK ON THE GUYS
          FIGHTING - The Asian man jabs Sam in the eye with the
          other end of the spoon, and Sam goes staggering backward,
          falling into John. They land on the table, smashing it
          in half. They fall to the floor on top of each other.
                         
                          ASIAN MAN
           You crazy! You crazy man!
                         
          The duck charges at Ted and slaps him across the face a
          few times with its wings.
                         
                          TED
           AAA! AAAA! OW!!
          The Asian man calls to the duck from the door.
                         
                          ASIAN MAN
           Come on, James Franco!
                         
          The duck takes one last whack at Ted and waddles over to
          the Asian man, fluttering up into his arms.
                         
           ASIAN MAN (CONT'D)
           (to John and Sam)
           You pay for wall!
                         
          He exits, slamming the door.
                         
                         
          INT. TED'S APARTMENT - LATER
                         
          John sits on the couch as Guy enters, holding hands with
          another man.
                          (CONTINUED)
                          83
                         CONTINUED:
                         
                          JOHN
           Guy?
                         
                          GUY
           Hey. What's goin' on. This is Jared.
           He's the guy who beat me up. We're in
           love.
                         
                          JOHN
           What??
                         
                          GUY
           Yeah. Turns out I'm gay or whatever.
           Had no idea. C'mon Jared, let's get a
           drink.
                         
          He and Jared walk off.
          ANGLE ON JOHN, who sits on the couch, looking zoned out
          and drained. Sam Jones approaches.
                         
                          SAM
           How you doin' there, ace? You comin'
           down?
                         
                          JOHN
           Yeah. Yeah, I don't feel good.
                         
                          SAM
           Give it a couple hours, you'll be golden,
           Pony Boy. Want a Xanax?
                         
          John looks at the clock. His eyes widen in panicked
          realization.
                         
                          JOHN
           Holy shit. Holy shit, oh my god!
                         
                          SAM
           What?
                         
                          JOHN
           I gotta-- I gotta go! Shit!
                         
          John scrambles to his feet, and runs for the front door.
                         
                         
          INT. STAIRWELL - CONTINUOUS
                         
          John opens the door and runs down the hall. He runs
          partway down the stairwell, and stops short as he sees
          Lori at the bottom, coming partway up the stairs. They
          stare at each other for a beat. She looks as hurt,
          angry, and betrayed as a woman can be.
                         
                          (CONTINUED)
                          84
                         CONTINUED:
                         
                          JOHN
           Lori... I...
                         
          He throws up all over the floor.
                         
                         
          EXT. TED'S APARTMENT - MOMENTS LATER
                         
          Lori storms out into the street. After a beat, John runs
          out after her.
                         
                          JOHN
           Lori! Lori wait!
                         
          She hastily pays the cabbie who waits outside. John
          catches up to her and grabs her arm, but she shakes him
          off. She is clearly hurt, and on the verge of tears.
                          JOHN (CONT'D)
           I'm sorry! I messed up! I--
                         
                          LORI
           I want you out of the apartment...
           tonight. Gimme my car keys.
                         
                          JOHN
           Can I please just explain--
                         
                          LORI
           No.
                         
                          JOHN
           I was gonna--
                         
                          LORI
           I have given up a big chunk of my life
           for you.
                         
                          JOHN
           I was gonna stop in for like five
           minutes, and then Flash Gordon--
                         
                          LORI
           Just give me my keys, John!
                         
          He reluctantly hands her her keys. She turns and walks
          toward her car.
                         
                          JOHN
           Lori... please. I love you.
                         
          She gets in the car and drives away with a screech.
          Angle on Ted, who is walking out the door.
                         
                         
                          (CONTINUED)
                          85
                         CONTINUED:
                         
                          TED
           Johnny, come on upstairs. Tami-Lynn's
           gonna make some RC Cola from scratch.
                         
                          JOHN
           Fuck you! I don't want to talk to you!
                         
                          TED
           What?
                         
                          JOHN
           Do you know what just happened? Do you
           have any clue? My life just ended.
                         
                          TED
           Oh come on, she'll go home, watch Bridget
           Jones' Somethin' Asshole, cry a little
           bit, she'll be fine, you'll talk to her
           tomorrow.
                         
                          JOHN
                          (EXPLODING)
           Are you even listening to me?! Do you
           give any shred of a shit?!
                         
          Ted pauses, realizing John is serious.
                         
                          TED
           Well... `course I do, Johnny. Thunder
           buddies for life.
                         
                          JOHN
           Jesus, Lori was right. I should have
           stopped hanging out with you a long time
           ago. I'm never gonna have a life with you
           around. I'm 35 years old and I'm going
           nowhere. All I do is smoke pot and watch
           movies with a teddy fucking bear. And
           because of that, I just lost the love of
           my life.
                         
                          TED
           Johnny, I'm... I'm sorry.
                         
                          JOHN
           I just... I gotta be on my own, Ted. I
           can't see you anymore.
                         
          John turns and walks away.
                         
                          TED
           Johnny, wait! Hey, listen!
                         
                         
                         
                          (CONTINUED)
                          86
                         CONTINUED:
                         
          Ted pushes his own stomach in. We hear his soundbox
          squeak out the words "I wuv you." John does not turn
          around. Ted looks after him, then slowly lowers his head
          sadly. He sits down on the sidewalk, dazed and defeated.
                         
                          DISSOLVE TO:
                         
                         
          MONTAGE: SET TO MUSIC - SONG TBD
                         
                         
          EXT. MIDTOWN HOTEL - NIGHT
                         
          John pulls up in his car, and sadly goes inside.
                         
                         
          INT. MIDTOWN HOTEL - NIGHT
          John sits on the bed and turns on the TV. He flips
          through the channels, seeing various clips of shows.
          Eventually, he shuts off the TV. He opens his wallet,
          and takes out a picture of Lori. He looks at it sadly.
                         
                          DISSOLVE TO:
                         
                         
          EXT. MINI GOLF COURSE - NIGHT
                         
          John and Lori play mini-golf. She putts, and the ball
          stops just short of the hole. John walks up to it, and
          "looks the other way" as he taps it in with his foot.
          She smiles warmly at him.
                         
                          DISSOLVE TO:
                         
          EXT. BOSTON COMMON - SUNSET
                         
          John and Lori are on a swan boat ride, throwing bread to
          the ducks. They're both leaning over the side with their
          hands on the rail. His hand moves partway on top of
          hers. They look at each other, and share a slow,
          romantic kiss.
                         
                          DISSOLVE TO:
                         
                         
          INT. JOHN AND LORI'S APARTMENT - NIGHT
                         
          Lori sits on the couch, wrapped in a blanket, her face
          wet with tears. ANGLE ON the TV screen, where a Bridget
          Jones film is playing. ANGLE BACK ON Lori, who is
          looking at the screen, but is really looking inward...
                         
                          DISSOLVE TO:
                          87
                         
                         
          EXT. BEACH - DUSK
                         
          ANGLE ON a partially full moon. PAN DOWN to John and
          Lori, walking along the beach, holding hands. He kisses
          her on the cheek, then looks down, noticing something
          O.S. He leans down and picks up a dead horseshoe crab.
          He dangles it in Lori's face. She freaks out, and runs
          into the water. They both laugh.
                         
                          DISSOLVE TO:
                         
                         
          INT. JOHN AND LORI'S APARTMENT - NIGHT
                         
          ANGLE ON A BIRTHDAY CARD ON THE TABLE - We pull out to
          reveal Lori sitting at the table, with a couple of
          candles in front of her. John comes out of the kitchen
          wearing an apron, and holding an entire turkey with a
          candle in it. She smiles and puts her hands over her
          mouth with delighted hilarity. He sets the turkey down,
          and she gives him a big, laughing smile as she shakes her
          head.
                         
                          DISSOLVE TO:
                         
                         
          INT. TED'S APARTMENT - NIGHT
                         
          SLOW PAN ACROSS TED'S APARTMENT - The party is now over.
          Everyone has gone, and the place is a mess. ANGLE INTO
          TED'S BEDROOM - He lies alone in his bed, flipping
          through channels with his remote. He turns and stares at
          a picture in a frame next to his bed. ANGLE ON THE
          PICTURE It shows John and Ted as kids, standing in the
          snow, smiling at the camera. They stand next to a
          soapbox car that they have built and painted.
                          DISSOLVE TO:
                         
                         
          EXT. SUBURBAN STREET - DAY
                         
          8-year-old John and Ted are at the top of a hill with the
          soapbox racer. Ted is in the racer, wearing a helmet.
          John gives the racer a push, and Ted speeds off down the
          hill. At the bottom, he smashes into a tree, shattering
          the racer, and sending him flying out of it onto the
          ground. A dog runs into frame, snatches Ted up, and runs
          off with him. John sprints after the dog.
                         
                          DISSOLVE TO:
                          88
                         
                         
          INT. JOHN'S HIGH-SCHOOL ROOM - NIGHT
                         
          ANGLE ON a TV Guide cover that reads, "Simpsons Reaches
          5th season!" ANGLE ON 17 year-old John and Ted watching
          TV, laughing hysterically.
                         
                          DISSOLVE TO:
                         
                         
          EXT. MOVIE THEATER - NIGHT
                         
          The marquee out front reads "Star Wars: The Phantom
          Menace." We pan down a line of moviegoers, eventually
          getting to 22 year-old John and Ted. John is dressed as
          Darth Maul, and Ted is dressed as Yoda. They excitedly
          wait in line.
                          DISSOLVE TO:
                         
                         
          EXT./ ESTAB. CHUCK E. CHEESE - DAY
                         
                         
          INT. CHUCK E. CHEESE - SAME
                         
          John and Ted share a pizza. Ted has sauce all over his
          mouth and fur. John hands him a napkin and he wipes it
          off. Ted looks O.S., then excitedly gives John a "hang
          on, check this out" gesture. He runs O.S. ANGLE ON the
          stage, where the animal band play their instruments. Ted
          is there among them, stiffly playing the banjo and
          looking very animatronic. A couple little kids walk up
          to watch. After a beat, Ted gets in their faces, scaring
          the shit out of them. They run away, crying and
          traumatized. ANGLE ON John, who laughs hysterically.
                          DISSOLVE TO:
                         
                         
          INT. JOHN AND LORI'S APARTMENT - DAY
                         
          John and Lori paint the walls of their then new
          apartment. They start to playfully splatter paint on
          each other. ANGLE ON Ted, who watches from the other
          side of the room, where he leans against the wall. He
          shakes his head in a "whatever" fashion, and walks toward
          the door. When he turns, we see there is a white stripe
          of paint going down his back.
                         
                         
          EXT. JOHN AND LORI'S APARTMENT - LATER
                         
          Ted exits the apartment, holding a pack of cigarettes and
          a lighter. He pulls one cigarette out with his mouth and
          goes to light it.
                          (CONTINUED)
                          89
                         CONTINUED:
                         
          He then notices something out of the corner of his eye.
           He reacts with a take, and sprints O.S., dropping the
          cigarette and the lighter. After a beat, a skunk
          shuffles through frame after him.
                         
                          DISSOLVE TO:
                         
                         
          INT. JOHN AND LORI'S APARTMENT - NIGHT
                         
          ANGLE ON a TV Guide cover that reads, "Simpsons Reaches
          20th season!" ANGLE ON present-day John and Ted watching
          TV, expressionless and bored-looking.
                         
                          DISSOLVE TO:
                         
          INT./ ESTAB. LORI'S OFFICE - DAY
                         
                         
          INT. REX'S OFFICE - SAME
                         
          Rex sits at his desk and stares out the window.
                         
                          REX
           So, word through the grapevine is you are
           newly solo. I have tickets to see Norah
           Jones at the Hatch Shell tonight, and I
           would love it if you'd go with me.
                         
                          LORI
           You're asking me out the day after I
           broke up with someone.
                         
                          REX
           Look, I'm gonna cut the shit here.
                          LORI
           Okay.
                         
                          REX
           This is the first time you've been single
           in all the years you've worked here.
           Just go out with me one time. And if
           you're miserable and you hate it, I
           promise I will never even hint at the
           subject again. Please.
                         
                          LORI
           Rex, I don't think it's smart.
                         
                          REX
           Look, I'm an asshole. I know that. It
           worked for me in high school, and it's
           been like a reflex ever since.
                          (MORE)
                          (CONTINUED)
                          90
                         CONTINUED:
                          REX (CONT'D)
           (sigh) Lori, the worst that can happen is
           you have a fun, casual date with a guy
           who only wants a chance to prove to you
           that he can be something more than a
           jerk. Besides, you're a huge catch and
           it's about time somebody treated you that
           way.
                         
                          LORI
           Fine... I guess it beats crying myself to
           sleep every night.
                         
                          REX
           Great. Pick you up at seven?
                         
                         
          EXT./ ESTAB. MIDTOWN HOTEL - NIGHT
          It's raining outside.
                         
                         
          INT. MIDTOWN HOTEL - SAME
                         
          John sulks on the bed, leafing through a Tintin comic
          book. There's a knock at the door.
                         
                          JOHN
           Who is it?
                         
                          TED
           Johnny, it's me.
                         
                          JOHN
           Go away.
                         
                          TED
           Johnny, open the door, please. I wanna
           talk.
                         
          John ignores him. A few beats go by, then the window
          slides open from the outside, and Ted tumbles in, landing
          on the floor, soaked.
                         
                          JOHN
                          JESUS--
                         
          Ted shakes the water off himself like a dog. John
          flinches back, trying not to get wet.
                         
                          JOHN (CONT'D)
           Jesus Christ!
                         
                         
                         
                         
                          (CONTINUED)
                          91
                         CONTINUED:
                         
                          TED
           Sorry. Look, Johnny, I know you're
           pissed, but just listen to me for five
           seconds. I saw Lori out on a date with
           Rex.
                         
                          JOHN
           What?
                         
                          TED
           I'm serious, John, I went over to your
           house to talk to Lori to try and take
           some of the heat off you, and I saw Rex
           picking her up. They were going to the
           Hatch Shell.
                         
                          JOHN
           You're un-fucking-believable, you know
           that? How stupid do you think I am?
           First of all, Lori would never go out
           with Rex, and second of all, if you think
           that by making shit like that up you're
           gonna make me choose some kind of loyalty
           to you over her--
                         
                          TED
           Johnny, it's the truth. I'm tellin' ya--
                         
                          JOHN
           Get outta here.
                         
                          TED
                          (BEAT)
           You know, you're actin' like a cock, you
           know that?
                          JOHN
           What? I'm acting like a cock?
                         
                          TED
           Yes. You are actin' like a giant, V-
           shaped-funny-lookin'-guy-in-a-porno cock.
                         
                          JOHN
           Huh?
                         
                          TED
           `Member that porno we saw with the guy
           with the V-shaped cock--forget it. What
           I'm sayin' is that you're blamin' me for
           somethin' you did to yourself.
                         
          John glares at him.
                         
                         
                          (CONTINUED)
                          92
                         CONTINUED:
                         
                          TED (CONT'D)
           Lori was right about you. You can't take
           responsibility for anything that goes on
           in your life.
                         
                          JOHN
           Oh, and you can?
                         
                          TED
           I don't have to, I'm a fuckin' teddy
           bear! Y'know somethin', I didn't tie you
           up and drag you to that party. I wanted
           you to come because you're supposedly my
           best friend.
                         
                          JOHN
           Oh, yeah? Is that why you've manipulated
           me for years to stay eternally eight
           years old at the expense of the rest of
           my life?
                         
                          TED
           Whoa whoa, it's not my fault you didn't
           care enough about your relationship.
                         
                          JOHN
           You can't stand there and tell me you
           haven't always seen Lori as a threat to
           our friendship! It works out so much
           better for you when you and I are getting
           fucked up on the couch at 9 am, doesn't
           it?
                         
                          TED
           Wow. Listen to yourself. What am I,
           Emperor Ming here, controllin' your mind?
           That's your choice, John! And you know,
           by blamin' me, you just make yourself
           look like a pussy.
                         
                          JOHN
                          (BEAT)
           You know... sometimes I think back to
           that Christmas morning when I was eight
           years old... and I wish I'd just gotten a
           Teddy Ruxpin.
                         
                          TED
                          (BEAT)
           Say that one more time.
                         
                          JOHN
           Teddy... Rux-fucking-pin.
                         
                         
                          (CONTINUED)
                          93
                         CONTINUED:
                         
          Ted stares at him for a beat, then lunges at him,
          wrapping his whole body around John's face and head, like
          the facehuggers from "Aliens." John stumbles around the
          room, trying to pry Ted off. Eventually, he stumbles
          into the bathroom, and crashes through the shower door,
          shattering it. He and Ted exchange punches to the face.
          John lands a particularly hard one, which sends Ted
          flying across the room, and slamming into the wall. Ted
          hits the floor, and runs out of the bathroom. John
          stumbles to his feet. Ted scrambles across the bed,
          reaches into the bedside drawer, and pulls out a Bible.
          John staggers out of the bathroom, just in time to be
          pelted in the head as Ted throws the Bible at him.
                         
                          JOHN (CONT'D)
           AAAAAA!!! Fucking Jesus fucking Christ!
           god fucking dammit!!!
          Ted throws other objects at him, including beer cans and
          the phone. John and Ted stare at each other for a beat,
          each one breathing heavily (Ted is now on the floor).
          John charges at Ted, sailing across the bed, and tackling
          him, knocking over the side table and lamp in the
          process. John and Ted scuffle on the floor, engaging in
          a realistic-as-possible fistfight. Each one gets a
          number of blows in. John throws Ted off him, and back
          onto the bed. Ted taunts him.
                         
                          TED
           C'mon, motherfucker!
                         
          John jumps at Ted, throwing a jab at him. But Ted
          dodges, and John's fist goes into the wall above the
          headboard. He struggles to pull free as he flails about
          with his other hand, grabbing at Ted. Ted dodges again,
          and scrambles up John's head, jumping up and grabbing the
          chain on the ceiling fan, turning it on, and causing Ted
          to swing back and forth. John pulls free, and stumbles
          backward off the bed. He notices a tall, free-standing
          lamp in the corner. He pulls the plug out of the wall,
          and uses the lamp to take a swing at Ted. Ted swings out
          of the way. John takes a second swing, but the lamp cord
          catches on the fan's motor. The lamp is ripped from
          John's grasp, it swings around through the air, and
          cracks him in the side of the head. John goes down,
          whacking his head a second time on the baseboard of the
          bed. He howls in pain as he lies on his stomach,
          clutching his head. Ted takes advantage of this. He
          jumps down from the cord, and pulls the antenna off the
          clock radio next to the bed. He jumps down to the floor,
          yanks John's pants partway down, and starts whipping his
          bare ass with the antenna. John yells in fury, and kicks
          blindly at Ted. He turns over, kicking ted in the face,
          and kicking the cabinet that the TV is on.
                         
                          (CONTINUED)
                          94
                         CONTINUED:
                         
          The TV wobbles, and falls off the cabinet, landing with a
          crash, right on his groin. John lies there, with the TV
          on his crotch and his pants down, and breathes heavily.
          Ted, still dazed from the kick to the face, crawls over
          to him. Both breathe heavily. John's breathing
          deteriorates into sobs.
                         
                          TED (CONT'D)
                          (BREATHING HEAVILY)
           Why...why are you crying?
                         
                          JOHN
           My dick is in the TV.
                         
          John continues to sob. Ted climbs down off the table and
          up onto the bed. He pushes the TV off John, then lies
          down next to him. Ted starts to sob himself.
                          TED
           I'm so sorry, Johnny. I'm so sorry.
                         
                          JOHN
           So am I, man.
                         
                          TED
           I love you.
                         
                          JOHN
           I love you, too.
                         
          John hugs Ted, who hugs him back.
                         
                          TED
           Listen... you gotta let me help you make
           things right with you and Lori.
                          JOHN
           There is no putting things right. She
           hates me.
                         
                          TED
           No, John, we can get her back. Look,
           remember when you were ten, and you hit
           that squirrel with your BB gun, and then
           when we saw it fall from the tree we both
           starting crying? Remember? And then we
           ran up to it and tried to give it CPR?
           And it came back to life? John, we could
           do that again.
                         
                          JOHN
           Ted, we crushed its rib cage and blew out
           its lungs trying to give it CPR. It
           died.
                         
                          (CONTINUED)
                          95
                         CONTINUED:
                         
                          TED
                          (LONG BEAT)
           We can get Lori back.
                         
                         
          EXT. HATCH SHELL - NIGHT
                         
          A huge crowd has gathered for the Norah Jones concert.
          They cheer as she sings "Come Away With Me," backed by a
          large string section. ANGLE ON Rex and Lori, who cheer
          in the audience along with everyone else. They seem to
          be having a fantastic time.
                         
                          REX
           God, she's so brave. YOUR MUSIC IS SO
           FUCKING BRAVE!!
          Norah finishes the song.
                         
                          NORAH
           Thanks so much! We're gonna take a short
           break, but we'll be back in a few!
                         
          The crowd cheers.
                         
                         
          INT. BACKSTAGE - SHORTLY AFTER
                         
          ANGLE ON a dressing room sign which reads NORAH JONES.
          We move inside the dressing room as Norah enters and
          pours a drink.
                         
           TED (O.S.)
           Hey, play chopsticks, you jazzy slut!
                         
                          NORAH
           (turning, recognizing)
           Teddy!! How you doin', you fuzzy little
           asshole?
                         
          She hugs him.
                         
                          TED
           Well, I'm not a hot half-Muslim chick who
           sold 37 million records, but I'm hangin'
           in there.
                         
                          NORAH
           Well, half-Indian, but thanks.
                         
                          TED
           Eh, ooga booga, whatever. Hey, I want
           you to meet a good pal of mine. Hey
           Johnny, come on in!
                         
                          (CONTINUED)
                          96
                         CONTINUED:
                         
          ANGLE ON the doorway, where John enters, a little
          nervous.
                         
                          TED (CONT'D)
           Norah, this is my friend John.
                         
                          JOHN
                          (SELF-CONSCIOUSLY EXTENDS
                          HAND)
           Hi. Hi, Norah Jones.
                         
                          NORAH
           (shaking his hand)
           Ha. Whoa, relax there, sweaty. You
           ready to bring down the house?
                         
                          JOHN
           Yes ma'am. Thank you for the
           opportunity, Ms.-- Ma'am Jones.
                         
                          TED
           Jesus, you look fantastic.
                         
                          NORAH
           Well, you're probably not used to seeing
           me fully clothed.
                         
                          TED
           Me and Norah met in 2002 at a party at
           Belinda Carlisle's house and we had
           awkward, fuzzy sex in the coatroom.
                         
                          NORAH
           Actually, you weren't so bad for a guy
           with no penis.
                          TED
           I have written so many letters to Hasbro
           about that.
                         
                         
          EXT. HATCH SHELL - SHORTLY AFTER
                         
          The crowd is cheering. Norah is back out on stage at the
          piano.
                         
                          NORAH
           Okay, I'm gonna give my chops a rest here
           and invite a friend of mine up to the
           stage. He's gonna sing a song to a very
           special lady in the audience who he loves
           very much. Let's give a big hand to John
           Bennett!
                         
                         
                          (CONTINUED)
                          97
                         CONTINUED:
                         
          The crowd applauds dutifully as John walks out onstage.
          ANGLE ON Lori and Rex. Lori reacts, shocked.
                         
                          LORI
           Oh my god.
                         
          John takes center stage, and looks down at Lori.
                         
                          JOHN
           Uh, hi. Um... This is for Lori Collins.
           Because I love her. This song always
           reminds me of the most important night of
           my life. The night we met. It's the
           theme song from the movie "Octopussy."
                         
          The band begins playing. "All Time High". Inexplicably,
          Norah is playing the saxophone with a pair of shades on.
                          JOHN (CONT'D)
           ALL I WANTED WAS A SWEET DISTRACTION FOR
           AN HOUR OR TWO / HAD NO INTENTION TO DO
           THE THINGS WE'VE DONE / FUNNY HOW IT
           ALWAYS GOES WITH LOVE, WHEN YOU DON'T
           LOOK, YOU FIND / BUT THEN WE'RE TWO OF A
           KIND / WE MOVE AS ONE
                         
          ANGLE ON Lori and Rex. Rex is visibly derisive, but we
          see that Lori is softening. It's working...
                         
                          JOHN (CONT'D)
           WE'RE AN ALL-TIME HIGH / WE'LL CHANGE ALL
           THAT'S GONE BEFORE / DOING SO MUCH MORE /
           THAN FALLING IN LOVE
                         
                          REX
           (fake voice, covering his
           mouth and looking away)
           You suck, get off the stage!
           (then, for Lori's benefit)
           Hey, come on guys!
                         
          The crowd starts to take the cue.
                         
                          CROWD
           Get off the stage! / Boooo! / You suck! /
           We wanna hear Norah! / Come on!
                         
          ANGLE ON Ted in the wings.
                         
                          TED
           Ah, god.
                         
                          JOHN
           SO HOLD ON TIGHT / LET THE FLIGHT
           BEGIN...
                          (CONTINUED)
                          98
                         CONTINUED:
                         
          ANGLE ON a crazed audience member, who rushes the stage,
          racing toward John.
                         
                          CRAZY GUY
           You're an asshole!
                         
          John flinches as he raises the mic stand off the floor at
          the last second, so the base is sticking out
          horizontally. The crazy guy runs right into it, bashing
          himself in the face. He goes down, unconscious and
          bleeding. Everyone gasps as the music stops.
                         
                          NORAH
           Jesus.
                         
          A few concert personnel rush out to check the guy.
                          STAGEHAND
           Someone call an ambulance!
                         
          The crowd is now shouting angrily at John. But he is
          only focused n one spot in the crowd. He sees that Lori
          and Rex are gone. Almost oblivious to the rest of the
          frenzy, he sighs, heartbroken. A couple of concert
          security personnel haul him offstage.
                         
                         
          EXT. HATCH SHELL PARKING LOT - NIGHT
                         
          Rex escorts Lori to his car.
                         
                          REX
           That was insane. Did you see the way
           that guy's body hit the ground? It was
           like a rag doll!
                          LORI
           Yeah, I'd rather just not talk about it.
                         
                          REX
           You want to go get a drink after this? I
           feel like I could use one after seeing a
           guy almost die.
                         
                          LORI
           Nope, I think I'd rather you just take me
           home.
                         
                          REX
           One drink, come on.
                         
                          LORI
           Nope, not really feeling up to it.
                         
                         
                          (CONTINUED)
                          99
                         CONTINUED:
                         
                          REX
           Alright, alright, I get it. I don't
           blame you. When you think about it, it
           was actually really unfair of him to
           embarrass you like that.
                         
                          LORI
           Just to be clear, I am not embarrassed.
           Listen, John and I may have our problems
           but at least he tried. You know what? I
           don't feel like talking to you about
           this.
                         
          She walks away.
                         
                          REX
           Where you going?
                          LORI
           Taking a cab. I'm going home.
                         
          As she disappears out of earshot, Rex closes his eyes and
          releases a fart.
                         
                          REX
           Finally.
                         
                         
          EXT./ ESTAB. JOHN & LORI'S APARTMENT BUILDING - DAY
                         
                         
          INT. JOHN AND LORI'S APARTMENT - BATHROOM - SAME
                         
          Lori gets out of the shower, and begins towelling off,
          still reeling with disgust from her encounter with Rex.
          After a few moments, there's a knock at the door. Lori
          sighs with annoyance, and walks to the door, still in her
          towel. She looks through the peephole, but there's no
          one there. She opens the door cautiously, and looks out
          into the hall. There's no one there.
                         
           TED (O.S.)
           Down here, I swear to god I'm not lookin'
           up your towel.
                         
          She looks down with a start, and sees Ted standing there.
          He's blocking his view with one hand.
                         
                          TED (CONT'D)
           Not lookin' up your towel. Not lookin'
           at your funny business.
                         
                         
                         
                         
                          (CONTINUED)
                          100
                         CONTINUED:
                         
                          LORI
           (pulling towel closer to her)
           Ted? What're you doing here? What do
           you want?
                         
                          TED
           I need to talk to you.
                         
                          LORI
           Look, if you're here to fight John's
           battle for hi--
                         
                          TED
           Lori, do me a favor and let me talk
           first, and then you can say whatever you
           want.
          There's a beat. She reluctantly considers.
                         
                         
          INT. JOHN AND LORI'S LIVING ROOM - MOMENTS LATER - DAY
                         
          Lori, now in a robe, sits down on the couch, facing Ted.
                         
                          TED
           Look, John loves you very much. More
           than anything in the world. And he's
           fallin' to fuckin' pieces without you.
           He knows he screwed up big time, but you
           gotta believe me that is wasn't all his
           fault. If you'll just give him one more
           chance to be with you--
                         
          She rolls her eyes.
                         
                          TED (CONT'D)
           Listen to me! If you'll just give him
           one more chance... I promise I will leave
           and never come back. He'll be all yours.
           Just give him one more chance.
                         
                          LORI
           Ted... that's a very nice offer, but I
           don't want you to do that. This is about
           John and me and our problems. And I
           don't think it can be fixed.
                         
                          TED
           Because of me! Look, you want him to be
           a man. And I'm the one who's keepin'
           that from happening. As long as he's got
           his teddy bear, he's still a boy. And I
           care about him as much as you do. But
           I'm willing to give up the boy so you can
           have the man.
                          (CONTINUED)
                          101
                         CONTINUED:
                         
          We can see Lori starting to soften a bit.
                         
                          TED (CONT'D)
           Look, I'm givin' this the best shot I got
           here, Lori. I'm beggin' you. I'm no
           good at this emotional crap, but I gotta
           help my best friend. Please. Just talk
           to him.
                         
                          LORI
                          (SIGH)
           I'll talk to him.
                         
                          TED
           Thank you. He's waitin' for me down at
           Charley's. So... maybe you could,
           y'know... go down instead of me?
                          LORI
           What... now?
                         
                          TED
           Please. You'll regret it for the rest of
           your life if you don't.
                         
                          LORI
           Alright, alright, I'll go.
                         
                         
          INT. JOHN AND LORI'S APARTMENT - SHORTLY AFTER
                         
          Lori emerges from the bedroom, dressed, and heads for the
          door. Ted is on the couch watching TV.
                         
                          TED
           (flipping on TV)
           Hey, you mind if I stay and watch the
           Sox?
                         
          The door shuts and she's gone. Ted gets up and walks
          into the kitchen. He opens the fridge.
                         
                          TED (CONT'D)
           Jesus Christ, what a chick fridge.
           Yoplait, a cantaloupe, and a Brita water
           filter.
                         
          He opens up a crisper drawer, and looks at a six-pack of
          beer bottles.
                         
                          TED (CONT'D)
           Michelob Ultra Tuscan Orange Grapefruit.
           My god, America is imploding.
                         
                         
                          (CONTINUED)
                          102
                         CONTINUED:
                         
          He shakes his head as he opens the beer, and walks into
          the other room. He settles down in a recliner, and
          watches the game. After a moment, there's a knock at the
          door. Ted sighs with annoyance, and gets up.
                         
                          TED (CONT'D)
           Forget your keys?
                         
          He walks to the door, and opens it up.
                         
                          TED (CONT'D)
           You know, your beer suck--
                         
          He freezes, and looks up. We reveal Donny, the creepy
          man from earlier, with his son Robert.
                         
                          DONNY
           Hi, Ted.
                         
                          TED
           Fuck.
                         
          Donny throws a sack over Ted, trapping him.
                         
                         
          EXT./ ESTAB. CHARLEY'S - LATER DAY
                         
          Lori's car pulls up, and she gets out.
                         
                         
          INT. CHARLEY'S - CONTINUOUS
                         
          Lori enters, and looks around. She spots John, who looks
          up from a menu. He is surprised to see her. She sighs
          and walks over to him.
                          JOHN
           Lori! What-- what are you doing here?
                         
                          LORI
           You can thank Ted.
                         
          A beat. John smiles slightly.
                         
                          LORI (CONT'D)
           How are you?
                         
                          JOHN
           Good, good. I've, uh... made myself a
           nice little home at the Midtown Hotel up
           the street. I'd show you around, but
           it's kinda classy. They require an
           undershirt and at least one visible cold
           sore for all customers.
                         
                          (CONTINUED)
                          103
                         CONTINUED:
                         
                          LORI
                          (LAUGHS HUMORLESSLY)
           Well. Shall I sit?
                         
                          JOHN
           Uh, yeah.
                         
          She does. There's a beat. A busboy brings them each a
          water.
                         
                          JOHN (CONT'D)
           So, work's good? Everything good there?
                         
                          LORI
           Yeah. Work's fine.
                         
                          JOHN
           How's Rex?
                         
                          LORI
           There is no Rex.
                         
                          JOHN
           Oh. Good.
                          (BEAT)
           Well... I guess we can't make small talk
           all day, so I'll say what I wanna say. I
           could sit here and tell you I'm sorry, it
           was a huge misunderstanding, and I'm
           ready to change. But I don't think you
           wanna hear any of that crap. I'm not
           gonna try and get you to take me back.
           Why would you? I've been a really shitty
           boyfriend for the last four years. I
           don't deserve you. I didn't take our
           relationship seriously, even though I
           love you more than life itself. All I
           want is... just to end on good terms.
           Because I owe that to you. I want you to
           be happy... and for us to be friends.
                         
                          LORI
           (a little taken aback)
           Wow. Thank you. I appreciate that.
                         
                          JOHN
           Well. That's pretty much it.
                         
          He takes out some money, and puts it on the table, paying
          the check. He smiles at her and walks out. She sits
          there for a beat.
                          104
                         
                         
          EXT. DONNY'S HOUSE - LATE DAY
                         
          Donny's car pulls up. The house is a low-class, creepily
          shabby-looking Boston home (think Buffalo Bill in
          "Silence of the Lambs"). It's close to one end of the
          base of a bridge.
                         
                         
          INT. DONNY'S HOUSE - LATE DAY
                         
          Donny carries the sack inside, and unceremoniously dumps
          Ted onto the floor. Ted looks around. It's just as
          shitty on the inside as on the outside. On the walls,
          there are a disturbing number of newspaper clippings,
          photo spreads, etc. Most are from press from Ted's media
          heyday, but some are photographs of Ted and John out in
          public that Donny clearly took himself.
                          TED
           Whoa...
                         
                          DONNY
           Yes, as you can see, you've been part of
           our family for quite some time. Welcome
           home.
                         
                          TED
           Heh, you know what's hilarious, I got
           tons of pictures of you guys at my house.
                         
                          ROBERT
           Daddy, is he all mine?
                         
                          DONNY
           He's all yours, my little winner.
           You've arrived at a lucky time, Ted.
           It's almost Robert's play hour.
                         
                          TED
           I'm guessin' you guys don't have a PS3.
           I'm guessin' you're more of a wooden
           horse with a wig kinda family.
                         
                         
          INT. ROBERT'S ROOM - MOMENTS LATER
                         
          Ted is led into Robert's room. It's a fairly sparse room
          with some toys strewn about. A wooden rocking horse with
          a wig stands in the corner.
                         
                          TED
           Huh. Wig horse.
                         
          Robert sits down on the floor, smiling at him. Donny
          stands in the doorway.
                          (CONTINUED)
                          105
                         CONTINUED:
                         
                          DONNY
           Now, remember, Ted, you belong to Robert
           now. So you will do as he says.
                         
                          TED
           Y'know, you think you're just gonna get
           away with a kidnapping? Nice fuckin'
           example you're settin' for your kid.
                         
                          DONNY
           (leaning in to Ted with
                          ANGER)
           LANGUAGE!!!
                         
          Ted flinches nervously. Donny moves back.
                         
                          DONNY (CONT'D)
           When I was a little boy, I saw you on
           television. And I thought you were the
           most amazing, most wonderful thing I'd
           ever seen. Ever. And I asked my father
           if I could have a magical teddy bear,
           too. And he said no. And I was
           heartbroken. I decided that if I ever
           had a son, I would never say no to him.
                         
                          TED
           Maybe "no" to a Snickers bar every once
           in awhile wouldn't hurt.
                         
                          ROBERT
           Me and Ted are gonna be best friends,
           daddy.
                         
                          DONNY
           Yes. You are. Happy play time.
          Donny shuts the door. Robert stares at Ted.
                         
                          TED
           Jesus fucking Christ!
                         
                          ROBERT
           No! Daddy said no bad words!
                         
                          TED
           Yeah well, fuck your dad.
                         
          Ted scrambles for the window and tries to open it. It
          doesn't budge. He takes a running leap at it, but just
          bounces off like a plush toy, and lands on the floor.
                         
                          TED (CONT'D)
           Shit!
                         
                          (CONTINUED)
                          106
                         CONTINUED:
                         
          Robert stands over him.
                         
                          ROBERT
           I said a bad word one time, and daddy
           punished me for it.
                         
                          TED
           That's a great story, I felt like I was
           there.
                         
                          ROBERT
           Daddy gave me an ouch. Now I have to
           give you an ouch.
                         
          Robert grabs Ted with one hand, and gets a grip on one of
          Ted's ears with the other hand. Robert pulls on the ear
          as hard as he can, and rips the ear off. Ted screams as
          loud as he can. Robert looks at him, holding the ear.
                         
                          TED
           Okay... okay, kid. You win. We'll do it
           your way. You wanna play a game or
           somethin'? It's play time, let's play a
           game.
                         
                          ROBERT
           Yeah, I wanna play a game!
                         
                          TED
           Good, good, hey, how `bout we play a
           little game of hide and seek?
                         
                          ROBERT
           I love hide and seek! I'll hide!
                         
                          TED
           Well, now, Robert, your dad likes you to
           show good manners, right?
                         
                          ROBERT
           Yes.
                         
                          TED
           Well, a well-mannered kid lets his guest
           hide first, don't ya think?
                         
          There's a beat. Robert stares blankly at him, then:
                         
                          ROBERT
           Okay, you hide first.
                         
                          TED
           Great. Fantastic. Okay, now you count
           to a hundred and then try to find me,
           okay?
                          (CONTINUED)
                          107
                         CONTINUED:
                         
                          ROBERT
           Do I need to wash my hands before this
           game?
                         
                          TED
           You... well-- no, you-- god, that's a
           weird fuckin' question, no, just start
           countin'.
                         
          Robert sits down, covers his eyes and starts counting.
                         
                          ROBERT
           One... two... three...
                         
          Ted grabs a chair and starts sliding it over toward the
          door.
                          TED
           Okay, no peekin', now, or you'll get kid
           cancer.
                         
          Ted reaches the door, climbs up onto the chair, and turns
          the doorknob. He opens the door, and exits out into the
          hallway. After a beat, he re-enters, grabs his severed
          ear, and exits again.
                         
                         
          INT. HALLWAY - LATE DAY
                         
          Ted nervously moves down the hallway toward the front
          door. He has it in sight on the far end of the living
          room, but when he gets closer to the living room doorway,
          he sees that Donny is sitting in an armchair, watching
          The Incredible Hulk (the old TV show). Ted darts back
          into the hallway before he's seen, but in the process,
          bumps into a small table with a lamp and a couple knick
          knacks on it. One of them, a small ceramic penguin,
          falls over, making a sound. Donny turns and looks in the
          direction of the hallway.
                         
                          DONNY
                          (BEAT)
           Robert? How's play time?
                         
                         
          INT. ROBERT'S ROOM - LATE DAY
                         
          Robert's hands still cover his eyes.
                         
                          ROBERT
           Good, daddy!
                          108
                         
                         
          INT. LIVING ROOM - LATE DAY
                         
                          DONNY
           Ted, are you making friends with Robert?
                         
          Ted looks panicky, not knowing what to do. After a beat,
          Donny leans forward as if he's about to get up.
                         
                          DONNY (CONT'D)
           Ted?
                         
           ROBERT (O.S.)
           Daddy, you're gonna ruin the game!
                         
                          DONNY
                          (CHUCKLING)
           Okay.
          Ted breathes a sigh of relief, and walks the other way
          down the hall. He passes a door. He opens it, but it's
          just a storage closet. He's about to shut it, but
          notices a stapler amidst the odds and ends. He hastily
          begins stapling his ear back on.
                         
                         
          INT. DONNY'S LIVING ROOM - CONTINUOUS
                         
          Donny's hears something, and turns to look. We think
          he's about to get up, but he then settles back in.
                         
          ANGLE BACK ON TED, who puts on last staple in.
          Satisfied, he exits the closet and continues down the
          hall.
                         
                         
          INT. DONNY'S KITCHEN - LATE DAY
          Ted looks around, and spots a phone on the counter. He
          jumps up, grabs the handset, and jumps back down. He
          dials John's number.
                         
                         
          EXT. BOSTON STREET - CONTINUOUS
                         
          John is walking back to the Midtown Hotel. After a beat,
          Lori's car pulls up slowly alongside him. She leans
          over.
                         
                          LORI
           Hey.
                         
                          JOHN
           Hey.
                         
                         
                          (CONTINUED)
                          109
                         CONTINUED:
                         
                          LORI
           Kinda late to be walkin' home by
           yourself.
                         
                          JOHN
           Oh, I'll be okay. If I get raped, it'll
           be my fault with what I'm wearing.
                         
                          LORI
           Listen, John... there's something I wanna
           say to you, too.
                         
          He pauses, then gets into the car and sits down next to
          her. She prepares to speak, but John's phone rings. He
          shuts it off without looking at it.
                         
                          JOHN
           Go ahead.
                         
                         
          INT. DONNY'S KITCHEN - LATE DAY/DUSK
                         
          Ted nervously holds the phone to his ear.
                         
                         
          INT. LORI'S CAR - LATE DAY/DUSK
                         
                          LORI
           John, I just want you to know that... I
           mean, I hope you don't think that--
                         
          John's phone rings. He looks down at it, annoyed. It
          reads "Unknown caller." He silences it.
                         
                          LORI (CONT'D)
           I, um... I just feel like we should...
           keep talking. Because--
                         
          John's phone rings again. Exasperated, he answers it.
                         
                          JOHN
           Whoever this is, it's not a good time.
                         
          INTERCUT BACK & FORTH BETWEEN TED AND JOHN:
                         
                          TED
           John! It's me! Can you hear me?
                         
                          JOHN
           Ted?
                         
          Lori sighs, slightly annoyed.
                         
                          JOHN (CONT'D)
           Listen, I gotta call you back.
                          (CONTINUED)
                          110
                         CONTINUED:
                         
                          TED
           No, John! Don't hang up, I'm in trouble!
                         
                          JOHN
           What do you mean, what kinda trouble?
                         
          Lori turns, slightly curious, but still annoyed.
                         
                          TED
           They got me! That freaky guy and his
           freaky fat kid!
                         
                          JOHN
           What?
                         
                          TED
           I'm in their house, John! You gotta call
           the police, they won't let me outta here!
           They tore my ear off!
                         
                          JOHN
           Wait, slow down! Where are you?
                         
                          TED
           Uh... I'm not sure, it's uh--
                         
          Suddenly, a hand grabs the phone away from Ted. He gasps
          and looks up. It's Donny, who slams the phone back down
          in its cradle.
                         
                          DONNY
           (dark, brewing rage)
           You're not a very polite guest.
                         
                          TED
           Shit.
                         
                         
          INT. LORI'S CAR - LATE DAY/DUSK
                         
                          JOHN
                          (INTO PHONE)
           Ted? Ted? Hello? Ted!
                         
                          LORI
           What's the matter, is he all right?
                         
                          JOHN
           I don't know.
                         
                          LORI
           Where is he?
                         
                          JOHN
           I don't know, but he's in trouble.
                          (CONTINUED)
                          111
                         CONTINUED:
                         
                          LORI
           Why? What happened? Can you call him
           back?
                         
                          JOHN
           No, it's blocked-- wait a second.
                         
          John scrambles for his wallet. He opens it, and pulls
          out the address given to him earlier by Donny at the
          Common. He looks at it, then points out the window.
                         
                          JOHN (CONT'D)
           Go! Take Columbus to Herald and get on
           the expressway!
                         
                         
          EXT. BOSTON STREET - CONTINUOUS
          Lori's car peels out and races off.
                         
                         
          INT. DONNY'S KITCHEN - LATE DAY
                         
          Donny stands over Ted.
                         
                          DONNY
           You've put us in a pickle here, haven't
           you? We have to go now.
                         
                          TED
           Yeah, good idea.
                         
          Ted runs through Donny's legs, and out into the hall. He
          races for the living room and the exit, but Robert steps
          in front of the door, blocking him.
                          TED (CONT'D)
           Aaaa!
                         
                          ROBERT
           Found you.
                         
          Robert turns the deadbolt on the door, locking it. Ted
          turns and bolts in the other direction back down the
          hallway, but sees Donny heading for him. Ted ducks into
          the dining room, as Donny lunges for him and misses.
                         
                         
          INT. DINING ROOM - LATE DAY - CONTINUOUS
                         
          Donny pursues Ted around the table. Ted ducks under the
          table, under the chairs, etc. trying to escape Donny (and
          Robert, who has entered the room). Ted slips past them
          and back out into the hall.
                         
                          (CONTINUED)
                          112
                         CONTINUED:
                         
          He races for the door, but the deadbolt is too high to
          reach. He runs into the living room, and pushes open a
          door.
                         
                         
          INT. BASEMENT - LATE DAY - CONTINUOUS
                         
          Ted tumbles down the dark stairs into the basement, which
          is lit only by a single bulb hanging from the ceiling.
          He lands, gets his bearings, then freezes in shock, as he
          sees that the basement is loaded with ripped and
          mutilated teddy bears.
                         
                          TED
           AAAAAA!
                         
          Donny and Robert move in to frame behind him.
                          DONNY
           We tried to make do with other teddy
           bears. But none of them were you, Ted.
                         
          Ted whirls around in shock, as we cut to:
                         
                         
          EXT. STREET - DUSK
                         
          John and Lori race through the streets of Boston.
                         
                         
          INT. LORI'S CAR - DUSK
                         
                          JOHN
           It's this creepy fucked-up guy who wants
           Ted for his creepy fucked-up son. They
           got him somehow.
                          LORI
           Which way?
                         
                          JOHN
           Shoot up 99!
                         
                         
          EXT. BOSTON STREET - DUSK - CONTINUOUS
                         
          The car makes a hard left.
                         
                         
          INT. LORI'S CAR - DUSK - CONTINUOUS
                         
          John finishes punching numbers into his cellphone.
                         
                         
                         
                          (CONTINUED)
                          113
                         CONTINUED:
                         
                          JOHN
                          (INTO PHONE)
           Hello, 911? I need the police right
           away! This guy took my teddy bear!
                          (BEAT)
           ...Hello?
                         
                         
          EXT. BOSTON STREET - DUSK - CONTINUOUS
                         
          Lori's car speeds away.
                         
                         
          EXT. DONNY'S HOUSE - NIGHT
                         
          Donny and Robert emerge from the house. Donny clutches
          the sack. We can see it move as Ted struggles to get
          free. Robert gets in the back seat of the car as Donny
          opens the way back door, and dumps Ted inside.
                         
                         
          INT. DONNY'S CAR - NIGHT - CONTINUOUS
                         
          Ted tumbles out of the sack and into the way back. Donny
          slams the door. He gets into the car.
                         
                          DONNY
           Robert, seat belt.
                         
          Robert buckles up.
                         
          EXT. DONNY'S HOUSE - NIGHT - CONTINUOUS
                         
          Donny pulls away down the alley.
                         
          INT. DONNY'S CAR - NIGHT - CONTINUOUS
          Ted scrambles to his feet.
                         
                         
          INT. LORI'S CAR - NIGHT - CONTINUOUS
                         
          John looks around frantically, then spots something out
          of the passenger's side window.
                         
          JOHN'S POV - They pass the alley, where we see Donny's
          car heading out of the alleyway.
                         
                          JOHN
                          (TO LORI)
           Whoa whoa, stop stop stop!
                         
          The car slows down, and John sees Donny's car make the
          turn out onto the street. Ted is looking out the back.
                          114
                         
                         
          INT. DONNY'S CAR - NIGHT - CONTINUOUS
                         
                          TED
           Johnny!
                         
          Robert and Donny both hear this. Donny looks in his side-
          view mirror, just in time to see Lori's car swing a U-
          turn to pursue them. Donny speeds up, and races off up
          the street. Lori's car speeds up in pursuit.
                         
                         
          EXT. STREETS OF BOSTON - NIGHT
                         
          We do several quick cuts as the chase blasts its way
          through the Boston streets, avoiding traffic and
          pedestrians.
                         
          INT. TUNNEL - NIGHT - CONTINUOUS
                         
          Donny's car races through the tunnel. Lori's car
          pursues.
                         
                         
          INT. DONNY'S CAR - NIGHT - CONTINUOUS
                         
          Ted continues to stare out the back. He then notices a
          crowbar on the floor in the way back. He grabs it, and
          takes a hard swing at the rear window. It does not
          break. Robert sees this, and scrambles to undo his seat
          belt.
                         
                         
          INT. LORI'S CAR - NIGHT - CONTINUOUS
                         
                          JOHN
           Come on, we're losing him!
                         
          Lori speeds up.
                         
                         
          INT. DONNY'S CAR - NIGHT - CONTINUOUS
                         
          Ted takes another swing at the window. The glass does
          not break. Robert undoes his seat belt, and scrambles
          back. He grabs Ted, who drops the crowbar. He starts to
          pull Ted back over into the back seat, but Ted manages to
          wriggle free.
                         
                         
          INT. TUNNEL - NIGHT - CONTINUOUS
                         
          The chase continues.
                          115
                         
                         
          INT. DONNY'S CAR - NIGHT - CONTINUOUS
                         
          Ted grabs the crowbar, and again takes a swing at the
          window. This time, it shatters. He drops the crowbar,
          and climbs up onto the edge of the window.
                         
                         
          INT. LORI'S CAR - NIGHT - CONTINUOUS
                         
          They see Ted in the window.
                         
                          JOHN
           Get closer!
                         
                          LORI
           I'm trying!
                         
          INT. DONNY'S CAR - NIGHT - CONTINUOUS
                         
          Ted gets one leg and one arm up onto the edge of the
          window, when suddenly he is whacked hard in the side of
          the head, sending him tumbling onto the floor. We see
          that Robert has struck him hard with the crowbar.
                         
                          TED
           (holding head in pain)
           Aaaaa! Shit!!
                         
                         
          INT. LORI'S CAR - NIGHT - CONTINUOUS
                         
          They continue watch with held breath, as they keep up.
                         
                         
          INT. DONNY'S CAR - NIGHT - CONTINUOUS
          Ted shakes himself off, still a little dazed, and climbs
          back up. Robert climbs into the way back and grabs one
          of his legs.
                         
                          ROBERT
           No! You're being bad!
                         
          Ted reaches down and grabs the crowbar with one arm, and
          brandishes it threateningly at Robert.
                         
                          TED
           Back off, Susan Boyle.
                         
          Robert backs off in fear. Ted climbs out onto the rear
          of the car, and positions himself to make the jump. He
          tosses the crowbar away into the tunnel. John and Lori
          speed up, getting closer to him, so he can make the jump.
                          116
                         
                         
          INT. LORI'S CAR - NIGHT - CONTINUOUS
                         
                          JOHN
           Easy...
                         
                          LORI
           I know.
                         
                          JOHN
                          EASY--
                         
                          LORI
           I know!
                         
                         
          INT. TUNNEL - NIGHT - CONTINUOUS
          Lori's car moves closer to Donny's. There's a tense
          moment with some back and forth cutting... and then Ted
          makes the jump! He lands on the hood of Lori's car, and
          slides across, grabbing the windshield wiper to avoid
          falling off. He pulls himself back up. John and Lori
          breathe energetic sighs of relief.
                         
                          TED
           Johnny! Total T.J. Hooker, right?
                         
          John and Lori laugh.
                         
                          JOHN
           Yes! Fuckin' A right!
                         
                         
          INT. DONNY'S CAR - NIGHT - CONTINUOUS
                         
          Donny sees what's happening in his side mirror. He puts
          his foot on the brakes, and the car screeches as it
          drastically reduces speed. John's car slams into Donny's
          causing Ted to go flying back through open rear window of
          Donny's car, past Robert (who is still in the way back)
          and tumbling into the back seat.
                         
                          TED
           God dammit!
                         
          Ted gets his bearings, and notices the sack that Donny
          captured him in, lying on the floor. He looks up at
          Donny for a beat, then grabs the sack.
                         
          ANGLE ON Donny driving. Suddenly, Ted jumps up from
          behind, and throws the sack over Donny's head, bracing
          himself against the back of the front seat. Donny yells
          in anger, and pulls at Ted, trying to get him off.
                          117
                         
                         
          INT. TUNNEL - NIGHT - CONTINUOUS
                         
          Donny's car scrapes against the side of the tunnel,
          sending sparks flying.
                         
                         
          INT. DONNY'S CAR - NIGHT - CONTINUOUS
                         
          Donny grabs Ted and flings him off his face, onto the
          floor on the passengers' side. Donny rips the sack off
          his head, and reacts as he looks out the front window.
          He's approaching the end of the tunnel, and there is
          opposing traffic moving in the other direction.
                         
                         
          EXT. BOSTON CITY STREETS - NIGHT - CONTINUOUS
          Donny swerves past the traffic, narrowly avoiding
          clipping one of the cars. A moment later, John and Lori
          come racing out of the tunnel. However, a truck drives
          through the intersection, stopping them in their tracks.
                         
                          LORI
           Shit!
                         
          She pounds on the steering wheel, frantically willing the
          truck to get out of the way. Finally it does, and they
          continue on into the city.
                         
                         
          EXT. BOSTON CITY STREETS - NIGHT - CONTINUOUS
                         
          Donny's car races through the streets, pursued by John
          and Lori, who are catching up again, but are still a ways
          behind.
                         
          INT. DONNY'S CAR - NIGHT - CONTINUOUS
                         
          Ted is still on the floor on the passenger's seat side.
          He looks around, and spots a "Club" underneath the seat.
          He glances at Donny, whose eyes are on the road. Ted
          grabs the club, and scrambles up the seat, taking a swing
          at Donny. Donny ducks out of the way, and tries to slap
          Ted away as Ted continues to takes swings at him. A few
          of them land, eventually drawing blood. Donny smacks Ted
          away. Ted tumbles back onto the passenger's seat. Then,
          with determination, he grabs the Club again, scurries in
          front of Donny, and locks the Club onto the steering
          wheel with a snap! Donny's eyes widen as Ted scrambles
          into the back seat. Donny tries to turn the wheel, but
          can't.
                          118
                         
                         
          EXT. BOSTON CITY STREETS - CONTINUOUS - NIGHT
                         
          Donny's car swerves out of control, veering up the
          street, and crashing into a lamppost, fishtailing as it
          impacts. The airbags go off as the car comes to a stop.
          Taking advantage of the situation, Ted scrambles out the
          back window. He catches his fur on a jagged shard of
          glass, slightly ripping his side. He hangs and struggles
          for a bit, then drops to the ground. He sways a bit.
          TED'S POV - We see that his vision is swimming slightly.
          That little rip has done something... He shakes it off,
          and runs up the sidewalk. ANGLE ON DONNY, who scrambles
          out of the wrecked car, followed by Robert. They chase
          Ted up the street. Ted spots a garage with the door
          slightly open. He squeezes himself underneath, and
          disappears inside.
          ANGLE ON JOHN AND LORI - They screech to a stop behind
          Donny's car. They hurry out, just in time to see Donny
          and Robert duck underneath the door. They run up the
          sidewalk after them.
                         
                         
          INT. UNDERGROUND AREA - CONTINUOUS
                         
          Ted runs down a ramp, looking frantically around for an
          escape route. He darts off to the left, sprinting up a
          ramp, followed by Donny and Robert. Ted stops at a red
          metal fence, and squeezes through, rushing up the stairs
          on the other side. Donny reaches the fence, but with his
          larger size he has to climb over the top, which slows him
          down a bit.
                         
          ANGLE ON JOHN AND LORI - We catch them ducking in through
          the garage door, and running inside. They look around
          for a beat. ANGLE ON ROBERT, who turns and sees them
          (Donny has already made it over the fence). ANGLE BACK
          ON JOHN.
                         
           ROBERT (O.S.)
           NO!!
                         
          John and Lori turn just in time to see Robert charging at
          them!
                         
                          ROBERT (CONT'D)
           You can't have my teddy bear!!
                         
          When Robert reaches John, John knocks him down with one
          punch to the face. Robert collapses. Lori and John look
          down at him.
                         
                          LORI
           Oh my god.
                         
                          (CONTINUED)
                          119
                         CONTINUED:
                         
                          JOHN
           Sorry, someone had to go Joan Crawford on
           that kid.
                          (THEN)
           Come on!
                         
          John and Lori run up the ramp, leaving a stunned Robert
          behind. When they reach the red fence, they look around,
          but it's unclear which way Ted and Donny have gone. John
          continues up the ramp (in the wrong direction) with Lori
          just behind him.
                         
                         
          INT. WALKWAY - CONTINUOUS
                         
          Ted runs as fast as his stubby legs will carry him.
          Donny is in pursuit, and getting closer. The chase moves
          past a concession area, and up a few flights of stairs.
                         
                         
          EXT. UPPER SEATING AREA - CONTINUOUS
                         
          Ted runs out onto the upper level, and stops. The camera
          PIVOTS 180 DEGREES and ascends to reveal the expanse of
          FENWAY PARK down below. A few lights are on, and one
          lone maintenance man sweeps the dirt. Donny emerges from
          the stairwell, which snaps Ted out of it. Ted sprints
          past the front row of seats, and comes to a dead end. He
          has nowhere else to go. With Donny closing in, Ted
          scurries out onto the ledge, and pulls himself up onto
          the lighting tower. He looks down. From TED'S POV, it's
          a long drop. Donny reaches out to grab him, but can't
          quite reach. Donny glances down at the drop for a beat,
          then pulls himself out onto the ledge to go after Ted.
          Ted climbs farther up the tower.
                         
          INT. WALKWAY - CONTINUOUS
                         
          John and Lori emerge and continue to look around
          frantically. They run up the walkway.
                         
                         
          EXT. LIGHTING TOWER - CONTINUOUS
                         
          Donny pursues Ted up the tower.
                         
                         
          EXT. LOWER SEATING AREA - CONTINUOUS
                         
          John and Lori emerge into the lower seating section, and
          run down the aisle, looking around with desperation.
                         
                         
                         
                          (CONTINUED)
                          120
                         CONTINUED:
                         
                          LORI
           (spotting the action on the
                          TOWER)
           Look!
                         
          John turns and sees the drama playing out on the distant
          lighting tower.
                         
                          JOHN
           Oh Jesus...
                          (THEN)
           Stay here.
                         
                          LORI
           Wait, John! What are you--
                         
                          JOHN
           STAY THERE!!
                         
          He turns and runs back up the aisle, toward the
          concession area.
                         
                         
          EXT. LIGHTING TOWER - CONTINUOUS
                         
          Ted is starting to gain ground, but he slips, and falls
          back down. He's about to pulls himself up again, when
          Donny grabs one of his legs.
                         
                         
          EXT. LOWER SEATING AREA - CONTINUOUS
                         
          John continues up the aisle as fast as he can move.
                         
                         
          EXT. LIGHTING TOWER - CONTINUOUS
          Ted struggles to pull himself from Donny's grasp, but he
          can't. CLOSE UP ON TED'S SIDE - The small rip from
          earlier begins to tear again. CLOSE UP ON TED'S FACE -
          His eyes go wide, and for a moment, his face freezes with
          fear. TED'S POV - His vision swims a bit more. He knows
          this is not good...
                         
                         
          EXT. CONCESSION AREA - CONTINUOUS
                         
          John reaches the top of the lower seating area, and
          sprints past the concession bar, heading for the stairs.
                          121
                         
                         
          EXT. LIGHTING TOWER - CONTINUOUS
                         
          The struggle continues. As Ted tries to pull himself
          free, the rip gets bigger. He reacts again, and again we
          see his vision swimming even more.
                         
                         
          EXT. STAIRS - CONTINUOUS
                         
          John runs up the stairwell.
                         
                         
          EXT. LIGHTING TOWER - CONTINUOUS
                         
          The struggle continues. Ted tries to pull himself up,
          but he's visibly weakened and his hands are slipping.
                         
          EXT. - STAIRS - CONTINUOUS
                         
          John continues up the stairwell.
                         
                         
          EXT. LIGHTING TOWER - CONTINUOUS
                         
          Ted manages to pull free from Donny. He uses all his
          depleted strength to pull himself farther up.
                         
                         
          EXT. UPPER SEATING AREA - CONTINUOUS
                         
          John runs past the top of the stairwell, and sprints over
          toward the lighting tower, just in time to see...
                         
                         
          EXT. LIGHTING TOWER - CONTINUOUS
          Donny makes one final reach for Ted. He grabs Ted by the
          foot again, and pulls hard. With one great RRRIIIIIIP,
          Ted tears into two pieces. As John watches in shock, Ted
          falls through the air in SLO-MOTION, a shower of white
          stuffing descending with him. Lori watches with a hand
          over her mouth. The two halves of Ted land, along with
          the scattered white stuffing. Donny, still hanging,
          stares down at the fallen teddy bear. He starts pulling
          himself back over the ledge.
                         
          We lead and follow John as he runs back down through the
          stadium with desperate numbness. Lori climbs over the
          edge of the seating area, and runs toward him as well.
          ANGLE BACK ON DONNY, who pulls himself back over into the
          upper seating area. He hears the sound of a cop siren,
          and peers over the edge of the stadium. Seeing a cop car
          pull up far below, he makes a break for it.
                         
                          (CONTINUED)
                          122
                         CONTINUED:
                         
          Down below, Ted's top half lies on the grass, looking
          around in a daze, like a badly wounded soldier for whom
          there is not much hope. John and Lori race to his side,
          and kneel down.
                         
                          JOHN
           Ted!
                         
                          LORI
           Oh my God...
                         
                         
                          TED
           (weak, slow breathing)
           Johnny...
                         
          Ted looks glassy-eyed for a beat. John starts to
          frantically gather up the chunks of stuffing.
                         
                          JOHN
           Lori, get the stuffing! Get it all!
                         
          Lori starts helping him, desperately grabbing chunks of
          the white cotton.
                         
                          TED
           Johnny...
                         
          John leans back over Ted.
                         
                          JOHN
           You're gonna be okay, buddy. you
           understand? You're gonna be fine.
                         
                          TED
                          (WEAK)
           Jesus, I look like the robot from
           "Aliens".
                         
                          JOHN
           No, look at me, buddy. I promise, you're
           gonna be okay.
                         
                          TED
           I... I don't think so. I'm... I'm in
           trouble. I need... I need to tell you
           something.
                         
                          JOHN
           What is it?
                         
                          TED
           Don't... don't ever lose her again.
           She's the most important... most
           important part of your life.
                          (MORE)
                          (CONTINUED)
                          123
                         CONTINUED:
                          TED (CONT'D)
           Even more than me. She's your thunder
           buddy now. She's--
                         
          Ted closes his eyes... and dies. ANGLE DIRECTLY ABOVE
          TED as we pull away, and it starts to rain...
                         
                         
          EXT. JOHN AND LORI'S APARTMENT - NIGHT
                         
          The rain is pouring now. Lori's car pulls up. She and
          John hurry out, John holding the remains of Ted. They
          race inside.
                         
                         
          INT. JOHN AND LORI'S APARTMENT - NIGHT
                         
          John and Lori burst in with the remains of Ted. They're
          both drenched from the rain. Lori frantically searches
          drawers for sewing materials. She finds a needle and
          thread, and John puts Ted on the table. Lori starts to
          sew him up as John watches intently.
                         
                          LORI
           John... I don't know if this is gonna--
                         
                          JOHN
           Just try. Please. Just try.
                         
          She continues sewing, until she is all finished. They
          wait. Ted still does not move. John and Lori lower
          their heads.
                         
                         
          INT. LIVING ROOM - SHORTLY AFTER
                         
          John sits on the couch, head in hands. Ted still lies on
          the coffee table. Lori enters with a blanket, and drapes
          it around him. She sits down next to him, bringing part
          of the blanket around herself. She places a hand on his
          shoulder.
                         
                          LORI
           John... I'm sorry. You did everything
           you could. I'm... I'm just so sorry.
                         
          She gently puts an arm around him. There is a
          thunderclap outside. John does not react.
                         
                          LORI (CONT'D)
           (almost too softly to be
                          HEARD)
           You're not afraid...
                         
                         
                         
                          (CONTINUED)
                          124
                         CONTINUED:
                         
          ANGLE ON TED (shortly after) as a white sofa blanket is
          placed over him. John and Lori shut off the lights, and
          exit...
                         
                          DISSOLVE TO:
                         
                         
          INT. JOHN AND LORI'S BEDROOM/KITCHEN - NIGHT
                         
          John is asleep, but we see that Lori is still lying
          awake. She sighs restlessly, and gets up. She walks
          over to the window, and looks out.
                         
                         
          EXT. JOHN AND LORI'S APARTMENT - SAME
                         
          ANGLE UPWARD - We see a cloudy sky, much like the one
          from that night when John was a child. As before, there
          is a small clear patch in the center. A shooting star
          whizzes by through the opening.
                         
                         
          INT. JOHN AND LORI'S BEDROOM - NIGHT
                         
          Lori's eyes widen a bit in recognition. She stares at
          the shooting star for a beat, then closes her eyes and
          makes a wish...
                         
                         
          EXT./ESTAB. JOHN AND LORI'S APARTMENT - TIME LAPSE
                         
                         
          INT. JOHN AND LORI'S BEDROOM - MORNING
                         
          John wakes up, looks around groggily, then remembers. He
          gets out of bed, and walks toward the living room.
                         
                         
          INT. LIVING ROOM - CONTINUOUS
                         
          He pauses for a beat... and walks in. The blanket is
          where it was left. John slowly removes it. Ted is still
          motionless. John lowers his head sadly. Suddenly, Ted's
          eyes snap open.
                         
                          JOHN
           Ted!
                         
                          TED
                          (RETARDED-SOUNDING VOICE)
           I'm alive, Johnny!
                         
                          JOHN
           Oh my god!
                         
                          (CONTINUED)
                          125
                         CONTINUED:
                         
                          TED
                          (RETARDED-SOUNDING VOICE)
           I'm alive! Your magical wish worked!
                         
                          JOHN
           You're back!
                         
                          TED
                          (RETARDED-SOUNDING VOICE)
           Yeah! I mean, when you sewed me up, you
           put some of the stuffing in the wrong
           places, so I'm a little fucked up. Will
           you take care of me forever and ever?
                         
          John stares at him, confused.
                         
                          TED (CONT'D)
                          (NORMAL VOICE)
           Nah, I'm just kiddin' ya, I thought it'd
           be funny if you thought I was fuckin'
           retarded.
                         
                          JOHN
           You asshole!
                         
          John grabs him and hugs him. Lori enters. She sees
          what's happening, and a huge smile crosses her face.
                         
                          LORI
           Welcome back, Ted.
                         
          John turns to Lori, and realizes...
                         
                          JOHN
           It... it was you. You did it. (cover
           this line with addition:) It was your
           wish.
                         
                          TEDDY
           (smiling, speechless)
           Son of a bitch...You wished for my life
           back.
                         
          She smiles at him.
                         
                          LORI
           No. I wished for my life back. Because
           I love you both.
                         
          John goes to her, and kisses her passionately.
                         
                          TED
           You were pretty great out there at
           Fenway, Johnny.
                         
                          (CONTINUED)
                          126
                         CONTINUED:
                         
                          LORI
           Yeah, that's my big brave man.
                         
                          JOHN
           Oh my god, do you know how awesome it was
           punching a kid? I felt so powerful! I
           mean if that's what it's like to hit a
           woman, watch out, I liked it.
                         
                          LORI
                          (SMILING)
           I love you.
                         
                          JOHN
           I love you, too.
                          (THEN)
           And, I want you to know that... I'm
           probably never gonna be any more than a
           guy who rents cars, but... I don't care.
           You're the only thing that matters in my
           life.
                         
           TED (O.S.)
                          AY--
                         
                          JOHN
           You and Ted.
                         
           TED (O.S.)
           Yes!
                         
                          JOHN
           And after last night, I... I don't ever
           want to lose anyone who matters to me
           ever again. I'm not gonna wait any
           longer for my life to start. Lori...
           will you marry me?
                         
                          LORI
           (beat, she smiles)
           That's all I ever wanted.
                         
          John and Lori kiss as we pull away...
                         
           NARRATOR (V.O.)
           And so John, Lori, and Ted lived happily
           ever after, having discovered at last
           that all they really needed was each
           other. John and Lori were married in a
           beautiful ceremony in Cambridge, by a
           very special Justice of the Peace.
                          127
                         
                         
          INT. CHURCH - DAY
                         
          We hear the Flash Gordon Wedding March as we ANGLE ON Sam
          J. Jones standing in robes at the altar. Ted, in a tux,
          stands in the best man's position. John stands on the
          steps smiling and looking out as we cut to...
                         
          ANGLE ON Lori, walking down the aisle in a wedding dress,
          smiling warmly. TIME CUT to shortly after, as Sam Jones
          addresses the two of them, standing at the altar.
                         
                          SAM JONES
           I now pronounce you man and wife. You
           may kiss the bride.
                         
          John and Lori kiss each other. They turn and wave to the
          cheering crowd. Ted waves happily to John, who waves
          back. John and Lori run down the aisle joyfully, passing
          pews full of people from the movie: Lori's co-workers,
          John's co-workers, (Guy sitting with HIS BOYFRIEND, Alix
          and Tanya, etc.).
                         
                         
          EXT. OLD BOSTON CHURCH - CONTINUOUS
                         
          John and Lori come running out of the church, as the
          crowd throws rice at them. They run to a waiting limo
          with a "Just Married" sign on the back. John gets in,
          and Lori turns to throw the bouquet toward Gina,
          Michelle, Tracy, and Tanya. Tanya catches it. She turns
          and smiles at Alix. Then suddenly, Tami-Lynn bursts into
          frame, punching Tanya in the jaw. Tanya goes down as
          Tami-Lynn tackles her, and the crowd tries to pull her
          off. ANGLE ON the limo as it pulls away...
                         
          Ted stands next to Sam J. Jones, watching with a smile as
          his best friend heads off.
                         
                          TED
           Y'know Sam, there's only one way to end a
           perfect day.
                         
                          SAM JONES
           What's that?
                         
                         
                          TED
           On three.
                         
                          SAM JONES
           What on three?
                         
                          TED
           Flash jump.
                         
                          (CONTINUED)
                          128
                         CONTINUED:
                         
                          SAM JONES
                          (REALIZING)
           Right.
                         
                         
           One... two... three.
                         
          DOWNSHOT Ted and Sam Jones leap into the air at the same
          time...
                         
           TED/SAM JONES
           YEAH!!!
                         
          They freeze frame in mid-air, as the Flash Gordon theme
          kicks in. Over the music:
                         
           NARRATOR (V.O.)
           And that's the story of how one magical
           wish forever changed the lives of three
           very special friends.
                         
          INSERT: footage of Ted and Tami-Lynn from their double
          date.
                         
           NARRATOR (V.O.)
           Ted and Tami-Lynn continued their torrid
           love affair for quite some time. One
           afternoon Ted was caught behind the deli
           counter eating potato salad off of Tami-
           Lynn's bare bottom. He was instantly
           promoted to store manager.
                         
          INSERT: footage of Sam Jones, walking toward John in slow
          motion.
                         
           NARRATOR (V.O.)
           Sam Jones moved back to Hollywood with
           the goal of restarting his film career.
           He currently resides in Burbank where he
           shares a studio apartment with his
           roommate Brandon Routh.
                         
          INSERT: photo of BRANDON ROUTH.
                         
           NARRATOR (V.O.)
           Remember Brandon Routh from that god-
           awful "Superman" movie? Jesus Christ.
           Thanks for getting our hopes up and
           taking a giant shit on us.
                         
          INSERT: footage or Rex at the office.
                         
                         
                         
                         
                          (CONTINUED)
                          129
                         CONTINUED:
                         
           NARRATOR (V.O.)
           Rex gave up his pursuit of Lori. Not
           long after he fell into a deep depression
           and died of Lou Gehrig's disease.
                         
          INSERT: footage of Donny dancing in his living room.
                         
           NARRATOR (V.O.)
           Donny was arrested by Boston police and
           charged with kidnapping a plush toy. The
           charges were dropped when everyone
           realized how completely stupid that
           sounded.
                         
          INSERT: footage of Robert, talking to Ted in his bedroom.
                         
           NARRATOR (V.O.)
           Robert got a trainer, lost a substantial
           amount of weight, and went on to become
           Taylor Lautner.
                         
          INSERT: photo of TAYLOR LAUTNER.
                         
                         
                         
                          THE END
'''
#Gesprochenes zählen

# script.txt contains the sample text you posted
#with codecs.open(script, 'r', 'utf8') as f:

  # read the file content
  #f = f.read()

  # store all the clean text that's accumulated
spoken_text = ''

  # split the file into a list of strings, with each line a member in the list
for line in script.split('\n'):

    # split the line into a list of words in the line
    words = line.split()

    # if there are no words, do nothing
    if not words:
        continue

    # if this line is a person identifier, do nothing
    if len(words[0]) > 1 and all([i.isupper() for i in words[0]]):
        continue

    # if there's a good amount of whitespace to the left, this is a spoken line
    if len(line) - len(line.lstrip()) > 4:
        spoken_text += line.strip() + ' '

spoken = word_tokenize(spoken_text)
#print(spoken)
dialog = len(spoken)


#bestimmt den gesprochenen Anteil
words_spoken = defaultdict(Counter)
currently_speaking = 'Narrator'
speaking_people = []

for line in script.split('\n'):
    name = line.replace('(CONT\'D)', '').strip()
    if re.match('^[A-Z]+$', name):
        currently_speaking = name
        speaking_people.append(currently_speaking)
    else:
        words_spoken[currently_speaking].update(line.split())


pprint(words_spoken)

character1 = input("Enter name of character:")
character2 = input("Enter name of another character:")
character3 = input("Character:")
character4 = input("Character:")


sumchar1 = sum(words_spoken[character1].values())
sumchar2 = sum(words_spoken[character2].values())
sumchar3 = sum(words_spoken[character3].values())
sumchar4 = sum(words_spoken[character4].values())
print(sumchar1)
print(sumchar2)
print(sumchar3)
print(sumchar4)


#Diagramme

labels = [character1,character2]
values = [sumchar1,sumchar2]
sonstige= dialog - sumchar1-sumchar2-sumchar3

word_counts = [sumchar1, sumchar2, sumchar3 , sonstige]
names = [character1, character2, character3, "Sonstige"]
colors = ['#b284be', '#e52b50', '#abcdef', '#848484']
plt.pie(word_counts, labels=names, colors=colors, startangle=90, autopct='%.1f%%')
plt.title('Research on words spoken')
plt.show()
pprint(set(speaking_people))
#f.close()