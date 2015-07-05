# Program to calculate the median number of unique words per tweet.
import sys;

# Accept input file path 
inputArgument = sys.argv[1];
# Open file in Read-only mode
twiterInput = open(inputArgument, "r");
# Accept output file path
outputArgument = sys.argv[2];

currentTweet = -1;
# Read the first tweet
tweetText = twiterInput.readline();

uniqueWordSet = set();
medianList = list();

# Open file in write mode
featureOutput = open(outputArgument, "w",);

while(tweetText):
	# stores the index of current tweet in the medianList
	currentTweet = currentTweet + 1;
	# To strip the tweet of the preceeding and following spaces if any.
	tweetText = tweetText.strip();
	# Convert text into list of words
	tweetList = tweetText.split();
	# Iterate through all the words in the List and store unique words in the Set
	for word in tweetList:
		uniqueWordSet.add(word);
	# Append the number of unique words in the tweet to the medianList
	medianList.append(len(uniqueWordSet));
	# clear the Set
	uniqueWordSet.clear();
	# calculate the median using the medianList and currentTweet.
	if(currentTweet % 2 ==0):
		featureOutput.write(str(medianList[currentTweet/2]) + '\n');		
	else:
		# perform a floating-point division to calculate the median, given two integers.
		featureOutput.write(str((medianList[currentTweet/2] + medianList[(currentTweet+1)/2])/2.0) + '\n');
	tweetText = twiterInput.readline();

# close the input tweets file
twiterInput.close();
# Close the output file.
featureOutput.close();
