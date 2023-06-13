# Oppenheimer Nos

Checks if the Oppenheimer movie is available in NOS Cinemas.

Runs every hour.

When the movie is available:
- Logs to console
- Plays a sound
- Sends a notification to Discord

# Instructions

pip install -r requirements.txt

python app.py

# Discord

Go to a text channel > settings > integrations > create webhook

Copy the webhook url and paste it in the `DISCORD_WEBHOOK_URL` variable in the `.env` file.