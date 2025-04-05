# Written by Ovi, 2025-04-04: Vocabulary flashcard generator that creates an Excel file from Group 2 vocabulary entries with difficulty, synonyms, and antonyms.
import pandas as pd
import os

# Create a directory for flashcards if it doesn't exist
os.makedirs('flashcards', exist_ok=True)

# Initialize lists
target_words = []
bangla_meanings = []
translations = []
parts_of_speech = []
sample_sentences = []
levels = []
synonyms = []
antonyms = []

# 1. Adulterate
target_words.append("Adulterate")
bangla_meanings.append("ভেজাল মেশানো")
translations.append("render poorer in quality by adding another substance")
parts_of_speech.append("Verb")
sample_sentences.append("The milk was found to be adulterated with water.")
levels.append("Advanced")
synonyms.append("contaminate, degrade")
antonyms.append("purify, refine")

# 2. Advocate
target_words.append("Advocate")
bangla_meanings.append("সমর্থন করা")
translations.append("publicly recommend or support")
parts_of_speech.append("Verb")
sample_sentences.append("He advocates for equal education rights.")
levels.append("Intermediate")
synonyms.append("support, recommend")
antonyms.append("oppose, protest")

# 3. Aggrandize
target_words.append("Aggrandize")
bangla_meanings.append("বড় করা, গুরুত্ব বাড়ানো")
translations.append("increase power, status, reputation of someone")
parts_of_speech.append("Verb")
sample_sentences.append("The king aggrandized his kingdom through conquest.")
levels.append("Advanced")
synonyms.append("amplify, magnify")
antonyms.append("diminish, belittle")

# 4. Alacrity
target_words.append("Alacrity")
bangla_meanings.append("উৎসাহ, আগ্রহ")
translations.append("brisk and cheerful readiness")
parts_of_speech.append("Noun")
sample_sentences.append("She accepted the invitation with alacrity.")
levels.append("Advanced")
synonyms.append("eagerness, willingness")
antonyms.append("reluctance, hesitation")

# 5. Ambivalent
target_words.append("Ambivalent")
bangla_meanings.append("দ্বৈত অনুভূতিসম্পন্ন")
translations.append("having mixed feelings or contradictory ideas")
parts_of_speech.append("Adjective")
sample_sentences.append("He was ambivalent about quitting his job.")
levels.append("Advanced")
synonyms.append("uncertain, conflicted")
antonyms.append("certain, decided")

# 6. Ameliorate
target_words.append("Ameliorate")
bangla_meanings.append("উন্নতি করা")
translations.append("make something bad better")
parts_of_speech.append("Verb")
sample_sentences.append("Steps were taken to ameliorate living conditions.")
levels.append("Advanced")
synonyms.append("improve, enhance")
antonyms.append("worsen, degrade")

# 7. Amenable
target_words.append("Amenable")
bangla_meanings.append("সহজে প্রভাবিত হয় এমন")
translations.append("open to suggestions, easily persuaded")
parts_of_speech.append("Adjective")
sample_sentences.append("She was amenable to the new proposal.")
levels.append("Advanced")
synonyms.append("compliant, agreeable")
antonyms.append("stubborn, uncooperative")

# 8. Anachronistic
target_words.append("Anachronistic")
bangla_meanings.append("কালভ্রান্তিপূর্ণ")
translations.append("belonging to a different period; old-fashioned")
parts_of_speech.append("Adjective")
sample_sentences.append("The movie’s costumes were anachronistic.")
levels.append("Advanced")
synonyms.append("outdated, antiquated")
antonyms.append("modern, current")

# 9. Audacious
target_words.append("Audacious")
bangla_meanings.append("দুঃসাহসিক")
translations.append("bold, showing impudent lack of respect")
parts_of_speech.append("Adjective")
sample_sentences.append("He made an audacious move in the debate.")
levels.append("Advanced")
synonyms.append("bold, daring")
antonyms.append("timid, cautious")

# 10. Avaricious
target_words.append("Avaricious")
bangla_meanings.append("লোভী")
translations.append("showing extreme greed for wealth")
parts_of_speech.append("Adjective")
sample_sentences.append("The avaricious businessman exploited his workers.")
levels.append("Advanced")
synonyms.append("greedy, covetous")
antonyms.append("generous, charitable")

# 11. Banal
target_words.append("Banal")
bangla_meanings.append("সাধারণ, অপ্রভাৱশালী")
translations.append("lacking in originality, obvious and boring")
parts_of_speech.append("Adjective")
sample_sentences.append("The story was full of banal clichés.")
levels.append("Advanced")
synonyms.append("trite, cliché")
antonyms.append("original, fresh")

# 12. Benign
target_words.append("Benign")
bangla_meanings.append("সৌম্য, নিরীহ")
translations.append("gentle and kind; not harmful")
parts_of_speech.append("Adjective")
sample_sentences.append("The tumor was found to be benign.")
levels.append("Intermediate")
synonyms.append("harmless, kind")
antonyms.append("malignant, harmful")

# 13. Brazen
target_words.append("Brazen")
bangla_meanings.append("লজ্জাহীন")
translations.append("bold and without shame")
parts_of_speech.append("Adjective")
sample_sentences.append("He told a brazen lie to the teacher.")
levels.append("Advanced")
synonyms.append("shameless, bold")
antonyms.append("modest, shy")

# 14. Calumny
target_words.append("Calumny")
bangla_meanings.append("অপবাদ, নিন্দা")
translations.append("false and slanderous statement")
parts_of_speech.append("Noun")
sample_sentences.append("He was the victim of a political calumny.")
levels.append("Advanced")
synonyms.append("slander, defamation")
antonyms.append("praise, compliment")

# 15. Candid
target_words.append("Candid")
bangla_meanings.append("খোলামেলা, অকপট")
translations.append("truthful and straightforward")
parts_of_speech.append("Adjective")
sample_sentences.append("She gave a candid interview.")
levels.append("Intermediate")
synonyms.append("honest, frank")
antonyms.append("deceptive, dishonest")

# 16. Castigate
target_words.append("Castigate")
bangla_meanings.append("কঠোরভাবে তিরস্কার করা")
translations.append("reprimand severely")
parts_of_speech.append("Verb")
sample_sentences.append("He was castigated for his poor performance.")
levels.append("Advanced")
synonyms.append("criticize, reprimand")
antonyms.append("praise, compliment")

# 17. Caustic
target_words.append("Caustic")
bangla_meanings.append("তিক্ত, ব্যঙ্গাত্মক")
translations.append("sarcastic in a bitter way; burning")
parts_of_speech.append("Adjective")
sample_sentences.append("His caustic remarks hurt everyone.")
levels.append("Advanced")
synonyms.append("biting, sarcastic")
antonyms.append("kind, gentle")

# 18. Construe
target_words.append("Construe")
bangla_meanings.append("বিশ্লেষণ করা, ব্যাখ্যা করা")
translations.append("interpret in a particular way")
parts_of_speech.append("Verb")
sample_sentences.append("His silence was construed as guilt.")
levels.append("Advanced")
synonyms.append("interpret, understand")
antonyms.append("misunderstand, confuse")

# 19. Contrite
target_words.append("Contrite")
bangla_meanings.append("অনুতপ্ত")
translations.append("feeling remorse for wrongdoing")
parts_of_speech.append("Adjective")
sample_sentences.append("She was contrite after the mistake.")
levels.append("Advanced")
synonyms.append("remorseful, apologetic")
antonyms.append("unrepentant, indifferent")

# 20. Convoluted
target_words.append("Convoluted")
bangla_meanings.append("জটিল, প্যাঁচানো")
translations.append("complex, twisted")
parts_of_speech.append("Adjective")
sample_sentences.append("The explanation was too convoluted to follow.")
levels.append("Advanced")
synonyms.append("complicated, intricate")
antonyms.append("simple, straightforward")

# 21. Covet
target_words.append("Covet")
bangla_meanings.append("লোভ করা")
translations.append("yearn to possess something of another")
parts_of_speech.append("Verb")
sample_sentences.append("He coveted his friend’s success.")
levels.append("Advanced")
synonyms.append("desire, crave")
antonyms.append("dislike, reject")

# 22. Craven
target_words.append("Craven")
bangla_meanings.append("কাপুরুষ, ভীতু")
translations.append("cowardly")
parts_of_speech.append("Adjective")
sample_sentences.append("The craven soldier fled the battlefield.")
levels.append("Advanced")
synonyms.append("cowardly, timid")
antonyms.append("brave, courageous")

# 23. Decorum
target_words.append("Decorum")
bangla_meanings.append("ভদ্রতা, শালীনতা")
translations.append("proper behavior and manners")
parts_of_speech.append("Noun")
sample_sentences.append("He maintained decorum during the ceremony.")
levels.append("Intermediate")
synonyms.append("propriety, politeness")
antonyms.append("rudeness, impropriety")

# 24. Deft
target_words.append("Deft")
bangla_meanings.append("দক্ষ, নিপুণ")
translations.append("demonstrating skill and cleverness")
parts_of_speech.append("Adjective")
sample_sentences.append("The pianist's deft fingers flew over the keys.")
levels.append("Intermediate")
synonyms.append("skilled, nimble")
antonyms.append("clumsy, inept")

# 25. Demur
target_words.append("Demur")
bangla_meanings.append("অসন্তোষ প্রকাশ করা")
translations.append("raise objections or show reluctance")
parts_of_speech.append("Verb")
sample_sentences.append("She demurred at the idea of working late.")
levels.append("Advanced")
synonyms.append("object, protest")
antonyms.append("accept, approve")

# 26. Derivative
target_words.append("Derivative")
bangla_meanings.append("অনুকরণমূলক")
translations.append("imitative of another's work")
parts_of_speech.append("Adjective")
sample_sentences.append("The song was dull and derivative.")
levels.append("Advanced")
synonyms.append("unoriginal, copied")
antonyms.append("innovative, original")

# 27. Desiccate
target_words.append("Desiccate")
bangla_meanings.append("শুকিয়ে ফেলা")
translations.append("cause to become completely dry")
parts_of_speech.append("Verb")
sample_sentences.append("The desert sun desiccated the plants.")
levels.append("Advanced")
synonyms.append("dry, dehydrate")
antonyms.append("moisten, hydrate")

# 28. Diatribe
target_words.append("Diatribe")
bangla_meanings.append("তীব্র সমালোচনা")
translations.append("forceful and bitter verbal attack")
parts_of_speech.append("Noun")
sample_sentences.append("He launched into a diatribe against the media.")
levels.append("Advanced")
synonyms.append("tirade, rant")
antonyms.append("praise, compliment")

# 29. Incredulous
target_words.append("Incredulous")
bangla_meanings.append("অবিশ্বাসী")
translations.append("unwilling or unable to believe something")
parts_of_speech.append("Adjective")
sample_sentences.append("She gave him an incredulous look.")
levels.append("Advanced")
synonyms.append("skeptical, doubtful")
antonyms.append("trusting, believing")

# 30. Ingenuous
target_words.append("Ingenuous")
bangla_meanings.append("সরল, সৎ, শিশুসুলভ")
translations.append("innocent, naive or unsuspecting")
parts_of_speech.append("Adjective")
sample_sentences.append("He is too ingenuous to suspect deceit.")
levels.append("Advanced")
synonyms.append("naive, innocent")
antonyms.append("deceitful, cunning")

# Create a DataFrame
df = pd.DataFrame({
    'target_word': target_words,
    'bangla_meaning': bangla_meanings,
    'translation': translations,
    'part_of_speech': parts_of_speech,
    'sample_sentence': sample_sentences,
    'level': levels,
    'synonyms': synonyms,
    'antonyms': antonyms
})

# Save to Excel
df.to_excel('flashcards/flashcards2.xlsx', index=False)

print("Excel file 'flashcards/flashcards2.xlsx' has been created successfully.")