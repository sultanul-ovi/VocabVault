# Written by Ovi, 2025-04-04: Vocabulary flashcard generator that creates an Excel file from Group 3 vocabulary entries with difficulty, synonyms, and antonyms.
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

# 1. Abate
target_words.append("Abate")
bangla_meanings.append("প্রচণ্ডতা বা তীব্রতা হ্রাস পাওয়া")
translations.append("become less intense or widespread")
parts_of_speech.append("Verb")
sample_sentences.append("The storm suddenly abated.")
levels.append("Intermediate")
synonyms.append("diminish, subside")
antonyms.append("intensify, escalate")

# 2. Abjure
target_words.append("Abjure")
bangla_meanings.append("শপথপূর্বক পরিত্যাগ করা")
translations.append("solemnly renounce a belief or claim")
parts_of_speech.append("Verb")
sample_sentences.append("He abjured his former beliefs.")
levels.append("Advanced")
synonyms.append("renounce, reject")
antonyms.append("embrace, accept")

# 3. Anomalous
target_words.append("Anomalous")
bangla_meanings.append("ব্যতিক্রমী, অস্বাভাবিক")
translations.append("deviating from what is standard")
parts_of_speech.append("Adjective")
sample_sentences.append("Scientists found an anomalous result.")
levels.append("Advanced")
synonyms.append("abnormal, irregular")
antonyms.append("normal, typical")

# 4. Antipathy
target_words.append("Antipathy")
bangla_meanings.append("ঘৃণা, বিরূপতা")
translations.append("a deep-seated feeling of aversion")
parts_of_speech.append("Noun")
sample_sentences.append("He felt a strong antipathy towards injustice.")
levels.append("Advanced")
synonyms.append("hostility, hatred")
antonyms.append("affection, sympathy")

# 5. Arcane
target_words.append("Arcane")
bangla_meanings.append("গোপন, রহস্যময়")
translations.append("understood by few, mysterious or secret")
parts_of_speech.append("Adjective")
sample_sentences.append("The document was full of arcane language.")
levels.append("Advanced")
synonyms.append("esoteric, mysterious")
antonyms.append("obvious, known")

# 6. Arduous
target_words.append("Arduous")
bangla_meanings.append("কষ্টসাধ্য, শ্রমসাধ্য")
translations.append("requiring strenuous effort, tiring")
parts_of_speech.append("Adjective")
sample_sentences.append("Climbing the mountain was an arduous task.")
levels.append("Intermediate")
synonyms.append("difficult, strenuous")
antonyms.append("easy, effortless")

# 7. Artless
target_words.append("Artless")
bangla_meanings.append("সরল, নির্মল")
translations.append("without deception, natural")
parts_of_speech.append("Adjective")
sample_sentences.append("Her artless charm won everyone over.")
levels.append("Advanced")
synonyms.append("naive, innocent")
antonyms.append("cunning, deceitful")

# 8. Ascetic
target_words.append("Ascetic")
bangla_meanings.append("ত্যাগী, কঠোর জীবনযাপনকারী")
translations.append("severe self-discipline, austere")
parts_of_speech.append("Adjective")
sample_sentences.append("The monk led an ascetic lifestyle.")
levels.append("Advanced")
synonyms.append("austere, self-denying")
antonyms.append("indulgent, hedonistic")

# 9. Assuage
target_words.append("Assuage")
bangla_meanings.append("উপশম করা, প্রশমিত করা")
translations.append("make an unpleasant feeling less intense")
parts_of_speech.append("Verb")
sample_sentences.append("He tried to assuage her fear.")
levels.append("Advanced")
synonyms.append("relieve, ease")
antonyms.append("aggravate, intensify")

# 10. Betray
target_words.append("Betray")
bangla_meanings.append("বিশ্বাসভঙ্গ করা")
translations.append("be disloyal, unintentionally reveal")
parts_of_speech.append("Verb")
sample_sentences.append("He betrayed his friend's trust.")
levels.append("Intermediate")
synonyms.append("deceive, expose")
antonyms.append("support, conceal")

# 11. Bucolic
target_words.append("Bucolic")
bangla_meanings.append("গ্রাম্য, পল্লীবিষয়ক")
translations.append("relating to the countryside")
parts_of_speech.append("Adjective")
sample_sentences.append("They enjoyed the bucolic scenery.")
levels.append("Advanced")
synonyms.append("rural, pastoral")
antonyms.append("urban, metropolitan")

# 12. Burgeon
target_words.append("Burgeon")
bangla_meanings.append("দ্রুত বিকশিত হওয়া")
translations.append("begin to grow rapidly, flourish")
parts_of_speech.append("Verb")
sample_sentences.append("The tech industry continues to burgeon.")
levels.append("Advanced")
synonyms.append("expand, thrive")
antonyms.append("shrink, decline")

# 13. Cacophonous
target_words.append("Cacophonous")
bangla_meanings.append("কর্ণভেদী শব্দে পূর্ণ")
translations.append("producing harsh sounds")
parts_of_speech.append("Adjective")
sample_sentences.append("The cacophonous alarm startled everyone.")
levels.append("Advanced")
synonyms.append("noisy, jarring")
antonyms.append("melodious, harmonious")

# 14. Canonize
target_words.append("Canonize")
bangla_meanings.append("পবিত্র বা গুরত্বপূর্ণ হিসেবে স্বীকৃতি দেওয়া")
translations.append("treat as of great significance")
parts_of_speech.append("Verb")
sample_sentences.append("He was canonized for his achievements.")
levels.append("Advanced")
synonyms.append("honor, glorify")
antonyms.append("disgrace, condemn")

# 15. Censure
target_words.append("Censure")
bangla_meanings.append("নিন্দা করা, তিরস্কার করা")
translations.append("express severe disapproval")
parts_of_speech.append("Verb")
sample_sentences.append("The senator was censured for misconduct.")
levels.append("Advanced")
synonyms.append("condemn, criticize")
antonyms.append("praise, approve")

# 16. Chicanery
target_words.append("Chicanery")
bangla_meanings.append("চাতুরী, প্রতারণা")
translations.append("use of deception")
parts_of_speech.append("Noun")
sample_sentences.append("He was known for political chicanery.")
levels.append("Advanced")
synonyms.append("deceit, trickery")
antonyms.append("honesty, sincerity")

# 17. Coalesce
target_words.append("Coalesce")
bangla_meanings.append("একত্রিত হওয়া")
translations.append("come together to form one whole")
parts_of_speech.append("Verb")
sample_sentences.append("The streams coalesced into a river.")
levels.append("Advanced")
synonyms.append("unite, merge")
antonyms.append("separate, divide")

# 18. Cogent
target_words.append("Cogent")
bangla_meanings.append("প্রভাবশালী, যুক্তিপূর্ণ")
translations.append("clear, logical and convincing")
parts_of_speech.append("Adjective")
sample_sentences.append("She made a cogent argument.")
levels.append("Advanced")
synonyms.append("persuasive, compelling")
antonyms.append("weak, unconvincing")

# 19. Compelling
target_words.append("Compelling")
bangla_meanings.append("মনোযোগ আকর্ষণকারী, বাধ্যকর")
translations.append("evoking interest irresistibly")
parts_of_speech.append("Adjective")
sample_sentences.append("The documentary was compelling.")
levels.append("Advanced")
synonyms.append("captivating, forceful")
antonyms.append("uninteresting, weak")

# 20. Contend
target_words.append("Contend")
bangla_meanings.append("তর্ক করা, সংগ্রাম করা")
translations.append("struggle or assert in argument")
parts_of_speech.append("Verb")
sample_sentences.append("He contended that the law was unjust.")
levels.append("Intermediate")
synonyms.append("argue, compete")
antonyms.append("agree, surrender")

# 21. Copious
target_words.append("Copious")
bangla_meanings.append("প্রচুর, ব্যাপক")
translations.append("abundant in supply")
parts_of_speech.append("Adjective")
sample_sentences.append("She took copious notes.")
levels.append("Intermediate")
synonyms.append("plentiful, abundant")
antonyms.append("scarce, sparse")

# 22. Cosmopolitan
target_words.append("Cosmopolitan")
bangla_meanings.append("বহুজাতিক, আন্তর্জাতিক")
translations.append("mixture of cultures")
parts_of_speech.append("Adjective")
sample_sentences.append("New York is a cosmopolitan city.")
levels.append("Intermediate")
synonyms.append("worldly, multicultural")
antonyms.append("provincial, local")

# 23. Deference
target_words.append("Deference")
bangla_meanings.append("সম্মান, শ্রদ্ধা")
translations.append("polite submission and respect")
parts_of_speech.append("Noun")
sample_sentences.append("He addressed the judge with deference.")
levels.append("Advanced")
synonyms.append("respect, honor")
antonyms.append("disrespect, defiance")

# 24. Desultory
target_words.append("Desultory")
bangla_meanings.append("অলক্ষ্য, এলোমেলো")
translations.append("lacking plan or enthusiasm")
parts_of_speech.append("Adjective")
sample_sentences.append("The conversation was desultory.")
levels.append("Advanced")
synonyms.append("random, aimless")
antonyms.append("focused, methodical")

# 25. Diffident
target_words.append("Diffident")
bangla_meanings.append("আত্মবিশ্বাসহীন, লাজুক")
translations.append("modest or shy due to lack of confidence")
parts_of_speech.append("Adjective")
sample_sentences.append("He gave a diffident reply.")
levels.append("Advanced")
synonyms.append("shy, timid")
antonyms.append("confident, bold")

# 26. Dilatory
target_words.append("Dilatory")
bangla_meanings.append("ধীর, সময় ক্ষেপণকারী")
translations.append("slow to act; causing delay")
parts_of_speech.append("Adjective")
sample_sentences.append("His dilatory tactics frustrated the team.")
levels.append("Advanced")
synonyms.append("tardy, sluggish")
antonyms.append("prompt, timely")

# 27. Equivocate
target_words.append("Equivocate")
bangla_meanings.append("কৌশলে বিভ্রান্ত করা")
translations.append("use ambiguous language")
parts_of_speech.append("Verb")
sample_sentences.append("She equivocated when asked about her plans.")
levels.append("Advanced")
synonyms.append("hedge, prevaricate")
antonyms.append("clarify, be honest")

# 28. Polarize
target_words.append("Polarize")
bangla_meanings.append("দ্বিধাবিভক্ত করা")
translations.append("divide into contrasting groups")
parts_of_speech.append("Verb")
sample_sentences.append("The debate polarized the audience.")
levels.append("Advanced")
synonyms.append("divide, split")
antonyms.append("unify, reconcile")

# 29. Prodigal
target_words.append("Prodigal")
bangla_meanings.append("অপচয়কারী, অতিচয়কারী")
translations.append("spending money recklessly")
parts_of_speech.append("Adjective")
sample_sentences.append("His prodigal habits left him broke.")
levels.append("Advanced")
synonyms.append("wasteful, extravagant")
antonyms.append("frugal, thrifty")

# 30. Verbose
target_words.append("Verbose")
bangla_meanings.append("অতিমাত্রায় বাক্প্রচুর")
translations.append("using more words than necessary")
parts_of_speech.append("Adjective")
sample_sentences.append("His writing is too verbose.")
levels.append("Intermediate")
synonyms.append("wordy, long-winded")
antonyms.append("concise, succinct")

# Create DataFrame and save
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

df.to_excel('flashcards/flashcards3.xlsx', index=False)

print("Excel file 'flashcards/flashcards3.xlsx' has been created successfully.")