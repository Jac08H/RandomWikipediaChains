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
