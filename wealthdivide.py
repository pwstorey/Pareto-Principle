
import streamlit as st 
import numpy as np
import matplotlib.pyplot as plt


st.title("Wealth Distribution")
st.header("The Pareto Principle")
st.write("""
- As applied to the distribution of wealth, the Pareto Principle proposes that the 80% of all wealth is owned by 20% of the population. 
- This can be illustrated by a simple coin toss experiment. 
- Imagine a trading game between 'n' players who all start the game with 10 coins. 
- Each player tosses a coin agaist a random opponent and the winner takes 1 coin from the loser. 
- When a player has no coins left, that player stops playing. 
         """)
"---"

# Set up the array of n players all starting with 10 coins. 
n = st.slider("Select number of players (n):", min_value=100, max_value=1000, value=100, step=100)  # Sets the number of players. 1000
coins = 10 # Sets the number coins each player starts with.   
players = coins * np.ones(n)

st.write("As you can see from the histogram below all players start with 10 coins each.") 

plt.title("Initial Distribution of Wealth")
plt.xlabel("Number of coins owned")
plt.ylabel("Number of players")
plt.hist(players,bins = np.linspace(0, 60, num=60))

st.pyplot(plt, clear_figure=True)
"---"

# Returns the winner of a coin toss between two players "x" and "y".
def coinToss(x,y):
    return x if np.random.binomial(1,0.5) else y


# We iterate through the players 0 to n and pick an opponent at random.  
def playRound(players):   
    for i, player in np.ndenumerate(players): 
        a = i[0]
        
        # A player that has zero coins is out the game so we skip that player.
        if players[a] != 0:
            
            # pick a random opponent
            b = np.random.randint(0,n)

            # Player cannot play against him/her self so pick another opponent. 
            # If that opponent has zero coins, pick another opponent. 
            while b == a or players[b] == 0:  
                b = np.random.randint(0,n)

            # Toss a coin to determine winner.
            winner = coinToss(a,b)  
            
            # Winner takes coin from loser. 
            if winner == a:
                players[a] += 1
                players[b] -= 1
            else:
                players[b] += 1
                players[a] -= 1
    return players

st.write("Now let's play the game and see how the distribution of wealth changes.")

rounds = st.slider("Select number of rounds to play:", min_value=10, max_value=1000, value=250, step=10) # start 300

for r in range(rounds):
    playRound(players)

plt.title("Distribution of Wealth after " + str(rounds) + " Rounds")
plt.xlabel("Number of coins owned")
plt.ylabel("Number of players")
plt.hist(players,bins = np.linspace(0, 60, num=60))
st.pyplot(plt, clear_figure=True)

"---"

st.write("Let's look at the cumulative distribution of wealth.")

dist = np.sort(players)[::-1]
cumsum = np.cumsum(dist)/float(n*coins)
pcent = round(np.count_nonzero(cumsum <= 0.8)/n*100)

plt.title("Cumulative Distribution")
plt.xlabel("Number of players")
plt.ylabel("% of coins owned")
plt.grid(True)
plt.plot(cumsum)
st.pyplot(plt, clear_figure=True)

"---"

st.write("""**The Result:**""")
st.write("The richest "+str(pcent)+"% of players own 80 % of all the coins.")

"---"

code = """

import streamlit as st 
import numpy as np
import matplotlib.pyplot as plt


st.title("Wealth Distribution")
st.header("The Pareto Principle")
st.write("
- As applied to the distribution of wealth, the Pareto Principle proposes that the 80% of all wealth is owned by 20% of the population. 
- This can be illustrated by a simple coin toss experiment. 
- Imagine a trading game between 'n' players who all start the game with 10 coins. 
- Each player tosses a coin agaist a random opponent and the winner takes 1 coin from the loser. 
- When a player has no coins left, that player stops playing. 
         ")
"---"

# Set up the array of n players all starting with 10 coins. 
n = st.slider("Select number of players (n):", min_value=100, max_value=1000, value=100, step=100)  # Sets the number of players. 1000
coins = 10 # Sets the number coins each player starts with.   
players = coins * np.ones(n)

st.write("As you can see from the histogram below all players start with 10 coins each.") 

plt.title("Initial Distribution of Wealth")
plt.xlabel("Number of coins owned")
plt.ylabel("Number of players")
plt.hist(players,bins = np.linspace(0, 60, num=60))

st.pyplot(plt, clear_figure=True)
"---"

# Returns the winner of a coin toss between two players "x" and "y".
def coinToss(x,y):
    return x if np.random.binomial(1,0.5) else y


# We iterate through the players 0 to n and pick an opponent at random.  
def playRound(players):   
    for i, player in np.ndenumerate(players): 
        a = i[0]
        
        # A player that has zero coins is out the game so we skip that player.
        if players[a] != 0:
            
            # pick a random opponent
            b = np.random.randint(0,n)

            # Player cannot play against him/her self so pick another opponent. 
            # If that opponent has zero coins, pick another opponent. 
            while b == a or players[b] == 0:  
                b = np.random.randint(0,n)

            # Toss a coin to determine winner.
            winner = coinToss(a,b)  
            
            # Winner takes coin from loser. 
            if winner == a:
                players[a] += 1
                players[b] -= 1
            else:
                players[b] += 1
                players[a] -= 1
    return players

st.write("Now let's play the game and see how the distribution of wealth changes.")

rounds = st.slider("Select number of rounds to play:", min_value=10, max_value=1000, value=250, step=10) # start 300

for r in range(rounds):
    playRound(players)

plt.title("Distribution of Wealth after " + str(rounds) + " Rounds")
plt.xlabel("Number of coins owned")
plt.ylabel("Number of players")
plt.hist(players,bins = np.linspace(0, 60, num=60))
st.pyplot(plt, clear_figure=True)

"---"

st.write("Let's look at the cumulative distribution of wealth.")

dist = np.sort(players)[::-1]
cumsum = np.cumsum(dist)/float(n*coins)
pcent = round(np.count_nonzero(cumsum <= 0.8)/n*100)

plt.title("Cumulative Distribution")
plt.xlabel("Number of players")
plt.ylabel("% of coins owned")
plt.grid(True)
plt.plot(cumsum)
st.pyplot(plt, clear_figure=True)

"---"

st.write("**The Result:**")
st.write("The richest "+str(pcent)+"% of players own 80 % of all the coins.")

"---"

"""

show_code = st.checkbox("Click here to see source code.")

if show_code: 
    st.code(code, language="python")