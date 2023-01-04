class script(object):
    START_TXT = """<b>Hello {}

I Can Provide Movies And Series,
Just Add Me To Your Group And Enjoy.
I Work On Both Group And PM (For Owner Only).</b>"""

    HELP_TXT = """<b>Hey {}

Here Is The Help For My Commands.</b>"""

    ABOUT_TXT = """<b>✯ My Name : {}</b>

<b>✯ Creator : <a href=https://t.me/toonswood>ToonsWood</a></b>

<b>✯ Updates : <a href=https://t.me/toonswood>ToonsWood</a></b>

<b>✯ Build Status : ᴠ1.0 [Stable]</b>"""

    SOURCE_TXT ="""
<b>This Is An Private Project Of ToonsWood.In.

- Source - <a href=https://t.me/toonswood>ToonsWood</a></b>
"""
 
    MANUELFILTER_TXT = """Help: <b>Filters</b>
- Filter IS A Feature Were Users Can Set Automated Replies For A Particular Keyword And I Will Respond Whenever A Keyword Is Found In The Message.
<b>Note:</b>
1. This Bot Should Have Admin Privilege.
2. Only Admins Can Add Filters In A Chat.
3. Alert Buttons Have a Limit Of 64 Characters.

<u><b>Commands And Usage:</b></u>
• /filter - <code>Add A Filter In A Chat</code>
• /filters - <code>List All The Filters Of A Chat</code>
• /del - <code>Delete A Specific Filter In A Chat</code>
• /delall - <code>Delete The Whole Filters In A Chat (Chat Owner Only)</code>

~ Add The Bot As Admin On Your Group.
~ Use /connect And Connect Your Group To The Bot.
~ Use /settings On Bot's PM And Turn On/Off Auto Delete & Manual Filters On The Settings Menu."""

    BUTTON_TXT = """Help: <b>Buttons</b>

- This Bot Supports Both URL And Alert Inline Buttons.

<b>Note:</b>
1. Telegram Will Not Allows You To Send Buttons Without Any Content, So Content Is Mandatory.
2. This Bot Supports Buttons With Any Telegram Media Type.
3. Buttona Should Be Properly Parsed As Markdown Format.

<b>URL Buttons:</b>
<code>[Button Text](buttonurl:https://t.me/toonswood)</code>

<b>Alert Buttons:</b>
<code>[Button Text](buttonalert:This Is An Alert Message)</code>"""

    AUTOFILTER_TXT = """ʜᴇʟᴘ: <b>Auto Filter</b>

<u><b>Note: File Index</b></u>
1. Make Me The Admin Of Your Channel If It's Private.
2. Make Sure That Your Channel Does Not Contains CamRips, Porn And Fake Files.
3. Forward The Last Message To Me With Quotes. I'll Add All The Files In That Channel To My DB.

<u><b>Note: Auto Filter</b></u>
1. Add The Bot As Admin On Your Group.
2. Use /connect And Connect Your Group To The Bot.
3. Use /settings On Bot's PM And Turn On/Off AutoFilter & Auto Delete On The Settings Menu.
4. Use /set_template To Set Your Custom IMDb Template."""

    CONNECTION_TXT = """ʜᴇʟᴘ: <b>ᴄᴏɴɴᴇᴄᴛɪᴏɴꜱ</b>

- ᴜꜱᴇᴅ ᴛᴏ ᴄᴏɴɴᴇᴄᴛ ʙᴏᴛ ᴛᴏ ᴘᴍ ꜰᴏʀ ᴍᴀɴᴀɢɪɴɢ ꜰɪʟᴛᴇʀꜱ 
- ɪᴛ ʜᴇʟᴘꜱ ᴛᴏ ᴀᴠᴏɪᴅ ꜱᴘᴀᴍᴍɪɴɢ ɪɴ ɢʀᴏᴜᴘꜱ.

<b>ɴᴏᴛᴇ:</b>
1. ᴏɴʟʏ ᴀᴅᴍɪɴꜱ ᴄᴀɴ ᴀᴅᴅ ᴀ ᴄᴏɴɴᴇᴄᴛɪᴏɴ.
2. ꜱᴇɴᴅ <code>/connect</code> ꜰᴏʀ ᴄᴏɴɴᴇᴄᴛɪɴɢ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ᴘᴍ

<u><b>Cᴏᴍᴍᴀɴᴅs Aɴᴅ Usᴀɢᴇ:</b></u>
• /connect  - <code>ᴄᴏɴɴᴇᴄᴛ ᴀ ᴘᴀʀᴛɪᴄᴜʟᴀʀ ᴄʜᴀᴛ ᴛᴏ ʏᴏᴜʀ ᴘᴍ</code>
• /disconnect  - <code>ᴅɪꜱᴄᴏɴɴᴇᴄᴛ ꜰʀᴏᴍ ᴀ ᴄʜᴀᴛ</code>
• /connections - <code>ʟɪꜱᴛ ᴀʟʟ ʏᴏᴜʀ ᴄᴏɴɴᴇᴄᴛɪᴏɴꜱ</code>"""

    ADMIN_TXT = """
<code>Tʜɪs Mᴏᴅᴜʟᴇ Oɴʟʏ Wᴏʀᴋs Fᴏʀ Mʏ Aᴅᴍɪɴs</code>

• /logs - <code>ᴛᴏ ɢᴇᴛ ᴛʜᴇ ʀᴇᴄᴇɴᴛ ᴇʀʀᴏʀꜱ</code>
• /stats - <code>ᴛᴏ ɢᴇᴛ ꜱᴛᴀᴛᴜꜱ ᴏꜰ ꜰɪʟᴇꜱ ɪɴ ᴅʙ.</code>
• /delete - <code>ᴛᴏ ᴅᴇʟᴇᴛᴇ ᴀ ꜱᴘᴇᴄɪꜰɪᴄ ꜰɪʟᴇ ꜰʀᴏᴍ ᴅʙ.</code>
• /deleteall - <code>ᴛᴏ ᴅᴇʟᴇᴛᴇ ᴀʟʟ ꜰɪʟᴇs ꜰʀᴏᴍ ᴅʙ.</code>
• /users - <code>ᴛᴏ ɢᴇᴛ ʟɪꜱᴛ ᴏꜰ ᴍʏ ᴜꜱᴇʀꜱ ᴀɴᴅ ɪᴅꜱ.</code>
• /chats - <code>ᴛᴏ ɢᴇᴛ ʟɪꜱᴛ ᴏꜰ ᴍʏ ᴄʜᴀᴛꜱ ᴀɴᴅ ɪᴅꜱ</code>
• /channel - <code>ᴛᴏ ɢᴇᴛ ʟɪꜱᴛ ᴏꜰ ᴛᴏᴛᴀʟ ᴄᴏɴɴᴇᴄᴛᴇᴅ ᴄʜᴀɴɴᴇʟꜱ</code>
• /setskip - <code>Tᴏ sᴋɪᴘ ɴᴜᴍʙᴇʀ ᴏғ ᴍᴇssᴀɢᴇs ᴡʜᴇɴ ɪɴᴅᴇxɪɴɢ ғɪʟᴇs.</code>
• /leave  - <code>ᴛᴏ ʟᴇᴀᴠᴇ ꜰʀᴏᴍ ᴀ ᴄʜᴀᴛ.</code>
• /disable  -  <code>ᴛᴏ ᴅɪꜱᴀʙʟᴇ ᴀ ᴄʜᴀᴛ.</code>
• /invite - <code>Tᴏ ɢᴇᴛ ᴛʜᴇ ɪɴᴠɪᴛᴇ ʟɪɴᴋ ᴏғ ᴀɴʏ ᴄʜᴀᴛ ᴡʜᴇʀᴇ ᴛʜᴇ ʙᴏᴛ ɪs ᴀᴅᴍɪɴ.</code>
• /ban_user  - <code>ᴛᴏ ʙᴀɴ ᴀ ᴜꜱᴇʀ.</code>
• /unban_user  - <code>ᴛᴏ ᴜɴʙᴀɴ ᴀ ᴜꜱᴇʀ.</code>
• /usend - <code>Tᴏ Sᴇɴᴅ ᴀ Mᴇssɢᴀᴇ ᴛᴏ Pᴇʀᴛɪᴄᴜʟᴀʀ Usᴇʀ</code>
• /gsend - <code>Tᴏ Sᴇɴᴅ ᴀ Mᴇssᴀɢᴇ ᴛᴏ Pᴇʀᴛɪᴄᴜʟᴀʀ Cʜᴀᴛ</code>
• /broadcast - <code>ᴛᴏ ʙʀᴏᴀᴅᴄᴀꜱᴛ ᴀ ᴍᴇꜱꜱᴀɢᴇ ᴛᴏ ᴀʟʟ ᴜꜱᴇʀꜱ</code>
• /group_broadcast - <code>ᴛᴏ ʙʀᴏᴀᴅᴄᴀsᴛ ᴀ ᴍᴇssᴀɢᴇ ᴛᴏ ᴀʟʟ ᴄᴏɴɴᴇᴄᴛᴇᴅ ɢʀᴏᴜᴘs</code>
• /gfilter - <code>ᴛᴏ ᴀᴅᴅ ɢʟᴏʙᴀʟ ғɪʟᴛᴇʀs</code>
• /gfilters - <code>ᴛᴏ ᴠɪᴇᴡ ʟɪsᴛ ᴏғ ᴀʟʟ ɢʟᴏʙᴀʟ ғɪʟᴛᴇʀs<code>
• /delg - <code>ᴛᴏ ᴅᴇʟᴇᴛᴇ ᴀ sᴘᴇᴄɪғɪᴄ ɢʟᴏʙᴀʟ ғɪʟᴛᴇʀ</code>
• /delallg - <code>ᴛᴏ ᴅᴇʟᴇᴛᴇ ᴀʟʟ ɢʟᴏʙᴀʟ ғɪʟᴛᴇʀs</code>"""

    STATUS_TXT = """<b>📂 ғɪʟᴇs sᴀᴠᴇᴅ:</b> <code>{}</code>
<b>👤 ᴜsᴇʀs:</b> <code>{}</code>
<b>👥 ɢʀᴏᴜᴘs:</b> <code>{}</code>
<b>📉 ᴏᴄᴄᴜᴘɪᴇᴅ:</b> <code>{}</code>

<b><a href=https://t.me/toonswood>Maintained By ToonsWood.In</a></b>"""

    ADMIN_STATUS_TXT = """<b>⍟────[ ʙᴏᴛ sᴛᴀᴛᴜ𝗌 ]────⍟</b>

<b>⏳ ʙᴏᴛ ᴜᴘᴛɪᴍᴇ:</b> <code>{}</code>

<b>☣️ ᴄᴘᴜ:</b> <code>{}%</code>

<b>☢️ ʀᴀᴍ:</b> <code>{}%</code>

<b>📊 ғɪʟᴇs sᴀᴠᴇᴅ:</b> <code>{}</code>

<b>👤 ᴜsᴇʀs:</b> <code>{}</code>

<b>👥 ɢʀᴏᴜᴘs:</b> <code>{}</code>

<b>♻️ ᴛᴏᴛᴀʟ:</b> <code>512 MB</code>

<b>🉐 ᴏᴄᴄᴜᴘɪᴇᴅ:</b> <code>{}</code>

<b>🆓 ғʀᴇᴇ:</b> <code>{}</code>

<b>⍟────[ @ToonsWood ]─────⍟</b>"""

    LOG_TEXT_G = """<b>#NewGroup
    
Gʀᴏᴜᴘ = {} (<code>{}</code>)

Tᴏᴛᴀʟ Mᴇᴍʙᴇʀs = <code>{}</code>

Aᴅᴅᴇᴅ Bʏ - {}</b>
"""
    LOG_TEXT_P = """<b>#NewUser
    
ID - <code>{}</code>

Nᴀᴍᴇ - {}</b>
"""
    ALRT_TXT = """⚠️ 𝖧ᴇʏ !
    
𝖲ᴇᴀʀᴄʜ 𝖸ᴏᴜʀ 𝖮ᴡɴ 𝖥ɪʟᴇ, 
    
𝖣ᴏɴ'ᴛ 𝖢ʟɪᴄᴋ 𝖮ᴛʜᴇʀ𝗌 𝖱ᴇ𝗌ᴜʟᴛ𝗌 😬
"""

    OLD_ALRT_TXT = """⚠️ 𝖧ᴇʏ ! 
    
𝖸ᴏᴜ Aʀᴇ U𝗌ɪɴɢ Oɴᴇ Oғ Mʏ Oʟᴅ Mᴇ𝗌𝗌ᴀɢᴇ𝗌, 
    
Sᴇɴᴅ Tʜᴇ Rᴇǫᴜᴇ𝗌ᴛ Aɢᴀɪɴ
"""

    CUDNT_FND = """<b>sᴏʀʀʏ ɴᴏ ꜰɪʟᴇs ᴡᴇʀᴇ ꜰᴏᴜɴᴅ

ᴄʜᴇᴄᴋ ʏᴏᴜʀ sᴘᴇʟʟɪɴɢ ɪɴ ɢᴏᴏɢʟᴇ ᴀɴᴅ ᴛʀʏ ᴀɢᴀɪɴ

ʀᴇᴀᴅ ɪɴsᴛʀᴜᴄᴛɪᴏɴs ꜰᴏʀ ʙᴇᴛᴛᴇʀ ʀᴇsᴜʟᴛs ☟</b>
"""

    I_CUDNT = """
<b>Sᴏʀʀʏ

I Cᴏᴜʟᴅ Nᴏᴛ Fɪɴᴅ Aɴʏᴛʜɪɴɢ Rᴇʟᴀᴛᴇᴅ Tᴏ Tʜᴀᴛ
Pʟᴇᴀsᴇ Cʜᴇᴄᴋ Yᴏᴜʀ Sᴘᴇʟʟɪɴɢ 🤧</b>
"""

    I_CUD_NT = """ɪ ᴄᴏᴜʟᴅɴ'ᴛ ꜰɪɴᴅ ᴀɴʏ ᴍᴏᴠɪᴇ ʀᴇʟᴀᴛᴇᴅ ᴛᴏ {}.
ᴘʟᴇᴀꜱᴇ ᴄʜᴇᴄᴋ ᴛʜᴇ ꜱᴘᴇʟʟɪɴɢ ᴏɴ ɢᴏᴏɢʟᴇ ᴏʀ ɪᴍᴅʙ...
"""

    MVE_NT_FND = """<b>Mᴏᴠɪᴇ Nᴏᴛ Fᴏᴜɴᴅ...
    
Rᴇᴀsᴏɴs
𝟷) O.T.T Oʀ DVD Nᴏᴛ Rᴇʟᴇᴀsᴇᴅ

𝟸) Tʏᴘᴇ Nᴀᴍᴇ Wɪᴛʜ Yᴇᴀʀ

𝟹) Mᴏᴠɪᴇ Is Nᴏᴛ Aᴠᴀɪʟᴀʙʟᴇ ɪɴ ᴛʜᴇ Dᴀᴛᴀʙᴀsᴇ 
Rᴇᴘᴏʀᴛ Hᴇʀᴇ @TheToonsWood</b>
"""

    TOP_ALRT_MSG = """Cʜᴇᴄᴋɪɴɢ Fᴏʀ Mᴏᴠɪᴇ Iɴ Dᴀᴛᴀʙᴀsᴇ...
"""
    
    OWNER_INFO = """
<b>⍟───[ ᴏᴡɴᴇʀ ᴅᴇᴛᴀɪʟꜱ ]───⍟
    
• ꜰᴜʟʟ ɴᴀᴍᴇ : ToonsWood『🇮🇳』
• ᴜꜱᴇʀɴᴀᴍᴇ : @ToonsWood
• ᴘᴇʀᴍᴀɴᴇɴᴛ ʟɪɴᴋ : <a href='t.me/thetoonswood'>Chat Group</a></b>
"""

    KD_IMDB = """
<u><b>Cᴏᴍᴍᴀɴᴅs Aɴᴅ Usᴀɢᴇ:</b></u>

• /imdb  - <code>ɢᴇᴛ ᴛʜᴇ ꜰɪʟᴍ ɪɴꜰᴏʀᴍᴀᴛɪᴏɴ ꜰʀᴏᴍ ɪᴍᴅʙ ꜱᴏᴜʀᴄᴇ.</code>
• /search  - <code>ɢᴇᴛ ᴛʜᴇ ꜰɪʟᴍ ɪɴꜰᴏʀᴍᴀᴛɪᴏɴ ꜰʀᴏᴍ ᴠᴀʀɪᴏᴜꜱ ꜱᴏᴜʀᴄᴇꜱ.</code>
"""

    KD_MISC = """
<u><b>Cᴏᴍᴍᴀɴᴅs Aɴᴅ Usᴀɢᴇ:</b></u>

• /id - <code>ɢᴇᴛ ɪᴅ ᴏꜰ ᴀ ꜱᴘᴇᴄɪꜰɪᴇᴅ ᴜꜱᴇʀ.</code>
• /info  - <code>ɢᴇᴛ ɪɴꜰᴏʀᴍᴀᴛɪᴏɴ ᴀʙᴏᴜᴛ ᴀ ᴜꜱᴇʀ.</code>
"""

    KD_FILSTR = """
<b>⍟ Wᴇʟᴄᴏᴍᴇ Tᴏ Fɪʟᴇ Sᴛᴏʀᴇ Mᴏᴅᴜʟᴇ ⍟</b>

» ᴀ ᴍᴏᴅᴜʟᴇ ᴛᴏ ɢᴇᴛ sʜᴀʀᴀʙʟᴇ ʟɪɴᴋ ғᴏʀ ᴀɴʏ ᴛᴇʟᴇɢʀᴀᴍ ᴍᴇᴅɪᴀ.

<u><b>Cᴏᴍᴍᴀɴᴅs Aɴᴅ Usᴀɢᴇ:</b></u>

• /link <code>- ʀᴇᴘʟʏ ᴛᴏ ᴀɴʏ ᴛᴇʟᴇɢʀᴀᴍ ᴍᴇᴅɪᴀ.<code>
• /batch <code>- ᴛᴏ ᴄʀᴇᴀᴛᴇ ʟɪɴᴋ ғᴏʀ ᴍᴜʟᴛɪᴘʟᴇ ᴍᴇᴅɪᴀ.<code>

<b>Exᴀᴍᴘʟᴇ:</b>
<code>/batch https://t.me/toonswood/1 
https://t.me/toonswood/9</code>
"""

    KD_CNL = """
<b>⍟ Cʜᴀɴɴᴇʟs & Gʀᴏᴜᴘs Mᴏᴅᴜʟᴇ ⍟</b>

<b>🎬 Cᴏᴍᴘʟᴇᴛᴇ Mᴏᴠɪᴇ Rᴇǫᴜᴇsᴛɪɴɢ Gʀᴏᴜᴘ.
🚦 Aʟʟ Lᴀɴɢᴜᴀɢᴇs Mᴏᴠɪᴇs & Sᴇʀɪᴇs.
🗣️ Bᴏᴛ Sᴜᴘᴘᴏʀᴛ Gʀᴏᴜᴘ.
📢 Bᴏᴛ Uᴘᴅᴀᴛᴇs Cʜᴀɴɴᴇʟ.</b>
"""

    FORCE_SUB = """
**⚠️ ᴘʟᴇᴀsᴇ ғᴏʟʟᴏᴡ ᴛʜɪs ʀᴜʟᴇs ⚠️

ɪɴ ᴏʀᴅᴇʀ ᴛᴏ ɢᴇᴛ ᴛʜᴇ ᴍᴏᴠɪᴇ ʀᴇǫᴜᴇsᴛᴇᴅ ʙʏ ʏᴏᴜ.

ʏᴏᴜ ᴡɪʟʟ ʜᴀᴠᴇ ᴛᴏ ᴊᴏɪɴ ᴏᴜʀ ᴏғғɪᴄɪᴀʟ ᴄʜᴀɴɴᴇʟ ғɪʀsᴛ.

ᴀғᴛᴇʀ ᴛʜᴀᴛ ᴛʀʏ ᴀᴄᴄᴇssɪɴɢ ᴛʜᴀᴛ ᴍᴏᴠɪᴇ ᴛʜᴇɴ ᴄʟɪᴄᴋ ᴏɴ ᴛʜᴇ ᴛʀʏ ᴀɢᴀɪɴ.

ɪ'ʟʟ sᴇɴᴅ ʏᴏᴜ ᴛʜᴀᴛ ᴍᴏᴠɪᴇ ᴘʀɪᴠᴀᴛᴇʟʏ.**
"""
    
    BANP_LOG_TXT = """<b>⍟ Bᴀɴɴᴇᴅ Usᴇʀ Lᴏɢs ⍟</b>

<b>Aᴅᴍɪɴ :</b> </b> <b>{}</b>

<b>Nᴀᴍᴇ :</b> <b>{}</b>

<b>Rᴇᴀsᴏɴ :</b> <code>{}</code>

<b>⍟ #BannedUser ⍟</b>
"""
    UNBANP_LOG_TXT = """<b>⍟ UɴBᴀɴɴᴇᴅ Usᴇʀ Lᴏɢs ⍟</b>

<b>Aᴅᴍɪɴ :</b> </b> <b>{}</b>

<b>Nᴀᴍᴇ :</b> <b>{}</b>

<b>⍟ #UnBannedUser ⍟</b>
"""
    BANG_LOG_TXT = """<b>⍟ Bᴀɴɴᴇᴅ Gʀᴏᴜᴘ Lᴏɢs ⍟</b>

<b>Cʜᴀᴛ ID :</b> <code>{}</code>

<b>Rᴇᴀsᴏɴ :</b> <code>{}</code>

<b>Aᴅᴍɪɴ :</b> </b> <b>{}</b>

<b>⍟ #BannedGroup ⍟</b>
"""
    UNBANG_LOG_TXT = """<b>⍟ UɴBᴀɴɴᴇᴅ Gʀᴏᴜᴘ Lᴏɢs ⍟</b>

<b>Cʜᴀᴛ ID :</b> <code>{}</code>

<b>Aᴅᴍɪɴ :</b> </b> <b>{}</b>

<b>⍟ #UnBannedGroup ⍟</b>
"""

    REQINFO2 = """
⚠ ɪɴꜰᴏʀᴍᴀᴛɪᴏɴ ⚠

ɪꜰ ʏᴏᴜ ᴅᴏ ɴᴏᴛ ꜱᴇᴇ ᴛʜᴇ ʀᴇǫᴜᴇsᴛᴇᴅ ᴍᴏᴠɪᴇ / sᴇʀɪᴇs ꜰɪʟᴇ, ʟᴏᴏᴋ ᴀᴛ ᴛʜᴇ ɴᴇxᴛ ᴘᴀɢᴇ
"""

    REQINFO = """
⚠ ɪɴꜰᴏʀᴍᴀᴛɪᴏɴ ⚠

ᴀꜰᴛᴇʀ 10 ᴍɪɴᴜᴛᴇꜱ ᴛʜɪꜱ ᴍᴇꜱꜱᴀɢᴇ ᴡɪʟʟ ʙᴇ ᴀᴜᴛᴏᴍᴀᴛɪᴄᴀʟʟʏ ᴅᴇʟᴇᴛᴇᴅ

ɪꜰ ʏᴏᴜ ᴅᴏ ɴᴏᴛ ꜱᴇᴇ ᴛʜᴇ ʀᴇǫᴜᴇsᴛᴇᴅ ᴍᴏᴠɪᴇ / sᴇʀɪᴇs ꜰɪʟᴇ, ʟᴏᴏᴋ ᴀᴛ ᴛʜᴇ ɴᴇxᴛ ᴘᴀɢᴇ
"""

    MINFO = """
⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯
ᴍᴏᴠɪᴇ ʀᴇǫᴜᴇꜱᴛ ꜰᴏʀᴍᴀᴛ
⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯

ɢᴏ ᴛᴏ ɢᴏᴏɢʟᴇ ➠ ᴛʏᴘᴇ ᴍᴏᴠɪᴇ ɴᴀᴍᴇ ➠ ᴄᴏᴘʏ ᴄᴏʀʀᴇᴄᴛ ɴᴀᴍᴇ ➠ ᴘᴀꜱᴛᴇ ᴛʜɪꜱ ɢʀᴏᴜᴘ

ᴇxᴀᴍᴘʟᴇ : Black Adam 2022

🚯 ᴅᴏɴᴛ ᴜꜱᴇ ➠ ':(!,./)
"""

    SINFO = """
⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯
ꜱᴇʀɪᴇꜱ ʀᴇǫᴜᴇꜱᴛ ꜰᴏʀᴍᴀᴛ
⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯

ɢᴏ ᴛᴏ ɢᴏᴏɢʟᴇ ➠ ᴛʏᴘᴇ ꜱᴇʀɪᴇꜱ ɴᴀᴍᴇ ➠ ᴄᴏᴘʏ ᴄᴏʀʀᴇᴄᴛ ɴᴀᴍᴇ ➠ ᴘᴀꜱᴛᴇ ᴛʜɪꜱ ɢʀᴏᴜᴘ

ᴇxᴀᴍᴘʟᴇ : Loki S01E01 or Loki S01 E01

🚯 ᴅᴏɴᴛ ᴜꜱᴇ ➠ ':(!,./)
"""

    PAGEINFO = """
ᴘᴀɢᴇs ᴍᴇᴀɴs 10 ғɪʟᴇs ɪɴ ᴏɴᴇ ᴘᴀɢᴇ

ɪғ ʏᴏᴜ ɴᴏᴛ sᴇᴇ ʏᴏᴜʀ ғɪʟᴇs ᴏɴ ᴛʜɪs ᴘᴀɢᴇ ᴛʜᴇɴ ᴄʟɪᴄᴋ ᴏɴ ɴᴇxᴛ ᴘᴀɢᴇ.

Powered by :- ToonsWood.In
"""

    SPLMD = """
ᴍᴏᴠɪᴇ ʀᴇǫᴜᴇsᴛ ғᴏʀᴍᴀᴛ

ᴇxᴀᴍᴘʟᴇ : Black Adam or Black Adam 2022

sᴇʀɪᴇs ʀᴇǫᴜᴇsᴛ ғᴏʀᴍᴀᴛ

ᴇxᴀᴍᴘʟᴇ : Loki S01E01 or Loki S01 E01

🚯ᴅᴏɴ'ᴛ ᴜsᴇ ➠ ':(!,./)

Powered by :- ToonsWood.In
"""
    
    REQUEST_TXT = """
<u><b>📫 Rᴇǫᴜᴇsᴛ Dᴇᴛᴀɪʟs :</b></u>

<b>🔖 Mᴇssᴀɢᴇ :</b><code>{}</code>

<b>🕵️ Rᴇǫᴜᴇsᴛᴇᴅ Bʏ :</b> <b>{} [ <code>{}</code> ] </b>
"""

    REQUEST2_TXT = """
<i><b>Yᴏᴜʀ Rᴇǫᴜᴇsᴛ Hᴀs Bᴇᴇɴ Aᴅᴅᴇᴅ!
Pʟᴇᴀsᴇ Wᴀɪᴛ Fᴏʀ Sᴏᴍᴇ Tɪᴍᴇ.</b></i>
"""

    SGROUP_TXT = """
<b>Dᴇᴀʀ, {}

<code>{}</code> Rᴇsᴜʟᴛs Aʀᴇ Aʟʀᴇᴀᴅʏ Aᴠᴀɪʟᴀʙʟᴇ Fᴏʀ Yᴏᴜʀ Rᴇǫᴜᴇsᴛ <code>{}</code> Iɴ <a href=https://t.me/{}>Oᴜʀ Bᴏᴛ</a>.</b>
"""

    DONE_UPLOAD = """
Tʜᴇ Rᴇǫᴜᴇsᴛ Is Cᴏᴍᴘʟᴇᴛᴇᴅ !! Cʜᴇᴄᴋ Bᴏᴛ & Cʜᴀɴɴᴇʟ !!
"""

    REQ_REJECT = """
Tʜᴇ Rᴇǫᴜᴇsᴛ Is Rᴇᴊᴇᴄᴛᴇᴅ Mᴀʏʙᴇ Dᴜᴇ Tᴏ Sᴀᴍᴇ Rᴇǫᴜᴇsᴛ, Nᴏᴛ Iɴ Fᴏʀᴍᴀᴛ !!
"""

    REQ_NO = """
Tʜᴇ Rᴇǫᴜᴇsᴛ Is Nᴏᴛ Aᴠᴀɪʟᴀʙʟᴇ Mᴀʏʙᴇ Dᴜᴇ Tᴏ Nᴏᴛ Rᴇʟᴇᴀsᴇᴅ Oʀ Nᴏᴛ Aᴠᴀɪʟᴀʙʟᴇ !!
"""

    DONE_ALREADY = """
Tʜᴇ Rᴇǫᴜᴇsᴛ Is Aʟʀᴇᴀᴅʏ Uᴘʟᴏᴀᴅᴇᴅ !! Cʜᴇᴄᴋ Bᴏᴛ & Cʜᴀɴɴᴇʟ !!
""" 
    
    DONE_UPLOAD2 = """
<b>Yᴏᴜʀ Rᴇǫᴜᴇsᴛ Sᴜᴄᴇssғᴜʟʟʏ Uᴘʟᴏᴀᴅᴇᴅ Sᴇᴀʀᴄʜ Aɢᴀɪɴ..🙃</b>
"""

    REQ_REJECT2 = """
<b>Rᴇǫᴜᴇsᴛ Rᴇᴊᴇᴄᴛᴇᴅ 🚫 !!

Yᴏᴜʀ Rᴇǫᴜᴇsᴛ Aʟʀᴇᴀᴅʏ Mᴀʏʙᴇ Iɴ Tʜᴇ Rᴇǫᴜᴇsᴛ Lɪsᴛ Oʀ Yᴏᴜʀ Rᴇǫᴜᴇsᴛ Is Mᴀʟғᴏʀᴍᴀᴛᴛᴇᴅ. Kɪɴᴅʟʏ Rᴇǫᴜᴇsᴛ Aɢᴀɪɴ Oʀ Cᴏɴᴛᴀᴄᴛ Aᴅᴍɪɴ Fᴏʀ Hᴇʟᴘ.</b>
"""

    REQ_NO2 = """
<b>Sᴏʀʀʏ Yᴏᴜʀ Rᴇǫᴜᴇsᴛ Nᴏᴛ Aᴠᴀɪʟᴀʙʟᴇ 😔,
Kɪɴᴅʟʏ Cᴏɴᴛᴀᴄᴛ Aᴅᴍɪɴ Fᴏʀ Hᴇʟᴘ.</b>
"""

    DONE_ALREADY2 = """
<b>Rᴇǫᴜᴇsᴛ Aʟʀᴇᴀᴅʏ Uᴘʟᴏᴀᴅᴇᴅ ❗,
Kɪɴᴅʟʏ Cʜᴇᴄᴋ Tʜᴇ Bᴏᴛ Bᴇғᴏʀᴇ Rᴇǫᴜᴇsᴛɪɴɢ.</b>
"""

    CAP_DLT_TXT = """
<b>Tʜᴇ Rᴇꜱᴜʟᴛꜱ Fᴏʀ ☞ <code>{}</code></b>

<b>Rᴇǫᴜᴇsᴛᴇᴅ Bʏ ☞ {}</b>

<b>‣ Tʜɪs Mᴇssᴀɢᴇ Wɪʟʟ ʙᴇ Aᴜᴛᴏ-Dᴇʟᴇᴛᴇᴅ Aғᴛᴇʀ 𝟷𝟶 Mɪɴᴜᴛᴇs.</b>
"""

    CAP_TXT = """
<b>Tʜᴇ Rᴇꜱᴜʟᴛꜱ Fᴏʀ ☞ <code>{}</code></b>

<b>Rᴇǫᴜᴇsᴛᴇᴅ Bʏ ☞ {}</b>

<u><b>Hᴇʏ Cʟɪᴄᴋ Oɴ Tʜᴇ Bᴜᴛᴛᴏɴ Bᴇʟᴏᴡ Tʜᴇ Fɪʟᴇs Yᴏᴜ Wᴀɴᴛ Aɴᴅ Sᴛᴀʀᴛ Tʜᴇ Bᴏᴛ.</b></u>
"""
