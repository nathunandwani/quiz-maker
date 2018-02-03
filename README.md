# quiz-maker

Quiz Maker is a simple script which can load a list of questions and present a quiz for you.

An example of a question format is:

"Which layer of the TCP/IP model is concerned with end-to-end communication and offers multiplexing service?","Transport","Internet","Link Layer","Application","ANS|0"

The first index of the CSV is the question while the remaining ones are choices except for the one with "ANS|". The value after "ANS|" is the index of the correct answer for the question. In this case, "Transport" is the correct answer which makes the index equal to 0. If the correct answer is "Application", the value of "ANS|" should be 3 making it "ANS|3".
