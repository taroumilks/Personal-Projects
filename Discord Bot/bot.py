import datetime
import os
import hikari
import lightbulb
import miru

Yessers = "**Any Valoranters?**\n Yes: "

class Valorants(miru.View):
    
    @miru.button(label = "Yes", emoji = "✅", style = hikari.ButtonStyle.PRIMARY)
    async def btn_Yes(self, button: miru.Button, ctx: miru.Context) -> None:
        global Yessers
        if str(ctx.user.mention) in Yessers:
            return
        else:
            Yessers = Yessers + "\n" + str(ctx.user.mention)
        await ctx.edit_response(content = Yessers)

    @miru.button(label = "Close", emoji = "❌", style = hikari.ButtonStyle.PRIMARY)
    async def btn_Exit(self, button: miru.Button, ctx: miru.Context) -> None:
        global Yessers
        Yessers = "**Any Valoranters?**\n Yes: "
        await ctx.edit_response("closed", components = [])
        self.stop()

    async def on_timeout(self) -> None:
        global Yessers
        Yessers = "**Any Valoranters**\n Yes: "
        await self.message.edit("The Menu has Ended", components = [])
        self.stop()


bot = lightbulb.BotApp(token="MTAxNjUyNjc3NTU4MjQ3NDI1MA.GSaO6A.pnJI39HL56iZcfcuBp8Z64ZqON-p2cPYteFrl8" , 
default_enabled_guilds=(1016526879534088243))

miru.load(bot)

# Creates a Looking for Group (LFG) for people who want to play Valorant
@bot.command()
@lightbulb.command('valorant', 'Creates a group for Valorant')
@lightbulb.implements(lightbulb.SlashCommand)
async def Valorant(ctx):
    view = Valorants(timeout=1800)
    message = await ctx.respond("Any Valoranters?", components=view.build())
    message = await message
    view.start(message)
    await view.wait()
    print("All done.")



bot.load_extensions('Plug-Ins.testplugin')
bot.run()
