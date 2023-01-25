# djangoi18n-phrase-pet
Test django i18n with phrase

## Setup

```sh
python3 -m venv venv
source venv/bin/activate
```

```
pip install -r requirements.txt
```

## Run
```
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```
## Settings
```
In settings file, you can change the language code to your language code.
And setup supported language in LANGUAGES.
```
## Django i18n
```
django-admin makemessages -l en (create .po file)
django-admin compilemessages (create .mo file)
```

# Phrase
add phrase yml files
phrase push (push target files to phrase)
phrase pull (pull from phrase)
phrase uploads clenup --id <download_id> (cleanup unused translates)
