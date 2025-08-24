init python:
    import random

define f = Character("Fami-kun", color="#ff0000")
define b = Character("Boss", color="#0000ff")
define s = Character("Steve", color="#00ff00")
define j = Character("Jim", color="#ff00ff")

image bg callcenter = "bg/callcenter.png"
image bg home = "bg/home.png"
image bg intro = "bg/intro.png"
image bg meeting = "bg/meeting.png"

image fami-kun bored = "fami-kun/default.png"
image fami-kun default = "fami-kun/default.png"
image fami-kun phone-default = "fami-kun/default.png"
image fami-kun phone-fail = "fami-kun/default.png"
image fami-kun phone-hold = "fami-kun/default.png"
image fami-kun phone-success = "fami-kun/default.png"

image boss default = "fami-kun/default.png"
image boss phone-default = "fami-kun/default.png"

image jim default = "fami-kun/default.png"

image steve default = "fami-kun/default.png"

label start:
    $ points = 0
    $ sales = 0

    # tutorial: track which phone support outcomes the player has already seen, only explain each once
    $ seenSupportSuccess = False
    $ seenSupportFail = False
    $ seenSupportHold = False

    scene bg intro
    show fami-kun default

    "Fami-kun needs your help to climb to the top position in the company."
    "From a simple salaryman to chairman of the company."
    "Do your best in answering phone calls, attending meetings and follow good manners on business dinners."
    "It's gonna be a tough career."
    "Let's start off with some simple phone support. Just assist customers when they call in."
    jump call0

label supportSuccess:
    show fami-kun phone-success
    "Problem solved!"
    if not seenSupportSuccess:
        "Keep it up and you'll be promoted in no time!"
        $ seenSupportSuccess = True

    $ points += 1
    show fami-kun phone-default
    return

label supportFail:
    show fami-kun phone-fail
    "They hung up, apparently unsatisfied."
    if not seenSupportFail:
        "The customer will complain to your manager later. If this happens enough, you'll be fired!"
        $ seenSupportFail = True

    $ points -= 1
    show fami-kun phone-default
    return

label supportHold:
    show fami-kun phone-hold
    "You put them on hold."
    if not seenSupportHold:
        "There's a 50\% chance the next rep is competent enough to solve their problem. Otherwise, the customer will complain to your manager. If this happens enough, you'll be fired!"
        $ seenSupportHold = True

    if random.choice([True, False]):
        $ points += 1
    else:
        $ points -= 1
    show fami-kun phone-default
    return

label call0:
    show bg callcenter
    with pixellate
    show fami-kun phone-default

    "Caller (The White House)" "I lost my launch codes."

    menu:
        "If you'd like some false hope, I can tell you how to defragment your hard drive.":
            "Caller (The White House)" "Can I skip all the steps and just buy a new computer?"
            f "Let me transfer you to the Imarichidiot Department."
            "You scored a sale somehow, earning ¥10,000 in commission! Not that you have any free time to spend it."
            $ sales += 1
            jump call1

        "Don't worry, our security system isn't functional. You don't need the codes to launch our nuclear weapons.":
            call supportSuccess from _call_supportSuccess
            jump call1

        "I'll need your serial number, which is conveniently located inside the unit.":
            jump serial

label serial:
    "Caller (The White House)" "The sticker says my warranty will be void if I open the case."

    menu:
        "Well, call me if anything changes.":
            call supportFail from _call_supportFail
            jump call1

        "Your stubbornness is becoming an obstacle to my financial success.":
            call supportFail from _call_supportFail_1
            jump call1

        "Please hold, another representative will be with you shortly.":
            call supportHold from _call_supportHold
            jump call1

label call1:
    "Caller (Department 5)" "Help, my computer imploded??"

    menu:
        "Shut up and hang up.":
            call supportFail from _call_supportFail_2
            jump call2

        "Have you tried turning it off and on again?":
            call supportSuccess from _call_supportSuccess_1
            jump call2

        "Hello, this is tech support. May I close your ticket now?":
            call supportFail from _call_supportFail_3
            jump call2

label call2:
    "Caller (Vladimir Putin)" "The error message says my copy of Wingdows is not genuine."

    menu:
        "Install Gentoo":
            call supportSuccess from _call_supportSuccess_2
            jump call3

        "I'll walk you through a series of steps that won't work.":
            "Caller (Vladimir Putin)" "Can I skip all the steps and just buy a new computer?"
            f "Let me transfer you to the Imarichidiot Department."
            "You scored a sale somehow, earning ¥10,000 in commission! Not that you have any free time to spend it."
            $ sales += 1
            jump call3

        "Your mousepad is incompatible with your operating system.":
            jump mousepad

label mousepad:
    "Caller (Vladimir Putin)" "How do I fix it?"

    menu:
        "Google it.":
            "They found a better tech support provider on Google."
            call supportSuccess from _call_supportSuccess_3
            jump call3

        "Try hanging up and slamming your head in a drawer.":
            call supportFail from _call_supportFail_4
            jump call3

        "Please hold, another representative will be with you shortly.":
            call supportHold from _call_supportHold_1
            jump call3

label call3:
    "Caller (Jesus Christ)" "I think my digital modem is broken."

    menu:
        "Please hold while I pretend to be testing it... Okay, it looks fine from here. The problem must be in your wiring.":
            jump problemwiring

        "Have you tried turning it off and on again?":
            jump offon

        "Please hold, another representative will be with you shortly.":
            call supportHold from _call_supportHold_2
            jump call4

label problemwiring:
    "Caller (Jesus Christ)" "How do I fix it?"

    menu:
        "Google it.":
            "They found a better tech support provider on Google."
            call supportSuccess from _call_supportSuccess_4
            jump call4

        "You'll have to rip out all of the wiring in your entire house to locate the problem.":
            jump ripwiring

        "Your stubbornness is becoming an obstacle to my financial success.":
            call supportFail from _call_supportFail_5
            jump call4

label offon:
    "Caller (Jesus Christ)" "I can't find my power button."

    menu:
        "Install Gentoo.":
            call supportSuccess from _call_supportSuccess_5
            jump call4

        "Have you tried turning it off and on again?":
            jump offon

        "Try hanging up and slamming your head in a drawer.":
            call supportFail from _call_supportFail_6
            jump call4

label ripwiring:
    "Caller (Jesus Christ)" "Are you sure? Because the lights on the modem aren't even on."

    menu:
        "That means you have moisture on your internal wiring. You'll also need to replace all of your plumbing and get a new roof.":
            "They gave up and switched to a better ISP."
            call supportSuccess from _call_supportSuccess_6
            jump call4

        "Please hold, another representative will be with you shortly.":
            call supportHold from _call_supportHold_3
            jump call4

        "Your stubbornness is becoming an obstacle to my financial success.":
            call supportFail from _call_supportFail_7
            jump call4

label call4:
    "Caller (The Monkeys in Sales)" "COMPUTER'S BROKEN!"

    menu:
        "Is it a PC or a Mac?.":
            jump pcmac

        "Have you tried turning it off and on again?":
            jump offon1

        "What's the precise nature of the problem?":
            jump precisenature

label pcmac:
    "Caller (The Monkeys in Sales)" "YES!"

    menu:
        "The problem is in the part of your brain that handles intelligence.":
            call supportFail from _call_supportFail_8
            jump meeting0

        "What's wrong with it?":
            jump whatswrong

        "What's the precise nature of the problem?":
            jump precisenature

label offon1:
    "Caller (The Monkeys in Sales)" "I CAN'T FIND MY POWER BUTTON!"

    menu:
        "Install Gentoo.":
            call supportSuccess from _call_supportSuccess_7
            jump meeting0

        "Have you tried turning it off and on again?":
            jump offon1

        "Try hanging up and slamming your head in a drawer.":
            call supportFail from _call_supportFail_9
            jump meeting0

label precisenature:
    "Caller (The Monkeys in Sales)" "EMAIL!"

    menu:
        "Email me a list of things you already tried. I'll go down the list and make you try every single thing again, sometimes more than once.":
            call supportFail from _call_supportFail_10
            jump meeting0

        "What's wrong with it?":
            jump whatswrong

        "The battery on my phone is dying! *click*":
            call supportSuccess from _call_supportSuccess_8
            jump meeting0

label whatswrong:
    "Caller (The Monkeys in Sales)" "BROKEN DOWN!"

    menu:
        "Broken down how?":
            jump brokenhow

        "Our software is perfect. The problem must be with you.":
            call supportFail from _call_supportFail_11
            jump meeting0

        "What's the precise nature of the problem?":
            jump precisenature

label brokenhow:
    "Caller (The Monkeys in Sales)" "BIG LOUD NOISE!"

    menu:
        "Google it.":
            call supportFail from _call_supportFail_12
            jump meeting0

        "Your stubbornness is becoming an obstacle to my financial success.":
            call supportFail from _call_supportFail_13
            jump meeting0

        "What's the precise nature of the problem?":
            jump precisenature

label meeting0:
    show boss phone-default at right
    show fami-kun phone-default at left
    b "Fami-kun! It's time for today's meeting on things... and stuff."

    menu:
        "On my way!":
            jump meeting1
        "The battery on my phone is dying! *click*":
            jump gohome

label meeting1:
    show bg meeting
    with pixellate
    show boss default at right
    "Welcome to your first meeting!"
    "Here's your chance to show your boss the value you add to the company."
    "The general idea is to use as many meaningless buzzwords as possible."
    b "Hey all."
    b "Let's start today's meeting off with some introductions. Bob, you can start us off."
    show steve default at left
    s "Uh, hi. I'm Bob."
    "..."
    b "You call that an introduction? You're fired."
    b "Wait here, I've got Bobs to fire."
    hide boss
    s "Joke's on him. I'm Steve."
    "Well, that's one strategy."
    "It's an easy ride to the top if you get all your coworkers fired!"
    show boss default at right
    b "Alright, carry on. Jim?"
    show jim default
    j "Yo. I'm Jim, in Sales. I hold the office's high score in Minesweeper."
    s "No one cares."
    b "Hey, I fired you!"
    b "...I think."
    b "Whatever. Fami-kun?"

    menu:
        "I'm Fami-kun, in tech support. I started working here last week. I look forward to working with you all.":
            jump lastweek
        "I'm Fami-kun, in tech support. I'll have you know I graduated top of my class in first grade, and I've been involved in numerous phone calls, and I have over 3 closed tickets. I am trained in gorilla phone support and I'm the top support guy in the entire department. You are nothing to me but just another employee.":
            jump gorillasupport
        "Uh, hi. I'm John.":
            jump imjohn

label lastweek:
    $ points -= 3
    b "Wait, you've only been working here for a week?"
    "Your boss doesn't have the best memory. Seems he's looking for reasons to fire people, so be careful!"
    jump meeting2

label gorillasupport:
    $ points += 2
    b "That sounds impressive."
    b "...I think."
    jump meeting2

label imjohn:
    $ points -= 2
    b "Nice try! No one named John works here."
    b "...I think."
    jump meeting2

label meeting2:
    b "Anyhow, on to the meeting!"
    b "I lost the meeting agenda, so let's just do status reports and pretend the meeting accomplished something."
    b "Bob, what have you been working on today?"
    s "I arrived to work an hour late and proceeded to stare at the ceiling all day."
    b "Well, you were two hours late yesterday. Good work!"
    b "...I think."
    b "Jim?"
    j "I sold some equipment to myself, and made way too much in commission."
    j "I'm gonna resell it on ePay tonight."
    b "Uh..."
    b "Good enough! A sale's a sale."
    b "Fami-kun?"

    menu:
        "I leveraged proven just-in-time cloud strategies to efficiently integrate solutions with customers.":
            jump cloudstrategies
        "I sold some computers.":
            jump salessalessales
        "I beat Jim's Minesweeper score.":
            jump beatjim

label cloudstrategies:
    $ points += 2
    b "Whatever that means, it sure sounds impressive!"
    jump meeting3

label salessalessales:
    if sales > 0:
        $ points += sales * 2
        b "Wow! That's not even your job! Keep it up, Fami-kun."
    else:
        $ points -= 2
        b "No you didn't."
    jump meeting3

label beatjim:
    $ points += 2
    b "Wow! That's not your job, but Minesweeper is probably more profitable than tech support anyway."
    b "...I think."
    jump meeting3

label meeting3:
    b "Well, that's all for today's meeting! I'll see you all at dinner tonight."
    jump dinner0

label gohome:
    show fami-kun default at center
    hide boss
    "Uh..."
    "You managed to avoid the meeting!"
    "Everyone else is distracted in the meeting, so you may as well go home early."

    scene bg home
    with pixellate
    show fami-kun default
    "On second thought, there's nothing to do at home."

    $ stares = 0
    jump homeactivities

label homeactivities:
    menu:
        "Stare at the ceiling.":
            jump stare
        "Stare at the wall.":
            jump stare
        "Stare at the floor.":
            jump stare
        "Take a nap.":
            jump nap

label stare:
    $ stares += 1
    if stares == 100:
        "That's enough of that."
        jump dinner0
    else:
        show fami-kun bored
        "Thrilling."
        "Now what?"
        show fami-kun default
        jump homeactivities

label nap:
    show bg home
    with fade
    "That's enough of that."
    jump dinner0

label dinner0:
    return

label call5:
    "Caller (Bob)" "I can't log in."

    menu:
        "You were fired.":
            jump bobfired

label call6:
    "Caller (Jim)" "Minesweeper won't open."