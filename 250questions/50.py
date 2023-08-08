# This is file 48.py

favourite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'java',
    'jad': 'go'
}

print("The following language have been mentioned")
for language in favourite_languages.keys():
    print(language.title())
