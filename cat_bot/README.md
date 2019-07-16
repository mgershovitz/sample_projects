# cat_bot
This is a very simple implementation of a slack bot.
The cat_bot is a slack app I created for this demonstration, if you want to create your own app, 
you can do it here - https://api.slack.com/apps.

To send messages to your slack, the bot needs 2 things - a token and a channel id:
 
1. Token
    An API token is basically your way to give this bot permissions to send you\your channels messages.
    To get this token you need to install the cat_bot app in your slack, and generate a "Bot User OAuth Access Token".
    then you can take your generated token and save it locally on your computer with this command - 
        export SLACK_API_TOKEN="xxxx-xxxxxxxxxxxx-xxxxxxxxxxxx-xxxxxxxxxxxx"
        
        
2. Channel ID
    The channel id is the destination to which the bot send messages.
    Remember - with great bots comes great responsibility!
    Never use dev apps to send messages to public channels!
    
    The channel id you can use is your own user id, this creates a channel in which the bot can send you direct messages.
    To get your user id look for your member id in your slack profile, it should look something like this - ABCD012EF.
    Then you can take your channel id and save it locally on your computer with this command - 
        export SLACK_CHANNEL_ID="@ABCD012EF"

That's it, you can run the cat bot locally like any python script and watch the cat pics flow.

After you get the hang of it, you can crete your own bots to do anything from write "hello world" 
to predicting the future!