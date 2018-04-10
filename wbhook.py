from DiscordWebHooks import Webhook
import sys, math
x = str(sys.argv[1])
y = str(sys.argv[2])
a = str(sys.argv[3])
url = str(sys.argv[4])
#url = 'https://discordapp.com/api/webhooks/428122624128843787/QLs82QdyH0h8WSBgOzD2ttdml226-VkDQ0zoGnuimjUlCaJ0iNUR57qDHCqjLZR-xxPf'
embed = Webhook(url, color=1234123)
embed.set_author(name=y,icon='https://i.imgur.com/rdm3W9t.png')
embed.add_field(name=x,value=a)
embed.set_footer(text='Time =>',ts=True)
embed.post()




