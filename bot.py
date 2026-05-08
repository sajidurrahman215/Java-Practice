import telebot

BOT_TOKEN = "8533816989:AAGZnHCXvUIjSKfS3HSt_FgFitpypx_iWPw"
GROUP_ID = -3986646042
CHANNEL_ID = -3408829451

bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(func=lambda message: message.chat.id == GROUP_ID)
def forward_message(message):
    bot.copy_message(
        chat_id=CHANNEL_ID,
        from_chat_id=message.chat.id,
        message_id=message.message_id
    )

print("Bot is running...")
bot.polling()
