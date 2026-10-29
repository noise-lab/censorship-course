# Filter Bubbles

Filter bubbles are created when algorithms personalize content for users based
on their past behavior and preferences. This can lead to users only seeing
content that is tailored to their interests, which can limit their exposure to
new ideas and perspectives. This can lead to an echo chamber effect, where
users are only exposed to content that reinforces their existing beliefs and
opinions.

In this activity, you will try to uncover evidence of filter bubbles on online
search portals (search engines, news portals, etc.).

## Part 1: Search Engines

Search engines often use algorithms to personalize search results for users.
Personalization algorithms are based on a variety of factors, including user
geography, search history, and past behavior, the collection of which
constitutes a user "profile". This profile is used to tailor search results to
a user's preferences. It may also be used to target advertising to a user.

A potential drawback of personalization is that it potentially results in
users only seeing content that match their past (or existing) interests.

Try the following experiment. You may want to work with a partner for this
exercise, as different users have different profiles and may thus see
different search results.

1. Pick a handful of search terms that you are interested in. Choose a range
   of topics, from politics, to current events, to retail, to local businesses.
   
2. Explore how search results vary across browsers. Search for these terms in
   the following search engines:
    * Google
    * DuckDuckGo
    
    What do you notice about the differences in the search results? Are there any
    differences that you find surprising? Are any aspects of Google's that you could
    imagine are tailored based on your past behavior on Google products? (Note
    that DuckDuckGo does personalize results based on your *current* profile, such
    as your geography, but does not perform tracking or history.)

3. Repeat the above experiment, but do your best to alter your profile in
   certain ways. For example, you might try one or more of the following:
    * Logged out of your Google account
    * Incognito mode
    * From Tor browser
    * Using a VPN to change your geographic location
    * From your phone

4. Repeat the above experiment (Steps 1-3) with other platforms that perform
   personalization. One idea to try would be the [Google news
   portal](https://news.google.com/). You might also try other platforms that
   perform personalization (e.g., Amazon).
   
## Part 2: Feeds

A search engine at least waits for a query. A feed (TikTok's For You page,
Instagram Reels, YouTube Shorts, the X "For You" timeline) decides what you see
with no question asked, from signals you may not know you are giving: what you
watched to the end, what you scrolled past, how long you paused. There is no
query to vary, so the thing to probe is the account itself. This part asks you
to audit the "algorithm" the way an outside researcher would: from its
outputs, with controlled inputs.

Work with a partner so you have two feeds to compare. Use your own accounts,
or a logged-out or fresh session where the platform allows it; do not engage
with content you would not want in your history.

1. **Baseline.** Each of you opens the same feed and scrolls the next 20 to 30
   items without liking, following, or watching anything to the end. Tally
   what you were shown by rough category (news, politics, sports, music,
   shopping, a hobby, and so on). How different are the two feeds already,
   and what in your histories would explain it?

2. **Intervene.** Pick one topic that is absent from your baseline and
   harmless to you (a sport you do not follow, a cooking style, a city).
   For five minutes, engage only with that topic: watch those items to the
   end, like a few, skip everything else quickly. Then scroll another 20 to
   30 items and tally again. How many items did it take for the feed to
   move? How much of the feed is now that topic?

3. **Try to get out.** Use whatever the platform offers (not interested,
   hide, clear watch history, "reset" or "refresh" the feed, switching to a
   chronological or Following view). Scroll again. Did the topic fade, and how
   quickly? This is the question the class kept coming back to: how much
   agency does a user actually have?

4. **Compare notes.** Put the two feeds side by side after the same
   intervention. Did the same five minutes move you both the same way? Then
   find what the platform says the feed optimizes for (its "how
   recommendations work" page) and compare it with what you observed. Does
   personalizing for engagement look different from personalizing to help you
   find things, and could you tell the two apart from the outside?

Keep your tallies. They are small, but they are the same kind of evidence an
audit study collects, and they show both what you can conclude from the
outside and what you cannot: you saw the outputs move, but not which signal
moved them.

## Part 3: Chatbots

Increasingly, people ask a chatbot instead of a search engine, and the chatbot
returns one synthesized answer rather than a list of links. That makes the
question from Part 1 harder to answer, not easier: there is no result page to
compare, and nothing tells you what the model left out.

Repeat the experiment with two or three assistants (ChatGPT, Claude, Gemini,
Copilot, Perplexity, or a model served from another country).

1. Reuse a few of your Part 1 queries (and, if you did Part 2, the topic you pushed your feed toward), especially the political or
   current-events ones and anything with a regional angle (an election, a
   border dispute, a local health question). Ask each model the same question,
   worded the same way.

2. Vary the vantage point the way you did for search: logged in versus out, a
   fresh session, and, if you have a VPN, the same question asked from two or
   three different countries. Try asking in a second language if you can.

3. Compare the answers side by side. Which sources does each model cite, if
   any? Does the framing change with location or language? Does one model
   decline or hedge where another answers directly? Do two sessions of the
   same model agree with each other?

Note what you can and cannot conclude. A search engine's personalization can be
measured by diffing result lists from many vantage points, which is how the
studies in the lecture work. For a chatbot, what would the equivalent
measurement even be? Think about what you would need to control, and how you
would tell personalization from randomness in the model's output.

## Part 4: Discussion

Bring your tallies from Parts 1 to 3 and work through these in your group.
Several of them came straight out of class discussion; none has a settled
answer.

**Is personalization censorship?**

1. Nothing was removed, so the access is still there. Is personalization
   then a form of friction, in the same way that throttling is, or is
   "censorship" the wrong word for it? Where would you draw the line, and
   is the line anything more than "I know it when I see it"?
2. Someone in class argued that even when you are actively looking for
   something and know what to type, personalization can keep you from
   finding it. Have you seen this? What would it take to show it with data
   rather than anecdotes?

**Looking versus being fed**

3. Two situations came apart in discussion. In the first you search for X
   and the ranking hands you Y. In the second you open a feed looking for
   nothing in particular and are handed Y anyway. Most people's first
   instinct is that the first is worse. Is it? One view is that the passive
   case is more coercive, because there was never a real choice; another is
   that it is no different from turning on the television in 1985 and
   watching whatever was on. What distinguishes a feed from that channel?
4. Does the answer change with what the feed is optimized for? Compare a
   feed tuned to maximize engagement with one tuned to help you find what
   you need and leave, or a shopping ranking tuned to what the seller most
   wants you to buy. Could you tell these apart from the outside, using only
   what Parts 1 to 3 let you observe?

**Agency: the algorithm, or us?**

5. The loop runs in both directions: you click and scroll, the system
   predicts what will hold you, shows it, and reads your reaction. Is
   "blame" even the right word? Put it instead as a question about agency:
   how much do you really have, and what in Part 2 showed you the limits of
   it?
6. Does agency depend on who the user is? A thirteen-year-old and a
   forty-year-old sit differently with respect to an engagement-optimized
   feed, and recent litigation against the major platforms turns on exactly
   that. Should the answer to "is it the algorithm or us" differ by age, and
   if so, what follows for design or for law?
7. What can an individual do, short of regulation: screen-time limits,
   chronological views, clearing history, choosing not to be on the
   platform? Which of these did Part 2 suggest actually works, and which are
   mostly symbolic?

**Transparency and regulation**

8. Personalization creates an incentive to collect more data, and every
   claim of the form "we need X to do Y safely" (age verification, for
   instance) deserves an audit. Who is in a position to audit it?
9. Should platforms be required by law to disclose how they decide what to
   show you? It is not a yes or no. Which signals they use (location, age,
   inferred religion or sexual orientation, scroll and watch history) is one
   level of disclosure; how those signals are combined is another, and is
   also the revenue-critical part. Argue it from the regulator's side, then
   from the position of an engineer at the platform who will be asked to
   open it up. Where is the reasonable middle?
10. If chatbots become the main way people look things up, does the filter
    bubble get bigger or smaller? Who could audit it, and how?
