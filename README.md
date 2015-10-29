# online-radio-channels

This project offers schemata for XML and JSON to describe channels for online radio stations. Note that the formats differ slightly. However, using these formats enables radio stations to automatically broadcast which channels and playlists in different formats an qualities they are offer. At the same time descriptions, artwork and metadata on last playing and number of listerers is being made available.

With approval from [SomaFM](https://somafm.com), these schemas have been derived and fine tuned according to existing XML and JSON data that they already have in use. Examples are [https://api.somafm.com/channels.xml](https://api.somafm.com/channels.xml) and [https://api.somafm.com/channels.json](https://api.somafm.com/channels.json) respectively.

The schemata developed are [channels.xsd](channels.xsd) and [channels.json](channels.json) for which the XSD contains annotation and documentation in HTML and SVG can be found in the [doc](doc) direcory. However these files cannot be browsed from within the GitHub website and must be downloaded first.

Showcases of projects using the content of channel.xsd files are the folling:
* The music server [Mopidy](https://mopidy.com) has a [SomaFM backend](https://docs.mopidy.com/en/latest/ext/backends/#mopidy-somafm), see also its [GitHub project](https://github.com/AlexandrePTJ/mopidy-somafm).
* The home theatre [Kodi](https://kodi.tv) has a [SomaFM add-on](http://kodi.wiki/view/Add-on:SomaFM), see also its [GitHub project](https://github.com/Oderik/xbmc-somafm).

Tools that are practical to use in this context are http://jsoneditoronline.org and http://jsonviewer.stack.hu for JSON. At http://json-schema.org the definition of the JSON schema itself can be found. For XML the tool XML Copy Editor http://xml-copy-editor.sourceforge.net might come in handy.

This project also provides example XML and JSON files and scripts that validate them against their schema and report on their content. See the directory [examples](examples) for more.
