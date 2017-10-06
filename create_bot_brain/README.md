# Mycroft chat bot fallback

uses AIML to answer on intent_failure

chatbot mode can be activated to trigger this in all utterances

single queries can also be made

test.py can be run directly to see what kind of responses the bot will give you

# video

[![AIML in action](https://img.youtube.com/vi/6gbKz2u-q8k/0.jpg)](https://www.youtube.com/watch?v=6gbKz2u-q8k)

# usage

    test chatbot with { your question }

    chatbot engage

    stop chatbot

# requires

    IntentParser
    Converse
    the new fallback system

# changing responses

On first run the AIML files will be saved to a brain file (bot_brain.brn), this makes next loading much faster, but if you change the AIML files you must delete the brain file for changes to take effect

AIML files taken from Mitsuku and Alice