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
        await e.edit("SAYANG ARAA 💝💖💘")
        await e.edit("💝💘💓💗")
        await e.edit("💞💕💗💘")
        await e.edit("💘💞💕💗")
        await e.edit("SAYANG")
        await e.edit("ARAAAA")
        await e.edit("SELAMANYA 💕")
        await e.edit("💘💘💘💘")
        await e.edit("SAYANG")
        await e.edit("ARA")
        await e.edit("SAYANG")
        await e.edit("ARA")
        await e.edit("I LOVE YOUUUU")
        await e.edit("MY BABY")
        await e.edit("💕💞💘💝")
        await e.edit("💘💕💞💝")
        await e.edit("CINTA SEKEBON💞")


@register(outgoing=True, pattern='^.nembakara(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("`Jadi gini aku sebelumnya udah bilang itu`")
    sleep(2)
    await typew.edit("`Itu loh anu`")
    sleep(1)
    await typew.edit("`Jadi gini gw kan itu`")
    sleep(1)
    await typew.edit("`Ga tau kapan sih gw mati`")
    sleep(1)
    await typew.edit("`Maka dari itu tata kata gw jd kiasan`")
    sleep(2)
    await typew.edit("`Eh jadi udang di balik batu`")
    sleep(1)
    await typew.edit("`Trs insecure liat Arra yg cantik`")
    sleep(1)
    await typew.edit("`Trs pungguk jadi bisa terbang `")
    sleep(1)
    await typew.edit("`Buat ngejar Ara`")
    sleep(1)
    await typew.edit("`Tapi kalah sm botnya beelzebub`")
    sleep(1)
    await typew.edit("`jadi gini kenapa ikan `")
    sleep(1)
    await typew.edit("`Ngaa`")
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
    await typew.edit("`Buat Araaaa`")
    sleep(1)
    await typew.edit("`Gw naksir sm Aara`")
    sleep(1)
    await typew.edit("`Sayang Sikap Ara yg tegas`")
    sleep(1)
    await typew.edit("`Bodonya yg lucu`")
    sleep(1)
    await typew.edit("`Jangan di puji mulu y kan`")
    sleep(1)
    await typew.edit("`JADI GMN??`")
    sleep(1)
    await typew.edit("`ARA MAU GA SI?`")
    sleep(1)
    await typew.edit("`JADI PACAR DARI PEMILIK AKUN BEELZEBUB`")
    sleep(2)
    await typew.edit("`Jangan di tolak`")
    sleep(1)
    await typew.edit("`Nanti aku nangis`")
    sleep(1)
    await typew.edit("`Terserah padamu aku begini adanya`")
    sleep(2)
    await typew.edit("`Kuhormati keputusanmu`")
    sleep(1)
    await typew.edit("`Aaaaaarrrrraaaaaaa`")
    sleep(1)
    await typew.edit("`Mau ga jadi pacar yg nyusun kata kata ini??`")
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

    animation_ttl = range(0, 13)

    input_str = event.pattern_match.group(1)

    if input_str == "cinta":

        await event.edit(input_str)

        animation_chars = [
            "`Connecting Ke Server Cinta`",
            "`Mencari Server Cinta`",
            "`Menemukan server Ara`",
            "`Menghubungkan server Ara `",
            "`Mengirim Cintaku.. 0%\n▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",
            "`Mengirim Cintaku.. 4%\n█▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",
            "`Mengirim Cintaku.. 8%\n██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",
            "`Mengirim Cintaku.. 20%\n█████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",
            "`Mengirim Cintaku.. 36%\n█████████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",
            "`Mengirim Cintaku.. 52%\n█████████████▒▒▒▒▒▒▒▒▒▒▒▒ `",
            "`Mengirim Cintaku.. 84%\n█████████████████████▒▒▒▒ `",
            "`Mengirim Cintaku.. 100%\n█████████CINTAKU███████████ `",
            f"`Cinta gw Sekarang Sepenuhnya Terkirim Pada Ara,Gw Cintai Ara, ILY SEKEBON Ara💞`"]

        for i in animation_ttl:

            await asyncio.sleep(animation_interval)

            await event.edit(animation_chars[i % 11])


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
