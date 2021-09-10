from time import sleep
from userbot import CMD_HELP, bot
from userbot.events import register
from telethon import events
import asyncio


@register(outgoing=True, pattern="^.sayang$")
async def koc(e):
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        await e.edit("I LOVEE YOUUU 💕")
        await e.edit("💝💘💓💗")
        await e.edit("💞💕💗💘")
        await e.edit("💝💘💓💗")
        await e.edit("💞💕💗💘")
        await e.edit("💘💞💗💕")
        await e.edit("💘💞💕💗")
        await e.edit("SAYANG Bila 💝💖💘")
        await e.edit("💝💘💓💗")
        await e.edit("💞💕💗💘")
        await e.edit("💘💞💕💗")
        await e.edit("SAYANG")
        await e.edit("Salsabila")
        await e.edit("SELAMANYA 💕")
        await e.edit("💘💘💘💘")
        await e.edit("SAYANG")
        await e.edit("Mamah")
        await e.edit("SAYANG")
        await e.edit("SASA")
        await e.edit("I LOVE YOUUUU")
        await e.edit("MY SASA")
        await e.edit("💕💞💘💝")
        await e.edit("💘💕💞💝")
        await e.edit("CINTA SEKRESEK💞")


@register(outgoing=True, pattern='^.nembasasa(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("`Jadi gini sa`")
    sleep(2)
    await typew.edit("`Itu loh anu`")
    sleep(2)
    await typew.edit("`Jadi gini gw kan itu`")
    sleep(1)
    await typew.edit("`Ga tau kapan sih gw mati`")
    sleep(2)
    await typew.edit("`Jadi gw mo ngetik`")
    sleep(2)
    await typew.edit("`Eh jadi udang di balik batu`")
    sleep(2)
    await typew.edit("`Trs malas ku tengok korang`")
    sleep(2)
    await typew.edit("`Trs pungguk jadi bisa terbang `")
    sleep(2)
    await typew.edit("`Buat timpuk korang`")
    sleep(2)
    await typew.edit("`Tapi kalah sm jago sm gw`")
    sleep(1)
    await typew.edit("`jadi gini kenapa ikan `")
    sleep(1)
    await typew.edit("`Ngaa gtu sii`")
    sleep(1)
    await typew.edit("`Jay ini sadar diri sebenernya`")
    sleep(1)
    await typew.edit("`Udah kurang Gd Luking`")
    sleep(1)
    await typew.edit("`Rekening gw pas pasan`")
    sleep(1)
    await typew.edit("`Fisik tinggi dikit`")
    sleep(1)
    await typew.edit("`Hobi motoran`")
    sleep(1)
    await typew.edit("`Mageran`")
    sleep(1)
    await typew.edit("`Tapi pemalas adalah orang`")
    sleep(1)
    await typew.edit("`tercepat mengerjakan tugas`")
    sleep(1)
    await typew.edit("`ko blibet knp siii`")
    sleep(1)
    await typew.edit("`Buat Salsa`")
    sleep(1)
    await typew.edit("`Gw nyaman`")
    sleep(1)
    await typew.edit("`Sayang Sikap bila yg tegas`")
    sleep(1)
    await typew.edit("`Khilafnya yg lucu`")
    sleep(1)
    await typew.edit("`Jangan di puji mulu y kan`")
    sleep(1)
    await typew.edit("`JADI GMN??`")
    sleep(1)
    await typew.edit("`SASA MAU GA SI?`")
    sleep(1)
    await typew.edit("`Jd Pacar dr Jay`")
    sleep(2)
    await typew.edit("`Harus diterima`")
    sleep(1)
    await typew.edit("`Klo ditolak ya uda si`")
    sleep(1)
    await typew.edit("`Terserah padamu aku begini adanya`")
    sleep(2)
    await typew.edit("`Kuhormati keputusanmu`")
    sleep(1)
    await typew.edit("`Salsabila`")
    sleep(1)
    await typew.edit("`Mau ga jadi Pacar gw??`")
    sleep(2)
    await typew.edit("`Mau yaaaaaa??`")
    sleep(1)
    await typew.edit("`??????`")
    sleep(3)
    await typew.edit("`Sedang menuggu jawaban`")
    sleep(2)
    await typew.edit("`Sedang menuggu jawabann`")
    sleep(2)
    await typew.edit("`Sedang menuggu jawabann.`")
    sleep(2)
    await typew.edit("`Sedang menuggu jawabann..`")
    sleep(2)
    await typew.edit("`Sedang menuggu jawabann...`")
    sleep(2)
    await typew.edit("`Maaf anda terlalu alay dan jelek`")
    sleep(2)
    await typew.edit("`Selamat ANDA TERTOLAK SECARA HALUS`")


@register(outgoing=True, pattern="^.mf$")
async def koc(e):
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        await e.edit("`mf g dl` **ミ(ノ;_ _)ノ=3** ")


@bot.on(events.NewMessage(pattern=r"\.(.*)", outgoing=True))
async def _(event):

    if event.fwd_from:

        return

    animation_interval = 2

    animation_ttl = range(0, 15)

    input_str = event.pattern_match.group(1)

    if input_str == "cinta":

        await event.edit(input_str)

        animation_chars = [
            "`Connecting Ke Server Cinta`",
            "`Mencari Server Cinta`",
            "`Menemukan server Sabil`",
            "`Menghubungkan server Sasa `",
            "`Mengirim Cintaku.. 0%\n▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",
            "`Mengirim Cintaku.. 4%\n█▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",
            "`Mengirim Cintaku.. 8%\n██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",
            "`Mengirim Cintaku.. 20%\n█████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",
            "`Mengirim Cintaku.. 36%\n█████████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",
            "`Mengirim Cintaku.. 52%\n█████████████▒▒▒▒▒▒▒▒▒▒▒▒ `",
            "`Mengirim Cintaku.. 84%\n█████████████████████▒▒▒▒ `",
            "`Mengirim Cintaku.. 100%\n█████████CINTAKU███████████ `",
            "`Reported `",
            "``Cinta gw sepenuhnya buat Sasa,Gw Cintai Sasa,Gw janji ga bakal niggalin Sasa tanpa alasan jelas `",
            f" ILY SEKEBON SA💞`"]

        for i in animation_ttl:

            await asyncio.sleep(animation_interval)

            await event.edit(animation_chars[i % 15])


@register(outgoing=True, pattern='^.yatim(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(1)
    await typew.edit("`Hai Anak Kontol 🙈, Jangan Lupa Makan Yaa`")
    sleep(1)
    await typew.edit("`Jangan Bilang Lu Ga Dikasih Makan Sama Ortu 😁`")
    sleep(1)
    await typew.edit("`APA PERLU GUA SANTUNIN ?? 🙈🙈 xixixi`")
    sleep(1)
    await typew.edit("`OH IYAA LUPAAA, LU KAN BEBAN KELUARGA 🤣`")
    sleep(1)
    await typew.edit("`MANA MUNGKIN ORTU LU PEDULII xixixi 🙈`")
    sleep(1)
    await typew.edit("`KETAWA DULU BOLEH KALI YAA 😁`")
    sleep(1)
    await typew.edit("`HAHAHAHAHAHAHA`")
    sleep(1)
    await typew.edit("`KASIAN ORTUNYAA GAPEDULIII 🙈🤣`")
    sleep(1)
    await typew.edit("`MAAF YA, CANDAA BEBANNNN xixixi 🙈`")
    sleep(1)
    await typew.edit("`Tapi Bo'ong Hiyahiyahiya`")
# Create by myself @localheart

CMD_HELP.update({
    "animasi4":
    "𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `.gabut` atau `.dino`\
    \n↳ : Dikala gabut, yaaa pake aja xixixi.\
    \n\n𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `.yatim`\
    \n↳ : Buat bercandaan, kalo gasuka jangan dipake.\
    \n\n𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `.cinta`\
    \n↳ : Mengirim cinta tai anjiing ke seseorang.\
    \n\n𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `.sayang`\
    \n↳ : Berubah menjadi kadal.\
    \n\n𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `.sangean`\
    \n↳ : Kasih aja buat orang yang sangean."
})
