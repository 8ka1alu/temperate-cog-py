from discord.ext import commands, tasks # Bot Commands Frameworkのインポート
import discord
import asyncio
import json
import urllib.request

great_owner_id = 459936557432963103

# コグとして用いるクラスを定義。
class eew(commands.Cog):
    # testクラスのコンストラクタ。Botを受取り、インスタンス変数として保持。
    def __init__(self, bot):
        self.bot = bot
        self.code = 0
        self.loop.start()

    def cog_unload(self, bot):
        self.loop.cancel() 

    @commands.command()
    async def eew(self, ctx):
        """地震情報(最新)"""
        resp = urllib.request.urlopen('http://svir.jp/eew/data.json')
        eew = json.loads(resp.read().decode('utf-8'))
        embed=discord.Embed(title="**地震情報**", description=eew['Head']['Title'])
        embed.add_field(name="発表時刻", value=eew['Body']['Earthquake']['OriginTime'], inline=False)
        embed.add_field(name="震源地", value=eew['Body']['Earthquake']['Hypocenter']['Name'], inline=False)
        embed.add_field(name="マグニチュード", value=eew['Body']['Earthquake']['Magnitude'], inline=False) 
        embed.add_field(name="深さ", value=eew['Body']['Earthquake']['Hypocenter']['Depth'] + "km" , inline=False)
        embed.add_field(name="予想震度[震源地付近の推定です]", value=eew['Body']['Intensity']['TextInt'], inline=False)
        await ctx.send(embed=embed)

    @commands.command()
    async def eewop(self, ctx):
        """地震情報(確認用)"""
        resp = urllib.request.urlopen('http://svir.jp/eew/data.json')
        eew = json.loads(resp.read().decode('utf-8'))
        #Head
        embed=discord.Embed(title="**API識別タイトル、「緊急地震速報（予報）」で固定**", description=eew['Head']['Title'])
        embed.add_field(name="**緊急地震速報の発表時刻**", value=eew['Head']['DateTime'], inline=False)
        embed.add_field(name="**緊急地震速報を発表した管区気象台名**", value=eew['Head']['EditorialOffice'], inline=False)
        embed.add_field(name="**発表官庁名、「気象庁」で固定**", value=eew['Head']['PublishingOffice'], inline=False) 
        embed.add_field(name="**地震識別ID、地震ごとに異なる**", value=eew['Head']['EventID'], inline=False)
        embed.add_field(name="**電文の状態、「通常」は通常配信、「取消」はキャンセル報、「訓練」は訓練配信、「訓練取消」は訓練をキャンセル、「試験」は試験配信**", value=eew['Head']['Status'], inline=False)
        embed.add_field(name="**電文の配信数、地震識別IDごとに増えていく**", value=eew['Head']['Serial'], inline=False)
        embed.add_field(name="**電文バージョン**", value=eew['Head']['Version'], inline=False)
        await ctx.send(embed=embed)
        
        embed=discord.Embed(title="**震源情報**", description=eew['Body']['Earthquake'])
        embed.add_field(name="**緊急地震速報の発表時刻**", value=eew['Body']['Earthquake'], inline=False)
        embed.add_field(name="**緊急地震速報を発表した管区気象台名**", value=eew['Body']['Earthquake'], inline=False)
        embed.add_field(name="**発表官庁名、「気象庁」で固定**", value=eew['Body']['Earthquake'], inline=False) 
        embed.add_field(name="**地震識別ID、地震ごとに異なる**", value=eew['Body']['Earthquake'], inline=False)
        embed.add_field(name="**電文の状態、「通常」は通常配信、「取消」**", value=eew['Body']['Earthquake'], inline=False)
        embed.add_field(name="**電文の配信数、地震識別IDごとに増えていく**", value=eew['Body']['Earthquake'], inline=False)
        embed.add_field(name="**電文バージョン**", value=eew['Body']['Earthquake'], inline=False)
        embed.add_field(name="**緊急地震速報の発表時刻**", value=eew['Body']['Earthquake'], inline=False)
        embed.add_field(name="**緊急地震速報を発表した管区気象台名**", value=eew['Body']['Earthquake'], inline=False)
        embed=discord.Embed(title="**震源情報**", description=eew['Body']['Earthquake'])
        embed.add_field(name="**緊急地震速報の発表時刻**", value=eew['Body']['Earthquake'], inline=False)
        embed.add_field(name="**緊急地震速報を発表した管区気象台名**", value=eew['Body']['Earthquake'], inline=False)
        embed.add_field(name="**発表官庁名、「気象庁」で固定**", value=eew['Body']['Earthquake'], inline=False) 
        embed.add_field(name="**地震識別ID、地震ごとに異なる**", value=eew['Body']['Earthquake'], inline=False)
        embed.add_field(name="**電文の状態、「通常」は通常配信、「取消」**", value=eew['Body']['Earthquake'], inline=False)
        embed.add_field(name="**電文の配信数、地震識別IDごとに増えていく**", value=eew['Body']['Earthquake'], inline=False)
        embed.add_field(name="**電文バージョン**", value=eew['Body']['Earthquake'], inline=False)
        embed.add_field(name="**緊急地震速報の発表時刻**", value=eew['Body']['Earthquake'], inline=False)
        embed.add_field(name="**緊急地震速報を発表した管区気象台名**", value=eew['Body']['Earthquake'], inline=False)
        embed=discord.Embed(title="**震源情報**", description=eew['Body']['Earthquake'])
        embed.add_field(name="**緊急地震速報の発表時刻**", value=eew['Body']['Earthquake'], inline=False)
        embed.add_field(name="**緊急地震速報を発表した管区気象台名**", value=eew['Body']['Earthquake'], inline=False)
        embed.add_field(name="**発表官庁名、「気象庁」で固定**", value=eew['Body']['Earthquake'], inline=False) 
        embed.add_field(name="**地震識別ID、地震ごとに異なる**", value=eew['Body']['Earthquake'], inline=False)
        embed.add_field(name="**電文の状態、「通常」は通常配信、「取消」**", value=eew['Body']['Earthquake'], inline=False)
        embed.add_field(name="**電文の配信数、地震識別IDごとに増えていく**", value=eew['Body']['Earthquake'], inline=False)
        embed.add_field(name="**電文バージョン**", value=eew['Body']['Earthquake'], inline=False)
        embed.add_field(name="**緊急地震速報の発表時刻**", value=eew['Body']['Earthquake'], inline=False)
        embed.add_field(name="**緊急地震速報を発表した管区気象台名**", value=eew['Body']['Earthquake'], inline=False)
        embed=discord.Embed(title="**震源情報**", description=eew['Body']['Earthquake'])
        embed.add_field(name="**緊急地震速報の発表時刻**", value=eew['Body']['Earthquake'], inline=False)
        embed.add_field(name="**緊急地震速報を発表した管区気象台名**", value=eew['Body']['Earthquake'], inline=False)
        embed.add_field(name="**発表官庁名、「気象庁」で固定**", value=eew['Body']['Earthquake'], inline=False) 
        embed.add_field(name="**地震識別ID、地震ごとに異なる**", value=eew['Body']['Earthquake'], inline=False)
        embed.add_field(name="**電文の状態、「通常」は通常配信、「取消」**", value=eew['Body']['Earthquake'], inline=False)
        embed.add_field(name="**電文の配信数、地震識別IDごとに増えていく**", value=eew['Body']['Earthquake'], inline=False)
        embed.add_field(name="**電文バージョン**", value=eew['Body']['Earthquake'], inline=False)
        embed.add_field(name="**緊急地震速報の発表時刻**", value=eew['Body']['Earthquake'], inline=False)
        embed.add_field(name="**緊急地震速報を発表した管区気象台名**", value=eew['Body']['Earthquake'], inline=False)
        
        await ctx.send(embed=embed)

    @tasks.loop(seconds=5)
    async def loop(self):
        channels=self.bot.get_all_channels()
        chw=[ch for ch in channels if ch.name == "eew"]
        resp = urllib.request.urlopen('http://svir.jp/eew/data.json')
        eew = json.loads(resp.read().decode('utf-8'))
        eew_code = eew['Head']['EventID']
        if eew_code != self.code:
            embed=discord.Embed(title="**地震情報**", description=eew['Head']['Title'])
            embed.add_field(name="発表時刻", value=eew['Body']['Earthquake']['OriginTime'], inline=False)
            embed.add_field(name="震源地", value=eew['Body']['Earthquake']['Hypocenter']['Name'], inline=False)
            embed.add_field(name="マグニチュード", value=eew['Body']['Earthquake']['Magnitude'], inline=False) 
            embed.add_field(name="深さ", value=eew['Body']['Earthquake']['Hypocenter']['Depth'] + "km" , inline=False)
            embed.add_field(name="予想震度[震源地付近の推定です]", value=eew['Body']['Intensity']['TextInt'], inline=False)
            for chj in chw:   
                await chj.send(embed=embed)
            self.code = eew_code
    

# Bot本体側からコグを読み込む際に呼び出される関数。
def setup(bot):
    bot.add_cog(eew(bot))
