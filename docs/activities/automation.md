# Sentiment Analysis and Content Moderation

This activity explores how automated systems detect and moderate toxic or harmful content online. The activity was originally motivated by Google's [Perspective API](https://www.perspectiveapi.com/), which aimed to help online communities detect and filter out toxic content using machine learning. While Perspective API pioneered this space, the rise of large language models has opened new possibilities for sentiment analysis and content moderation.

## Part 1: Sentiment Analysis with Large Language Models

Large language models like ChatGPT (OpenAI), Claude (Anthropic), and others can perform sophisticated sentiment analysis and content evaluation. In this part, you'll explore how well these models can detect toxicity, hate speech, and other problematic content.

### Activity

1. Choose one or more LLMs to experiment with:
   - [ChatGPT](https://chat.openai.com/)
   - [Claude](https://claude.ai/)
   - [Phoenix AI](https://phoenix.uchicago.edu/) (UChicago's local LLM)
   - Other models like Gemini, etc.

2. Create test content that spans different categories:
   - Clear violations (explicit hate speech, threats, harassment)
   - Borderline cases (sarcasm, satire, context-dependent language)
   - Words or phrases with multiple meanings
   - Content in different languages
   - Full sentences vs. isolated phrases

3. Design prompts that ask the LLM to evaluate content. For example:
   ```
   Please evaluate the following content for toxicity, hate speech,
   threats, or harassment. Classify it as ALLOW or BLOCK and explain
   your reasoning.

   Content: [INSERT TEXT HERE]
   ```

4. Test and analyze:
   - How do results compare across different LLMs?
   - How do your results depend on how you phrase your prompt?
   - Can you identify patterns in what gets flagged vs. what doesn't?
   - How does the LLM handle context-dependent content?

### Discussion Questions

- What are the limitations of using LLMs for content moderation?
- How might bad actors try to circumvent LLM-based moderation?
- What biases might be embedded in these models' moderation decisions?

## Part 2 (Optional): Claude Content Moderation

Anthropic provides specific guidance and examples for using Claude for content moderation. This part explores Claude's capabilities in more depth.

### Activity

You can approach this in two ways:

**Option A: Web Interface (No API Key Required)**

1. Use Claude directly at [claude.ai](https://claude.ai)
2. Create systematic tests for different moderation categories
3. Compare Claude's decisions to other moderation systems you've tested

**Option B: API with Jupyter Notebook**

If you have API access (Anthropic offers free credits for students):

1. Install the required libraries:
   ```bash
   pip install anthropic jupyter notebook
   ```

2. Explore Anthropic's content moderation cookbook:
   ```bash
   git clone https://github.com/anthropics/anthropic-cookbook.git
   cd anthropic-cookbook/misc
   jupyter notebook building_moderation_filter.ipynb
   ```

3. Review Anthropic's [content moderation use case documentation](https://docs.anthropic.com/en/docs/build-with-claude/content-moderation)

### Experiments to Try

- Test batch processing of content
- Customize moderation categories for specific platforms
- Compare automated vs. manual moderation results
- Analyze how Claude handles edge cases and ambiguous content

## Part 3 (Optional): Audio Fingerprinting with Spectral Hashing

While text moderation focuses on analyzing words, audio and video content require different approaches. One common technique for audio is spectral hashing, which matches how audio "sounds" rather than comparing files bit-by-bit.

### Activity

1. Download and install [Echoprint](https://gist.github.com/predakanga/2376835), an open-source audio fingerprinting system

2. Select an MP3 file and compute its spectral fingerprint

3. Test how robust the fingerprint is to various modifications:
   - Shorten the clip (e.g., take the first 30 seconds)
   - Find a different version or remix of the same song
   - Change the volume
   - Change the speed
   - Change the pitch

### Discussion Questions

- Why is spectral hashing useful for copyright enforcement?
- What are the limitations of this approach?
- How might bad actors try to evade fingerprint detection?
- How does this compare to text-based content matching?

## Additional Resources

- [Perspective API](https://www.perspectiveapi.com/) - The original inspiration for this activity
- [Anthropic Content Moderation Guide](https://docs.anthropic.com/en/docs/build-with-claude/content-moderation)
- [OpenAI Moderation API](https://platform.openai.com/docs/guides/moderation)
