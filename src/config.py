if not __name__.endswith("config"):
    import sys

    print(
        "The README is there to be read. Extend this sample config to a config file, don't just rename and change "
        "values here. Doing that WILL backfire on you.\nBot quitting.",
        file=sys.stderr,
    )
    quit(1)


# Create a new config.py file in same dir and import, then extend this class.
class Config(object):
    LOGGER = True

    # REQUIRED
    API_KEY = '5164091383:AAEgA7Euk646V1521-WkDEW1sQ2gdXNgH4Y' 
    API_ID = "9124164"
    API_HASH = "e922c979399634e27463ae08f06bc84a"
    OWNER_ID = "1725431624"  # If you dont know, run the bot and do /id in your private chat with it
    OWNER_USERNAME = "Its_shu3"

    # RECOMMENDED
    SQLALCHEMY_DATABASE_URI = "postgres://fotbot_user:D3TG0wnGIPM2EvJaGQoFVuJzBAxBhQpO@oregon-postgres.render.com/fotbot"   #needed for any database modules
    MESSAGE_DUMP = None  # needed to make sure 'save from' messages persist
    LOAD = []
    # sed has been disabled after the discovery that certain long-running sed commands maxed out cpu usage
    # and killed the bot. Be careful re-enabling it!
    NO_LOAD = ["translation", "rss", "sed"]
    WEBHOOK = False
    URL = None

    # OPTIONAL
    SUDO_USERS = (
        []
    )  # List of id's (not usernames) for users which have sudo access to the bot.
    SUPPORT_USERS = (
        []
    )  # List of id's (not usernames) for users which are allowed to gban, but can also be banned.
    WHITELIST_USERS = (
        []
    )  # List of id's (not usernames) for users which WONT be banned/kicked by the bot.
    DONATION_LINK = None  # EG, paypal
    CERT_PATH = None
    PORT = 5000
    DEL_CMDS = False  # Whether or not you should delete "blue text must click" commands
    STRICT_GBAN = False
    WORKERS = 8  # Number of subthreads to use. This is the recommended amount - see for yourself what works best!
    BAN_STICKER = "CAADAgADOwADPPEcAXkko5EB3YGYAg"  # banhammer marie sticker
    ALLOW_EXCL = False  # Allow ! commands as well as /
    LASTFM_API_KEY = ''
    WALL_API = ''
    MOE_API = ''
    AI_API_KEY = ''
    SPAMWATCH_API = 'lD5CQ2pCJGYfoHWNVv6G4NWjZk3SzPVI10u7wFePh5FhUs1y4QNId2UnCbwnL4j~'

class Production(Config):
    LOGGER = False


class Development(Config):
    LOGGER = True
