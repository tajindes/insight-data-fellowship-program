# Program to calculates the total number of times each word has been tweeted.
import sys;

# Accept input file path 
inputArgument = sys.argv[1];
# Open file in Read-only mode
twiterInput = open(inputArgument, "r");
# Accept output file path
outputArgument = sys.argv[2];

# Read the first tweet
tweetText = twiterInput.readline();

# create dictionary with KEY: each word, Value: Count of the word (number of times the word has been tweeted)
wordsTweetedDict = dict();

while(tweetText):
	# Exception Hanlding
	try:	
		# To strip the tweet of the preceeding and following spaces if any.
		tweetText = tweetText.strip();
		# Convert text into list of words
		tweetList = tweetText.split();
		# Iterate through all the words in the List
		for word in tweetList:
			# Check if the word exists in the dictionary
			if(word not in wordsTweetedDict):
				wordsTweetedDict[word] = 1;
			else:
				# increment the counter if the word already exists
				wordsTweetedDict[word] = wordsTweetedDict[word] + 1;
	except:
		pass;
	tweetText = twiterInput.readline();
# close the input tweets file
twiterInput.close();

# Open file in write mode
featureOutput = open(outputArgument, "w",);
# To retrieve the tweeted words (keys of dictionary) in sorted order
for asciiSortWord in sorted(wordsTweetedDict):
	# Write the content in the output file with vertical alignment.
	featureOutput.write('{:<40}  {:<40}'.format(asciiSortWord,wordsTweetedDict[asciiSortWord]) + '\n');
# Close the output file.
featureOutput.close();