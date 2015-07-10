# Program to calculate the median number of unique words per tweet.
# Using MinHeap and MaxHeap
import sys;
import heapq;

def heappushMAX(heap, item):
    heapq.heappush(heap, -item)

def heappopMAX(heap):
    return -heapq.heappop(heap)

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

minHeap = [];
maxHeap = [];
firstElement = 0.0;
secondElement = 0.0;
# Open file in write mode
featureOutput = open(outputArgument, "w",);

while(tweetText):
	# stores the index of current tweet in the medianList
	currentTweet = currentTweet + 1;
	# Exception Handling
	try:
		# To strip the tweet of the preceeding and following spaces if any.
		tweetText = tweetText.strip();
		# Convert text into list of words
		tweetList = tweetText.split();
		# Iterate through all the words in the List and store unique words in the Set
		for word in tweetList:
			uniqueWordSet.add(word);

		nextElement = len(uniqueWordSet) + 0.0;

		if (currentTweet >= 2):
			if(nextElement < (-1 * maxHeap[0])):
				heappushMAX(maxHeap, nextElement);
			else:
				heapq.heappush(minHeap, nextElement);

			maxHeapLength = len(maxHeap);
			minHeapLength = len(minHeap);

			# Balance both MinHeap and MaxHeap
			if(abs(maxHeapLength - minHeapLength) > 1):
				if(maxHeapLength > minHeapLength):
					root = heappopMAX(maxHeap);
					heapq.heappush(minHeap, root);
				else:
					root = heapq.heappop(minHeap);
					heappushMAX(maxHeap, root);

			maxHeapLength = len(maxHeap);
			minHeapLength = len(minHeap);

			# Find Median using both Heaps
			if(maxHeapLength == minHeapLength):
				featureOutput.write(str("%.2f" % ((minHeap[0] + (-1 * maxHeap[0]))/2.0)) + '\n');
			elif(maxHeapLength > minHeapLength):
				featureOutput.write(str("%.2f" % (-1 * maxHeap[0])) + '\n');
			else:
				featureOutput.write(str("%.2f" % minHeap[0]) + '\n');

		elif (currentTweet == 1):
			secondElement = len(uniqueWordSet);
			# Push first and second element on the Heaps
			if(firstElement > secondElement):
				heapq.heappush(minHeap, firstElement);
				heappushMAX(maxHeap, secondElement);
			else:
				heapq.heappush(minHeap, secondElement);
				heappushMAX(maxHeap, firstElement);			

			# Find Median using first and second element
			featureOutput.write(str("%.2f" % ((firstElement + secondElement)/2.0)) + '\n');
		elif(currentTweet == 0):
			firstElement = len(uniqueWordSet);
			featureOutput.write(str("%.2f" % firstElement) + '\n');

	except:
		featureOutput.write('ERROR PROCESSING THIS TWEET \n');		
	# clear the Set
	uniqueWordSet.clear();

	tweetText = twiterInput.readline();

# close the input tweets file
twiterInput.close();
# Close the output file.
featureOutput.close();