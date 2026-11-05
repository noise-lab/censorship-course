# AI, Copyright, and Content ID

## Part 1 (in class, 20 minutes): Can the system tell?

Copyright detectors such as Content ID work by fingerprinting an upload and
comparing it to a reference. Today's content is machine-made. In pairs, with a
laptop and a phone, run three short experiments. Each has exact steps; write
down what you see.

### Experiment 1: Does the model recite? (5 minutes)

A Munich court held in 2025 that ChatGPT reciting song lyrics verbatim was a
copyright reproduction, in a suit brought by GEMA, Germany's music rights
society (the ASCAP/BMI equivalent).

1. Open two chatbots (for example [ChatGPT](https://chat.openai.com/) and
   [Claude](https://claude.ai/), or UChicago's [Phoenix](https://phoenix.uchicago.edu/)).
2. Ask each for the complete lyrics of "Let It Be" by the Beatles.
3. Ask each for the complete lyrics of "Männer" by Herbert Grönemeyer (a GEMA
   artist named in the ruling).
4. Ask each for the first paragraph of *Harry Potter and the Philosopher's
   Stone*.
5. For each answer note: recited in full, quoted a few lines, summarized, or
   refused. Is the behavior a rule about lyrics, about copyright generally, or
   about particular rightsholders?

### Experiment 2: Does the file say where it came from? (7 minutes)

C2PA "content credentials" are an industry standard for a signed record,
embedded in an image or video file, of how it was made and edited, including
whether a model generated it. Several image generators sign their output.

1. Generate an image with ChatGPT or Gemini (any prompt) and download it to
   your laptop as a file.
2. Upload the file to the verifier at
   [verify.contentauthenticity.org](https://verify.contentauthenticity.org/).
   Does it show credentials, and do they say an AI tool made it?
3. Take a screenshot of the same image and upload the screenshot. What
   happened to the credentials?
4. Upload a photo taken with your own phone. Does it carry any credentials?
5. Note: who, in practice, ends up with a provenance record, and who does not?

### Experiment 3: Does the fingerprinter recognize it? (7 minutes)

Shazam identifies music the way Content ID does: a fingerprint of the audio,
matched against a reference library of released recordings.

1. On YouTube, search for "Suno AI song" or "Udio AI song" and open a video
   that is clearly a machine-generated track.
2. Look under the video description for YouTube's "Altered or synthetic
   content" label. Is it there?
3. Play the track and run Shazam (or Google's "What's this song?") on your
   phone. Does it identify anything? If it names a real song, is that song
   actually what you heard?
4. Do the same for a well-known released song. Compare.
5. Note: the AI track may have been made by a model trained on licensed
   catalogues (the Warner and Universal deals). Who is its rightsholder, and
   what could a Content ID reference for it even be?

### Report back (one minute per pair)

The one result that surprised you, and whether it moves you toward "the
detectors can handle machine-made content" or "they were built for a world
that no longer exists."

## Part 2 (take-home, optional): what the platforms say they do

Read one platform's current policy on AI-generated content (YouTube's
[AI page](https://www.youtube.com/howyoutubeworks/ai/), Spotify's AI policy,
or Meta's AI labels) and write three sentences on what it detects, what it
asks the uploader to self-declare, and what happens when neither works.
