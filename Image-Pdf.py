import telebot
import os
from PIL import Image

# Replace YOUR_TOKEN with your actual bot token from BotFather
bot = telebot.TeleBot('5548949558:AAE4up5JKhZ5gQ31JTK-8YarFP6eoXmzwAA')

# This function converts the image to PDF
def convert_to_pdf(image_path):
    image = Image.open(image_path)
    pdf_path = os.path.splitext(image_path)[0] + '.pdf'
    image.save(pdf_path, 'PDF', resolution=100.0)
    return pdf_path

# This function handles the /start command
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, 'Welcome to the Weedo image to PDF converter bot! Send me an image and I will convert it to a PDF for you.')

# This function handles the image messages
@bot.message_handler(content_types=['photo'])
def handle_image(message):
    # Download the image
    file_info = bot.get_file(message.photo[-1].file_id)
    downloaded_file = bot.download_file(file_info.file_path)
    # Save the image to a file
    image_path = 'image.jpg'
    with open(image_path, 'wb') as new_file:
        new_file.write(downloaded_file)
    # Convert the image to PDF
    pdf_path = convert_to_pdf(image_path)
    # Send the PDF back to the user
    with open(pdf_path, 'rb') as pdf_file:
        bot.send_document(message.chat.id, pdf_file)
    # Delete the temporary files
    os.remove(image_path)
    os.remove(pdf_path)

# Start the bot
bot.polling()
v
