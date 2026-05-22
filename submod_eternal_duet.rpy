
init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="monika_moon_eternal_duet",
            category=['music'],
            prompt="Listen to Monika Play the Piano",
            random=True,
            aff_range=(mas_aff.ENAMORED, None)  
        )
    )
 
transform piano_move:
    xpos -1.5 yalign 0.5
    linear 5.0 xpos 0

transform piano_return:
    xpos 0 yalign 0.5
    linear 5.0 xpos -1.5

label monika_moon_eternal_duet:
    m 1esa "[player], from the excitement and present affection you are showing me..."
    extend 5hub "I will remember everything you have provided for me."
    m 2hubsb "For this reason, I practiced a piece of music just for you. I think it will bring you a sense of peace. {w=1} I hope you enjoy it~"
    show monika at Transform(xpos=-800) with move
    m 2hua "Let me just get the piano ready..."
    window hide
    $ store.mas_sprites.zoom_out()
    $HKBHideButtons()  
    $ original_music = renpy.music.get_playing(channel='music')
    show mas_piano at Transform(xpos=-1800, ypos=-195) zorder 13
    show mas_piano at Transform(xpos=-5, ypos=-195) with MoveTransition(4.0)
    pause 4.0
    show monika at Transform(xpos=640) with move
    play music "Submods/Literature_and_Daily_Life/L&DL_Assets/music/CaughtinaTropical.ogg" loop fadein 2.0  
    pause 99
    stop music fadeout 0.0
    show monika at Transform(xpos=-800) with move
    pause 1.0
    show mas_piano at Transform(xpos=-1800, ypos=-195) with MoveTransition(4.0)
    pause 5.0
    show monika 2hua zorder MAS_MONIKA_Z at t11 with dissolve_monika  
    show monika at Transform(xpos=640) with move
    $HKBShowButtons()
    window show
    play music original_music fadein 2.0
    return