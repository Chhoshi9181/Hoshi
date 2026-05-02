card = input().strip().upper()

# แยกแต้มกับดอก
rank = card[:-1]
suit = card[-1]

# แปลงแต้ม
if rank == 'A':
    rank_name = 'ace'
elif rank == 'J':
    rank_name = 'jack'
elif rank == 'Q':
    rank_name = 'queen'
elif rank == 'K':
    rank_name = 'king'
else:
    rank_name = rank

# แปลงดอก
if suit == 'D':
    suit_name = 'diamonds'
elif suit == 'H':
    suit_name = 'hearts'
elif suit == 'S':
    suit_name = 'spades'
elif suit == 'C':
    suit_name = 'clubs'

print(f"{rank_name} of {suit_name}")