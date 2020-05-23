import random
from discord.ext import commands
import discord

DEBUG_MODE = False
randomMessagesOriginal = [
    "大吉  すべてがうまくいき、やがてガチプロになる。ただしcoinsに来た時点で恋は諦めるべき。",
    "吉  頑張ると報われ、いろいろなことがいうまくいくらしい。ただしcoinsに来た時点で恋は諦めるべき。",
    "中吉  頑張ると割と報われるらしい。ただしcoinsに来た時点で恋は諦めるべき。",
    "小吉  すこしいいことがあるらしい。ただしcoinsに来た時点で恋は諦めるべき。",
    "末吉  頑張るといつか報われるかもしれない。ただしcoinsに来た時点で恋は諦めるべき。",
    "凶  落単する。頑張れば回避できるらしい。",
    "大凶  除籍される。coinsではなくなるので恋愛ができる。"
]
randomMessages = randomMessagesOriginal

class RoleCog(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def changerole(self, context, role: discord.Role):
        if (role.name != '見学者') and (role.name != '参加者'):
            await context.send(':sintyokudamedesu:')
            return

        roles = context.author.roles
        roleNames = [r.name for r in roles]
        if '見学者' in roleNames:
            await context.author.remove_roles(roles[roleNames.index('見学者')])
        if '参加者' in roleNames:
            await context.author.remove_roles(roles[roleNames.index('参加者')])

        await context.author.add_roles(role)
        await context.send('ロールを付与しました')

    @changerole.error
    async def changerole_error(self, context, error):
        if not DEBUG_MODE and isinstance(error, commands.errors.BadArgument):
            await context.send('うーん…うーん……うー')
            return

        await context.send(str(error))


class OmikujiCog(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.group()
    async def omikuji(self, context):
        if context.invoked_subcommand is not None:
            return
        await context.send(random.choice(randomMessages))

    @omikuji.command()
    async def edit(self, context, target: int, newMessage: str):
        if target < 0 or target >= len(randomMessages):
            await context.send('存在しない要素が指定されました')

        randomMessages[target] = randomMessages[target].split('  ', 1)[0] + '  ' + newMessage
        await context.send('メッセージを変更しました')


    @omikuji.command()
    async def list(self, context):
        i = 0
        res  = ''
        for message in randomMessages:
            res += str(i) + ' : ' + message.split('  ', 1)[0] + '\n'
            i += 1
        await context.send(res)

    @omikuji.command()
    async def reset(self, context):
        randomMessages = randomMessagesOriginal
        await context.send('おみくじのメッセージをリセットしました')

    @omikuji.command()
    async def help(self, context):
        await context.send('omikujiコマンドのヘルプ\n【コマンド】\n\
`!omikuji`:おみくじを引く\n`!omikuji edit index message`:おみくじリストのindexの要素を置き換え\n\
`!omikuji list`:おみくじリストのindexとの対応表を表示\n`!omikuji reset`:おみくじのメッセージをリセット\n`!omikuji help`:このヘルプを表示\n\
【注意】\nメッセージの変更はアプリケーションが再起動されると自動的にリセットされます。')


def setup(bot):
    bot.add_cog(RoleCog(bot))
    bot.add_cog(OmikujiCog(bot))