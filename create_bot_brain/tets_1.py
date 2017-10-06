import aiml
from os import listdir
from os.path import dirname, isfile

kernel = aiml.Kernel()

aiml_path = "/home/cp/Desktop/Mycroft_AIML_fallback-master/aiml"
brain_path = "/home/cp/Desktop/Mycroft_AIML_fallback-master/bot_brain.brn"
print aiml_path

if isfile(brain_path):
    kernel.bootstrap(brainFile = "bot_brain.brn")
else:
    aimls = listdir(aiml_path)
    print aimls
    for aiml in aimls:
        kernel.bootstrap(learnFiles="/home/cp/Desktop/Mycroft_AIML_fallback-master/aiml"+ "/" + aiml)
    kernel.saveBrain("bot_brain.brn")

# kernel now ready for use
while True:
    print kernel.respond(raw_input("Enter your message >> "))
