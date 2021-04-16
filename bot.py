import discord
import random
import requests
import json
import strings
import time
import os
from discord.ext.commands import has_permissions, MissingPermissions
from discord.ext import commands
from discord.utils import get


VERMELHO = 0xff0000

intents = discord.Intents(messages = True, guilds = True, reactions = True, members = True, presences = True)
client = commands.Bot(command_prefix = 'b!', intents = intents)



@client.event
async def on_ready():
	atividade = f"b!help"
	activity = discord.Activity(name=atividade, type=discord.ActivityType.watching)
	await client.change_presence(activity=activity)
	print('bot on')

@client.event
async def on_member_join(member):
    canal_entrou = client.get_channel(789255180616728656)
    await canal_entrou.send(f'<@{member.id}> entrou no servidor! Seja bem vindo(a)!')
    print(f'{member} entrou no server')


@client.event
async def on_member_remove(member):
    canal_saiu = client.get_channel(789255216277094412)
    await canal_saiu.send(f'<@{member.id}> saiu do servidor!')
    print(f'{member} saiu do server')


@client.event
async def on_message(message):

    global embed_help
    embed_help = discord.Embed(title = "Meus comandos:", color = VERMELHO)


    #embed_help.add_field(name="🐶 » Animais", value="☛ -𝘣𝘰𝘳𝘣𝘰𝘭𝘦𝘵ɑ, -𝘭𝘦α̃𝘰, -𝘨ɑ𝘵𝘰, -𝘤ɑ𝘤𝘩𝘰𝘳𝘳𝘰 𝘦 -𝘨ɑ𝘭𝘪𝘯𝘩ɑ", inline=False)
    embed_help.add_field(name="🔒 » Administração", value="☛ b!𝘣𝘢𝘯, b!𝘭𝘰𝘤𝘬, b!𝘶𝘯𝘭𝘰𝘤𝘬, b!𝘬𝘪𝘤𝘬, b!𝘶𝘯𝘣𝘢𝘯, b!𝘤𝘭𝘦𝘢𝘳, b!𝘤𝘭𝘦𝘢𝘳 e b!𝘶𝘯𝘮𝘶𝘵𝘦", inline=False)
    embed_help.add_field(name="💬 » Interação", value="☛ b!𝘴𝘭𝘢𝘱, b!𝘱𝘢𝘵, b!𝘱𝘶𝘯𝘤𝘩, b!𝘬𝘪𝘴𝘴, -𝘤𝘢𝘴𝘢𝘳, -𝘢𝘷𝘢𝘵𝘢𝘳, -𝘶𝘴𝘦𝘳𝘪𝘯𝘧𝘰 𝘦 -𝘥𝘪𝘷𝘰𝘳𝘤𝘪𝘰", inline=False)
    embed_help.add_field(name="❓» Informações", value="☛ -𝘴𝘦𝘳𝘷𝘦𝘳𝘪𝘯𝘧𝘰", inline=False)

    embed_interacao = discord.Embed(title = "interacao", color = VERMELHO, description = r"""
b!slap @
b!hug @
b!kiss @
b!punch @
b!pat @
""")

    embed_cotacao = discord.Embed(title = "[+]----------Moedas---------[+]", color = VERMELHO, description = r"""
b!dolar - preco dolar (R$)
b!euro - preco euro (R$)
b!bitcoin - preco bitcoin (R$)
b!litecoin - preco litecoin (R$)
b!iene - preco iene japones (R$)
b!etherium - preco etherium (R$)
b!yuan - preco yuan chines (R$)
""")

    embed_administracao = discord.Embed(title = "[+]----------Administração----------[+]", color = VERMELHO, description = r"""
b!ban @
b!unban ID
b!kick @
b!bannedmembers
b!clear <QUANTIDADE>
b!lock
b!unlock
""")

    if message.content.lower().startswith('b!help'):
        await message.channel.send(embed=embed_help)
    
    if message.content.lower().startswith('b!interacao'):
        await message.channel.send(embed=embed_interacao)
    
    if message.content.lower().startswith('b!cotacao'):
        await message.channel.send(embed=embed_cotacao)
    
    if message.content.lower().startswith('b!adm'):
        await message.channel.send(embed=embed_administracao)

    if message.content.lower().startswith("<@!791032012907347979>"):
        await message.channel.send(embed=embed_help)



    if message.content.lower().startswith('b!euro'):
        requisicao = requests.get('https://economia.awesomeapi.com.br/json/all/EUR')

        cotacao = json.loads(requisicao.text)
        msg0 = "Preco euro: R$" + cotacao['EUR'] ['bid']

        await message.channel.send(msg0)
        print(message.author,  " fez o comando $euro no canal:", message.channel, "no servidor:",  message.guild)

    if message.content.lower().startswith('b!dolar'):
        requisicao = requests.get('https://economia.awesomeapi.com.br/json/all/USD')

        cotacao = json.loads(requisicao.text)
        msg1 = "Preco dolar: R$" + cotacao['USD'] ['bid']

        await message.channel.send(msg1)
        print(message.author,  " fez o comando $dolar no canal:", message.channel, "no servidor:",  message.guild)

    if message.content.lower().startswith('b!bitcoin'):
        requisicao = requests.get('https://economia.awesomeapi.com.br/json/all/BTC')

        cotacao = json.loads(requisicao.text)
        msg2 = "Preco bitcoin: R$" + cotacao['BTC'] ['bid']

        await message.channel.send(msg2)
        print(message.author,  " fez o comando $bitcoin no canal:", message.channel, "no servidor:",  message.guild)

    if message.content.lower().startswith('b!litecoin'):
        requisicao = requests.get('https://economia.awesomeapi.com.br/json/all/LTC')

        cotacao = json.loads(requisicao.text)
        msg3 = "Preco litecoin: R$" + cotacao['LTC'] ['bid']

        await message.channel.send(msg3)
        print(message.author,  " fez o comando $litecoin no canal:", message.channel, "no servidor:",  message.guild)

    if message.content.lower().startswith('b!iene'):
        requisicao = requests.get('https://economia.awesomeapi.com.br/json/all/JPY')

        cotacao = json.loads(requisicao.text)
        msg4 = "Preco Iene japones: R$" + cotacao['JPY'] ['bid']

        await message.channel.send(msg4)
        print(message.author,  " fez o comando $iene no canal:", message.channel, "no servidor:",  message.guild)

    if message.content.lower().startswith('b!etherium'):
        requisicao = requests.get('https://economia.awesomeapi.com.br/json/all/ETH')

        cotacao = json.loads(requisicao.text)
        msg5 = "Preco etherium: R$" + cotacao['ETH'] ['bid']

        await message.channel.send(msg5)
        print(message.author,  " fez o comando $etherium no canal:", message.channel, "no servidor:",  message.guild)


    if message.content.lower().startswith('b!yuan'):
        requisicao = requests.get('https://economia.awesomeapi.com.br/json/all/CNY')

        cotacao = json.loads(requisicao.text)
        msg6 = "Preco Yuan chines: R$" + cotacao['CNY'] ['bid']

        await message.channel.send(msg6)
        print(message.author,  " fez o comando $yuan no canal:", message.channel, "no servidor:",  message.guild)



    if message.content.lower().startswith('b!ban'):
        if message.author.guild_permissions.ban_members:

            msg = message.content.replace('@', '')
            msg = msg.replace('>', '')
            msg = msg.replace('<', '')
            msg = msg.replace('!', '')

            if "&" in msg:
                msg = msg.replace('&', '')

            if "  " in msg:
                msg = msg.replace('  ', ' ')

            args = msg.split(' ')

            embed_ban = discord.Embed(title = "Banido(a)", color = VERMELHO, description = f"""
                                                                            Voce foi banido(a) do servidor {message.guild}.""")

            if len(args) == 2:
                #member: Member = discord.utils.find(lambda m: args[1] in m.name, message.guild.members)
                member = discord.utils.find(lambda m: args[1] in str(m.id), message.guild.members)

            else:
                await message.channel.send('Voce precisa especificar o membro que quer kickar. $ban <membro>')

                try:
                    if member:
                        user = client.get_user(member.id)
                        try:
                            await user.send(embed=embed_ban)
                        except Exception:
                            pass

                        await member.ban()
                        await message.channel.send(f'<@{member.id}> foi banido(a).')
                        print(message.author,  " fez o comando $ban no canal:", message.channel, "no servidor:",  message.guild, "e baniu", args[1])

                    else:
                        await message.channel.send(f'Hmm... nao consegui achar um membro com o id {args[1]}...')

                except Exception:
                    pass
        else:
            await message.channel.send(f'<@{member.id}> | Voce nao tem permissao para executar esse comando.')
    

    if message.content.lower().startswith('b!unban') and message.author.guild_permissions.ban_members:
        args = message.content.split(' ')

        if len(args) == 2:
            user = discord.utils.find(lambda m: args[1] in str(m.user.id), await message.guild.bans()).user

            if user:
                await message.guild.unban(user)
                await message.channel.send(f'<@{user.id}> foi desbanido(a).')
                print(message.author,  " fez o comando $unban no canal:", message.channel, "no servidor:",  message.guild, "e desbaniu", user.id)

            else:
                await message.channel.send(f'Nenhum membro banido com o id {args[1]} encontrado.')
    


    if message.content.lower().startswith('b!kick') and message.author.guild_permissions.kick_members:
        if message.author.guild_permissions.kick_members:

            msg = message.content.replace('@', '')
            msg = msg.replace('>', '')
            msg = msg.replace('<', '')
            msg = msg.replace('!', '')

            if "&" in msg:
                msg = msg.replace('&', '')

            elif "  " in msg: 
                msg = msg.replace('  ', ' ')

            args = msg.split(' ')

            embed_kick = discord.Embed(title = "Kickado(a)", color = VERMELHO, description = f"""
                                                                            Voce foi kickado(a) do servidor {message.guild}.""")

            if len(args) == 2:
                member = discord.utils.find(lambda m: args[1] in str(m.id), message.guild.members) #Kick por id
            
            else:
                await message.channel.send('Voce precisa especificar o membro que quer kickar. $kick <membro>')

            try:
                if member:
                        user = client.get_user(member.id)
                        try:
                            await user.send(embed=embed_kick)
                        except Exception:
                            pass

                        await member.kick()
                        await message.channel.send(f'<@{args[1]}> foi kickado(a).') #marca a pessoa
                        print(message.author,  " fez o comando $kick no canal:", message.channel, "no servidor:",  message.guild, "e kickou", args[1])

                else:
                    await message.channel.send(f'Hmm... Nao consegui encontrar o id {args[1]}...')

            except Exception:
                pass
        
        else:
            await message.channel.send(f'<@{member.id}> | Voce nao tem permissao para executar esse comando.')


    if message.content.lower().startswith('b!bannedmembers') and message.author.guild_permissions.ban_members:
        membros_banidos = await message.guild.bans()

        for membros in membros_banidos:
            print(membros)
            await message.channel.send(f' ```{membros}``` ')

        if not membros_banidos:
            await message.channel.send("Nao existem membros banidos nesse servidor!")


    if message.content.lower().startswith('b!mute'):
        #print(dir(message.author.guild_permissions))
        if message.author.guild_permissions.manage_roles:
            #print(dir(message.guild))
            #return
            msg = message.content.replace('@', '')
            msg = msg.replace('>', '')
            msg = msg.replace('<', '')
            msg = msg.replace('!', '')

            if "&" in msg:
                msg = msg.replace('&', '')

            elif "  " in msg: 
                msg = msg.replace('  ', ' ')

            args = msg.split(' ')

            if len(args) == 2:
                member = discord.utils.find(lambda m: args[1] in str(m.id), message.guild.members)

            else:
                await message.channel.send(f'<@{message.author.id}>, voce precisa mencionar alguem pra mutar!')
                return

            
            if member:
                try:
                    if get(message.guild.roles, name="muted"):
                        #await message.channel.send("Cargo mute ja existe")
                        role = discord.utils.get(message.guild.roles, name="muted")
                        perms = discord.Permissions(send_messages=False, read_messages=True)
                        await member.add_roles(role)
                        #await message.channel.set_permissions(message.guild.get_role('🚫Cute-mute🚫'), send_messages=False)
                        await message.channel.set_permissions(role, send_messages=False)
                        await message.channel.send(f'Ok, ok, <@{message.author.id}>, mutei o <@{args[1]}>. Tava badernando ai? ')

                    else:
                        guild = message.channel.guild
                        perms = discord.Permissions(send_messages=False, read_messages=True)
                        await guild.create_role(name="muted", permissions=perms)
                        role = discord.utils.get(message.guild.roles, name="muted")

                        await member.add_roles(role)
                        await message.channel.set_permissions(role, send_messages=False)
                        await message.channel.send(f'Ok, ok, <@{message.author.id}>, mutei o <@{args[1]}>. Tava badernando ai? ')

                except Exception:
                    await message.channel.send(f'Por algum motivo eu nao estou conseguindo mutar o(a) <@{member.id}>... Por acaso eu tenho permissao pra isso?')
                    pass
            else:
                await message.channel.send('Nao encontrei ninguem com esse nome aqui, sertifique-se que ele esta no servidor!')

        else:
            await message.channel.send(f'<@{message.author.id}>, voce nao tem permissao pra usar esse comando!')



    if message.content.lower().startswith('b!unmute'):
        if message.author.guild_permissions.manage_roles:
            #print(dir(message.guild))
            #return
            msg = message.content.replace('@', '')
            msg = msg.replace('>', '')
            msg = msg.replace('<', '')
            msg = msg.replace('!', '')

            if "&" in msg:
                msg = msg.replace('&', '')

            elif "  " in msg: 
                msg = msg.replace('  ', ' ')

            args = msg.split(' ')

            if len(args) == 2:
                member = discord.utils.find(lambda m: args[1] in str(m.id), message.guild.members)

            else:
                await message.channel.send(f'<@{message.author.id}>, voce precisa mencionar alguem pra desmutar!')
                return

            if member:
                try:
                    role = discord.utils.get(message.guild.roles, name="muted")
                    await member.remove_roles(role)
                    await message.channel.send(f'Pronto, <@{message.author.id}>! Desmutei o <@{member.id}>!')
                
                except Exception:
                    await message.channel.send(f'Por algum motivo eu nao estou conseguindo mutar o(a) <@{member.id}>... Por acaso eu tenho permissao pra isso?')
                    pass
            else:
                await message.channel.send('Nao encontrei ninguem com esse nome por aqui, sertifique-se que ele ainda esta no server.')
        else:
            await message.channel.send('Voce nao tem permissao pra usar esse comando!')


    if message.content.lower().startswith('b!lock'):
        if message.author.guild_permissions.manage_channels:
            overwrite = message.channel.overwrites_for(message.guild.default_role)
            overwrite.send_messages = False
            await message.channel.set_permissions(message.guild.default_role, overwrite=overwrite)
            await message.channel.send(f'Ok, <@{message.author.id}>. Lockei o canal. TInha muita gente fazendo baderna? 🧐')
            #print(dir(message.author.guild_permissions))
        else:
            await message.channel.send(f'<@{message.author.id}>, voce nao tem permissao pra usar esse comando!')
    
    
    if message.content.lower().startswith('b!unlock'):
        if message.author.guild_permissions.manage_channels:
            overwrite = message.channel.overwrites_for(message.guild.default_role)
            overwrite.send_messages = True
            await message.channel.set_permissions(message.guild.default_role, overwrite=overwrite)
            await message.channel.send(f'Ja deslockei o canal, <@{message.author.id}> 👌👌')
        else:
            await message.channel.send(f'<@{message.author.id}>, voce nao tem permissao pra usar esse comando!')


        if message.content.lower().startswith('b!slap'):

            msg = message.content.replace('@', '')
            msg = msg.replace('>', '')
            msg = msg.replace('<', '')
            msg = msg.replace('!', '')

            if "&" in msg:
                msg = msg.replace('&', '')

            args = msg.split(' ')

            global ale_slap
            ale_slap = random.randint(1, 6)

            #print(msg)
            #print(args)
            #print(message.content)

            if len(args) == 2:
                member = discord.utils.find(lambda m: args[1] in str(m.id), message.guild.members)#procura pelo membro

            
            if member:
                if member == message.author:
                    await message.channel.send("Voce nao pode se tapear!")
                    print(f'{message.author} tentou se tapear no canal {message.channel} no server {message.channel.guild}')
                    return
                await message.channel.send(f"<@{message.author.id}> deu um tapa em <@{member.id}>!")
                await message.channel.send(random.choice(strings.lista_slap))
                #await message.channel.send(file=discord.File(r'C:\Users\Leonardo\Desktop\bot animais\acoes\aslap\0' + str(ale_slap) + '.gif'))
                print(f'{message.author} deu um tapa em {member} no canal {message.channel} no server {message.channel.guild}')
                
                if args[1] == "766849836455821322" or member == r"botest#7787": #id botest
                    await message.channel.send("Nossa man")

            else:
                await message.channel.send(f'Hmmm... Nao conseguir encontrar ninguem com o id {args[1]}')



    if message.content.lower().startswith('b!hug'):

        msg = message.content.replace('@', '')
        msg = msg.replace('>', '')
        msg = msg.replace('<', '')
        msg = msg.replace('!', '')

        if "&" in msg:
            msg = msg.replace('&', '')

        args = msg.split(' ')

        #print(msg)
        #print(args)
        #print(message.content)

        if len(args) == 2:
            member = discord.utils.find(lambda m: args[1] in str(m.id), message.guild.members)#procura pelo membro

        
        if member:
            if member == message.author:
                await message.channel.send("Voce nao pode se abracar!")
                print(f'{message.author} tentou se abracar no canal {message.channel} no server {message.channel.guild}')
                return

            #ale_hug = random.randint(1, 7)
            await message.channel.send(f"<@{message.author.id}> abracou <@{member.id}>!")
            await message.channel.send(random.choice(strings.lista_hug))
            #await message.channel.send(file=discord.File(r'C:\Users\Leonardo\Desktop\bot animais\acoes\hug\0' + str(ale_hug) + '.gif'))
            print(f'{message.author} abracou {member} no canal {message.channel} no server {message.channel.guild}')

            if args[1] == "766849836455821322" or member == r"botest#7787": #id botest
                await message.add_reaction(r"😊")

        else:
            await message.channel.send(f'Hmmm... Nao conseguir encontrar ninguem com o id {args[1]}')


    if message.content.lower().startswith('b!pat'):

        msg = message.content.replace('@', '')
        msg = msg.replace('>', '')
        msg = msg.replace('<', '')
        msg = msg.replace('!', '')

        if "&" in msg:
            msg = msg.replace('&', '')

        args = msg.split(' ')

        #print(msg)
        #print(args)
        #print(message.content)

        if len(args) == 2:
            member = discord.utils.find(lambda m: args[1] in str(m.id), message.guild.members)#procura pelo membro

        
        if member:
            if member == message.author:
                await message.channel.send("Voce nao pode se fazer carinho!!")
                print(f'{message.author} tentou se fazer carinho no canal {message.channel} no server {message.channel.guild}')
                return

            #ale_pat = random.randint(1, 12)
            await message.channel.send(f"<@{message.author.id}> fez carinho em <@{member.id}>!")
            await message.channel.send(random.choice(strings.lista_pat))
            #await message.channel.send(file=discord.File(r'C:\Users\Leonardo\Desktop\bot animais\acoes\pat\0' + str(ale_pat) + '.gif'))
            print(f'{message.author} fez carinho em {member} no canal {message.channel} no server {message.channel.guild}')

            if args[1] == "766849836455821322" or member == r"botest#7787": #id botest
                await message.add_reaction(r"😊")

        else:
            await message.channel.send(f'Hmmm... Nao conseguir encontrar ninguem com o id {args[1]}')





    if message.content.lower().startswith('b!kiss'):

        msg = message.content.replace('@', '')
        msg = msg.replace('>', '')
        msg = msg.replace('<', '')
        msg = msg.replace('!', '')

        if "&" in msg:
            msg = msg.replace('&', '')

        args = msg.split(' ')

        #print(msg)
        #print(args)
        #print(message.content)

        if len(args) == 2:
            member = discord.utils.find(lambda m: args[1] in str(m.id), message.guild.members)#procura pelo membro

        
        if member:
            if member == message.author:
                await message.channel.send("Voce nao pode se beijar!")
                print(f'{message.author} tentou se beijar no canal {message.channel} no server {message.channel.guild}')
                return

            #ale_kiss = random.randint(1, 9)
            await message.channel.send(f"<@{message.author.id}> beijou <@{member.id}>!")
            await message.channel.send(random.choice(strings.lista_kiss))
            #await message.channel.send(file=discord.File(r'C:\Users\Leonardo\Desktop\bot animais\acoes\kiss\0' + str(ale_kiss) + '.gif'))
            print(f'{message.author} beijou {member} no canal {message.channel} no server {message.channel.guild}')

            if args[1] == "766849836455821322" or member == r"botest#7787": #id botest
                await message.add_reaction(r"😳")

        else:
            await message.channel.send(f'Hmmm... Nao conseguir encontrar ninguem com o id {args[1]}')


    if message.content.lower().startswith('b!punch'):

        msg = message.content.replace('@', '')
        msg = msg.replace('>', '')
        msg = msg.replace('<', '')
        msg = msg.replace('!', '')

        if "&" in msg:
            msg = msg.replace('&', '')

        args = msg.split(' ')


        #print(msg)
        #print(args)
        #print(message.content)

        if len(args) == 2:
            member = discord.utils.find(lambda m: args[1] in str(m.id), message.guild.members)#procura pelo membro

#        if  == r"botest#7787":
#            print('teste')
        
        if member:

            if member == message.author:
                await message.channel.send("Voce nao pode se bater!")
                print(f'{message.author} tentou se bater no canal {message.channel} no server {message.channel.guild}')
                return

            #ale_punch = random.randint(1, 7)
            await message.channel.send(f"<@{message.author.id}> bateu em <@{member.id}>!")
            await message.channel.send(random.choice(strings.lista_punch))
            #await message.channel.send(file=discord.File(r'C:\Users\Leonardo\Desktop\bot animais\acoes\punch\0' + str(ale_punch) + '.gif'))
            print(f'{message.author} bateu em {member} no canal {message.channel} no server {message.channel.guild}')


            if args[1] == "766849836455821322" or member == r"botest#7787": #id botest
                await message.channel.send(r"'-'")

        else:
            await message.channel.send(f'Hmmm... Nao conseguir encontrar ninguem com o id {args[1]}')
    

    if message.content.lower().startswith('b!clear'):
        if message.author.guild_permissions.manage_channels:
                
            msg = message.content.replace('  ', ' ')
                
            args = msg.split(' ')

            if len(args) == 2:

                quantidade = args[1]
                quantidade = int(quantidade)

                if quantidade > 100 or quantidade <= 1:
                    await message.channel.send('Eu so apago entre 2 e 100 mensagens!', delete_after = 5)

                else:
                    await message.channel.purge(limit=quantidade)
                    await message.channel.send(f'O chat foi limpo por <@{message.author.id}>!', delete_after = 5)

        else:
            await message.channel.send(f'<@{message.author.id}> voce nao tem permissao para usar esse comando!')


    if message.content.lower().startswith('b!userinfo'):

        msg = message.content.replace('@', '')
        msg = msg.replace('>', '')
        msg = msg.replace('<', '')
        msg = msg.replace('!', '')
        msg = msg.replace('  ', ' ')

        if "&" in msg:
            msg = msg.replace('&', '')

        elif "  " in msg:
            msg = msg.replace('  ', ' ')

        args = msg.split(' ')

        if len(args) == 2:
            member = discord.utils.find(lambda m: args[1] in str(m.id), message.guild.members)

            if member:
                embed_userinfo = discord.Embed(Title="Informacoes de usuario", color = VERMELHO)

                embed_userinfo.add_field(name="Usuario", value=member, inline=True)
                embed_userinfo.add_field(name="Id", value=member.id, inline=True)
                embed_userinfo.add_field(name="Status", value=f"{member.activity}", inline=True)
                embed_userinfo.add_field(name="Entrou no servidor em", value=member.joined_at.strftime("%b %d, %Y"), inline=True)
                embed_userinfo.add_field(name="Conta criada em", value=member.created_at.strftime("%b %d, %Y"), inline=True)
                embed_userinfo.set_image(url=member.avatar_url)

                await message.channel.send(embed=embed_userinfo)
            else:
                await message.channel.send('Hmmm... Nao consegui encontrar esse membro do servidor...')

        else:
            await message.channel.send("Voce precisa marcar alguem para ver as informacoes dela.")


    if message.content.lower().startswith('b!serverinfo'):

        membros = message.channel.guild.members
        membros = len(membros)

        regiao = message.channel.guild.region

        embed_serverinfo = discord.Embed(title=f"Informacoes do servidor {message.channel.guild.name}", color = VERMELHO)

        embed_serverinfo.add_field(name='Dono', value=f"{message.channel.guild.owner}", inline=True)
        embed_serverinfo.add_field(name='Id do dono', value=f"{message.channel.guild.owner.id}", inline=True)
        embed_serverinfo.add_field(name='Regiao do servidor', value=f"{regiao}", inline=True)
        embed_serverinfo.add_field(name='Membros', value=f"{membros}", inline=True)
        embed_serverinfo.add_field(name="Servidor criado em", value=f"{message.channel.guild.created_at.strftime('%b %d, %Y')}", inline=True)
        embed_serverinfo.add_field(name='Id do servidor', value=f"{message.channel.guild.id}", inline=True)
        #embed_serverinfo.set_image(url=message.channel.guild.banner_url)
        embed_serverinfo.set_image(url=message.channel.guild.icon_url)
        
        await message.channel.send(embed=embed_serverinfo)




client.run('NzkxMDMyMDEyOTA3MzQ3OTc5.X-JP-A.GELb2jtEb0-XbBmC7VpT593Zco0')