# About
This project is just the mishmash of learning opportunities that seemed interesting.  My favorite podcasts, Django, a chance to play with a machine learning project, and possibly learn about Solr.


I borrowed time on a RTX 3090 (24Gb) to process Jupiter Broadcasting's catalog of podcasts
though [OpenAI's Whisper](https://github.com/openai/whisper) project. (*still working on some shows as this commit went in)

Whisper generates srt, vtt, and txt output of whatever audio you send through it by using the power of machine learning and various sized models.  The 3090 enabled the use of the Large model.  I have not had the opportunity to compare quality or speed between the different sized models.  Translation is even on the brochure, though I have not explored that.  It might be a way to extend show reach.  

# About the web app
The django app is fairly basic.  Most of the work is in jbcontent.  I did create an extra management command to load show content.

transcripts are to be placed in /media and can be found in an external repository located at [ShuffleBox/JB_content](https://github.com/ShuffleBox/JB_content)

The web player is [Able Player](https://ableplayer.github.io/ableplayer/) and the podcast audio is still served from [Fireside](https://fireside.fm/)

Extra management command example:

`./manage.py sync_shows https://coder.show/rss`

