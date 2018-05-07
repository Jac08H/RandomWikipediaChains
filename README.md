# SixDegreesOfWikipedia
Find hyperlinked paths between pages on wikipedia.

### Usage
    usage: six_degrees_of_wikipedia.py [-h] [-s STEPS] [-t TARGET] [-l LIMIT] [-v]
                                   [--site SITE]
                                   mode article
                             
                                   
* Mode `random`: find random route from the article; STEPS argument is mandatory

* Mode `target`: try to find route form starting article to target article using random hyperlinks; TARGET argument is mandatory

  
`random` example

    $ ./six_degrees_of_wikipedia.py random Python --steps 3 -v
    
    mode: random; article: Python; steps: 3
    1. step: Python (https://en.wikipedia.org/wiki/Python)
    2. step: Cython (https://en.wikipedia.org/wiki/Cython)
    3. step: Foreign function interface (https://en.wikipedia.org/wiki/Foreign_function_interface)
    https://en.wikipedia.org/wiki/Clean_(programming_language)


`target` example

    $ ./six_degrees_of_wikipedia.py target Python --target Slovakia
    
    mode: target; article: Python; target: Slovakia; limit: 10
    1.  Python -> Python of Catana
    2.  Python -> Python of Catana -> William Smith (lexicographer)
    3.  Python -> Python of Catana -> William Smith (lexicographer) -> Articled clerk
    4.  Python -> Python of Catana -> William Smith (lexicographer) -> Articled clerk -> Institute of Chartered Accountants of Sri Lanka
    5.  Python -> Python of Catana -> William Smith (lexicographer) -> Articled clerk -> Institute of Chartered Accountants of Sri Lanka -> New Zealand
    6.  Python -> Python of Catana -> William Smith (lexicographer) -> Articled clerk -> Institute of Chartered Accountants of Sri Lanka -> New Zealand -> The Gambia
    7.  Python -> Python of Catana -> William Smith (lexicographer) -> Articled clerk -> Institute of Chartered Accountants of Sri Lanka -> New Zealand -> The Gambia -> Military of the Gambia
    8.  Python -> Python of Catana -> William Smith (lexicographer) -> Articled clerk -> Institute of Chartered Accountants of Sri Lanka -> New Zealand -> The Gambia -> Military of the Gambia -> Music of the Gambia
    9.  Python -> Python of Catana -> William Smith (lexicographer) -> Articled clerk -> Institute of Chartered Accountants of Sri Lanka -> New Zealand -> The Gambia -> Military of the Gambia -> Music of the Gambia -> Senegal
    Python -> Python of Catana -> William Smith (lexicographer) -> Articled clerk -> Institute of Chartered Accountants of Sri Lanka -> New Zealand -> The Gambia -> Military of the Gambia -> Music of the Gambia -> Senegal -> Slovakia