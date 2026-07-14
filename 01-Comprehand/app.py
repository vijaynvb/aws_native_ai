import boto3

comprehend = boto3.client('comprehend', region_name='us-east-1')

textInput = "Hello, I am learning how to use AWS Comprehend for natural language processing."

response = comprehend.detect_sentiment(Text=textInput, LanguageCode='en')
print(response)
# print("Sentiment Analysis:", response['Sentiment'], "with confidence scores:", response['SentimentScore'])
# response2 = comprehend.detect_entities(Text=textInput, LanguageCode='en')
# print("Entity Analysis:", response2['Entities'])
# response3 = comprehend.detect_key_phrases(Text=textInput, LanguageCode='en')
# print("Key Phrase Analysis:", response3['KeyPhrases'])
# response4 = comprehend.detect_syntax(Text=textInput, LanguageCode='en')
# print("Syntax Analysis:", response4['SyntaxTokens'])
# response5 = comprehend.detect_dominant_language(Text=textInput)
# print("Dominant Language:", response5['Languages'])
# response6 = comprehend.detect_pii_entities(Text=textInput, LanguageCode='en')
# print("PII Entity Analysis:", response6['Entities'])
# response7 = comprehend.batch_detect_sentiment(TextList=[textInput], LanguageCode='en')
# print("Batch Sentiment Analysis:", response7['ResultList'])