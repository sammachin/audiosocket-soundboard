# audiosocket-soundboard

Demo app for playing audio files into a call via the websocket interface.

There are a selection of movie quotes in the /audio directory as L-PCM16 16kHz Wav files.

The server offers up 2 websocket interfaces one for the nexmo voice connection and one for the browser to control via.

To run this app you will need:
A Nexmo Voice Application.
A Nexmo Phone Number (LVN) linked to the application
A Server (local machine with ngrok is fine)

Configure the Nexmo App to point its answerURL to the host where you are running the server `/ncco` (eg http://example.com/ncco) and the event url to the same host at `/event`

Put the HOST and LVN parameters into server.py at the top.

install the requirements.txt using `pip install -r requirements.txt`

Run the server with `python ./server.py`

Goto http://[HOSTNAME] and you should get the control page, call your number and you should get a short TTS prompt then be connected to the websocket, clicking the buttons will play the audio files to the callers
