# © Copyright 2021 Lynx-Userbot LLC Company. (Axel Alexius Latukolan)
# GPL-3.0 License (General Public License) From Github
# WARNING !! Don't Delete This Hashtag if u Kang it !!
# Ported for Lynx-Userbot by @SyndicateTwenty4 (axel)
# Credits : @Vader and @TeamSecret_Kz (Kenzo)


from faker import Faker
from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError

from userbot import CMD_HELP
from userbot.events import register


# Ported for Lynx-Userbot
@register(outgoing=True, pattern=r"^\.adcc(?: |$)(.*)")
async def gencc(lynxevent):
    if lynxevent.fwd_from:
        return
    lynxcc = Faker()
    lynxname = lynxcc.name()
    lynxadre = lynxcc.address()
    lynxcard = lynxcc.credit_card_full()

    await edit_or_reply(lynxevent, f"__**👤 NAME :- **__\n`{lynxname}`\n\n__**🏡 ADDRESS :- **__\n`{lynxadre}`\n\n__**💸 CARD :- **__\n`{lynxcard}`")


# Ported for Lynx-Userbot
@register(outgoing=True, pattern=r"^\.bin(?: |$)(.*)")
async def bin(event):
    if event.fwd_from:
        return
    lynx_input = event.pattern_match.group(1)
    chat = "@lilornelwwttstbot"
    await event.edit("Checking...")
    async with event.client.conversation(chat) as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(
                    incoming=True,
                    from_users=1453545888))
            await event.client.send_message(chat, f"/bin {lynx_input}")
            response = await response
        except YouBlockedUserError:
            await event.reply("Please Unblock @lilornelwwttstbot")
            return
        else:
            await event.delete()
            await event.client.send_message(event.chat_id, response.message)


# Ported for Lynx-Userbot
@register(outgoing=True, pattern=r"^\.vbv(?: |$)(.*)")
async def vbv(event):
    if event.fwd_from:
        return
    lynx_input = event.pattern_match.group(1)
    chat = "@lilornelwwttstbot"
    await event.edit("Checking...")
    async with event.client.conversation(chat) as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(
                    incoming=True,
                    from_users=1453545888))
            await event.client.send_message(chat, f"/vbv {lynx_input}")
            response = await response
        except YouBlockedUserError:
            await event.reply("Please Unblock @lilornelwwttstbot")
            return
        else:
            await event.delete()
            await event.client.send_message(event.chat_id, response.message)


# Ported for Lynx-Userbot
@register(outgoing=True, pattern=r"^\.key(?: |$)(.*)")
async def key(event):
    if event.fwd_from:
        return
    lynx_input = event.pattern_match.group(1)
    chat = "@lilornelwwttstbot"
    await event.edit("Checking...")
    async with event.client.conversation(chat) as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(
                    incoming=True,
                    from_users=1453545888))
            await event.client.send_message(chat, f"/key {lynx_input}")
            response = await response
        except YouBlockedUserError:
            await event.reply("Please Unblock @lilornelwwttstbot")
            return
        else:
            await event.delete()
            await event.client.send_message(event.chat_id, response.message)


# Ported for Lynx-Userbot
@register(outgoing=True, pattern=r"^\.iban(?: |$)(.*)")
async def iban(event):
    if event.fwd_from:
        return
    lynx_input = event.pattern_match.group(1)
    chat = "@lilornelwwttstbot"
    await event.edit("Checking...")
    async with event.client.conversation(chat) as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(
                    incoming=True,
                    from_users=1453545888))
            await event.client.send_message(chat, f"/iban {lynx_input}")
            response = await response
        except YouBlockedUserError:
            await event.reply("Please Unblock @lilornelwwttstbot")
            return
        else:
            await event.delete()
            await event.client.send_message(event.chat_id, response.message)


# Ported for Lynx-Userbot
@register(outgoing=True, pattern=r"^\.ccheck(?: |$)(.*)")
async def ccheck(event):
    if event.fwd_from:
        return
    lynx_input = event.pattern_match.group(1)
    chat = "@lilornelwwttstbot"
    await event.edit("Checking...")
    async with event.client.conversation(chat) as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(
                    incoming=True,
                    from_users=1453545888))
            await event.client.send_message(chat, f"/ss {lynx_input}")
            response = await response
        except YouBlockedUserError:
            await event.reply("Please Unblock @lilornelwwttstbot")
            return
        else:
            await event.delete()
            await event.client.send_message(event.chat_id, response.message)


# Ported for Lynx-Userbot
@register(outgoing=True, pattern=r"^\.gen4(?: |$)(.*)")
async def ccbin(event):
    if event.fwd_from:
        return
    lynx_input = event.pattern_match.group(1)
    chat = "@lilornelwwttstbot"
    await event.edit(f"Trying to generate CC from the given bin `{lynx_input}`")
    async with event.client.conversation(chat) as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(
                    incoming=True,
                    from_users=1453545888))
            await event.client.send_message(chat, f"/gen 4 {lynx_input}")
            response = await response
        except YouBlockedUserError:
            await event.reply("Please Unblock @lilornelwwttstbot")
            return
        else:
            await event.delete()
            await event.client.send_message(event.chat_id, response.message)

# Ported for Lynx-Userbot
@register(outgoing=True, pattern=r"^\.g4(?: |$)(.*)")
async def g4(event):
    if event.fwd_from:
        return
    lynx_input = event.pattern_match.group(1)
    chat = "@lilornelwwttstbot"
    await event.edit("Checking...")
    async with event.client.conversation(chat) as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(
                    incoming=True,
                    from_users=1453545888))
            await event.client.send_message(chat, f"/g4 {lynx_input}")
            response = await response
        except YouBlockedUserError:
            await event.reply("Please Unblock @lilornelwwttstbot")
            return
        else:
            await event.delete()
            await event.client.send_message(event.chat_id, response.message)


# Ported for Lynx-Userbot
@register(outgoing=True, pattern=r"^\.g3(?: |$)(.*)")
async def g3(event):
    if event.fwd_from:
        return
    lynx_input = event.pattern_match.group(1)
    chat = "@lilornelwwttstbot"
    await event.edit("Checking...")
    async with event.client.conversation(chat) as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(
                    incoming=True,
                    from_users=1453545888))
            await event.client.send_message(chat, f"/g3 {lynx_input}")
            response = await response
        except YouBlockedUserError:
            await event.reply("Please Unblock @lilornelwwttstbot")
            return
        else:
            await event.delete()
            await event.client.send_message(event.chat_id, response.message)


# Ported for Lynx-Userbot
@register(outgoing=True, pattern=r"^\.g2(?: |$)(.*)")
async def g2(event):
    if event.fwd_from:
        return
    lynx_input = event.pattern_match.group(1)
    chat = "@lilornelwwttstbot"
    await event.edit("Checking...")
    async with event.client.conversation(chat) as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(
                    incoming=True,
                    from_users=1453545888))
            await event.client.send_message(chat, f"/g2 {lynx_input}")
            response = await response
        except YouBlockedUserError:
            await event.reply("Please Unblock @lilornelwwttstbot")
            return
        else:
            await event.delete()
            await event.client.send_message(event.chat_id, response.message)


# Ported for Lynx-Userbot
@register(outgoing=True, pattern=r"^\.g1(?: |$)(.*)")
async def g1(event):
    if event.fwd_from:
        return
    lynx_input = event.pattern_match.group(1)
    chat = "@lilornelwwttstbot"
    await event.edit("Checking...")
    async with event.client.conversation(chat) as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(
                    incoming=True,
                    from_users=1453545888))
            await event.client.send_message(chat, f"/g1 {lynx_input}")
            response = await response
        except YouBlockedUserError:
            await event.reply("Please Unblock @lilornelwwttstbot")
            return
        else:
            await event.delete()
            await event.client.send_message(event.chat_id, response.message)


# Ported for Lynx-Userbot
@register(outgoing=True, pattern=r"^\.g5(?: |$)(.*)")
async def g5(event):
    if event.fwd_from:
        return
    lynx_input = event.pattern_match.group(1)
    chat = "@lilornelwwttstbot"
    await event.edit("Checking...")
    async with event.client.conversation(chat) as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(
                    incoming=True,
                    from_users=1453545888))
            await event.client.send_message(chat, f"/g5 {lynx_input}")
            response = await response
        except YouBlockedUserError:
            await event.reply("Please Unblock @lilornelwwttstbot")
            return
        else:
            await event.delete()
            await event.client.send_message(event.chat_id, response.message)


# Ported for Lynx-Userbot
@register(outgoing=True, pattern=r"^\.g6(?: |$)(.*)")
async def g6(event):
    if event.fwd_from:
        return
    lynx_input = event.pattern_match.group(1)
    chat = "@lilornelwwttstbot"
    await event.edit("Checking...")
    async with event.client.conversation(chat) as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(
                    incoming=True,
                    from_users=1453545888))
            await event.client.send_message(chat, f"/g6 {lynx_input}")
            response = await response
        except YouBlockedUserError:
            await event.reply("Please Unblock @lilornelwwttstbot")
            return
        else:
            await event.delete()
            await event.client.send_message(event.chat_id, response.message)


@register(outgoing=True, pattern=r"^\.gen5(?: |$)(.*)")
async def ccbin(event):
    if event.fwd_from:
        return
    lynx_input = event.pattern_match.group(1)
    chat = "@lilornelwwttstbot"
    await event.edit(f"Trying to generate CC from the given bin `{lynx_input}`")
    async with event.client.conversation(chat) as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(
                    incoming=True,
                    from_users=1453545888))
            await event.client.send_message(chat, f"/gen 5 {lynx_input}")
            response = await response
        except YouBlockedUserError:
            await event.reply("Please Unblock @lilornelwwttstbot")
            return
        else:
            await event.delete()
            await event.client.send_message(event.chat_id, response.message)


# Ported for Lynx-Userbot
CMD_HELP.update({
    "ccarder": "✘ Pʟᴜɢɪɴ : CC Carder\
\n\n⚡𝘾𝙈𝘿⚡: `.adcc`\
\n↳ : Generate Fake Address\
\n\n⚡𝘾𝙈𝘿⚡: `.gen4` | `.gen5`\
\n↳ : Generates Fake CC.\
\n\n⚡𝘾𝙈𝘿⚡: `.ccheck` <Query>\
\n↳ : Checks That The Given CC is Live or Not.\
\n\n⚡𝘾𝙈𝘿⚡: `.iban` <Query>\
\n↳ : Checks That The Given IBAN ID is Live or Not.\
\n\n⚡𝘾𝙈𝘿⚡: `.key` <Query>\
\n↳ : Checks The Status of Probided Key.\
\n\n⚡𝘾𝙈𝘿⚡: `.vbv` <Query>\
\n↳ : Checks The Vbv Status of Given Card.\
\n↳ : Checks The Status of Probided Key.\
\n\n⚡𝘾𝙈𝘿⚡: `.g6` <Query>\
\n↳ : Checks The g6 Status of Given Card.\
\n↳ : Checks The Status of Probided Key.\
\n\n⚡𝘾𝙈𝘿⚡: `.g5` <Query>\
\n↳ : Checks The g5 Status of Given Card.\
\n↳ : Checks The Status of Probided Key.\
\n\n⚡𝘾𝙈𝘿⚡: `.g4` <Query>\
\n↳ : Checks The g4 Status of Given Card.\
\n↳ : Checks The Status of Probided Key.\
\n\n⚡𝘾𝙈𝘿⚡: `.g3` <Query>\
\n↳ : Checks The g3 Status of Given Card.\
\n↳ : Checks The Status of Probided Key.\
\n\n⚡𝘾𝙈𝘿⚡: `.g2` <Query>\
\n↳ : Checks The g2 Status of Given Card.\
\n↳ : Checks The Status of Probided Key.\
\n\n⚡𝘾𝙈𝘿⚡: `.g1` <Query>\
\n↳ : Checks The g1 Status of Given Card.\
\n\n⚡𝘾𝙈𝘿⚡: `.bin` <Query>\
\n↳ : Checks That The Given Bin is Valid or Not.\
\n\n⚡𝘾𝙈𝘿⚡: `.ccbin` <Bin>\
\n↳ : Generates CC From The Given Bin."
})
