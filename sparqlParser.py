example = '''PREFIX testapp: <http://www.mypro.org/ontologies/Test#>
    SELECT ?count
    WHERE { { SELECT ?count
    WHERE { { SELECT ?count
    WHERE { { { SELECT ( COUNT( DISTINCT ?source ) AS ?count )
    WHERE { GRAPH <http://www.mypro.org/branch/master> { { SELECT ?source ?type ?date ?docId ?title ?docText ?docTitleR ?publishDate ?position ?captionR ?caption ?textR ?text ?relTitle ?relR ?relPubDate
    WHERE { { SELECT DISTINCT ?source
    WHERE { { ?id testapp:Destination <http://www.mypro.org/testObj> . } UNION { ?id testapp:Destination <http://www.mypro.org/testobj> . }
    ?id a <http://www.mypro.org/ontologies/Test#Tag> ;
        testapp:Source ?source . }
    }
    ?source a ?type .
    ?source a <http://www.mypro.org/ontologies/Test#TestRef> .
    ?source <http://www.mypro.org/createdDate> ?date .
    OPTIONAL { ?source testapp:Text ?text . }
    OPTIONAL { ?source testapp:DocumentText ?docText . }
    OPTIONAL { ?source testapp:Position ?position . }
    OPTIONAL { ?source testapp:Ref ?textR . }
    OPTIONAL { ?source testapp:Caption ?caption . }
    OPTIONAL { ?source testapp:CaptionRef ?captionR . }
    OPTIONAL { ?source <http://purl.org/dc/elements/1.1/title> ?title . }
    OPTIONAL { ?source testapp:DocumentPublishedOn ?publishDate . }
    OPTIONAL { ?source testapp:DocumentTitleClass ?docTitleR . }
    OPTIONAL { ?source testapp:DocumentId ?docId .
    OPTIONAL { ?docId <http://purl.org/dc/elements/1.1/title> ?relTitle . }
    OPTIONAL { ?docId testapp:DocumentTitleClass ?relR . }
    OPTIONAL { ?docId testapp:DocumentPublishedOn ?relPubDate . } } }
    } } }
    } } UNION { { SELECT ( COUNT( DISTINCT ?source ) AS ?count )
    WHERE { GRAPH <http://www.mypro.org/branch/master> { { SELECT ?source ?type ?date ?docId ?title ?docText ?docTitleR ?publishDate ?position ?captionR ?caption ?textR ?text ?relTitle ?relR ?relPubDate
    WHERE { { SELECT DISTINCT ?source
    WHERE { { ?id testapp:Destination <http://www.mypro.org/testObj> . } UNION { ?id testapp:Destination <http://www.mypro.org/testobj> . }
    ?id a <http://www.mypro.org/ontologies/Test#Tag> ;
        testapp:Source ?source . }
    }
    ?source a ?type .
    ?source a <http://www.mypro.org/ontologies/Test#TestTable> .
    ?source <http://www.mypro.org/createdDate> ?date .
    OPTIONAL { ?source testapp:Text ?text . }
    OPTIONAL { ?source testapp:DocumentText ?docText . }
    OPTIONAL { ?source testapp:Position ?position . }
    OPTIONAL { ?source testapp:Ref ?textR . }
    OPTIONAL { ?source testapp:Caption ?caption . }
    OPTIONAL { ?source testapp:CaptionRef ?captionR . }
    OPTIONAL { ?source <http://purl.org/dc/elements/1.1/title> ?title . }
    OPTIONAL { ?source testapp:DocumentPublishedOn ?publishDate . }
    OPTIONAL { ?source testapp:DocumentTitleClass ?docTitleR . }
    OPTIONAL { ?source testapp:DocumentId ?docId .
    OPTIONAL { ?docId <http://purl.org/dc/elements/1.1/title> ?relTitle . }
    OPTIONAL { ?docId testapp:DocumentTitleClass ?relR . }
    OPTIONAL { ?docId testapp:DocumentPublishedOn ?relPubDate . } } }
    } } }
    } } UNION { { SELECT ( COUNT( DISTINCT ?source ) AS ?count )
    WHERE { GRAPH <http://www.mypro.org/branch/master> { { SELECT ?source ?type ?date ?docId ?title ?docText ?docTitleR ?publishDate ?position ?captionR ?caption ?textR ?text ?relTitle ?relR ?relPubDate
    WHERE { { SELECT DISTINCT ?source
    WHERE { { ?id testapp:Destination <http://www.mypro.org/testObj> . } UNION { ?id testapp:Destination <http://www.mypro.org/testobj> . }
    ?id a <http://www.mypro.org/ontologies/Test#Tag> ;
        testapp:Source ?source . }
    }
    ?source a ?type .
    ?source a <http://www.mypro.org/ontologies/Test#TestImage> .
    ?source <http://www.mypro.org/createdDate> ?date .
    OPTIONAL { ?source testapp:Text ?text . }
    OPTIONAL { ?source testapp:DocumentText ?docText . }
    OPTIONAL { ?source testapp:Position ?position . }
    OPTIONAL { ?source testapp:Ref ?textR . }
    OPTIONAL { ?source testapp:Caption ?caption . }
    OPTIONAL { ?source testapp:CaptionRef ?captionR . }
    OPTIONAL { ?source <http://purl.org/dc/elements/1.1/title> ?title . }
    OPTIONAL { ?source testapp:DocumentPublishedOn ?publishDate . }
    OPTIONAL { ?source testapp:DocumentTitleClass ?docTitleR . }
    OPTIONAL { ?source testapp:DocumentId ?docId .
    OPTIONAL { ?docId <http://purl.org/dc/elements/1.1/title> ?relTitle . }
    OPTIONAL { ?docId testapp:DocumentTitleClass ?relR . }
    OPTIONAL { ?docId testapp:DocumentPublishedOn ?relPubDate . } } }
    } } }
    } } UNION { { SELECT ( COUNT( DISTINCT ?source ) AS ?count )
    WHERE { GRAPH <http://www.mypro.org/branch/master> { { SELECT ?source ?type ?date ?docId ?title ?docText ?docTitleR ?publishDate ?position ?captionR ?caption ?textR ?text ?relTitle ?relR ?relPubDate
    WHERE { { SELECT DISTINCT ?source
    WHERE { { ?id testapp:Destination <http://www.mypro.org/testObj> . } UNION { ?id testapp:Destination <http://www.mypro.org/testobj> . }
    ?id a <http://www.mypro.org/ontologies/Test#Tag> ;
        testapp:Source ?source . }
    }
    ?source a ?type .
    { ?source a ?innerType .
    FILTER ( ?innerType = <http://www.mypro.org/ontologies/Test#testDocument> || ?innerType = <http://www.mypro.org/ontologies/Test#Document> ) }
    ?source <http://www.mypro.org/createdDate> ?date .
    OPTIONAL { ?source testapp:Text ?text . }
    OPTIONAL { ?source testapp:DocumentText ?docText . }
    OPTIONAL { ?source testapp:Position ?position . }
    OPTIONAL { ?source testapp:Ref ?textR . }
    OPTIONAL { ?source testapp:Caption ?caption . }
    OPTIONAL { ?source testapp:CaptionRef ?captionR . }
    OPTIONAL { ?source <http://purl.org/dc/elements/1.1/title> ?title . }
    OPTIONAL { ?source testapp:DocumentPublishedOn ?publishDate . }
    OPTIONAL { ?source testapp:DocumentTitleClass ?docTitleR . }
    OPTIONAL { ?source testapp:DocumentId ?docId .
    OPTIONAL { ?docId <http://purl.org/dc/elements/1.1/title> ?relTitle . }
    OPTIONAL { ?docId testapp:DocumentTitleClass ?relR . }
    OPTIONAL { ?docId testapp:DocumentPublishedOn ?relPubDate . } } }
    } } }
    } } }
    } }
    } }
'''

def addTabs(tabsC):
    tabs = ''
    for tab in range(tabsC):
        tabs += '    '
    return tabs


def countBackTrack(text, start, end, target):
    count = ''
    select_pos = text.rfind(target, start, end)
    if start == 0 or select_pos == -1:
        return ''
    for j in reversed(range(select_pos)):
        if text[j] == '\n':
            break
        else:
            count += ' '

    return count


def indentWhere(text):
    found = text.find('WHERE')
    start = 0
    end = ''

    while found != -1:
        spaces = countBackTrack(text, start, found, '{')
        # add /n and skip count before where
        # find add skipcount

        spaceCount = len(spaces)
        text = text[:found] + '\n' + spaces + \
            ('' if start == 0 else '     ') + text[found:]
        start = found
        # + 10 so it skips the where
        found = spaceCount + found + 10
        found = text.find('WHERE', found)

    return text


def indentFilter(text):
    found = text.find('FILTER')
    start = None
    end = ''

    while found != -1:
        # spaces = filterBackTrack(text, start, found)
        spaces = countBackTrack(text, start, found, '{')
        # add /n and skip count before where
        # find add skipcount
        start = found
        spaceCount = len(spaces)
        text = text[:found] + '\n' + spaces + '     ' + text[found:]
        # + 10 so it skips the where
        found = spaceCount + found + 10
        found = text.find('FILTER', found)

    return text


def indentSpecialWords(text):
    text = indentWhere(text)
    text = indentFilter(text)
    return text


def parse(text):
    cleanTokens = []
    tabCount = 0
    # get everything on the same line
    minText = text.replace('\n', ' ').replace('\r', '')
    # add \n and spaces in each bracket
    for t in minText:
        if len(cleanTokens) != 0 and cleanTokens[-1] == ' ' and t == ' ':
            continue

        elif len(cleanTokens) != 0 and cleanTokens[-1] == '\n':
            cleanTokens.append(t)
        elif t.strip() == '{':
            cleanTokens.append('\n')

            cleanTokens.append(addTabs(tabCount))
            cleanTokens.append(t)
            tabCount += 1
            cleanTokens.append('\n')

        elif t.strip() == '}':
            cleanTokens.append('\n')
            tabCount -= 1

            cleanTokens.append(addTabs(tabCount))
            cleanTokens.append(t)
            cleanTokens.append('\n')

        else:
            if len(cleanTokens) != 0:
                if cleanTokens[-1] == ' ':
                    lastToken = len(cleanTokens) - 1

                    while cleanTokens[lastToken] == ' ':
                        lastToken -= 1

                    if cleanTokens[lastToken] != '{' and cleanTokens[lastToken] != '}' and cleanTokens[lastToken] != '\n':

                        cleanTokens.append(t)
                    else:
                        count = tabCount + 1
                        cleanTokens.append(addTabs(tabCount))
                        cleanTokens.append(t)

                elif cleanTokens[len(cleanTokens) - 1] == '{' and cleanTokens[len(cleanTokens) - 1] == '}' and cleanTokens[len(cleanTokens) - 1] != '\n':
                    count = tabCount + 1
                    cleanTokens.append(addTabs(count))
                    cleanTokens.append(t)

                elif cleanTokens[len(cleanTokens) - 1] != '{' and cleanTokens[len(cleanTokens) - 1] != '}' and cleanTokens[len(cleanTokens) - 1] != '\n':
                    cleanTokens.append(t)
                else:
                    count = tabCount + 1
                    cleanTokens.append(addTabs(count))
                    cleanTokens.append(t)
            else:
                cleanTokens.append(t)

    parsedText = ''.join(cleanTokens)
    replacedTxt = parsedText.replace('\n\n', '\n').replace(
        '\n\n', '\n').replace('\n \n', '\n')
    # replacedTxt = parsedText

    # indent first SELECT
    select_pos = replacedTxt.find('SELECT')
    replacedTxt = replacedTxt[:select_pos] + '\n' + replacedTxt[select_pos:]

    goodText = indentSpecialWords(replacedTxt)
    # w = create file or override file if file exists
    # x = create file
    f = open('formattedSparql.txt', 'w')
    f.write(goodText)


goodText = ''
parse(example)
