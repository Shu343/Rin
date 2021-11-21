
__lang__ = "🇺🇸 English"

en = {

        "help_text": """
*All helpable commands are here*
""",


        "welcome_help": """
Welcome/bid farewell to members in your group with the help of this module!

*Admin only:*
 - /welcome <on/off>: enable/disable welcome messages.
 - /welcome: shows current welcome settings.
 - /welcome noformat: shows current welcome settings, without the formatting - useful to recycle your welcome messages!
 - /goodbye -> same usage and args as /welcome.
 - /setwelcome <sometext>: set a custom welcome message. If used replying to media, uses that media.
 - /setgoodbye <sometext>: set a custom goodbye message. If used replying to media, uses that media.
 - /resetwelcome: reset to the default welcome message.
 - /resetgoodbye: reset to the default goodbye message.
 - /cleanwelcome <on/off>: On new member, try to delete the previous welcome message to avoid spamming the chat.
 - /wlcmutehelp: gives information about welcome mutes.

 - /welcomehelp: view more formatting information for custom welcome/goodbye messages.
""",

       "warns_help": """
- /warns <userhandle>: get a user's number, and reason, of warnings.
 - /warnlist: list of all current warning filters

*Admin only:*
 - /warn <userhandle>: warn a user. After 3 warns, the user will be banned from the group. Can also be used as a reply.
 - /unwarn <userhandle>: remove the last warning of the user. Can also be used as a reply.
 - /rmwarn <userhandle>: same as /unwarn.
 - /resetwarn <userhandle>: reset the warnings for a user. Can also be used as a reply.
 - /addwarn <keyword> <reply message>: set a warning filter on a certain keyword. If you want your keyword to \
be a sentence, encompass it with quotes, as such: `/addwarn "very angry" This is an angry user`. 
 - /nowarn <keyword>: stop a warning filter
 - /warnlimit <num>: set the warning limit
 - /strongwarn <on/yes/off/no>: If set to on, exceeding the warn limit will result in a ban. Else, will just kick.
""",

       "userinfo_help": """
 - /setbio <text>: while replying, will save another user's bio
 - /bio: will get your or another user's bio. This cannot be set by yourself.
 - /setme <text>: will set your info
 - /me: will get your or another user's info

 - /afk <reason>: mark yourself as AFK.
 - brb <reason>: same as the afk command - but not a command.

When marked as AFK, any mentions will be replied to with a message to say you're not available!
""",

}
