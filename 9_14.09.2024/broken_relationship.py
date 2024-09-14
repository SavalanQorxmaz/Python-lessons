import pgui as pg
# import OpenAI
# import beautifulsoup4 # web parsing

broken_relationship_messages = [
    "It's hard to accept that we're no longer together, but I wish you the best.",
    "Saying goodbye is never easy, but sometimes it’s the best thing for both of us.",
    "I’ll always cherish the memories we shared, even though we've gone our separate ways.",
    "<3"
]

x, y = (1100, 1050)
pg.moveTo(x, y)
pg.leftClick()

for message in broken_relationship_messages:
    pg.typewrite(message, interval=0.01)
    pg.press("enter")