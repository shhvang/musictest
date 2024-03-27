ADMINC = """<b><u>Admin Commands -</b></u>
Use prefix c before commands to use them for channels

/pause - pause the track
/resume - resume the track
/skip - skip to the next track
/skip <number> - skip to the particular track in queue
/end ᴏʀ /stop - clears the queue and ends the stream
/player - get an interactive player panel
/queue - shows the track queue
"""

AUTHC = """
<b><u>Auth Users -</b></u>

Authorized users can mimic admin commands, they don't need to be chat admin.

/auth [username/userid] - authorize a user
/unauth [ᴜsᴇʀɴᴀᴍᴇ/ᴜsᴇʀ_ɪᴅ] - (un)authorize a user
/authusers - shows the list of authorized users 
"""

BROADC = """
<u><b>Broadcast Feature</b></u> -

/broadcast [Message or reply to a Message] - Broadcast a message to served chats of the bot.

<u>Broadcasting Modes -</u>
<b>- pin</b> - pins your broadcasted message in served chats
<b>- pinloud</b> - pins the message with notification 
<b>- user</b> - broadcasts the message to users who have started the bot
<b>- assistant</b> - broadcast your message from the assistant account of the bot
<b>- nobot</b> - forces the bot to not broadcast the message

<b>Example-</b> <code>/broadcast -user -assistant -pin Testing Broadcast</code>
"""

BLCC = """<u><b>Chat Blacklist Feature -</b></u> -

Restricting selected chats (if required) from using our bot.

/blacklistchat [Chat ID] - Blacklist a chat
/whitelistchat [Chat ID] - Whitelist a chat 
/blacklistedchat - Shows the list of blacklisted chats
"""

BLUC = """
<u><b>Block Users -</b></u> -

Restricting selected users (if required) from using the bot and its functions.

/block [username] - block a user
/unblock [username] - unblock a user
/blockedusers - Shows the list of blocked users
"""

CPLAYC = """
<u><b>Channel Play Commands -</b></u>

You can stream audio/video in a channel.

/cplay - Plays the requested track in Channel's VC.
/cvplay - Streams the requested video track in Channel's VC 
/cplayforce or /cvplayforce - Stops the ongoing stream and plays the requested track

/channelplay [Chat Username] or [Disable] - Connect channel to a group and start playing tracks from the group.
"""

GBANC = """
<u><b>Global Ban Feature -</b></u> -

/gban [username] - globally bans the user from using the bot
/ungban [username] - globally unbans the user
/gbannedusers - Shows the current list of <b>Globally Banned Users</b>
"""

LOOPC = """
<b><u>Loop Stream -</b></u>

<b>Starts streaming the ongoing stream on loop.</b>

/loop [enable/disable] - Enable/disable loop in your chat
/loop [1, 2, 3, ...] - Enables the loop (n) number of times
"""

MAINC = """
<u><b>Maintenance Mode -</b></u> -

/logs - Get logs of the bot
/logger [enable/disable] - Bot will start logging the activities happening with the bot
/maintenance [enable/disable] - enable/disable maintenance mode
"""

PINGC = """
<b><u>Ping / Stats -</b></u>

/start - Starts the bot
/help - Get help with explanation of commands
/ping - Ping the bot
/stats - Shows the stats of the bot
"""

PLAYC = """
<u><b>Play Commands -</b></u>

<b>v -</b> Stands for Video Play
<b>force -</b> Stands for Force Play

/play or /vplay - Starts streaming the requested track in VC
/playforce or /vplayforce - Stops the ongoing stream and plays the requested track in VC
"""

SHUFFLEC = """
<b><u>Shuffle / Queue -</b></u>

/shuffle - Shuffle the queue
/queue - Shows the queue
"""

SEEKC = """
<b><u>Seek Stream -</b></u>

/seek [Duration in Seconds] - Seek the stream to the desired duration 
/seekback [Duration in Seconds] - Seekback the stream to the desired duration 
"""

SONGC = """
<b><u>Song Download -</b></u>

/song [song name/yt url] - Download any track from youtube in mp3/mp4 format
"""

SPEEDC = """
<b><u>Speed Commands -</b></u>

You can control the playback speed of the ongoing stream [Admins Only].

/speed or /playback - For adjusting the audio playback speed in group
/cspeed or /cplayback - For adjusting the audio playback speed in channel
"""