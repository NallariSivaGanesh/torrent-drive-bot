import os
import aria2p
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

BOT_TOKEN = os.getenv("8372510028:AAFoNK_ZD3_IbCLv4SH7d8Io_LX3ZuX76cM")
ARIA2_SECRET = os.getenv("ARIA2_SECRET", "mysecret")

# Start aria2 as a subprocess
import subprocess
subprocess.Popen(["aria2c", "--enable-rpc", "--rpc-listen-all=true",
                  f"--rpc-secret={ARIA2_SECRET}", "--dir=/tmp/downloads"])

# Connect to aria2
aria2 = aria2p.API(
    aria2p.Client(host="http://localhost", port=6800, secret=ARIA2_SECRET)
)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Send /magnet <link> to start downloading!")

async def magnet(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not context.args:
        await update.message.reply_text("Usage: /magnet <magnet-link>")
        return
    magnet_link = " ".join(context.args)
    download = aria2.add_magnet(magnet_link)
    await update.message.reply_text(f"Started: {download.name}")

def main():
    app = Application.builder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("magnet", magnet))
    app.run_polling()

if __name__ == "__main__":
    main()
