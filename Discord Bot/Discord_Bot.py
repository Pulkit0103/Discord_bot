import discord
import random

TOKEN = 'OTczMjY2OTg3NTkxNTQ0ODQ0.YnlHhA.CSD7GMKRy_6YhXRKRvMr3_9M6u4'

client = discord.Client()

@client.event
async def on_ready():   # Printing message on opening
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    username = str(message.author).split('#')[0]
    user_message = str(message.content)
    channel = str(message.channel.name)
    print(f'{username}: {user_message} ({channel})')

    if message.author == client.user:    # If the message is sent by the bot itself then no respond to user
        return

    if message.channel.name == 'ai_bot':
        if user_message.lower() == 'hello':
            await message.channel.send(f'Hello {username}!')
            return
        elif user_message.lower() == 'bye':
            await message.channel.send(f'See you Later {username}!')
            return
        elif user_message.lower() == '!random':
            response = f'This is your random number: {random.randrange(10000000)}'
            await message.channel.send(response)
            return

        if user_message.lower() == '!anywhere':
            await message.channel.send(f'This can be used anywhere')
            return


client.run(TOKEN)