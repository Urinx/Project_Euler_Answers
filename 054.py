#!/usr/bin/env python
#coding:utf-8

"""

Poker hands

In the card game poker, a hand consists of five cards and are ranked, from lowest to highest, in the following way:

High Card: Highest value card.
One Pair: Two cards of the same value.
Two Pairs: Two different pairs.
Three of a Kind: Three cards of the same value.
Straight: All cards are consecutive values.
Flush: All cards of the same suit.
Full House: Three of a kind and a pair.
Four of a Kind: Four cards of the same value.
Straight Flush: All cards are consecutive values of same suit.
Royal Flush: Ten, Jack, Queen, King, Ace, in same suit.

The cards are valued in the order:
2, 3, 4, 5, 6, 7, 8, 9, 10, Jack, Queen, King, Ace.
If two players have the same ranked hands then the rank made up of the highest value wins; for example, a pair of eights beats a pair of fives (see example 1 below). But if two ranks tie, for example, both players have a pair of queens, then highest cards in each hand are compared (see example 4 below); if the highest cards tie then the next highest cards are compared, and so on.

Consider the following five hands dealt to two players:

Hand        Player 1        Player 2        Winner
1       5H 5C 6S 7S KD    2C 3S 8S 8D TD    Player 2
        Pair of Fives     Pair of Eights

2       5D 8C 9S JS AC    2C 5C 7D 8S QH    Player 1
       Highest card Ace   Highest card Queen

3       2D 9C AS AH AC    3D 6D 7D TD QD    Player 2
        Three Aces        Flush with Diamonds

4       4D 6S 9H QH QC    3D 6D 7H QD QS    Player 1
        Pair of Queens    Pair of Queens
        Highest card Nine Highest card Seven

5       2H 2D 4C 4D 4S    3C 3D 3S 9S 9D    Player 1
        Full House        Full House
        With Three Fours  with Three Threes

The file, poker.txt, contains one-thousand random hands dealt to two players. Each line of the file contains ten cards (separated by a single space): the first five are Player 1's cards and the last five are Player 2's cards. You can assume that all hands are valid (no invalid characters or repeated cards), each player's hand is in no specific order, and in each hand there is a clear winner.
How many hands does Player 1 win?

"""
S=['2','3','4','5','6','7','8','9','T','J','Q','K','A']

def win(hand):
    hand=hand.split(' ')
    card1,card2=rank(hand[:5]),rank(hand[5:])
    if compare(card1,card2): return True
    return False

def rank(card):
    card=bubble_sort(card)
    a=[i[0] for i in card]
    b=[i[1] for i in card]
    # Royal Flush
    if len(set(b))==1 and a==S[-5:]: r,c=10,a[-1]
    # Straight Flush
    elif len(set(b))==1 and is_consecutive(a): r,c=9,a[-1]
    # Four of a Kind
    elif most(a)[0]==4: r,c=8,most(a)[1]
    # Full House
    elif most(a)[0]==3 and len(set(a))==2: r,c=7,most(a)[1]
    # Flush
    elif len(set(b))==1: r,c=6,a[-1]
    # Straight
    elif is_consecutive(a): r,c=5,a[-1]
    # Three of a Kind
    elif most(a)[0]==3: r,c=4,most(a)[1]
    # Two Pairs
    elif most(a)[0]==2 and len(set(a))==3: r,c=3,most(a)[1]
    # One Pair
    elif most(a)[0]==2: r,c=2,most(a)[1]
    # High Card
    else: r,c=1,a[-1]
    return {'rank':r,'card':c}

def is_consecutive(arr):
    for i in xrange(len(S)-5):
        if arr==S[i:i+5]: return True
    return False

def bubble_sort(arr):
    tmp={}
    for i in xrange(len(arr)):
        tmp[arr[i]]=S.index(arr[i][0])
    return [i[0] for i in sorted(tmp.items(),lambda x,y:cmp(x[1],y[1]))]

def most(arr):
    return max(map(lambda x:(arr.count(x),x),arr))

def compare(card1,card2):
    if card1['rank']>card2['rank']: return True
    if card1['rank']==card2['rank'] and S.index(card1['card'])>S.index(card2['card']): return True
    return False

def answer():
    with open('poker.txt','r') as f:
        poker=f.read().split('\n')
        poker.pop()
    
        total=0
        for i in poker:
            if win(i): total+=1
        print total

import time
tStart=time.time()
answer()
print 'run time=',time.time()-tStart
# 376
# run time= 0.0720129013062