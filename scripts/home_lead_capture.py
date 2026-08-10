from pathlib import Path
import re

p=Path('index.html')
text=p.read_text(encoding='utf-8')

text=text.replace('Get the next note from Pastor Tate.','Get the free 2:00 A.M. Guide.')
text=text.replace('Every so often, I’ll send a short pastoral note for a question people are actually carrying—grief, doubt, depression, unanswered prayer, forgiveness, and more. I’ll also let you know when <em>Answers for a Broken Heart</em> is ready.','Seven Scriptures, short pastoral reminders, and simple prayers for the nights when your thoughts are loud and you do not know what else to do. I’ll also send occasional pastoral notes and let you know when <em>Answers for a Broken Heart</em> is ready.')
text=text.replace('New Answers for a Broken Heart homepage signup','New 2:00 A.M. Guide homepage signup')
text=text.replace('https://answersforabrokenheart.com/hope-thanks','https://answersforabrokenheart.com/2am-guide')
text=text.replace('A Note from Pastor Tate + free guides + book release updates','2:00 A.M. Guide + occasional pastoral notes + book release updates')
text=text.replace('Homepage Free Guides','Homepage 2:00 A.M. Guide')
text=text.replace('Send Me the Next Note','Send Me the Free Guide')
text=text.replace('No daily emails. Just occasional pastoral encouragement, new free guides, and book-release updates.','You’ll go straight to the guide after signing up. No daily emails—just occasional pastoral encouragement and book-release updates.')

p.write_text(text,encoding='utf-8')
print('Homepage lead magnet updated')
