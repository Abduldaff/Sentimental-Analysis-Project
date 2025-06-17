import string
from nltk.tokenize import word_tokenize
import matplotlib.pyplot as plt
from collections import Counter
from nltk.corpus import stopwords
from nltk.sentiment.vader import SentimentIntensityAnalyzer
 
  
#open the file with the open function and give it the valable
# text_file = open("text.txt").read()
text_file = input("enter the word: ")
print(text_file)
#print(text_file)
#covert the text in the lower case 

lower_case = text_file.lower()

#remove the punctuatio for the give file 

remove_text = lower_case.translate(str.maketrans(" "," ",string.punctuation))

#give the lop for the stopwords and store it in the final_world list

split_world = word_tokenize(remove_text,"english")
 
#print(split_world)
final_word=[]
for word in split_world:
    if word  not in  stopwords.words("english"):
        final_word.append(word)
#print(final_word)



emotion_list = []
with open("emotions.txt","r") as file:
    for line in file:
        clear_line  = line.replace("\n","").replace(",","").replace("'","").strip()
        if ":" in clear_line:
            word ,emotion = clear_line.split(":") 
        #print(" word -> "+word+", emotion -> "+emotion)
        if word in final_word:
            emotion_list.append(emotion)
#print(emotion_list)
counting_word = Counter(emotion_list)
#print(counting_word) 

#import matplotlib.pyplot as plt for bar type graph 
#adjust the space inbetween the word by the plt.subplots() function

fig,axl = plt.subplots()
axl.bar(counting_word.keys(),counting_word.values())
fig.autofmt_xdate()
plt.savefig("emotions")
plt.show()

#creat the def function to ayalyse the given review is in negative ,positive or neutral review

def analyse(sentiment_text):
    volue = SentimentIntensityAnalyzer().polarity_scores(sentiment_text)
    negative = volue["neg"]
    positive = volue["pos"]
    if  negative> positive:
        print("negative review")
    elif negative< positive:
        print("positive review")
    else:
        print("neutral review")
analyse(remove_text)