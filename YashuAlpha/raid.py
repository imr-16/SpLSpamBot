from .data import RAID, REPLYRAID
import random
from config import STUFF, DEV
import asyncio
from .data import KeshavX
from YashuAlpha.Database.replyraid import *
from YashuAlpha.Database.sudo import get_sudos
from .verify import verify

hl = STUFF.COMMAND_HANDLER

LEGENDS = DEV.SUDO_USERS + [DEV.OWNER_ID] + KeshavX

SUDOS = DEV.SUDO_USERS

async def raid(_, m):
    if not await verify(m.from_user.id):
        return
    try:
        count = int(m.text.split()[1])
    except:
        return await m.reply(f"{hl}raid [count]")
    for c in range(0, count):
        raid = random.choice(RAID)
        if m.reply_to_message:
            if await verify (m.reply_to_message.from_user.id):
                return await m.reply("`CAN'T RAID THEM !`")
            await m.reply_to_message.reply(raid)
        else:
            await _.send_message(m.chat.id, raid)
        await asyncio.sleep(0.02)

async def replyraid(_, m):
    if not await verify(m.from_user.id):
        return
    try:
        if m.reply_to_message:
            id = m.reply_to_message.from_user.id
        else:
            x = m.text.split()[1]
            if str(x)[0] == "@":
                id = (await _.get_users(x)).id
            else:
                id = int(x)
    except:
        return await m.reply(f"`{hl}replyraid [id|username|reply]`")
    if await verify(id):
        return await m.reply("`CAN'T RAID THEM !`")
    if await is_rr(id):
        return await m.reply("`RAID IS ALREADY ACTIVATED TO THIS USER !`")
    await add_rr(id)
    return await m.reply(f"`RAID REPLY ACTIVATED TO USER `<code>{id}</code>")
    
async def dreplyraid(_, m):
    if not await verify(m.from_user.id):
        return
    try:
        if m.reply_to_message:
            id = m.reply_to_message.from_user.id
        else:
            x = m.text.split()[1]
            if str(x)[0] == "@":
                id = (await _.get_users(x)).id
            else:
                id = int(x)
    except:
        return await m.reply(f"`{hl}dreplyraid [id|username|reply]`")
    if not await is_rr(id):
        return await m.reply("`RAID IS NOT ACTIVATED TO THIS USER !`")
    await del_rr(id)
    return await m.reply(f"`RAID REPLY DEACTIVATED TO USER `<code>{id}</code>")

async def raid_cwf(_, m):
    if m.from_user:
        if await is_rr(m.from_user.id):
            await m.reply(random.choice(REPLYRAID))
