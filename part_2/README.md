Explanation Part One
In the main file, it builds the logger + metadata manager
+ Kafka Publisher
Sends the metadata class a route to the folder
The object passes a file inside the folder and builds a metadata object for it
and returns one by one using yeild
the main func takes one by one and send it to kafka