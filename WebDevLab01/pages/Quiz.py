import streamlit as st


# RESTART FUNCTION
# Sets every question back to its starting answer.
def restart():
    st.session_state["activities"] = []
    st.session_state["friends"] = "The motivated one💪"
    st.session_state["bedtime"] = 8
    st.session_state["flavors"] = []
    st.session_state["weather"] = None

        
st.write('''
     # What Drink best describes U????
     ***Take this quiz to find out!!!!***
     ''')

st.image("Images/FINALDRINKS_transparent.png", width="stretch")

# initial scores for all drinks, highest score & 2nd highest score
coffeeS=0
teaS=0
lemonadeS=0
hotcocoaS=0
bobaS=0
sodaS=0
smoothieS=0
matchaS=0
highestScore=0
secondHScore=0



# NEW
# /////////QUESTION #1 MULTISELECT
# adds divider on the page in between things
st.divider()
st.header(":red[Question #1:]")

st.subheader("Pick The Perfect Activities For Your Perfect Day Below")
perfectActivity = st.multiselect(
    "Select the best activities for what the perfect day sounds like to you",
    ["Morning Workout", "Café with a good book", "Smores at a Campfire",
     "Trying out a new restaurant", "Crossing everything off a to-do list", "Beach Day",
     "Riding the scariest rides at Six Flags",
     "Doomscrolling on socials as much as your heart desires"], key = "activities" # saves this answer in st.session_state so restart() can clear it   
)

st.write("You selected:", perfectActivity)

if "Morning Workout" in perfectActivity:
    st.image("Images/m_w.jpg", width=200)

if "Café with a good book" in perfectActivity:
    st.image("Images/book_cafe.jpg", width=200)

if "Smores at a Campfire" in perfectActivity:
    st.image("Images/campfire.jpg", width=200)
    
if "Trying out a new restaurant" in perfectActivity:
    st.image("Images/new_rest.jpg", width=200)

if "Crossing everything off a to-do list" in perfectActivity:
    st.image("Images/todolist.jpg", width=200)

if "Beach Day" in perfectActivity:
    st.image("Images/beach_image.jpg", width=200)

if "Riding the scariest rides at Six Flags" in perfectActivity:
    st.image("Images/sixflags.jpg", width=200)

if "Doomscrolling on socials as much as your heart desires" in perfectActivity:
    st.image("Images/doomscroll.jpg", width=200)

#Scores for multiselect
if perfectActivity == "Morning Workout":
    smoothieS += 1
if perfectActivity == "Café with a good book":
    teaS += 1
if perfectActivity == "Smores at a Campfire":
    hotcocoaS += 1
if perfectActivity == "Trying out a new restaurant":
    bobaS += 1
if perfectActivity == "Crossing everything off a to-do list":
    coffeeS += 1
if perfectActivity == "Beach Day":
    lemonadeS += 1
if perfectActivity == "Riding the scariest rides at Six Flags":
    sodaS += 1
if perfectActivity == "Doomscrolling on socials as much as your heart desires":
    matchaS += 1





# NEW
# /////////QUESTION #2 MULTICHOICE
st.divider()
st.header(":red[Question #2:]")
st.subheader("Your friends would describe you as...")
multichoice = st.radio(
     "Your friends would describe you as...",
    ["The motivated one💪", "The wise one🤓", "The funny one🤣🤣🤣","The sweet one😛🍨👌","The trendsetter😉📈",
     "The wild card🤪🤪🤪","The healthy one☺👏🥦🍎", "The asethetic one💅💅💅" ],
    captions=[
        "Always chasing the next goal.",
        "Gives the best advice.",
        "Keeps everyone laughing.",
        "Kind to everyone.",
        "Knew about it before it was cool.",
        "Never know what's next.",
        "Gym, greens, good vibes.",
        "Everything matches.",
    ], key = "friends" # saves this answer in st.session_state so restart() can clear it
)



# Shows what choice was selected and updates the score
if multichoice == "The motivated one💪":
   st.write("You selected The motivated one💪")
   coffeeS += 3
elif multichoice == "The wise one🤓":
   st.write("You selected The wise one🤓")
   teaS += 3
elif multichoice == "The funny one🤣🤣🤣":
   st.write("You selected The funny one🤣🤣🤣")
   lemonadeS += 3
elif multichoice == "The sweet one😛🍨👌":
   st.write("You selected The sweet one😛🍨👌")
   hotcocoaS += 3
elif multichoice == "The trendsetter😉📈":
   st.write("You selected The trendsetter😉📈")
   bobaS += 3
elif multichoice == "The wild card🤪🤪🤪":
   st.write("You selected The wild card🤪🤪🤪")
   sodaS += 3
elif multichoice == "The healthy one☺👏🥦🍎":
   st.write("You selected The healthy one☺👏🥦🍎")
   smoothieS += 3 
else:
   st.write("You selected The asethetic one💅💅💅") 
   matchaS += 3



# NEW
# /////////QUESTION #3 BEDTIME SLIDER
st.divider()
st.header(":red[Question #3:]")
st.subheader("What time do you go to bed?")
bedtime = st.slider(
    "What time do you go to bed?", 1,12,8, key = "bedtime" # saves this answer in st.session_state so restart() can clear it
)

# makes the description in the caption change from am vs pm 
if bedtime in range(1,6) or bedtime == 12:
    st.write("I sleep at", bedtime, "am!")

else:
  st.write("I sleep at", bedtime, "pm!")

# updates scores based on bedtime
if bedtime in range(8,11):
    teaS += 2
    smoothieS += 2
    hotcocoaS += 2
    matchaS += 2
elif bedtime in range(11, 13):
    lemonadeS += 2
    bobaS += 2
else:
    coffeeS += 2
    sodaS += 2


# NEW
# /////////QUESTION #4 MULTISELECT
# adds divider on the page in between things
st.divider()
st.header(":red[Question #4:]")

st.subheader("Pick Your Favorite Flavors Below")
flavors = st.multiselect(
    "Select your favorite flavors from the options below",
    ["Vanilla", "Caramel", "Strawberry🍓",
     "Mango🥭", "Peach🍑", "Raspberry",
     "Chocolate🍫", "Coconut🥥🌴","Lemon🍋","Brown Sugar🧁🤎","Mint/Peppermint","Blueberry🫐",
     "Cherry🍒", "Pineapple🍍"], key = "flavors"    
)

st.write("You selected:", flavors)

#Scores for multiselect for the flavors
if "Vanilla" in flavors:
    smoothieS += 1
    coffeeS += 1
    hotcocoaS += 1
    matchaS += 1
    
if "Caramel" in flavors:
    coffeeS += 1
    hotcocoaS += 1
    bobaS += 1
    sodaS += 1
    
if "Strawberry" in flavors:
    lemonadeS += 1
    bobaS += 1
    smoothieS += 1
    matchaS += 1
    
if "Mango" in flavors:
    teaS += 1
    lemonadeS += 1
    bobaS += 1
    smoothieS += 1
    matchaS += 1
    
if "Peach" in flavors:
    teaS += 1
    lemonadeS += 1
    smoothieS += 1
    
if "Raspberry" in flavors:
    teaS += 1
    lemonadeS += 1
    sodaS += 1
    bobaS += 1
if "Chocolate" in flavors:
    smoothieS += 1
    coffeeS += 1
    hotcocoaS += 1
    
if "Coconut" in flavors:
    matchaS += 1
    bobaS += 1
    smoothieS += 1
if "Lemon" in flavors:
    teaS += 1
    lemonadeS += 1
    sodaS += 1
    
if "Brown Sugar" in flavors:
    matchaS += 1
    coffeeS += 1
    hotcocoaS += 1
    bobaS += 1
if "Mint/Peppermint" in flavors:
    teaS += 1
    hotcocoaS += 1
    lemonadeS += 1
if "Blueberry" in flavors:
    teaS += 1
    smoothieS += 1
    lemonadeS += 1
    
if "Cherry" in flavors:
    teaS += 1
    smoothieS += 1
    lemonadeS += 1
    
if "Pineapple" in flavors:
    teaS += 1
    smoothieS += 1
    lemonadeS += 1




# NEW
# /////////QUESTION #5 SELECTBOX
# adds divider on the page in between things
st.divider()
st.header(":red[Question #5:]")

st.subheader("Pick Your Favorite Type of Weather")
idealWeather = st.selectbox(
    "What is your favorite type of weather?",
    ["Hot & Sunny☀", "Rainy🌧", "Cold❄","Warm & Breezy🌤","Cloudy☁",
     "Stormy⛈","Cool/Fall Weather🍂","Tropical/Hot🌴"],
    index=None,
    placeholder="Select what weather you prefer", key="weather" # saves this answer in st.session_state so restart() can clear it
)

if idealWeather is not None :
    st.write("You selected:", idealWeather)
# GIF for the resulting weather the user picks!!!
if idealWeather == "Hot & Sunny☀":
    st.image("Images/H&S.gif")
    lemonadeS += 3
    bobaS += 3
    sodaS += 3
    smoothieS += 3
    teaS += 3
    
if idealWeather == "Rainy🌧":
    st.image("Images/Rainy.gif")
    st.audio("Images/rainSound.mp3", end_time= 5, loop=False, autoplay=True)
    teaS += 3
    hotcocoaS += 3
    coffeeS += 3
    bobaS += 3
    
if idealWeather == "Cold❄":
    st.image("Images/Cold.gif")
    matchaS += 3
    teaS += 3
    hotcocoaS += 3
    coffeeS += 3
    
if idealWeather == "Warm & Breezy🌤":
    st.image("Images/W&B.gif")
    st.audio("Images/wind.mp3", end_time= 5, loop=False, autoplay=True)
    smoothieS += 3
    teaS += 3
    lemonadeS += 3
    matchaS += 3
    
if idealWeather == "Cloudy☁":
    st.image("Images/Cloudy.gif")
    coffeeS += 3
    teaS += 3
    hotcocoaS += 3
    matchaS += 3
    
if idealWeather == "Stormy⛈":
    st.image("Images/Stormy.gif")
    st.audio("Images/StormySound.mp3", end_time= 5, loop=False, autoplay=True)
    teaS += 3
    hotcocoaS += 3
    coffeeS += 3
    
if idealWeather == "Cool/Fall Weather🍂":
    st.image("Images/C&FW.gif")
    hotcocoaS += 3
    coffeeS += 3
    matchaS += 3
    teaS += 3
    
if idealWeather == "Tropical/Hot🌴":
    st.image("Images/T&H.gif")
    st.audio("Images/hotBeachSound.mp3", end_time= 5, loop=False, autoplay=True)      
    smoothieS += 3
    lemonadeS += 3
    bobaS += 3
    sodaS += 3




# SCOREEEEEEEEEEESSSSSSSSSSSSSSSSSSS
    
# /////////DETERMINES SECOND PLACE AND HIGHEST SCORE



# ///////Calculates which drink has the HIGHEST SCORE

highScoreList = []
highScoreList= [sodaS, matchaS, teaS, lemonadeS, hotcocoaS, bobaS, coffeeS, smoothieS]
for drinkscore in highScoreList:
    if drinkscore>highestScore:
        highestScore= drinkscore
secondScoreList = highScoreList[:]
secondScoreList.remove(highestScore)


# /////////Calculates the drink with the 2ND BEST SCORE
for dscore in secondScoreList:
    if dscore > secondHScore:
        secondHScore= dscore


# if drink is hot chocolate display snow -> st.snow()
# if drink isnt hot chocolate then -> st.balloons()
st.divider()
st.header("Click the result button below to reveal what drink you are!!!")
st.subheader(":red[MAKE SURE YOU HAVE ANSWERED ALL 3 QUESTIONS]")
mysSButton = st.button("IN SECOND PLACE!!!")
st.write(mysSButton)


# /////////WHEN YOU PRESS ON THE RESULT BUTTON THE SECOND HIGHEST SCORE POPS UP   
if mysSButton == True:
# NEW
    st.audio("Images/drumRollVictory.mp3", start_time=4, loop=False, autoplay=True)
    if secondHScore == sodaS:
        st.balloons()
        st.image("Images/sodavid.gif")
        st.subheader("YAY I GOT MY :rainbow[SODAAAAA]")
        st.subheader("You are:")
        st.write("- bubbly")
        st.write("- spontaneous")
        st.write("- the life of the party") 
    elif secondHScore == matchaS:
        st.balloons()
        st.image("Images/matchavid.gif")
        st.subheader("STAY CALM & DRINK :rainbow[MATCHA]")
        st.subheader("You are:")
        st.write("- health-conscious")
        st.write("- adventurous")
        st.write("- balanced")
        st.write("- mindful")
        st.write("- trendy")
    elif secondHScore == teaS:
        st.balloons()
        st.image("Images/teavid.gif")
        st.subheader("SPILL THE :rainbow[TEAAAAA]")
        st.subheader("You are:")
        st.write("- calm")
        st.write("- thoughtful")
        st.write("- a good listener")
    elif secondHScore == lemonadeS:
        st.balloons()
        st.image("Images/lemonadevid.gif")
        st.subheader("WHEN LIFE GIVES U LEMONS DRINK :rainbow[LEMONADEEEE]")
        st.subheader("You are:")
        st.write("- sunny")
        st.write("- upbeat")
        st.write("- the friend who makes everyone laugh")
    elif secondHScore == hotcocoaS:
        st.snow()
        st.image("Images/hotcocoavid.gif")
        st.subheader("SIP SLOWLY & STAY COZY WITH :rainbow[HOT COCOA]")
        st.subheader("You are:")
        st.write("- cozy")
        st.write("- sweet")
        st.write("- a homebody at heart")
    elif secondHScore == bobaS:
        st.balloons()
        st.image("Images/bobavid.gif")
        st.subheader(":rainbow[BOBA] 1ST EVERYTHING ELSE LATER")
        st.subheader("You are:")
        st.write("- trendy")
        st.write("- playful")
        st.write("- always up for something new")
    elif secondHScore == coffeeS:
        st.balloons()
        st.image("Images/coffeevid.gif")
        st.subheader("BUT 1ST.... :rainbow[COFFEEEEEEE]")
        st.subheader("You are:")
        st.write("- driven")
        st.write("- busy")
        st.write("- always on the go")
    elif secondHScore == smoothieS:
        st.balloons()
        st.image("Images/smoothievid.gif")
        st.subheader(":rainbow[SMOOTHIES] 4 LIFEEEE")
        st.subheader("You are:")
        st.write("- health-conscious")
        st.write("- balanced")
        st.write("- into self-care")
#st.audio("Images/drumRollVictory.mp3", end_time=4, loop=True, autoplay=True)



# ///////FIRST PLACE BUTTON
myHSButton = st.button("IN FIRST PLACE!!!")
st.write(myHSButton)

# /////////WHEN YOU PRESS ON THE RESULT BUTTON THE HIGHEST SCORE POPS UP
if myHSButton == True:
# NEW
    st.audio("Images/2ndPlaceVictory.mp3", loop=False, autoplay=True)
    if highestScore == sodaS:
        st.balloons()
        st.image("Images/sodavid.gif")
        st.subheader("YAY I GOT MY :rainbow[SODAAAAA]")
        st.subheader("You are:")
        st.write("- bubbly")
        st.write("- spontaneous")
        st.write("- the life of the party") 
    elif highestScore == matchaS:
        st.balloons()
        st.image("Images/matchavid.gif")
        st.subheader("STAY CALM & DRINK :rainbow[MATCHA]")
        st.subheader("You are:")
        st.write("- health-conscious")
        st.write("- adventurous")
        st.write("- balanced")
        st.write("- mindful")
        st.write("- trendy")
    elif highestScore == teaS:
        st.balloons()
        st.image("Images/teavid.gif")
        st.subheader("SPILL THE :rainbow[TEAAAAA]")
        st.subheader("You are:")
        st.write("- calm")
        st.write("- thoughtful")
        st.write("- a good listener")
    elif highestScore == lemonadeS:
        st.balloons()
        st.image("Images/lemonadevid.gif")
        st.subheader("WHEN LIFE GIVES U LEMONS DRINK :rainbow[LEMONADEEEE]")
        st.subheader("You are:")
        st.write("- sunny")
        st.write("- upbeat")
        st.write("- the friend who makes everyone laugh")
    elif highestScore == hotcocoaS:
        st.snow()
        st.image("Images/hotcocoavid.gif")
        st.subheader("SIP SLOWLY & STAY COZY WITH :rainbow[HOT COCOA]")
        st.subheader("You are:")
        st.write("- cozy")
        st.write("- sweet")
        st.write("- a homebody at heart")
    elif highestScore == bobaS:
        st.balloons()
        st.image("Images/bobavid.gif")
        st.subheader(":rainbow[BOBA] 1ST EVERYTHING ELSE LATER")
        st.subheader("You are:")
        st.write("- trendy")
        st.write("- playful")
        st.write("- always up for something new")
    elif highestScore == coffeeS:
        st.balloons()
        st.image("Images/coffeevid.gif")
        st.subheader("BUT 1ST.... :rainbow[COFFEEEEEEE]")
        st.subheader("You are:")
        st.write("- driven")
        st.write("- busy")
        st.write("- always on the go")
    elif highestScore == smoothieS:
        st.balloons()
        st.image("Images/smoothievid.gif")
        st.subheader(":rainbow[SMOOTHIES] 4 LIFEEEE")
        st.subheader("You are:")
        st.write("- health-conscious")
        st.write("- balanced")
        st.write("- into self-care")


# RESTART BUTTON
# on_click runs restart() BEFORE the page reruns,
# so every question goes back to its default answer.
# Scores reset on their own because they're set to 0 at the top of the file.
# RESTART BUTTON
# on_click runs restart() first, then the whole page reruns with fresh answers.
st.divider()
st.button("Restart Quiz 🔄", on_click=restart)

