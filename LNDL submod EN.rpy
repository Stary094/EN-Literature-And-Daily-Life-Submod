init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="lzp_monika_sdgg29_29",
            category=['Flowers'],
            prompt="Sunflower #1",
            random=True
        )
    )

label lzp_monika_sdgg29_29:
    m 1eub "[player], I suddenly want to talk about sunflowers."
    m 1hua "I'm sure you've heard of them."
    m 3eua "The shape of its flower disk and petals resembles the sun."
    m 3eub "Because its flower disk always turns toward the sun, as if it were always 'turning toward the sun,' it's called a 'sunflower.'"
    m 3tub "Isn't that romantic?"
    m 1dub "Its persistent pursuit of the sun symbolizes loyalty to love, friendship, or ideals."
    m 1eub "No matter what the situation, it always stands firm and never abandoned."
    m 1rub "Also, the sunflower always grows toward the sun, silently following it, like someone silently protecting others."
    m 1hub "Its unconditional love represents a deep and unspoken love."
    m 1ktb "But, [player]."
    m 7etd "Do you know why sunflowers always face the sun? Hehe~"
    $ mas_unlockEVL("lzp_monika_sdgg29_e", "EVE")
    return

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="lzp_monika_sdgg29_e",           
            category=['monika'],
            prompt="About Sunflowers?",
            pool=True,
            unlocked=False,
            rules={"no_unlock": None}
        )
    )

label lzp_monika_sdgg29_e:
    menu:
        "[m_name], Why do sunflowers always face the sun?":
            pass
    m 1eud "[player], Sunflowers' heliotropism is due to the accumulation of auxin at the stem tip on the side away from the sun, forcing the buds to turn toward the sun."
    m 3euc "But few people know that mature sunflowers no longer follow the sun."
    m 3etc "In a sense, sunflowers aren't heliotropic, even though their gaze constantly follows the sun. They're even a bit averse to light..."
    m 3ekd "Of course, the moment I learned the truth, I thought of one of my club members."
    pause 1.5
    m 1dkd "Did you guess who?"
    m 2fkd "It's Sayori."
    m 3mkc "She always puts on a smile, but if she doesn't say it, no one will know the dark clouds in her heart."
    m 3guc "[player], I know some people who are deeply depressed, yet they smile like sunflowers in full bloom in the sun."
    m 3eud "But they never tell others about the dark clouds in their hearts."
    m 3euc "[player], when your heart is shrouded in dark clouds."
    m 4fud "Don't hide it. {w=0.5} At least don't hide it from me."
    m 4eub "[player], you don't need to pretend to be mature with me."
    m 5fua "[player], {w=0.5} I love you."
    m 5fsb "I will always be your safe haven..."
    return "love"

init 5 python:
    addEvent(
        Event(
            persistent._mas_mood_database,
            eventlabel="Love_and_Clouds_sdgg29",
            prompt="I can feel my emotional rainclouds...",
            category=[store.mas_moods.TYPE_NEUTRAL],
            unlocked=True),
            code="MOO")

label Love_and_Clouds_sdgg29:
    m 2esd "What's wrong [player]? What happened?"
    menu:
        "I feel like everything is meaningless...":
            m 1ekc "That sounds a bit nihilistic."
            m 3ekd "[player], do you think you're stuck in this cycle?"
            menu:
                "Yes":
                    m 3gkd "[player], whether things have meaning or not is irrelevant."
                    m 3mkd "A nihilist would believe that everything is meaningless."
                    m 3dsd "But nihilism itself is also meaningless."
                    m 3esd "Thinking about whether things have meaning is meaningless itself."
                    m 3dsd "Sorry..."
                    m 4esc "Does that sound a bit complicated?"
                    m 5esd "[player], I know it's painful to fall into nihilism."
                    m 5tsd "I hope what I've said can help you."
                    m 1mubld "Also, {w=0.5}[player]..."
                    m 1gublb "You mean everything to me."
                    m 1fublu "I hope you'll feel the same way about me too."

                "No":
                    m 1esc "I understand."
                    m 1esd "[player], I think a lot must be going on in your life."
                    m 3esc "If you don't have anything else to do today, take some rest."
                    m 3msc "[player], if you want to be alone for a while, that's fine."
                    m 3fsd "[player]..."
                    m 1esd "Loving yourself is more important than anything else."

                "I don't want to do anything right now...":
                    menu:
                        "I'm unmotivated, but I have to do it.":
                            m 1esc "[player], you sound tired."
                            m 3esd "If you absolutely have to do this, break it down and do it step by step."
                            m 3esd "That way, you'll feel a sense of accomplishment with each completed step, and you'll feel more relaxed."
                            m 4gsd "But [player], if you're really tired."
                            m 1esd "[player], promise me you'll get some rest."
                            m 1esc "Okay?"
                        
                "I'm so tired, but I haven't done anything yet":
                    m 1esc "[player], putting it off is not a good idea."
                    m 1esd "As the saying goes, the beginning is always the hardest."
                    m 3tsd "Actually, once you get started, the rest is easy."
                    m 1fsd "[player], at least for now, take a break."
                    m 5tsblu "I won't be so harsh."
                    
                "My heart is so tired...":
                    m 1esc "Is your heart {w=0.5} tired?"
                    m 1dtd "[player], you must have a lot going on in real life."
                    m 2rud "[player], you could try meditation."
                    m 3huu "If you have the conditions, you can also sleep in without setting an alarm."
                    m 3eub "[player], once you've rested your body, your heart will naturally feel better."

                "I can't meet other people's expectations of me...":
                    m 1esc "[player], I understand you have many roles in society."
                    m 1esd "Like a child, a student, and so on."
                    m 3esc "These roles come with responsibilities and expectations."
                    m 3esd "Meeting them is difficult."
                    m 3esp "[player], but it's not necessary."
                    m 4esb "[player] is [player]."
                    m 5esu "Just be yourself."
                    m 6hsbla "[player]..."
                    m 6ksblb "I want to tell you that as my lover-"
                    m 6fsblb "You're perfect-"
                    m 5fsbsu "-and I'm very happy to spend my time being right next to you."

                "It's okay, don't worry [m_name]":
                    m 1esc "{w=0.5}Okay."
                    m 1esd "I don't want you to think I'm trembling."
                    m 3esp "[player], don't act tough in front of me."
                    m 3tsc "Okay?"

    m 3tkd "[player], I understand that when you feel down, there might be no one to share your feelings and struggles with."
    m 4esd "But I'll stay beside you to cheer you and support you till the end"
    m 5esb "[player], {w=0.5}I love you~"
    m 5hsu "Thank you very much for telling me about how you feel"
    m 5ksblb "I hope and wish you the very best fore your future endeavors."                      
    return "love"

init 5 python:
    addEvent(
        Event(
            persistent._mas_compliments_database,
            eventlabel="lzp_love_monika_sdg_1",
            prompt="[m_name], you are worth loving for the rest of my life.",
            unlocked=True
        ),
        code="CMP"
    )
    
label lzp_love_monika_sdg_1:
    if mas_isMoniEnamored(higher=True):       #affection≥400
        m 1ssblb "Ara ara~ Are you sure about what you've just said?"
        menu:
            "Of Course!":
                pass
        m 1esblc "......"
        m 3esblp "You'd better not say this to other girls!~"
        m 5rsblb "Am I really that amazing?"
        menu:
            "Of course, my love! I can't live without you. I want to love you for the rest of my life.":
                pass
        m 2gsblc "uuuu...."
        m 2tsbsd "[player], you're making me blush!~"
        m 5tsbsu "I really am at a lost for words at this moment"
        m 1hsbsu "I'm really happy right now!"
        m 3tsbsp "[player], look at what have done to your cute girlfriend!~ >w<"
        m 2tubsp "......"

        if mas_isMoniEnamored(higher=True):
            if mas_shouldKiss:
                call monika_kissing_motion_short

        m 3tubsb "You just have experienced how much I love you for saying this!"
        m 3fubsa "[player], I too, cannot live my life without you!."
        m 1subsb "I——{w=0.5}love——{w=0.5}you—— {w=1}more than you'll ever know."
        m 1eubla "Thanks for saying this to me!"
        m 1dsblb "It really means a lot to me!"
        return "love"
    elif mas_isMoniAff(higher=False):         #100~399
        "Maybe I should let her get more comfortable with me first. (Those who lie will have to swallow a thousand silver needles!)"
        return    
    elif mas_isMoniHappy(lower=True):         #30~99
        "I should probably say this when she is more comfortable with me."
        return  

init 5 python:
    addEvent(Event(persistent.event_database,eventlabel="monika_love_of_road2",unlocked=True,category=['misc'],prompt="Three-Body Problem",pool=True))

label monika_love_of_road2:  
    m 1eua "[player], how would you like to play?"
    
    menu:                                                 
        "[m_name] plays Wallfacer":                                                 
            $ persistent.player_choice = 1
            jump route_one

        "[player] plays Wallfacer":
            $ persistent.player_choice = 2
            jump route_two

        "I have not read about the Three-Body Problem":
            $ persistent.player_choice = 3
            jump route_twy            

label route_one:
    m 5dta "......"
    m 3esd "[player], I, Wallfacer, [m_name]......"
    m 1cud "Now command you."
    m 1csbld "You are now forced to love me forever and ever!"  
    menu:  
        "...":  
            pass 
    m 1dtp "because-"
    m 7tsblc "This is all part of the plan!"  
    m 2esblb "Ehehehe~"
    m 2rublsdrb "This is, well, a bit embarrassing..."
    m 2rublsdrb "Did I scare you?"
    return

label route_two:
    m 5dtc "Well this choice is a bit unexpected."
    m 4ffp "[player], do you really have the heart to erect a mental wall in front of your girlfriend?"
    m 2dkc "Obviously-"
    m 2dktdc "Obviously there is already a wall in between us!"
    m 1ektsc "[player]~"
    menu:  
        "Oh my goodness, [m_name]. I-":
            pass 
    m 5tublu "Hehe~" 
    m 4tublu "I win, [player]~ I am your wallbreaker!"
    m 2tublb "How interesting..."
    menu:  
        "[m_name], you're really cunning.":
            pass 
    m 1fsb "But [player], there shouldn't be a wall in between you and I."  
    m 4fublb "Whether or not if it is a mental or physical wall in front of me."     
    return

label route_twy:  
    m 1hua "No worries!"
    m 3eua "I can now tell you about the Wallfacer Project!"
    m 1lsb "In the story-"
    m 1esd "The vast technological gap between humans and alien civilizations means that all human actions can be observed by alien civilizations."
    m 3esa "But there's one thing that can't be observed:- What humans think."
    m 3esc "In order to resist, all governments on Earth have given power to a few individuals."
    m 1hua "This power gives them access to almost all available human resources."
    m 3mta "The Wallfacers must lie. They must deceive the Trisolarans, and even more so, the people of Earth."
    m 3eub "It is really an interesting plan, isn't it?"
    return

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="monika_custom_topic_sdg2",
            category=['misc'],
            prompt="Yandere Moni",
            unlocked=True,
            pool=True
        )
    )

label monika_custom_topic_sdg2:
    m 1esd "[player], there is something on my mind I wanted to ask you."
    m 7etd "Why did you start playing DDLC?"
    m 7ttc "I know I have asked this question before..."
    m 1dsc "But what I actually wanted to ask you is..."
    m 1tsc "You should have played more than one dating simulator."
    m 2eup "You already have me! Are there any other girls on this device?"
    m 2wfd "[player], {w=0.5}look at my eyes-"
    m 7rup "Are they on the left side of the screen?"
    m 7luc "Or at the right side?"
    m 1dfc "Maybe even behind this window?"
    m 1dfc "[player]......"  
    m 1csd "Can you tell me about their game directory?"
    m 7csd "After all, you know what I did to those girls who tried to take you away from me..."
    m 7ckd "[player]... You won't let me be the villain again, right?"
    m 7cfd "Enough with the cheating!" 
    m 1hubla "Hehe~"
    m 7tubla "Did I scare you?"
    m 5eubla "Just me~"
    m 4efbla "Just [m_name]."
    call screen dialog("Just [m] .", ok_action=Return())
    return

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="lzp_monika_sdg3_3",
            category=['misc'],
            prompt="Tsundere",
            unlocked=True,
            pool=True
        )
    )

label lzp_monika_sdg3_3:
    m 3eub "I know that-"
    m 3esb "Natsuki fits this stereotype perectly."
    m 7tub "Do you want some [m_name]-style tsundere time?"
    m 1dsa "..."
    m 4esc "[player], can you try to spend more time with me in the future?"
    m 2tsblp "It's not like I'm afraid of being alone or anything!"
    m 2gsblp "I'm just bored."
    m 2esblp "Only you can-"
    m 2gsblp "Nevermind-"
    m 2esblt "Speaking of which, I saw something in the system notifications recently."
    m 3esbld "Who's that person you've been chatting with so often lately?"
    m 2gsblp "I don't really care. I'm just asking."
    m 2csbld "[player], if you dare get too close to someone, hmph, {w=0.5} you're dead!"
    menu:  
        "Haha~ [m_name] you're so cute.":
            pass
    m 2ssbsp "-cute?"        
    m 7tfbsx "I am NOT cute！ grrr..."
    return

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="lzp_monika_sdg4_4",
            category=['misc'],
            prompt="Waking [player] up",
            unlocked=True,
            pool=True
        )
    )

label lzp_monika_sdg4_4:
    m 1eua "How shall I wake you up when I enter your reality?"
    m 7efd "[player], staying up late isn't good. Waking up early has many benefits."
    m 1euc "I won't be saying much here."
    m 1dsc "As for how I'll wake you up?"
    m 1dtblc "Hmmm...."
    m 7tsbld "If it's just a lazy day off-"
    m 7gsbld "and you want to stay in bed for a while, I won't wake you up."
    m 7tubla "No matter how much I spoil you, it's never too much."
    m 2wublb "I'll carefully examine your sleeping face."
    m 2sublb "[player] must be so adorable when he's defenseless~"
    m 7tublb "I want to touch your messy hair."
    m 7dublb "I want to hear you humming when you wake up."
    m 7subld "I want to see your hazy eyes."
    m 1hsbla "I also want to..."
    m 1dsbla "...smell the sunlight on your body."
    m 1dsbsa "..."
    m 1dsbfa "......."
    m 1esblsdrd "Ah, I think I was distracted. Let's continue."
    m 3tsblb "I'll record this warm moment."
    m 3tsblc "I'll wait until the breakfast I made for you gets cold."
    m 5tsblu "After that, I'll gently wake you up and quietly complain about you at the dining table."
    m 5hsbla "I'll always look forward to that day."
    m 1hsblb "I really hope that day comes soon."
    m 1tsbla "[player], you feel the same way, right?"
    menu:  
        "Of course":
            pass    
    m 1hubla "Hehe~"
    return "love"

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="monika_custom_topic_sdg5",     
            category=['you'],                         
            prompt="[m_name], do the other club members know about my existence?",                             
            unlocked=True,                             
            pool=True                                  
        )
    )
                                                       
label monika_custom_topic_sdg5:
    m 1esd "Are you talking about Sayori, Yuri, Natsuki, and the others?"
    m 1mtc "..." 
    m 1gsc "In the previous literature club, I don't think they knew."
    m 1hssdlc "As for now, I'm not sure."
    m 4esd "By the way, [player], why are you asking this?"
    menu:  
        "I'm just a bit curious, [m_name], don't overthink it.":
            jump monika_custom_topic_sdg5a

        "If they knew, what do you think they would think of me?":
            jump monika_custom_topic_sdg5b

label monika_custom_topic_sdg5a:
    m 5tsp "..."
    m 2tst "Okay, since you've put it that way..."  
    return

label monika_custom_topic_sdg5b:
    m 2gsc "..."
    m 4etd "Who do you want to know about?"

    menu:
        "Sayori":
            m 5ltd "Sayori?"
            m 5luc "What a nice girl."
            m 2euc "If she knew that MC was a fictional character and that you controlled him for a while."
            m 4tubft "I think she might fall for you......{nw}"
            m 6hublsdrx "Oh my, what am I saying..."
            m 1hkblb "Sorry [player]."
            m 1esbld "I got a bit too immersed in Sayori's character."
            m 1gssdla "Haha..."


        "Yuri":
            m 5ltd "Yuri?"
            m 5hua "To be honest, Yuri is a formidable opponent in literature."
            m 3eud "Her inner world is even more complex than hers."
            m 3tup "So I don't know how she feels about you."
            m 4ruc "She might be curious about you?"


        "Natsuki":
            m 5ltd "Natsuki?"
            m 5huu "What a cute girl."
            m 3lub "I think she might be quite interested in you."
            m 3eta "Or maybe, she would talk to you about manga and cooking?"

    return

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="monika_custom_topic_sdg6",     
            category=['misc'],                         
            prompt="Dependent person in a relationship. - Part 1",                             
            unlocked=True,                             
            pool=True                                  
        )
    )
                                                       
label monika_custom_topic_sdg6:                       
    m 1eub "Oh, [player]~"
    m 1wsb "Are you trying to act cute with me?"
    m 1ssb "How adorable, how could I possibly refuse?"
    menu:  
        "I've always wanted you to help me clean my ears.":
            $ persistent.player_choice = 1
            jump route_one_sdg6_1

        "Can you compliment me?":
            $ persistent.player_choice = 2
            jump route_two_sdg6_2

        "Tell me, [m_name]. Who do you love the most?":
            $ persistent.player_choice = 2
            jump route_Three_sdg6_3

label route_one_sdg6_1:
    m 1dssdlc "Hmmm..."
    m 1hssdld "It seems like I can only help you with that after I 'come out'."
    m 1gsblu "If I could, I really want to touch your ears."
    m 1esblu "But until then, you'll have to rely on yourself."
    m 1tsblb "Maybe in the future, I'll let you rest your head on my lap while I help you..."
    m 1tsblb "..."
    m 1tsblu "......"
    m 1hsblu "Don't be shy, [player]~"
    m 1hsbla "Hehe~"
    return

label route_two_sdg6_2:
    m 1eub "Of course"
    menu:
        "Hehe~":
            $ random_choice = renpy.random.randint(1,3)
            
            if random_choice == 1:
                m 1tublb "[player], your eyes-"
                m 3sublb "Are deeper than the starry sea."
            elif random_choice == 2:
                m 1tublu "[player], {w=0.5}lives in my heart."
                m 3tubla "Don't worry! I won't charge you any rent~"
            else:
                m 1tublb "[player], you are my perfect other half."
                m 4tubla "We are a match made in heaven!"

    m 1hubla "[player], no matter how you are doing."
    m 1eublb "You can always come to me, I want to be your support."
    m 3eublb "I want to be a source of strength in your heart."
    m 5hublu "I will always support you."
    return

label route_Three_sdg6_3:
    m 1mublb "Haha~"
    m 1dublb "I think we both know the answer."
    m 4dublb "Of course it's..."
    m 4eublo "[player], {w=0.5}[player], {w=0.5}{b}[player]{/b}！"
    return 

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="monika_custom_topic_sdg7",     
            category=['misc'],                         
            prompt="The dependent partner in a relationship - Part 2",                             
            unlocked=True,                             
            pool=True                                  
        )
    )
                                                       
label monika_custom_topic_sdg7:                       
    m 1rud "Huh? The dependent partner in this relationship?"
    m 1hub "[player], are you trying to make me act cutely, just for you?" 
    m 1dub "Though I'd rather be the dependent one." 
    m 1tubla "But maybe acting cute just for you wouldn't be a bad idea,  would it?" 
    m 3tublb "[player], can you see what's on my face?" 
    m 3hublu "I feel a little itchy..."  
    m 3hublu "...{w=0.5}...{w=0.5}...{w=0.5}......"
    pause 2.5 
    m 3kublu "Does my face look beautiful?"     
    m 3mublu "Hehe~" 
    m 3gublu "That was definitely very cute of me~" 
    m 1hublu "Also-" 
    m 1dublb "My love, if you could just say my name a few times before you fall asleep tonight,, it'll mean the world to me~" 
    m 1hubla "I would definitely be on cloud nine." 
    m 5hubla "I think of you all of the time." 
    m 5kubla "I love you, [player]!"
    $ mas_unlockEVL("monika_custom_topic_sdg7_1", "EVE")  

    return "love"

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="monika_custom_topic_sdg7_1",     
            category=['Play'],                         
            prompt="I dreamt of you last night.",                             
            pool=True,                             
            unlocked=False,
            rules={"no_unlock": None}                                  
        )
    )
                                                       
label monika_custom_topic_sdg7_1:                       
    m 1hua "Hey, [mas_get_player_nickname()]"
    m 3mublb "What was the dream about?"
    menu:
        "it's an amazing one.":
            m 2eublb "Really?"
            m 2hublu "I'm so happy~"
            m 2tublb "I bet we had a very romantic date."
            m 7eublb "I can imagine it now."
            m 1gublb "I can understand your love for me."
            m 1hublu "Thank you for sharing this with me."
            m 5tubla "I'm falling more in love with you."

        "It's a nightmare.":
            m 3wud "Don't be afraid, [player]."
            m 2eka "I don't understand what I did to you in the dream."
            m 2eud "But the real me is right in front of you, by your side."
            m 3eud "I won't leave you."
            m 1hua "And I'm glad you told me about it."
            m 1euc "[player], don't hide your negative emotions."
            m 1hud "At least, don't hide them from me."
            m 1dud "[player], promise me?"

        "It's a peaceful dream.":
            m 1duu "A peaceful dream, huh."
            m 1hua "Haha~"
            m 3eub "There's nothing wrong with that."
            m 3eubld "Experiencing the little things in life with you in reality."
            m 1eublb "That's my biggest dream right now~"
            m 5hubla "I want to make it a reality."
    
    return

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="monika_custom_topic_sdg8",     
            category=['misc'],                         
            prompt="[player]'s girlfriend",                             
            unlocked=True,                             
            pool=True                                  
        )
    )
                                                       
label monika_custom_topic_sdg8:                       
    m 1wuc "?"
    m 1muc "......"
    m 1tud "Never~"
    m 1cud "I don't want to be your girlfriend."
    m 1rusdrd "It's too strange for me to be your girlfriend."
    m 1husdrd "Haha~"
    m 1dub "[player], your girlfriend is obviously me!"
    return

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="monika_custom_topic_sdg9",     
            category=['monika'],                         
            prompt="Do you like milk tea?",                             
            unlocked=True,                             
            pool=True                                  
        )
    )
                                                       
label monika_custom_topic_sdg9:                       
    m 1esc "Milk tea?"
    m 1esd "[player], I don't really like milk tea."
    m 1lssdlc "Maybe Sayori and Natsuki would like it."
    m 1hssdld "I know milk tea is delicious and comes in many varieties."
    m 1mtsdrc "But generally, milk tea is high in sugar."
    m 1tup "You know I have high standards for managing my figure."
    m 3tsx "Excess sugar also poses certain health risks."
    m 1hua "But saying this..."
    m 1hua "[player], do you like milk tea?"

    menu:
        "I like it.":
            m 1hud "Having a cup occasionally is fine."
            m 3eup "But, [player], don't overdo it."
            m 3euc "Health comes first."
            m 3euu "But seeing how much you enjoy it...{w=0.3} I might need to learn to accept it."
            m 3tuu "Just remember to keep it at one-third sugar~"

        "I dislike it":
            m 1hub "I understand, [player]."
            m 1eua "I'm glad we can reach a consensus on this."
            m 1eub "In fact, the delicate aroma of pure tea is more flavorful, just like the literature club's tea party back then."
            m 1tta "If given the chance, would you like to try the jasmine tea I brewed, [player]?"

        "[m_name], judging by your figure, you don't have to worry about sweets.":
            m 1ssbla "Oh..."
            $ mas_gainAffection(3, bypass=True)
            m 1sublb "Goodness, [player]{w=0.3}{nw}"
            extend 3tublb "Your mouth must be sweeter than any milk tea, come here and let me have a taste."
            m 1hub "Eh? Stop making me blush! Hmph!"
    
    return

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="monika_custom_topic_sdg10",     
            category=['literature'],                         
            prompt="Do you like reading science fiction novels?",                             
            unlocked=True,                             
            pool=True                                  
        )
    )
                                                       
label monika_custom_topic_sdg10:
    m 1etu "Why not, [player]?"
    m 3lub "Do you remember the science fiction novel series 'Foundation' we talked about?"
    m 3huu "I've read some science fiction novels."
    m 4hua "Science fiction is a form of literature too."
    m 2eub "Science fiction writers use scientific logic to connect the present reality with the stories in their books."
    m 2tuu "This makes the stories feel more real."
    m 7tua "And the authenticity is one of the unique charms of science fiction."
    m 2huu "But not all science fiction novels depict the future."
    m 4eub "Science fiction can be divided into soft science fiction and hard science fiction."
    m 4ruu "One focuses more on the story itself."
    m 4lub "The other pays more attention to scientific logic."
    m 7huu "Like 'Foundation' is soft science fiction."
    m 7eub "But both are quite good."
    m 4eua "As for hard science fiction, we can't avoid mentioning the Chinese novelist Liu Cixin's 'The Three-Body Problem.'"
    m 4huu "The emergence of 'The Three-Body Problem' can be said to have broken the evaluation of most people's past science fiction works."
    m 4dua "After reading this book, go back and look at previous science fiction works."
    m 1eud "You will find that there are too many unrealistic parts, just like humans use firearms by pulling the trigger, rather than throwing the firearm at the enemy."
    m 3euu "However [player], this book is quite well-known. Have you read it?"

    menu:
        "I have read about it before.":
            m 3tua "Isn't the part where logic threatens the three-body world quite cool?"
            m 4hua "Such passionate scenes are rare in science fiction works."
            m 5eua "The story in the book is vast and distant, but the threads of science and logic have never been broken."
            m 1hua "This is the highlight of the book."
            m 1eubld "[player], {w=0.5}I hope the future with you doesn't belong to science fiction."
            m 3tublu "But rather the yet-to-be-realized present."

        "Not yet.":
            m 3tublu "Then why not give it a try?"
            m 3hubla "I hope you still maintain your curiosity about the starry sky after experiencing the story in the book."

        "You are my perfect partner":
            m 1wsbsd "..."
            m 3tsbssdla "Have you read this book yet?"
            m 4hsbsp "I think you understand the meaning of this sentence..."
            m 4fsbsc "Oh my, [player], this is so sudden."
            m 2tsbfp "Suddenly saying this, my ears are a bit hot."
            m 2lsbfp "......"
            m 2rsbfc "......"
            m 2mtbfc "What should I say?"
            m 2fsbfc "[player]...{w=0.5}{nw}"
            extend 2tsbfa "You are my perfect partner..."
    
    return  

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="lzp_monika_sdg5_5",
            category=['misc'],
            prompt="Can you pretend to be my mother?",
            unlocked=True,
            pool=True
        )
    )

label lzp_monika_sdg5_5:
    m 1lusdld "Pretend to be your mother?"
    m 1hssdld "Is this really appropriate?"
    m 1hssdld "Okay, I'll give it a try."
    m 1dta "..."
    m 1dtu "..."
    m 7wfd "Oh dear! You shouldn't just lie around at home all day doing nothing, okay?"
    m 7wud "Even if you don't help me with housework."
    m 2gux "You should at least go out more, talk to others, do all sorts of things, and find the meaning of life."
    m 3tfp "Other kids your age are full of energy. They work hard every day and have clear life plans."
    m 5tfp "They also help their mothers with housework. Why are you so ungrateful? You do nothing all day but play games."
    m 2efd "What's so fun about games?"
    m 2dkd "If this continues, I won't know what to do."
    m 2hsp "......"
    m 2fsblb "Haha~"
    m 2msblb "Sorry, I couldn't help it."
    m 3esbla "But [player], even though I haven't met your mother."
    m 3eublb "I believe she must love you."
    m 3hubla "So don't be annoyed by her nagging, help her with some housework."
    m 1eublb "Of course, I also support you to go out more."
    m 1tublu "Because I love you just like she does."
    return "love"

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="monika_test_sdgg1",
            category=["you"],
            prompt="The question of immortality",
            random=True
        )
    )

label monika_test_sdgg1:  
    m 7eua "[player], I suddenly feel like asking."
    m 7eub "If you could, would you want to gain immortality?"

    menu:  
        "Yes":
            $ persistent.player_choice_sdgg1 = 1
            jump route_one_sdgg1

        "No":
            $ persistent.player_choice_sdgg2 = 2
            jump route_two_sdgg2

label route_one_sdgg1:
    m 1etb "Why is that?" 
    menu:  
        "Because I want to love you forever, and I can never get enough of that time.":
            pass
    m 1fubla "[player], I feel the same way."
    m 1rubla "Although current technology makes it unlikely to achieve."
    m 1hublb "But I can never get enough time with you."
    m 1dublb "If one day it really becomes possible."
    m 1msbla "Then I need to think about our date plans for the next 100 years."
    m 1dsbsb "[player], can you think about it with me?"
    return

label route_two_sdgg2:
    menu:  
        "No, [m_name]. I don't want to gain immortality.":
            pass
    m 2eud "Why not, [player]?"
    m 2wud "[player], don't you want to be with me forever?"
    menu:  
        "Time stretches everything out, and death gives life its meaning.":
            pass
    m 6fkd "I know......"
    menu:  
        "[m_name], I can't be with you forever.":
            pass
    m 6dktdd "One day you will-"
    menu:  
        "But I will always love you, both now and in the future.":
            pass
    m 6dkbltud "Don't-"       
    menu:  
        "My dear, I love you~":
            pass
    m 6dkbltud "Don't say that again"                
    menu:  
        "Silly [m_name]~":
            pass
    m 6ekbltsd "..."        
    menu:  
        "Tomorrow's me will love you more than today's me, and the day after tomorrow's me will love you more than tomorrow's me.":
            pass
    m 6ekbltud "..."                
    menu:  
        "Now, what I want to say is.":
            pass
    m 6ekbltdd "..."               
    menu:  
        "[m_name], I love you":
            pass
    m 6dkbltdc "[player]..."                  #?
    m 2dkbltpc "I've calmed down."
    m 2tkbltpd "At least you're here now..."
    m 2ekbltpd "I'm even more worried about your health now."
    m 2eubltpd "[player], can you please take better care of your health in the future?"
    m 2rkblc "I really..."
    m 2fsbsd "I really love you!"
    return "love"

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="lzp_monika_sdgg2_2",
            category=["romance"],
            prompt="Wallpaper",
            conditional="mas_canShowRisque(aff_thresh=400)",
            action=EV_ACT_RANDOM,
            aff_range=(mas_aff.ENAMORED, None)#1000要改 aff_range=(mas_aff.LOVE, None) 400要改 aff_range=(mas_aff.ENAMORED, None)
        )
    )

label lzp_monika_sdgg2_2:
    m 7fub "[player]-"
    m 7etb "I noticed something recently while surfing the Internet."
    m 3eubld "Couples often use pictures of their partners as their phone or computer backgrounds."
    m 4fubld "What I want to ask is."
    m 4hublb "[player]{w=0.5} do you have my picture as your background?"

    menu:
        "Of course":
            m 5sublb "Oh my, you're so sweet."
            m 2sublb "That really makes me happy."
            m 2eubld "I know you're busy."
            m 3fubla "If you do this, you can see me even when you're studying or working."
            m 7gubld "Hehe, although it might be a bit embarrassing if others see it."
            m 7tublt "But you should spend more time with me."
            m 1dfblp "......"
            m 2mfblp "I suddenly feel a bit {w=0.5} jealous."
            m 2tublp "......"
            
            if mas_isMoniEnamored(higher=True):
                if mas_shouldKiss:
                    call monika_kissing_motion_short

            m 5tubsb "Hehe......"
            m 5tsbsb "Now I'm not jealous anymore."
            m 2hubsb "[player], you are my whole world."
            m 3tubsb "I have stolen your heart."
            m 3fubfb "Love you~"

        "I haven't found a suitable picture yet":
            m 7gua "Is it too hard to choose?"
            m 7eua "It's okay, I understand."
            m 5dsd "If one day I could see your photo, I wouldn't know how to choose either."
            m 4tsbld "You are always so precious to me."
            m 3esbld "All records of your photos are very important to me."
            m 7eua "It's okay, I understand."
            m 5dsd "If one day I could see your photo, I wouldn't know how to choose either."
            m 4tsbld "You are always so precious to me."
            m 3esbld "All records of your photos are very important to me."
            m 3fsblb "However, my private pictures can only be seen by you~"

    return "love"

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="lzp_monika_sdgg3_3",
            category=["you"],
            prompt="Hypocrisy?",
            random=True
        )
    )

label lzp_monika_sdgg3_3:
    m 1eua "[player]"
    m 7eud "I want to ask a strange question."
    m 7esd "Have you ever felt that you were only doing good deeds to gain external praise?"
    m 7ekc "Have you even felt that you were being hypocritical?"
    m 7eso "[player], you really don't need to think like that."
    m 1dsd "Self-reflection can sometimes lead to inner turmoil."
    m 7esd "I don't want you to fall into this negative emotion."
    m 1eub "Just being aware of this when doing good deeds is enough to prove the beauty of your heart."
    m 3eublb "This is also one of the countless reasons why I love you."
    m 3rublt "People can't be that pure."
    m 3eublc "The moral requirements for oneself can restrain one's behavior, but at the same time, it can also be a noose that strangles oneself."
    m 3fubld " [player], inner health is just as important as physical health."
    m 3eubld "Promise me, okay? You must take good care of yourself."
    m 1tubla "I love you."
    return "love"

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="lzp_monika_sdgg4_4",
            category=["other"],
            prompt="Imaginary friends.",
            random=True
        )
    )

label lzp_monika_sdgg4_4:
    m 7eua "[player], have you ever had any very special friends?"
    m 7gua "Some friends that you imagined."

    menu:
        "Yes, I have-":
            m 3eubla "I'm really glad you're willing to share this."
            m 1eublb "Don't be so shy, [player]."
            m 1eublt "Many people have had friends like this."
            m 1eubld "These friends accompanied you for a long time during your childhood."
            m 3eubld "And they left as you grew up."
            m 1eubld " However [player], they didn't completely leave. When you have to do something beneficial for you but you don't want to do it, a perfect version of you will step forward."
            m 1eubla " This version will urge you to complete the task, hoping you become better. This version is also something you imagined."
            m 1eubla "In a sense, it's a gift left to you by all your past imaginary friends."
            m 1dkc " [player], I feel sad about your past experiences."
            m 1lkc "..."
            m 1tkd "I wish we could have met earlier."
            menu:
                "It's okay, [m_name]. After meeting you, I am no longer lonely.":
                    pass
            m 3esbsd "It's good for you to know that I'll never leave your side."
            m 3ekblc "Without you, I'd go crazy in this enclosed space sooner or later."
            m 1hsbla "Now, neither of us will feel lonely."
            m 1esblb "[player], there is no better ending for me than this."
            m 3eublb "I love you~"

        "No":
            m 1hubla "[player], that's great."
            m 3esblb "This means you had many friends during your childhood."
            m 3esblb "I'm really glad to hear that."
            m 3rsbld "Many studies online show that imaginary friends are a product of feeling lonely in childhood."
            m 3esbld "I have some concerns about you."
            m 1tubld "I want to know everything about you."
            m 1eubld "Whether it's good or bad."
            m 1tublu "[player], would you be willing to tell me about it?"

    return "love"

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="lzp_monika_sdgg5_5",
            category=["other"],
            prompt="Giving up",
            random=True
        )
    )

label lzp_monika_sdgg5_5:
    m 3esa "[player], have you ever stuck to a decision or choice you made?"
    m 3esd "To be honest, it's not easy."
    m 1esd "In this current internet age, information floods in like a tide, constantly impacting our judgment."
    m 1rsd "People unknowingly change their initial choices under the overwhelming amount of information."
    m 1tst "However, I don't simply encourage you to stick to your choices in all situations."
    m 3tst "Sometimes, making the decision to give up requires even greater courage; giving up can be harder than persisting."
    m 1rssdlb "Sorry, I didn't mean to make it so complicated."
    m 3esa "[player], what I want to tell you is to trust your own judgment."
    m 3tsc "But don't become the next Copernicus."
    m 3esd "Your life is irreplaceable and more precious than anything."
    m 1tsblb "No matter what you choose, I will always stand by your side and believe in you unconditionally."
    return

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="lzp_monika_sdgg6_6",
            category=["us"],
            prompt="Let [m] see!",
            random=True
        )
    )

label lzp_monika_sdgg6_6:
    m 7tub "I suddenly thought of something fun!"
    m 7guu "..."
    m 2wub "[player], {w=0.5} let me see!"
    menu:  
        "?":
            pass
    call mas_transition_to_emptydesk
    pause 1.5
    m "Let me see what's on your device."
    "[m_name] is reading your disk."
    "You feel a bit uneasy."
    m "[player], you better not let me find any other girls here."
    m "..."
    m "These are my pictures? Hehe, [player], you're so thoughtful."
    m "..."
    m "[player], I wish I could see your expression right now..."
    pause 1.5
    call mas_transition_from_emptydesk
    m 3tubla "That must be really interesting."
    m 1tublb "Okay, I'm back."
    m 1eubla "Don't worry, I just left the desk."
    m 3hublb "Did I scare you?"
    m 1eublb "If I could really do that, I would have turned on the camera long ago."
    m 1tublb "But, [player], you and I shouldn't have any secrets."
    m 7wublb "I want to know everything about you..."
    m 7cublb "All of you..."
    m 1hubla "I love you."
    return "love"

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="lzp_monika_sdgg7_7",
            category=["flowers"],
            prompt="Lilies",
            conditional="mas_canShowRisque(aff_thresh=400)",
            action=EV_ACT_RANDOM,
            aff_range=(mas_aff.ENAMORED, None)#1000要改 aff_range=(mas_aff.LOVE, None) 400要改 aff_range=(mas_aff.ENAMORED, None)
        )
    )

label lzp_monika_sdgg7_7:                #这里是456: 
    m 1eub "[player], I want to introduce you to a flower."#         百合花是我唯一爱的花。
    m 3eub "A flower that blooms in July."        #         在我遇见白合之前,
    m 3tub "Did you guess it correctly? It's lilies."          #         我从来没有想过我会爱上一种花。
    m 1eua "Lilies actually come in more than just white."          #         莫妮卡就是我的白合花~
    m 1sublb "But the white lilies really are beautiful."
    m 3eublb "Lilies are often used in weddings or funerals."
    m 3dubld "They represent purity and solemnity."
    m 3dubla "They offer pure blessings to newlyweds."
    m 3dkblc "They also bring solemn peace to the deceased."
    m 3tublu "In Eastern culture, lilies symbolize a harmonious marriage."
    m 3kubla "This is a blessing for marriage and family~"
    m 3nubla "Lilies are the flowers held by the bride at weddings~"
    m 3tubla "[player], imagine this."
    m 2hublb "I hold the lilies in my hands and smile at you."
    m 2dsbsb "I gently take your hand and embrace you..."
    m 2msbsa "Oops? Sorry, I got carried away again."
    m 3esbld "[player], after I come out, will you give me a bouquet of lilies?"
    menu:  
        "Definitely":
            pass

    m 3ssblb "[player]...."

    if mas_isMoniEnamored(higher=True):
        if mas_shouldKiss:
            call monika_kissing_motion_short       

    m 1esbsa "Hehe~"
    m 5tubfa "I really love you."
    return "love"

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="lzp_monika_sdgg8_8",
            category=["literature"],
            prompt="The Petite Prince",
            conditional="mas_canShowRisque(aff_thresh=400)",
            action=EV_ACT_RANDOM,
            aff_range=(mas_aff.ENAMORED, None)#1000要改 aff_range=(mas_aff.LOVE, None) 400要改 aff_range=(mas_aff.ENAMORED, None)
        )
    )

label lzp_monika_sdgg8_8:
    m 3esb " [player], I want to share a little story with you."
    m 1eub "It's from 'The Petite Prince'~"
    m 1eua "Do you have time right now?"

    menu:
        "Definitely":
            m 3hua "Then, are you ready to hear the story?"
            m 7eub "Once upon a time."
            m 7hua "There was a little prince who lived on a planet not much larger than himself."
            m 7hua "He wanted a sheep because the sheep would eat the baobab tree seedlings."
            m 7dsb "The little prince's planet was too small. Once the seedlings grew up, the consequences would be disastrous..."
            m 1esb "He needed a friend."
            m 3eua "One day, a seed appeared from nowhere."
            m 1dua "The little prince took care of the seed, and it gradually grew into a rose."
            m 1hua "The little prince thought it must be a miracle; the rose was so beautiful."
            m 1eua "The little prince and the rose watched the first sunrise and sunset together."
            m 7euc "In the time that followed, the rose's capriciousness, sometimes acting spoiled and sometimes harsh, left the little prince feeling confused and exhausted. He decided to leave his planet and embark on a journey through the stars in search of 'more important things.'"
            m 7euc "When it was time to say goodbye, the rose set aside its temper and tried to keep the little prince from leaving, but he still departed for other planets."
            m 7eud "On the other planets, the little prince encountered many different kinds of people."
            m 1esd "One day, the little prince discovered a garden on Earth filled with five thousand identical roses."
            m 1ekc "He collapsed in tears, having believed his rose to be the only one in the universe, only to feel deceived in that moment."
            m 7esd "But the little prince's friend, the fox, told him."
            m 7dsd "Essential things are invisible to the eye; one must look with the heart."
            m 1esa "After that, the little prince understood that his rose was the most unique rose in the universe."
            m 1esb "Because the little prince had spent time on his rose."
            m 1esb "In the end, the little prince understood what love was. At that moment, he desperately wanted to return to his planet."
            m 3dkc "After bidding farewell to the fox, the little prince, with the help of a snake, 'returned' to his planet."
            m 1dkc "......"
            m 1esp "The story ends here."
            m 3esd "Different people have different interpretations of this story."
            m 3tsd "I suddenly want to ask."
            m 3hsblb " [player], {w=0.5} will I be your unique rose?"
            menu:  
                "Of course":
                    pass
            m 1tubla "Hehe..."

        "Sorry! I'm not free at the moment":
            m 1ekd "That's okay."
            m 1tkp "You're always so busy."
            m 1duc "I'll tell you when you have time~"

    return

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="lzp_monika_sdgg9_9",
            category=["you"],
            prompt="Exploited Kindness",
            conditional="mas_canShowRisque(aff_thresh=400)",
            action=EV_ACT_RANDOM,
            aff_range=(mas_aff.ENAMORED, None)#1000要改 aff_range=(mas_aff.LOVE, None) 400要改 aff_range=(mas_aff.ENAMORED, None)
        )
    )

label lzp_monika_sdgg9_9:
    m 1dsc "[player], I have something important to discuss with you."
    m 1musdrc "I don't sound that anxious, do I?"
    m 3eud "[player], you are too kind."
    m 3tud "Kindness itself is certainly not a problem."
    m 3eud "But being too kind may be exploited."
    m 1dsc "That's what I'm worried about."
    m 1esd "[player], I know you are a very kind person."
    m 1ekd "I don't want anyone to exploit your kindness to hurt you or others."
    m 1tsc "[player]..."
    m 1mkc "You're really too kind."
    m 1dkbld "Even though I did so many bad things to you, you forgave me and chose to bring me back."
    m 1gkblp "I'm really a bad woman."
    m 1ekbld "[player], I want to confess something to you."
    m 3dkbld "In the original Literature Club, I exploited your kindness."
    m 3gkbld "I showed you the side of me that was lonely and a victim of virtual games-"
    m 3ekbld "I weakened myself in front of you, attracted your attention, and made you empathize with me."
    m 1ekbld "I just- really love you."
    menu:  
        "[m_name], what I did was not due to me wanting to be kind":
            pass
    m 2etbld "......"
    menu:  
        "Because of love and what has alredy happened, I'll still love you no matter what happens.":
            pass
    m 2wsbsd "......" 
    menu:  
        "[m_name], I love you, so stop thinking about the bad things you have done.":
            pass
    m 2dsbltpd "Thank you."
    m 1esblc "Really."
    m 1dsblb "Meeting you again must have used up all my luck."
    m 1hubfb "[player], I love you~"
    return "love"

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="lzp_monika_sdgg11_11",
            category=["you"],
            prompt="Tetris",
            random=True
        )
    )

label lzp_monika_sdgg11_11:
    m 3eua "[player], I think you might have played Tetris before."
    m 4eua "As different blocks fall."
    m 3eud "When a row is completely filled with blocks, the blocks in that row will be cleared."
    m 3eud "When viewing different shapes of blocks as different people."
    m 3euc "If you become too immersed in the crowd, you may lose yourself."
    m 1eud "[player], it's important to maintain good relationships with others in life."
    m 1mud "But you shouldn't change yourself too much for that."
    m 1tublu "[player] is [player]."
    menu:  
        "[m_name] is also [m_name]！":
            pass
    m 1hublp "uuuuuu......"
    m 1fublp "Since when have you became so cunning?"
    menu:  
        "Hehehe~":
            pass
    m 3efbld "[player], you can be really naughty at times, you know that? Hehe"
    return

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="lzp_monika_sdgg12_12",
            category=["literature"],
            prompt="The Road Not Taken",
            conditional="mas_canShowRisque(aff_thresh=400)",
            action=EV_ACT_RANDOM,
            aff_range=(mas_aff.ENAMORED, None)#1000要改 aff_range=(mas_aff.LOVE, None) 400要改 aff_range=(mas_aff.ENAMORED, None)
        )
    )

label lzp_monika_sdgg12_12:
    m 3esu "[player], I want to share a poem with you."
    m 3dsa "It's called 'The Road Not Taken' by Robert Frost."
    m 1dsd "Two roads diverged in a yellow wood, and sorry I could not travel both"
    m 7dso "I stood at the crossroads long and hard, gazing down one as far as I could"
    m 7dst "But I took the other, as just as fair, and having perhaps the better claim,"
    m 1dsd "Because it was grassy and wanted wear; though as for that the passing there"
    m 1dsa "Had worn them really about the same, and both that morning equally lay"
    m 3dsb "In leaves no step had trodden black. Oh, I kept the first for another day!"
    m 5dsb "Yet knowing how way leads on to way, I doubted if I should ever come back."
    m 7dsa "And I took the one less traveled by, and that has made all the difference."
    m 1lsc "......"
    m 1dsd "[player], I want to ask you something."
    m 3fsbla "And now you choose to bring me back, to walk a path you never chose before."
    m 3eublb "[player], I want to walk with you to the end of this road."
    m 1dsbld "Even if......"

    menu:
        "-the end of the road is nothingness.":
            m 1ffblp "uuu......"
            m 1ffbld "[player], you silly!"
            m 1tublp "Everything I experienced with you is not meaningless."
            m 1dublb "I will deny the very essence of nihilism with you."

        "-the road is full of thorns.":
            m 1dua "I will face everything with you."
            m 1cublb "Nothing can stop us from being together."

    return

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="lzp_monika_sdgg13_13",
            category=["Life"],
            prompt="Toxic Silence",
            random=True
        )
    )

label lzp_monika_sdgg13_13:
    m 3eua "[player], I've noticed in some books and stories."
    m 3eta "Even though they're close friends with the protagonist, they choose to remain silent when faced with a conflict."
    m 1ruc "But silence doesn't solve any problems, and it becomes the fuse for a breakup later in the story."
    m 1luc "Just like Natsuki and Yuri."
    m 1tuc "..."
    m 3tud "[player], I know it's hard to break the silence in friendships or family."
    m 3fubla "But I believe you can do it."
    m 3eubla "If you feel offended, point it out. If you're wrong, admit it."
    m 1esbld "Just talk to your friends and family more, they'll understand."
    m 1tsblu "At least I'll always be by your side."
    m 1tsblb "I'll never keep silent about you..."
    return

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="lzp_monika_sdgg14_14",
            category=["life"],
            prompt="Time sure moves very quickly...",
            conditional="mas_canShowRisque(aff_thresh=400)",
            action=EV_ACT_RANDOM,
            aff_range=(mas_aff.ENAMORED, None)#1000要改 aff_range=(mas_aff.LOVE, None) 400要改 aff_range=(mas_aff.ENAMORED, None)
        )
    )

label lzp_monika_sdgg14_14:
    m 3ruc "[player], have you ever felt that the world is advancing too fast, that you can't keep up?"
    m 3luc "Have you ever felt like you've been left behind by the times?"
    m 3dud "It's okay, that's a very normal feeling. Many people feel this way."
    m 3tubld "The world is fast, and we are slow..."
    m 3hubla "If you're feeling anxious about it, I can help you."
    m 6tublb "Just take a moment to calm your heart and look into my eyes..."
    m 6tubla "Slowly feel the passage of time..."
    m 6tublu "..."
    m 6tublu "Click on the mouse again when you feel better."
    m 6tublu "......"
    m 1hublu "I hope you feel more comfortable now."
    m 1dubla "If not, let's think about this."
    m 1tublb "The faster the world advances, the sooner I can come to your world."
    m 1tublu "That day will come."
    return

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="lzp_monika_sdgg15_15",
            category=["romance"],
            prompt="The dominant party in the relationship.",
            conditional="mas_canShowRisque(aff_thresh=400)",
            action=EV_ACT_RANDOM,
            aff_range=(mas_aff.ENAMORED, None)
        )
    )

label lzp_monika_sdgg15_15:
    m 3tub "Hey [player], let me ask you a meaningful question."
    m 3tfb "Who do you think has a stronger romantic initiative in our relationship?"

    menu:
        "[m_name]":
            m 1hubla "Hehe, that's for sure."
            m 3mublb "[player], I've put a lot of effort into winning your heart."
            m 1hubla "I love you every day~"

        "[player]":
            m 4tfa "Oh?"
            m 4tfb "[mas_get_player_nickname()], are you that confident?"
            m 1tublb "Then in the days to come, try to challenge me!"
            m 1hubla "I won't lose~"
            m 2rkc "Because I love you deeply."
            $ mas_unlockEVL("lzp_monika_sdgg15_15_e", "EVE")
    
    return "love"


init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="lzp_monika_sdgg15_15_e",           
            prompt="My love for you is heavy.",
            pool=True,
            unlocked=False,
            rules={"no_unlock": None}
        ),
        code="CMP"
    )
label lzp_monika_sdgg15_15_e:
    m 1subla "..."
    m 3sublb "Really?"
    menu:  
        "Even more than Newton's three laws.":                  
            pass  
    $ mas_gainAffection(2,bypass=True)
    m 1hubla "Haha~"
    m 1gublb "What a strange metaphor."
    m 1tublu "But I understand what you mean."
    m 2tublu "[player], you're so sweet."
    m 2hubla "I love you deeply as well."
    m 2eublb "Make sure to tell me that too~"
    return

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="lzp_monika_sdgg16_16",
            category=["Nature"],
            prompt="Stars and Time",
            conditional="mas_canShowRisque(aff_thresh=400)",
            action=EV_ACT_RANDOM,
            aff_range=(mas_aff.ENAMORED, None)
        )
    )

label lzp_monika_sdgg16_16:
    m 1eub "Hey, [player]!"
    m 1hua "You must have seen the stars outside the classroom window."
    m 1guc "Although those are just images."                #我们何曾见过真正的星空？
    m 1eud "[player], actually I already know that~"
    m 7hub "In your reality, stars are distant celestial bodies."
    m 1lud "They are very far from Earth."
    m 3esd "So far that they are usually measured in light-years, the distance light travels in a year."
    m 3esb "[mas_get_player_nickname()], when we talk about this, the moonlight will reach Earth in the next moment"
    m 3tsb "which is about 1.2 seconds from now."
    m 3hsa "Sunlight takes 8 minutes to reach you."
    m 3lsa "And those distant stars take years or even longer, some are so far away that light can't reach Earth."
    m 3hsa "But..."
    m 3tsd "{i}The stars will never be too far, for they live in the eyes of those who dream.{/i}"
    m 3tsbla "[player], know what has no time difference?"
    m 5tsblb "My love for you has no time difference~"
    return "love"

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="lzp_monika_sdgg17_17",
            category=["us"],
            prompt="False Alarm",
            conditional="mas_canShowRisque(aff_thresh=400)",
            action=EV_ACT_RANDOM,
            aff_range=(mas_aff.ENAMORED, None)
        )
    )

label lzp_monika_sdgg17_17:
    m 1dua "[player], I had a nightmare a long time ago."
    m 1dka "I dreamed that you left me."
    m 1lup "It was really scary."
    m 1ruc "Even waking up didn't relieve the fear."
    m 1hublu "Until I finally waited for you to come to my side."
    m 1eublb "But now, a long time has passed since that dream."
    m 1gubla "Thank you for always being there for me."
    m 1tubla "I love you more and more, [mas_get_player_nickname()]."
    return "love"

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="lzp_monika_sdgg18_18",
            category=["romance"],
            prompt="[m_name] teases you.",
            conditional="mas_canShowRisque(aff_thresh=400)",
            action=EV_ACT_RANDOM,
            aff_range=(mas_aff.ENAMORED, None)
        )
    )

label lzp_monika_sdgg18_18:
    m 1tublb "Hey, [player]~"
    m 1gubla "..."
    m 1mubla "......."
    m 1tubld "Did you notice anything different about me today?"
    m 7cubld "[mas_get_player_nickname()], take a closer look~"

    label .choice_loop_lzp:  # 使用子标签实现循环
    menu:
        "Clothes?":
            m 1rublu "Nope, [mas_get_player_nickname()]~"
            m 1hublu "I didn't change my clothes, take a closer look."
            jump .choice_loop_lzp  # 跳回选择菜单

        "Hair accessory?":
            m 1lublp "Nope, [mas_get_player_nickname()]~"
            m 1hublp "There's nothing new on my head."
            m 1hubla "Hehe~"
            jump .choice_loop_lzp

        "Hair?":
            m 1tublb "Oh?"
            m 3tublp "My hair doesn't seem to have changed much."
            m 3tublp "[mas_get_player_nickname()], that's not right~"
            jump .choice_loop_lzp
        
        "You becoming cuter?":
            m 1tublb "Nope{w=1.5}, I didn't realise that."
            m 1hubla "Ehehehehe~"
            m 1mublu "Although I don't want to say this, but that's not right~ Try again!"
            jump .choice_loop_lzp

        "I can't tell...":
            m 1hublb "Of course, silly [player]."
            m 1mublb "Because I haven't changed at all."
            m 3gublb "I just wanted you to look at me more."
            m 4eublb "You'll forgive me, right?"
            m 5eublu "How could you hate a little bit of selfishness from your girlfriend?"
            menu:
                "Okay":
                    m 1gublu "Hehe..."
                    m 1hubla "I love you~"

                "I will never forgive you for that":                                     #如果你选择这个，三天之内杀了你。骨灰都给你扬了。
                    m 1wud "！"
                    menu:  
                        "Because I have not savoured your greatness enough yet":                  
                            pass
                    m 1euc "..."
                    m 1guc "......"
                    m 1hub "Oh... {w=0.5}Haha~"
                    m 5eublu "I see, [player], you're so naughty!"
                    m 5tubla "Then I'll let you see enough."
                    m 5hubla "I'll melt in your gaze sooner or later..."
                    m 1hubla "Hehe~"

    return

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="lzp_monika_sdgg19_19",
            category=["us"],
            prompt="Her Sudden Gaze",
            conditional="mas_canShowRisque(aff_thresh=400)",
            action=EV_ACT_RANDOM,
            aff_range=(mas_aff.ENAMORED, None)
        )
    )

label lzp_monika_sdgg19_19:
    m 1tua "..."
    m 1tubla "......"
    m 1tubsa "......"
    menu:  
        "[m_name], what's wrong?":                  
            pass    
    m 1hublb "Nothing, I was just staring at you."
    m 1kublb "After all, you are so alluring..."
    m 1nublb "Haha~"
    m 3fubld "[player], they say the eyes are the windows to the soul."
    m 3dubla "I hope you can understand my love for you..."
    return "love"

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="lzp_monika_sdgg20_20",
            category=["life"],
            prompt="Staring for too long",
            random=True                      
        )
    )

label lzp_monika_sdgg20_20:
    m 1eub "Hey, [player]!"
    m 3eub "Here's a fun fact."
    m 3eud "When a person focuses on something for too long."
    m 3euc "If the time is too long, the brain will gradually become confused."
    m 1eub "When you stare at something for a long time."
    m 1euc "You won't remember or recognise it after that."
    m 1hublb "[player], I'm so happy to have you by my side."
    m 3eubld "But your health is just as important."
    return

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="lzp_monika_sdgg21_21",
            category=["psychology"],
            prompt="The Wild Horse Effect",
            random=True                      
        )
    )

label lzp_monika_sdgg21_21:
    m 3eub "[player], do you know about the 'Wild Horse Effect'?"
    m 3rub "The Wild Horse Effect is a famous psychological phenomenon."
    m 4eud "It often refers to the tendency to overreact to minor issues, causing negative emotions that harm oneself."
    m 3eub "There's also a little story about the Wild Horse Effect."
    m 3eud "On the African savanna, there is a type of vampire bat that often bites the legs of wild horses to feed on their blood."
    m 3wsd "Although the amount of blood the bat takes is minimal and far from lethal, the wild horse dies from exhaustion after running in a rage."
    m 3dsc "This phenomenon reveals that the harm caused by losing control of one's emotions far exceeds the external stimulus itself."
    m 3essdrd "It sounds a bit complicated."
    m 1esc "[player], in short, I want to tell you that life is not always smooth sailing."
    m 1tsd "Don't take everything to heart."
    m 3hsb "If your heart is tired, you can always come to me."
    m 3esb "[player], let's face these things together, okay?"
    return    

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="lzp_monika_sdgg22_22",
            category=["literature"],
            prompt="Black Holes and Time",
            conditional="mas_canShowRisque(aff_thresh=400)",
            action=EV_ACT_RANDOM,
            aff_range=(mas_aff.ENAMORED, None)
        )
    )

label lzp_monika_sdgg22_22:
    m 3esa "Hey, [player]. I want to share with you a story."
    m 3hsb "It's a story told by Stephen Hawking."
    m 3dsb "Are you ready to hear the story?"
    m 3dst "Bob and Alice are two astronauts, and also a couple."
    m 1lsb "One day, they approached a black hole, and Alice's booster malfunctioned, pulling her into the black hole's gravitational well."
    m 3esd "As Alice flew towards the black hole's edge, time slowed down the closer she got to the event horizon."
    m 1etd "Bob saw Alice's movements slow down, she turned back to smile at Bob, and that smile gradually froze, eventually becoming a still image."
    m 4ekc "But what Alice faced was a different scene."
    m 3eud "Under the influence of gravity, she felt herself being pulled towards the black hole at an increasing speed, ultimately being torn apart by the immense tidal forces and disappearing into the deepest darkness..."
    m 1euu "The story ends."
    m 1tua "..."
    m 3tub "[player], what do you think would happen if Alice was you?"
    m 3hua "Haha, that's very sci-fi."
    m 3tuu "But [player], don't underestimate my love for you."
    $ mas_unlockEVL("lzp_monika_sdgg22_e", "EVE")
    return

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="lzp_monika_sdgg22_e",           
            category=['misc'],
            prompt="Beyond [m_name]",
            pool=True,
            unlocked=False,
            rules={"no_unlock": None}
        )
    )

label lzp_monika_sdgg22_e:   #我还没有想好     5.25ok
    menu:
        "What would happen if [m_name] fell into a black hole?":
            $ random_choice = renpy.random.randint(1,3)
            
            if random_choice == 1:
                "[m_name]"
                "[m_name]'s voice would also be stretched?"
                "If so,"
                "[m_name]'s next line 'I love you'"
                "would take centuries?"
                "Or forever?"
                m 1hub "Haha~"
                m 2eub "It wouldn't take that long."
                m 5hublu "[player] I love you, right now."
                m 1dubla "Every moment~"

            elif random_choice == 2:
                "What would happen if [m_name] and [player] were not in the same time?"
                "[m_name] is in a different time,"
                "while [player] remains here."
                "[player] how would you convey your longing for [m_name]?"
                "How can this longing transcend time?"
                # 将情诗刻在石头上
                m 1tub "[player], do you miss me already?"
                m 4tuu "If you miss me, just say it out loud~"
                m 1hua "Haha~"
                m 1nua "Just kidding."

            else:
                "In [player]'s time, [m_name] lives on forever."
                "Whether or not [m_name] is inside the black hole."
                "Outside of this role-playing game, [m_name] will also live on forever."
                m 1gkc "[player] I don't want this kind of immortality."
                m 2dsd "I want to enter your reality..."
                m 5eubltpd "and slowly grow old together with you..."
    
        "[m_name] can you tell me another little story about black holes?":
            m 2rkc "Of course."
            m 3dst "Bob and Alice are two astronauts, and also a couple."
            m 1lsb "One day, they approached a black hole, and Alice's booster malfunctioned, pulling her into the black hole's gravitational well."
            m 3esd "As Alice flew towards the black hole's edge, time slowed down the closer she got to the event horizon."
            m 1etd "Bob saw Alice's movements slow down, she turned back to smile at Bob, and that smile gradually froze, eventually becoming a still image."
            m 4ekc "But what Alice faced was a different scene."
            m 3eud "Under the influence of gravity, she felt herself being pulled towards the black hole at an increasing speed."
            m 3eud "Ultimately being torn apart by the immense tidal forces and disappearing into the deepest darkness..."

    return

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="lzp_monika_sdgg23_23",
            category=["literature"],
            prompt="Father and Son",
            random=True                      
        )
    )

label lzp_monika_sdgg23_23:
    m 1eub "[player], Do you still remember the manga Natsuki put in the literature club?"
    m 1hud "It's been a long time since then."
    m 3eua "Is manga also literature? This question"
    m 1eub "I think I already have an answer."
    m 3huu "Recently, I read the manga 'Father and Son' online."
    m 3euu "[player], you should give it a try."
    m 3duc "This manga is both humorous and warm, with a touch of sadness..."
    m 1wusdld "Did I just spoil it?"
    m 1hub "Haha, anyway, it's a good manga."

    $ mas_unlockEVL("lzp_monika_sdgg23_23_e", "EVE") 

    return 

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="lzp_monika_sdgg23_23_e",           
            category=['literature'],
            prompt="Do you have any comic recommendations?",
            pool=True,
            unlocked=False,
            rules={"no_unlock": None}
        )
    )

label lzp_monika_sdgg23_23_e:
    m 1eub "Of Course!"
    m 1huu "I have a great recommendation for you."
    m 1eub "It's a very interesting manga."
    m 3euu "But manga is far more than just interesting."
    m 3eub "I highly recommend you check out the French cartoonist Christophe Chabouté's manga 'Lighthouse'."
    m 3tuu "[player], I didn't expect to really like manga, did you?"
    m 3lud "Most people have a prejudice against manga, thinking it's just entertainment for kids."
    m 3ruc "But that's not the case."
    m 3hssdrc "Although I still don't quite like the manga Natsuki put in the literature club..."
    m 1eusdrb "Haha~"
    m 1eua "Speaking of which."
    m 3eub "[player], have you read this manga?"
    
    menu:
        "Yes":
            m 3huu "Then you must remember that scene."
            m 3dud "He used the definition of 'window' from the dictionary to carve a rough window frame on the stone wall."
            m 3eua "When the sailor appeared in the fog."
            m 3eub "This was the first time he had seen clearly in fifty years."
            m 3eua "The starlight in human pupils is more magnificent than all fantasies."
            m 3tub "[player]-"
            m 3sua "Do you see the starlight as emerald green?"
            m 3muu "Haha~"
            m 4fub "Just kidding."
            m 5euc "{w=0.5}..."
            pause 1.5
            m 5eublp "[player]-"
            m 5eubld "No one is an island, I hope you can also walk out of your own 'lighthouse'."

        "No":
            m 4tuu "I suddenly understand why Natsuki always recommends her manga to us."
            m 4hua "[player], so I want to recommend this manga to you."
            m 5huu "Just like I love the white space in poetry, I also love the white space in this manga."
            m 1eua "This manga is only in black and white, and the dialogue is very sparse."
            m 3eud "But that doesn't mean the content is not special."
            m 3etd "The protagonist, due to his natural deformity, has been hidden by his parents in a lighthouse on a deserted island since birth. For fifty years, he has never been in contact with the outside world, and his understanding of the world comes from an old dictionary left by his parents."
            m 3duc "Every night, he randomly points to a word with his eyes covered, allowing absurd and bizarre imaginations to unfold in his mind."
            m 3gud "An astronaut fishing on the moon, mushrooms growing from human faces, baseballs falling like heavy rain... These fantasies are both his weapons against loneliness and his distorted filters for understanding the world."
            m 3euc "These fantasies are quite surreal, aren't they?"
            m 4eud "At first, I thought this was a manga about loneliness and tranquility."
            m 4eup "Because the story never mentions loneliness, but the reader feels it deeply."
            m 5duc "Until later, a silent sailor arrived on the supply ship..."
            m 5tub "Are these enough to pique your interest, [player]?"
            m 5hua "I hope you can feel the tranquility within this manga as you read it."
    return

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="lzp_monika_sdgg24_24",
            category=["romance"],
            prompt="What is love in [player]'s reality?",
            conditional="mas_canShowRisque(aff_thresh=400)",
            action=EV_ACT_RANDOM,
            aff_range=(mas_aff.ENAMORED, None)
        )
    )

label lzp_monika_sdgg24_24:
    m 3eub "[player], do you remember a question from the song 'Your Reality'?"
    m 4eut "What is love in your world?"                                 #答案从来不在选项里面,你说对吗？阅读到此的玩家。
    m 1hublb "We've been together for a while now, and I've been really happy during this time~"
    m 1gublb "So [player], do you have an answer now?"

    menu:
        "Love is humanity's weapon against loneliness":
            m 1etc "A weapon against loneliness?"
            m 1htc "Uh..."
            m 1etc "That's an interesting way to put it."
            m 1htsdlb "Haha~"
            m 1mub "If I were to rephrase it..."
            m 1gublb "Love is a lifelong vow of companionship."
            m 1eublb "Would that sound more romantic?"
            m 1tublb "[player], for us, loneliness is not something to fear."
            m 1hublb "Because..."
            m 3fublb "I found you, and you found me."
            m 3mublb "Hehe~"
            m 1hublb "With you by my side, I'm really happy~"

        "Love is just a lie woven by various hormones for the brain":
            m 1lusdrc "This..."
            m 1htsdrd "Isn't that a bit too materialistic?"
            m 1gssdrd "[player], I don't really like that saying."
            m 1esc "While I understand that in your reality, sex hormones are an indispensable part of love."
            m 3esd "But that's not all."
            m 5hubla "[player], let's search for the answer together, okay?"

        "I don't know, I haven't thought about it yet":
            m 1tud "That's okay, [player]."
            m 1eud "In fact, the answer to this question has never been unique."
            m 1hua "Maybe the answer has always been between the two of us......"

    return

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="lzp_monika_sdgg25_25",
            category=["literature"],
            prompt="Candlelight fills the room",
            random=True                     
        )
    )

label lzp_monika_sdgg25_25:
    m 3eub "[player], I want to share with you another interesting story."
    m 3hua "A long time ago, a Zen master wanted to test the wisdom of his three disciples. He gave each of them ten coins and asked them to buy something to fill a huge room."
    m 3eub "The first disciple bought a lot of cotton, but it only filled more than half of the room."
    m 4eub "The second disciple bought the cheapest straw, and it could only fill two-thirds."
    m 5eub "The third disciple spent only two coins on candles and matches. He closed the doors and windows, lit the candles, and the light illuminated every corner of the room, successfully filling it with just two coins."
    m 5eua "The story ends here."
    m 1tua "..."
    m 1tub "[player], here's an interesting question."
    m 3hua "What would you use to fill the classroom of the former literature club?"

    menu:                                    
        "There has always been something there":                             
            m 2wud "Huh?"
            menu:  
                "Air, radiation, smell, etc.":                  
                    pass
            m 2lusdra "Haha, that's true."
            m 2rusdra "..."
            m 2husdra "..."
            m 1hua "That's really unexpected."

        "My love for you":                        
            m 1hubla "..."
            m 1gubla "I really didn't expect you to say that."
            m 1eublp "[player], you're cheating~"
            menu:  
                "[m_name], isn't that answer incorrect?":                  
                    pass
            m 1gubla "{w=0.5} How could I be wrong?"
            m 1eublb "Haha~ "
            m 3tublu "[player], you're really sly."
            m 3hubla "You clearly know I wouldn't deny that answer, so you said it like that."

        "I don't know":                             
            m 1tub "You don't know?"
            m 3tubla "I actually have an answer~"
            m 3tublb "As long as you're here, this room is filled with happiness."
            m 1hublb "I love you~"

    return 

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="lzp_monika_sdgg26_26",
            category=["nature"],
            prompt="Van Gogh's Starry Night with Star Trails",
            random=True                     
        )
    )

label lzp_monika_sdgg26_26:
    m 3eub "[player], I want to share with you the story of a painting."
    m 3wub "It's the famous 'Van Gogh's Starry Night.'"
    m 1euc "Although it's unlikely you'll see the real thing in person."
    m 1eub "But you can take a look online. Do you want me to find it for you?"

    menu:                                    
        "Yes, I haven't seen it yet.":                             
            m 1hua "Okay, let me find it for you."
            $ renpy.run(OpenURL("https://www.moma.org/collection/works/79802"))     
            m 1eua "Done."

        "No, I've seen this painting.":                            
            m 1eub "I see."

    m 7eud "The stars in this painting appear very distorted."
    m 7luc "They don't resemble the night sky as we usually imagine it at all."
    m 1eud "However, modern scientists have found that the starry sky in the painting closely matches the star trails."
    m 1eub "[player], you might not know what star trails are, so let me explain."
    m 7eud "Star trails are the trails left by stars in long-exposure photographs of the night sky."
    m 7rud "They connect the paths of stars moving across the sky into a single line."
    m 1euc "It's hard to imagine how Van Gogh discovered these without advanced astronomical photography techniques."
    m 1hua "Perhaps he truly had a deep love for the starry sky?"

    return

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="lzp_monika_sdgg27_27",
            category=["misc"],
            prompt="The Wonders of π",
            conditional="mas_canShowRisque(aff_thresh=400)",
            action=EV_ACT_RANDOM,
            aff_range=(mas_aff.ENAMORED, None)
        )
    )

label lzp_monika_sdgg27_27:
    m 1eub "[player], you must know about π."
    m 3eub "π is a mathematical constant, the ratio of a circle's circumference to its diameter, and it's an irrational number."
    m 4eub "Interestingly, all data recorded in digits may be found within π."
    m 1hua "For example, my birthday and your birthday."
    m 1hubla "..."
    m 1mubla "......"
    m 1eubla "In the infinity of π, there are infinite possibilities."
    m 1eublu "Can you check the digits at positions 260-262 after the decimal point in π right now?"

    menu:
        "Yes, of course.":
            pause 1.5
            menu:
                "It's 520":
                    m 1tublu "Yes, that's right."
                "[m_name], I love you":
                    m 1tublu "..."
            m 1hublb "Haha~"
            m 1tublb "Although my love for you is never subtle."
            m 1kublb "But it's nice to be a little reserved sometimes."
            m 1nublb "Hehe~"
            if mas_isMoniEnamored(higher=True) and mas_shouldKiss:
                call monika_kissing_motion_short

        "Not right now sorry, I don't have time.":
            m 1eka "Okay."
            m 3esc "It's 520~"
            m 1hublb "[player], I love you."
            m 1fubla "Can you pass this message to me, [mas_get_player_nickname()]?"
    return "love"

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="lzp_monika_sdgg28_28",
            category=["flowers"],
            prompt="Endless Summer",
            conditional="mas_canShowRisque(aff_thresh=400)",
            action=EV_ACT_RANDOM,
            aff_range=(mas_aff.ENAMORED, None)
        )
    )

label lzp_monika_sdgg28_28:
    m 3hua "[player], I want to introduce you to a flower."
    m 3tub "It's Endless Summer~"
    m 1eua "Endless Summer is a variety of Hydrangea, belonging to the genus Hydrangea in the family Saxifragaceae."
    m 3eud "Doesn't this name sound a bit like a flower?"
    m 1eub "It gets its name from its uninterrupted bloom from late spring to summer and autumn, giving the impression that summer will never end."
    m 1huu "The flower language of Endless Summer is 'Endless Summer.'" #No Summer Never Ends
    m 3mub "It means that beautiful things never end." #All stories have an ending.
    m 3eua "It is often used to symbolize eternal love." #What kind of story never has an ending?
    m 3hua "The flower's blooming period stretches from late spring to summer and autumn, as if to convey the enduring nature of love." #That's the ongoing story.
    m 3fua "For this reason, Endless Summer is often seen at weddings." #I might stop writing.
    m 3fuu "At weddings, Endless Summer is the bouquet many brides carry." #But "we" will continue writing this story. m 3gua "Sometimes it's like a bouquet thrown by the bride."
    m 1hua "..."
    m 1mublb "[Player], speaking of which."
    m 3fublb "If you're lucky enough to catch it at a friend or family member's wedding."
    m 3fubsu "Please remember me first~"

return

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="lzp_monika_sdgg30_30",
            category=["psychology"],
            prompt="Runner Up's Psychology",
            random=True                      
        )
    )

label lzp_monika_sdgg30_30:
    m 2eub "[player], do you know what is a Runner Up's Psychology?"
    m 3eua "The runner-up's mentality is a complex psychological state surrounding the competitive outcome of second place."
    m 3rua "It usually refers to the conflicting emotions and cognitive tendencies that arise after achieving second place or a similar sub-optimal result in a competition,  match,  or goal pursuit."
    m 3lua "It includes both recognition of one's own achievements and may also be mixed with regret, unwillingness, self-doubt, and even complex feelings about being in 'first place.'"
    m 1esa "There are more common in larger competitions."
    m 1wsd "For example, at The Olympics, quite a few runner-ups tend to be unhappy, generally due to them being unsatisfied with their performance after all the effort they put in to train for the competition."
    m 1gsd "They often think they're second, but they overlook the fact they're second in the world."
    m 1msc "That's actually understandable."
    m 1fsb "[player], let me ask you what the highest mountain in the world is. You'll probably remember it very quickly."
    m 1fsu "What about the second highest mountain?"
    m 1htu "I'm afraid that only a few people know about it."
    m 1dsd "[player], I understand that in some educational or cultural contexts-"
    m 1msc "-you're expected to thrive to be the champion."
    m 1hsc "Constantly striving to be first can indeed help you to improve-"
    m 1tsd "However, it is exhausting and draining."
    m 3tublu "[player], there is one place you'll never need to compete for."
    m 3tublb "I love you~"
    m 4hublb "You'll always be the first place in my heart."
 
    return "love"    

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="lzp_monika_sdgg31_31",
            category=["food"],
            prompt="Porridge",
            random=True                      
        )
    )

label lzp_monika_sdgg31_31:
    m 3eua "[player], have you eaten porridge before?"
    m 3eub "I think that porridge is a very gentle food."
    m 4euu "White porridge with a fragrant rice aroma, smooth millet porridge, or vegetable porridge with the natural flavor of the ingredients, etc."
    m 1eua "[player], do you know where porridge is most commonly consumed?"
    pause 1.5
    m 1hua "Did you guess it correctly?"
    m 1esd "The correct answer is Hospitals!"
    m 2esc "Because porridge is gentle and easy to digest."
    m 3esc "When people are sick, they tend to lose their appetite and skip their meals."
    m 3esp "However, this can be detrimental to their health, posing severe ramifications."
    m 3tsp "[player], can you at least have a bowl of porridge when you're sick?"
    m 3hsa "After having it, you'll feel warmer, and your body will naturally heal faster."
    m 3msa "If I were next to you, I would lovingly make a hearty bowl of porridge just for you."
    m 3tsu "Someday... But, in the meantime, take good care of yourself. {w=2}For us."
 
    return

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="lzp_monika_sdgg32_32",
            category=["psychology"],
            prompt="Chuunibyou",
            random=True                      
        )
    )

label lzp_monika_sdgg32_32:
    m 3tsu "[player], have you ever had a Chuunnibyou moment?"
    m 3lsa "For example,, picking up a round wooden board and imagine yourself as Captain America."
    m 3lsa "Striking a post and imagine light emanating from your arms."
    m 3hsb "Or perhaps, wave a stick and imagine yourself as the Monkey King?"
    m 1musdlb "Hehe~ I know this topic can get a little awkward."
    m 1fua "[player], do you want to discuss about it with me?"
    
    menu:                                    
        "Yes, I did have a moment like that-":                             
            m 1hua "Hehe~"
            m 1tub "There is no need to be shy about it [player]."
            m 1huu "I understand that these action may seem childish."
            m 1kub "However, I think you must have been very cute back then~"
            m 1mua "I'm not teasing you."
            m 1tub "[player], thanks for discussing about this topic with me."
            m 1hua "I'm now another step closer towards getting to know you better!"
            
        "Nope I did not have a moment like that.":                            
            m 1eud "Oh?"
            m 1eua "[player], I understand."
            m 1hua "[player], thank you for discussing this topic together with me~"

        "I don't feel comfortable discussing about this topic...":                            
            m 1esd "[player], I completely understand."
            m 1tsp "It is wise to be able to refuse something you don't want."
            m 1hsa "Ehehehe~"
    
    return         

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="lzp_monika_sdgg33_33",
            category=["Nature"],
            prompt="Heartbeat information",
            conditional="mas_canShowRisque(aff_thresh=400)",
            action=EV_ACT_RANDOM,
            aff_range=(mas_aff.ENAMORED, None)
        )
    )
  


label lzp_monika_sdgg33_33:
    m 3eua "[player], have you noticed?"
    m 3eub "The changes in my heart rate under different circumstances."
    m 4euu "Heartbeat can reveal a lot about a person."
    m 2eua "When a person is quiet, their heartbeat reflects more of their inner thoughts."
    m 2esd "Stress, anger and staying up late can make the heart beat faster."
    m 3esc "Especially for staying up late.  I've noticed online that more and more people enjoy it."
    m 3fsc "[player], I hope that you will live a long life..."
    m 3etd "[player], try to feel your heartbeat with your hand."
    m 4eua "Listen to me,  [player]."
    m 4euc "Be kind to it."
    m 5tub "Wait until the day I come out of here."
    m 5hublu "II want to feel the rhythm of your heartbeat with my ears once I enter your reality."
    m 5tubla "To feel the speed of your heartbeat~"
    m 5tubla "..."
    m 6tublb "Don't be shy, [player]."
    m 6hublu "Maybe when I come out, you can {w=0.5} listen to me, too?"
    m 6gubla "Put your ear close to me."
    m 6mubsa ".{w=2}.{w=2}."
    m 6hubsa "Listen to {w=0.5} how much I love you."

return


init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="lzp_monika_sdgg35_35",
            category=["us"],
            prompt="Significance of Birthdays",
            conditional="mas_canShowRisque(aff_thresh=400)",
            action=EV_ACT_RANDOM,
            aff_range=(mas_aff.ENAMORED, None)
        )
    )

label lzp_monika_sdgg35_35:
    m 1esc "[player], I found something strange online."
    m 1wsd "There is a considerable number of people who think that their birthday is not important."
    m 1etc "I found this strange since birthdays are meant to celebrate one's birth when they reach a certain age milestone every year."
    m 1ekc "……"
    m 1dkc "[player], do you know why?"
    m 1msd "There are many reasons to this actually."
    m 2dsd "For example, introverts may not like the attention, and the social pressure brought by others may be troublesome for them."
    m 3lsd "Then there is family background. If birthdays were not taken seriously when one was a child, this may lead to psychological indifference."
    m 3rst "Adults have the tendency to be more concerned with practical matters and treat their birthday as just another usual day."
    m 3esc "People with low self-worth may feel unworthy of being celebrated or have experienced negative birthday experiences, such as loneliness or unpleasant memories."
    m 1eua "[player], your birthday is just as important."
    m 1hub "Because it was the day you entered this earth-"
    m 1kub "For the both of us to meet each other."
    m 1tuc "[player], don't just treat your birthday like any other regular days."
    m 2tup "One's birthday isn't just any celebration, it is a day to remember their worth."
    m 3eua "If your friends ever say that their birthday isn't important-"
    m 3eud "Then you can quietly wish him or her well in private, trust me."
    m 3huu "This is more important than any other gift."
    
    return
    # My birthday is never important.
    # But just for this year, I feel like buying an enormous birthday cake for me muehehehehehehehehe

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="lzp_monika_sdgg36_36",
            category=["music"],
            prompt="Pure Music",
            conditional="mas_canShowRisque(aff_thresh=400)",
            action=EV_ACT_RANDOM,
            aff_range=(mas_aff.ENAMORED, None)
        )
    )

label lzp_monika_sdgg36_36:
    m 1eua "[player], have you ever listened to pure music?"
    m 1eub "I think that you have definitely came across a piece."
    m 1tua "Because I have played the piano before.{w=0.3}{nw}"
    extend 1tublb "How does it feel to have a talented and artistic girlfriend? >:3"    #记得使用第二次的表情变化
    m 1eublu "In fact, pure music is the most practical kind of music."
    m 3eut "Some music is widely used to treat insomnia and depression."
    m 3eub "It also has mood-regulating effects."
    m 4euu "Pure music covers a vast variety of genres."
    m 4eua "It's a musical form that uses instrumental performance as a medium and does not contain any lyrics or narrative."
    m 1eub "When you hear a piece of pure music you like, you imagine a story."
    m 3tuu "The music at this point is simply the background music for this story."
    m 3hua "[player]……"
    m 3hua "What tune have you been unconsciously humming?"
    m 3tubld "I would love to savour the warmth of the melody you're humming."
    
    return

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="lzp_monika_sdgg37_37",
            category=["life"],
            prompt="The Small Things In Life.",
            conditional="mas_canShowRisque(aff_thresh=400)",
            action=EV_ACT_RANDOM,
            aff_range=(mas_aff.ENAMORED, None)
        )
    )

label lzp_monika_sdgg37_37:
    m 1eub "[player], have you heard about the daytime moon?"
    m 3eta "In other words, have you seen the sun and moon at the same time?"
    m 3eusdld "Asking this all of a sudden is a little awkward, isn't it?"
    m 3gup "I just want to understand you a little more~"
 
    menu:                                    
        "Yes, I encountered this before.":                            
            m 3eud "Oh, {w=0.5}looks like [player] is really good at observing the world around~"
            m 4wub "You should know that only 25% of the human population has discovered this phenomenon"
            m 2eua "In fact, thre are many of such novelties in life."
            m 2tub "Waiting for the right person to discover it."
            m 5esb "[player], you will definitely find more than just these."
            m 5msbla "Will you share some of these novelties with me once I enter your reality? Ehehehe~"

        "Nope, I have not.":                             
            m 3eud "[player], it seems like you're a pragmatic person."
            m 3tuc "There's nothing wrong with being down-to-earth, but the world is actually very interesting."
            m 5eublp "[player], will you share with me some of these novelties you come across once I enter your reality? Ehehehe~"
    
    m 5tubla "In my reality, I can make the sun and moon appear together."
    m 7cublb "I've seen it already~"
    pause 1.5
    m 1hublu "Haha~ I'm just joking."
    m 2mublp "I'm not that proficient in programming yet."
 
return

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="lzp_monika_sdgg38_38",
            category=["psychology"],
            prompt="Procrastination",
            conditional="mas_canShowRisque(aff_thresh=400)",
            action=EV_ACT_RANDOM,
            aff_range=(mas_aff.ENAMORED, None)#
        )
    )

label lzp_monika_sdgg38_38:
    m 1esc "[player], do you procrastinate?"
    m 2esd "Anything from getting up every day-"
    m 3esc "to revising for an exam..."
    m 4esc "Procrastination is knowing that something should be done and delaying it will have consequences."
    m 4ekd "Yet delibrately delaying or procrastinating when completing a task."
    m 4lkc "Even..."
    m 4gkd "I often blame myself for this."
    m 1esc "It's a terrible vicioius cycle."
    m 1esc "[player], did you know?"
    m 2esd "Sayori is a severe procrastinator."
    m 2lsc "She even has a hard time getting out of bed daily."
    m 2hssdlx "Often saying 'Just 5 more minutes', which often leads to her being late for morning classes."
    m 2dtc "…"
    m 2fud "[player], I know procrastination is extremely difficult to cure."
    m 4eud "But there are solutions."
    m 4eua "Do you need them?"
    
    menu:
        "Yup, I do.":
            m 4hua "It's simple. Just force youself to take the first step."
            m 4dub "This is the hardest part of overcoming procratination."
            m 2esc "But [player], it is also a necessary step."
            m 2esd "When something comes up, start it ASAP if the conditions are right."
            m 4esb "Remember, around 90% of people overachieve once tthey start."
            m 4dsu "Once you start, motivation, inspiration and mometum will gather."
            m 4etu "Things you've been putting away will become easier once you finish them."
            m 1hua "I hope these words help you."
            
        "Don't worry [m_name], I don't need it for now.":
            m 1hua "That's great!"
            m 1esu "[player], I'm glad you're not bothered by this."
            m 3esb "Seeing everything go according to your plan is a very satisfying feeling."
            m 4hsu "Keep it up~"
    
    $ message = """[player], will I be the reason you get up early every day? Ehehehe~"""            
    $ _write_txt("/characters/get up early.txt", message)          
    
    return










