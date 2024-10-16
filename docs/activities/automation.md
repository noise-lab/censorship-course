# Automated Content Moderation

Platforms often use some type of automation to perform content moderation. In
the realm of copyright, one way of moderating content is to use some type of
matching algorithm, such as matching a hash or fingerprint of the content
against a known databased of infringing content. There are different ways of
performing these types of matches. 

## Sentiment Analysis: Perspectives

The [Perspective API](https://www.perspectiveapi.com/) aims to help online
communities detect and filter out toxic content. It is a machine learning
model that can be used to score the likelihood that a comment is toxic. The
model is trained on a variety of data sources, including Wikipedia talk page
comments, and is able to distinguish between different types of toxicity, such
as threats, obscenity, and identity-based hate.

1. Download and install the Perspectives library and try it on various text
   input. Here are some [instructions for getting started](https://developers.perspectiveapi.com/s/docs-get-started?language=en_US). 
   You can also try the API directly from the website.
2. You might try its effectiveness on the following:
    - Full sentences vs. phrases
    - Words or phrases with two meanings
    - Phrases in foreign languages

## Sentiment Analysis: Large Language Models

The Perspective API is just one example of a sentiment analysis tool. There
are many other tools and libraries that can be used to perform sentiment
analysis. More recently, the advent of OpenAI's GPT-3 has opened up new
possibilities for sentiment analysis. GPT-3 is a large language model that can
be used to perform a variety of natural language processing tasks.

Try asking ChatGPT or Claude to perform sentiment analysis on the same set of phrases
that you used with the Perspective API. 

* How do the results compare? 
* How do your results depend on how you prompt ChatGPT?

As a follow-up activity, you could input a platform's content moderation
policy into an LLM, and subsequently input other types of content into the LLM
to see how it might be classified.

## Bonus Activity: Spectral Hashing

One approach used for audio is to perform a so-called spectral or
frequency-based, which does not match the content bit-by-bit, but rather
matches how the audio "sounds", by matching frequencies and beats through
spectral analysis.

In this part of the hands-on assignment, you can download or compile the
Echoprint code and perform some spectral hashes on audio files. 

1. Download and install the Echoprint code. [Setup
   instructions.](https://gist.github.com/predakanga/2376835)
2. Select an mp3 file and compute the spectral fingerprint for that audio.
3. Try various modifications to see if Echoprint's fingerprint is affected:
    - Shorten the clip (e.g., take the first 30 seconds)
    - Find a different version of the same song
4. More generally, you could try more complex manipulations, including:
    - Change the volume of the audio
    - Change the speed of the audio
    - Change the pitch of the audio
