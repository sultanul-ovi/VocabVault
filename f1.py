# Written by Ovi, 2025-04-04: Vocabulary flashcard generator that creates an Excel file from vocabulary entries with difficulty, synonyms, and antonyms.
import pandas as pd
import os

# Create a directory for uploads if it doesn't exist
os.makedirs('uploads', exist_ok=True)

# Initialize lists for vocabulary flashcards
target_words = []
bangla_meanings = []
translations = []
parts_of_speech = []
sample_sentences = []
levels = []
synonyms = []
antonyms = []

# 1. Abound
target_words.append("Abound")
bangla_meanings.append("প্রচুর পরিমাণে থাকা")
translations.append("exist in large numbers or amounts")
parts_of_speech.append("Verb")
sample_sentences.append("Opportunities abound for skilled workers.")
levels.append("Intermediate")
synonyms.append("overflow, flourish")
antonyms.append("lack, fail")

# 2. Amorphous
target_words.append("Amorphous")
bangla_meanings.append("নির্দিষ্ট আকৃতি বা গঠনহীন")
translations.append("without a clearly defined shape or form")
parts_of_speech.append("Adjective")
sample_sentences.append("The cloud had an amorphous shape.")
levels.append("Advanced")
synonyms.append("shapeless, formless")
antonyms.append("defined, structured")

# 3. Austere
target_words.append("Austere")
bangla_meanings.append("কঠোর, জাঁকজমকহীন")
translations.append("strict in manner, having no comforts or luxuries")
parts_of_speech.append("Adjective")
sample_sentences.append("He lived an austere life in a small room.")
levels.append("Advanced")
synonyms.append("stern, ascetic")
antonyms.append("luxurious, lenient")

# 4. Belie
target_words.append("Belie")
bangla_meanings.append("ভুল ধারণা দেওয়া, খণ্ডন করা")
translations.append("fail to give true impression, contradict")
parts_of_speech.append("Verb")
sample_sentences.append("Her calm face belied the terror she felt.")
levels.append("Advanced")
synonyms.append("contradict, misrepresent")
antonyms.append("reveal, confirm")

# 5. Capricious
target_words.append("Capricious")
bangla_meanings.append("খামখেয়ালী, অস্থির মেজাজের")
translations.append("sudden change of mood, unpredictable")
parts_of_speech.append("Adjective")
sample_sentences.append("He is known for his capricious decisions.")
levels.append("Advanced")
synonyms.append("whimsical, fickle")
antonyms.append("stable, consistent")

# 6. Cerebral
target_words.append("Cerebral")
bangla_meanings.append("মস্তিষ্কসংক্রান্ত, বুদ্ধিবৃত্তিক")
translations.append("intellectual rather than physical")
parts_of_speech.append("Adjective")
sample_sentences.append("The novel was too cerebral for me.")
levels.append("Advanced")
synonyms.append("intellectual, brainy")
antonyms.append("emotional, instinctive")

# 7. Congenial
target_words.append("Congenial")
bangla_meanings.append("মনোমতো, উপযুক্ত")
translations.append("pleasant or agreeable")
parts_of_speech.append("Adjective")
sample_sentences.append("The café has a congenial atmosphere.")
levels.append("Intermediate")
synonyms.append("friendly, sociable")
antonyms.append("hostile, unfriendly")

# 8. Conspicuous
target_words.append("Conspicuous")
bangla_meanings.append("সহজে দৃশ্যমান, নজরকাড়া")
translations.append("clearly visible, attracting notice")
parts_of_speech.append("Adjective")
sample_sentences.append("Her red dress was conspicuous among the crowd.")
levels.append("Intermediate")
synonyms.append("noticeable, obvious")
antonyms.append("hidden, subtle")

# 9. Cursory
target_words.append("Cursory")
bangla_meanings.append("দ্রুত ও অগভীরভাবে করা")
translations.append("hasty and not thorough")
parts_of_speech.append("Adjective")
sample_sentences.append("He gave the report only a cursory glance.")
levels.append("Advanced")
synonyms.append("superficial, quick")
antonyms.append("thorough, detailed")

# 10. Daunting
target_words.append("Daunting")
bangla_meanings.append("ভীতিকর, কঠিন")
translations.append("difficult to deal with")
parts_of_speech.append("Adjective")
sample_sentences.append("The task ahead seemed daunting.")
levels.append("Intermediate")
synonyms.append("intimidating, challenging")
antonyms.append("encouraging, simple")

# 11. Deify
target_words.append("Deify")
bangla_meanings.append("দেবতা রূপে পূজা করা")
translations.append("worship as a god")
parts_of_speech.append("Verb")
sample_sentences.append("Some fans deify celebrities.")
levels.append("Advanced")
synonyms.append("worship, idolize")
antonyms.append("despise, ridicule")

# 12. Didactic
target_words.append("Didactic")
bangla_meanings.append("উপদেশমূলক, শিক্ষামূলক")
translations.append("instructive, often patronizing")
parts_of_speech.append("Adjective")
sample_sentences.append("The professor's tone was didactic.")
levels.append("Advanced")
synonyms.append("educational, instructive")
antonyms.append("uninformative, unteachable")

# 13. Disseminate
target_words.append("Disseminate")
bangla_meanings.append("ছড়িয়ে দেওয়া, প্রচার করা")
translations.append("spread widely")
parts_of_speech.append("Verb")
sample_sentences.append("The news was disseminated quickly.")
levels.append("Intermediate")
synonyms.append("distribute, circulate")
antonyms.append("gather, withhold")

# 14. Feasible
target_words.append("Feasible")
bangla_meanings.append("সম্ভবপর, বাস্তবসম্মত")
translations.append("possible to do easily")
parts_of_speech.append("Adjective")
sample_sentences.append("This plan seems quite feasible.")
levels.append("Beginner")
synonyms.append("possible, achievable")
antonyms.append("impossible, impractical")

# 15. Flout
target_words.append("Flout")
bangla_meanings.append("অগ্রাহ্য করা, উপহাস করা")
translations.append("openly disregard")
parts_of_speech.append("Verb")
sample_sentences.append("He flouted the school rules.")
levels.append("Advanced")
synonyms.append("mock, defy")
antonyms.append("respect, follow")

# 16. Homogeneous
target_words.append("Homogeneous")
bangla_meanings.append("একজাতীয়, সমগোত্রীয়")
translations.append("of the same kind")
parts_of_speech.append("Adjective")
sample_sentences.append("The population is largely homogeneous.")
levels.append("Intermediate")
synonyms.append("uniform, similar")
antonyms.append("heterogeneous, mixed")

# 17. Humdrum
target_words.append("Humdrum")
bangla_meanings.append("একঘেয়ে, বিরক্তিকর")
translations.append("lacking excitement or variety")
parts_of_speech.append("Adjective")
sample_sentences.append("The job is quite humdrum.")
levels.append("Intermediate")
synonyms.append("boring, dull")
antonyms.append("exciting, lively")

# 18. Insipid
target_words.append("Insipid")
bangla_meanings.append("নির্জীব, বিস্বাদ")
translations.append("tasteless, lacking interest")
parts_of_speech.append("Adjective")
sample_sentences.append("The soup was insipid.")
levels.append("Intermediate")
synonyms.append("bland, dull")
antonyms.append("flavorful, interesting")

# 19. Loquacious
target_words.append("Loquacious")
bangla_meanings.append("বাচাল, অতিরিক্ত কথা বলা")
translations.append("talkative")
parts_of_speech.append("Adjective")
sample_sentences.append("She's a loquacious host.")
levels.append("Advanced")
synonyms.append("chatty, talkative")
antonyms.append("taciturn, reserved")

# 20. Misanthropic
target_words.append("Misanthropic")
bangla_meanings.append("মানববিদ্বেষী")
translations.append("dislike of other people")
parts_of_speech.append("Adjective")
sample_sentences.append("He became misanthropic after years of isolation.")
levels.append("Advanced")
synonyms.append("antisocial, reclusive")
antonyms.append("sociable, friendly")

# 21. Misnomer
target_words.append("Misnomer")
bangla_meanings.append("ভুল নাম বা উপাধি")
translations.append("wrong or inaccurate name")
parts_of_speech.append("Noun")
sample_sentences.append("Calling it a 'smartphone' is a misnomer.")
levels.append("Advanced")
synonyms.append("wrong name, inaccurate term")
antonyms.append("accurate term, correct label")

# 22. Negligent
target_words.append("Negligent")
bangla_meanings.append("অবহেলাকারী")
translations.append("failing to take care")
parts_of_speech.append("Adjective")
sample_sentences.append("The company was negligent in its duties.")
levels.append("Intermediate")
synonyms.append("careless, neglectful")
antonyms.append("careful, attentive")

# 23. Obsequious
target_words.append("Obsequious")
bangla_meanings.append("অত্যন্ত বাধ্য বা চাটুকার")
translations.append("excessively obedient")
parts_of_speech.append("Adjective")
sample_sentences.append("The waiter was annoyingly obsequious.")
levels.append("Advanced")
synonyms.append("servile, submissive")
antonyms.append("assertive, defiant")

# 24. Placate
target_words.append("Placate")
bangla_meanings.append("শান্ত করা")
translations.append("make less angry")
parts_of_speech.append("Verb")
sample_sentences.append("He tried to placate the angry customer.")
levels.append("Intermediate")
synonyms.append("calm, appease")
antonyms.append("provoke, irritate")

# 25. Proclivity
target_words.append("Proclivity")
bangla_meanings.append("ঝোঁক, প্রবণতা")
translations.append("a tendency to do something regularly")
parts_of_speech.append("Noun")
sample_sentences.append("He has a proclivity for exaggeration.")
levels.append("Advanced")
synonyms.append("tendency, inclination")
antonyms.append("aversion, disinclination")

# 26. Puerile
target_words.append("Puerile")
bangla_meanings.append("শিশুসুলভ, ছেলেমানুষি")
translations.append("childishly silly")
parts_of_speech.append("Adjective")
sample_sentences.append("That was a puerile remark.")
levels.append("Advanced")
synonyms.append("childish, immature")
antonyms.append("mature, wise")

# 27. Quixotic
target_words.append("Quixotic")
bangla_meanings.append("অত্যন্ত আদর্শবাদী ও অবাস্তব")
translations.append("extremely idealistic, impractical")
parts_of_speech.append("Adjective")
sample_sentences.append("His quixotic dreams never came true.")
levels.append("Advanced")
synonyms.append("idealistic, unrealistic")
antonyms.append("pragmatic, realistic")

# 28. Spendthrift
target_words.append("Spendthrift")
bangla_meanings.append("অপচয়কারী ব্যক্তি")
translations.append("spends money irresponsibly")
parts_of_speech.append("Noun")
sample_sentences.append("He's a notorious spendthrift.")
levels.append("Intermediate")
synonyms.append("waster, prodigal")
antonyms.append("saver, frugal")

# 29. Taciturn
target_words.append("Taciturn")
bangla_meanings.append("স্বল্পভাষী")
translations.append("saying little")
parts_of_speech.append("Adjective")
sample_sentences.append("The old man was taciturn.")
levels.append("Advanced")
synonyms.append("reserved, silent")
antonyms.append("talkative, loquacious")

# 30. Wary
target_words.append("Wary")
bangla_meanings.append("সাবধান, সতর্ক")
translations.append("cautious")
parts_of_speech.append("Adjective")
sample_sentences.append("She was wary of strangers.")
levels.append("Intermediate")
synonyms.append("cautious, alert")
antonyms.append("careless, reckless")

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


df.to_excel('flashcards/flashcards1.xlsx', index=False)

print("Excel file 'uploads/vocabulary_flashcards.xlsx' has been created successfully.")