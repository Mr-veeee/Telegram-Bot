## Weedo Image to PDF Converter Bot

This bot allows users to convert images to PDF files.

### Usage

To use the bot, simply send an image to the bot. The bot will download the image, convert it to PDF, and send the PDF back to the user.

### Commands

The bot supports the following commands:

| Command | Description |
|---|---|
| `/start` | Sends a welcome message to the user. |

### Requirements

The bot requires the following Python libraries:

* telebot
* PIL

### Installation

To install the required libraries, run the following command in your terminal:

```
pip install telebot Pillow
```

### Running the Bot

To run the bot, save the code as a `.py` file and then run the following command in your terminal:

```
python <filename>.py
ex: bot.py
```

### Notes

* The bot will save downloaded images and generated PDFs to a temporary directory.
* The bot will delete temporary files after sending the PDF to the user.
* The bot uses the `Image` module from the PIL library to convert images to PDF.
