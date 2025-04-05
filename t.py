# Written by Ovi, 2025-04-04: Vocabulary flashcard generator that creates an Excel file from vocabulary entries.
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

# 2. Amorphous
target_words.append("Amorphous")
bangla_meanings.append("নির্দিষ্ট আকৃতি বা গঠনহীন")
translations.append("without a clearly defined shape or form")
parts_of_speech.append("Adjective")
sample_sentences.append("The cloud had an amorphous shape.")

# 3. Austere
target_words.append("Austere")
bangla_meanings.append("কঠোর, জাঁকজমকহীন")
translations.append("strict in manner, having no comforts or luxuries")
parts_of_speech.append("Adjective")
sample_sentences.append("He lived an austere life in a small room.")

# 4. Belie
target_words.append("Belie")
bangla_meanings.append("ভুল ধারণা দেওয়া, খণ্ডন করা")
translations.append("fail to give true impression, contradict")
parts_of_speech.append("Verb")
sample_sentences.append("Her calm face belied the terror she felt.")

# 5. Capricious
target_words.append("Capricious")
bangla_meanings.append("খামখেয়ালী, অস্থির মেজাজের")
translations.append("sudden change of mood, unpredictable")
parts_of_speech.append("Adjective")
sample_sentences.append("He is known for his capricious decisions.")

# 6. Cerebral
target_words.append("Cerebral")
bangla_meanings.append("মস্তিষ্কসংক্রান্ত, বুদ্ধিবৃত্তিক")
translations.append("intellectual rather than physical")
parts_of_speech.append("Adjective")
sample_sentences.append("The novel was too cerebral for me.")

# 7. Congenial
target_words.append("Congenial")
bangla_meanings.append("মনোমতো, উপযুক্ত")
translations.append("pleasant or agreeable")
parts_of_speech.append("Adjective")
sample_sentences.append("The café has a congenial atmosphere.")

# 8. Conspicuous
target_words.append("Conspicuous")
bangla_meanings.append("সহজে দৃশ্যমান, নজরকাড়া")
translations.append("clearly visible, attracting notice")
parts_of_speech.append("Adjective")
sample_sentences.append("Her red dress was conspicuous among the crowd.")

# 9. Cursory
target_words.append("Cursory")
bangla_meanings.append("দ্রুত ও অগভীরভাবে করা")
translations.append("hasty and not thorough")
parts_of_speech.append("Adjective")
sample_sentences.append("He gave the report only a cursory glance.")

# 10. Daunting
target_words.append("Daunting")
bangla_meanings.append("ভীতিকর, কঠিন")
translations.append("difficult to deal with")
parts_of_speech.append("Adjective")
sample_sentences.append("The task ahead seemed daunting.")

# 11. Deify
target_words.append("Deify")
bangla_meanings.append("দেবতা রূপে পূজা করা")
translations.append("worship as a god")
parts_of_speech.append("Verb")
sample_sentences.append("Some fans deify celebrities.")

# 12. Didactic
target_words.append("Didactic")
bangla_meanings.append("উপদেশমূলক, শিক্ষামূলক")
translations.append("instructive, often patronizing")
parts_of_speech.append("Adjective")
sample_sentences.append("The professor's tone was didactic.")

# 13. Disseminate
target_words.append("Disseminate")
bangla_meanings.append("ছড়িয়ে দেওয়া, প্রচার করা")
translations.append("spread widely")
parts_of_speech.append("Verb")
sample_sentences.append("The news was disseminated quickly.")

# 14. Feasible
target_words.append("Feasible")
bangla_meanings.append("সম্ভবপর, বাস্তবসম্মত")
translations.append("possible to do easily")
parts_of_speech.append("Adjective")
sample_sentences.append("This plan seems quite feasible.")

# 15. Flout
target_words.append("Flout")
bangla_meanings.append("অগ্রাহ্য করা, উপহাস করা")
translations.append("openly disregard")
parts_of_speech.append("Verb")
sample_sentences.append("He flouted the school rules.")

# 16. Homogeneous
target_words.append("Homogeneous")
bangla_meanings.append("একজাতীয়, সমগোত্রীয়")
translations.append("of the same kind")
parts_of_speech.append("Adjective")
sample_sentences.append("The population is largely homogeneous.")

# 17. Humdrum
target_words.append("Humdrum")
bangla_meanings.append("একঘেয়ে, বিরক্তিকর")
translations.append("lacking excitement")
parts_of_speech.append("Adjective")
sample_sentences.append("The job is quite humdrum.")

# 18. Insipid
target_words.append("Insipid")
bangla_meanings.append("নির্জীব, বিস্বাদ")
translations.append("tasteless, lacking interest")
parts_of_speech.append("Adjective")
sample_sentences.append("The soup was insipid.")

# 19. Loquacious
target_words.append("Loquacious")
bangla_meanings.append("বাচাল, অতিরিক্ত কথা বলা")
translations.append("talkative")
parts_of_speech.append("Adjective")
sample_sentences.append("She's a loquacious host.")

# 20. Misanthropic
target_words.append("Misanthropic")
bangla_meanings.append("মানববিদ্বেষী")
translations.append("dislike of other people")
parts_of_speech.append("Adjective")
sample_sentences.append("He became misanthropic after years of isolation.")

# 21. Misnomer
target_words.append("Misnomer")
bangla_meanings.append("ভুল নাম বা উপাধি")
translations.append("wrong or inaccurate name")
parts_of_speech.append("Noun")
sample_sentences.append("Calling it a \"smartphone\" is a misnomer.")

# 22. Negligent
target_words.append("Negligent")
bangla_meanings.append("অবহেলাকারী")
translations.append("failing to take care")
parts_of_speech.append("Adjective")
sample_sentences.append("The company was negligent in its duties.")

# 23. Obsequious
target_words.append("Obsequious")
bangla_meanings.append("অত্যন্ত বাধ্য বা চাটুকার")
translations.append("excessively obedient")
parts_of_speech.append("Adjective")
sample_sentences.append("The waiter was annoyingly obsequious.")

# 24. Placate
target_words.append("Placate")
bangla_meanings.append("শান্ত করা")
translations.append("make less angry")
parts_of_speech.append("Verb")
sample_sentences.append("He tried to placate the angry customer.")

# 25. Proclivity
target_words.append("Proclivity")
bangla_meanings.append("ঝোঁক, প্রবণতা")
translations.append("a tendency to do something regularly")
parts_of_speech.append("Noun")
sample_sentences.append("He has a proclivity for exaggeration.")

# 26. Puerile
target_words.append("Puerile")
bangla_meanings.append("শিশুসুলভ, ছেলেমানুষি")
translations.append("childishly silly")
parts_of_speech.append("Adjective")
sample_sentences.append("That was a puerile remark.")

# 27. Quixotic
target_words.append("Quixotic")
bangla_meanings.append("অত্যন্ত আদর্শবাদী ও অবাস্তব")
translations.append("extremely idealistic, impractical")
parts_of_speech.append("Adjective")
sample_sentences.append("His quixotic dreams never came true.")

# 28. Spendthrift
target_words.append("Spendthrift")
bangla_meanings.append("অপচয়কারী ব্যক্তি")
translations.append("spends money irresponsibly")
parts_of_speech.append("Noun")
sample_sentences.append("He's a notorious spendthrift.")

# 29. Taciturn
target_words.append("Taciturn")
bangla_meanings.append("স্বল্পভাষী")
translations.append("saying little")
parts_of_speech.append("Adjective")
sample_sentences.append("The old man was taciturn.")

# 30. Wary
target_words.append("Wary")
bangla_meanings.append("সাবধান, সতর্ক")
translations.append("cautious")
parts_of_speech.append("Adjective")
sample_sentences.append("She was wary of strangers.")

# Create a DataFrame
df = pd.DataFrame({
    'target_word': target_words,
    'bangla_meaning': bangla_meanings,
    'translation': translations,
    'part_of_speech': parts_of_speech,
    'sample_sentence': sample_sentences
})

# Save to Excel in the uploads directory
df.to_excel('uploads/vocabulary_flashcards.xlsx', index=False)

print("Excel file 'uploads/vocabulary_flashcards.xlsx' has been created successfully.")