example = '''PREFIX dewapp: <http://www.projectdewey.org/ontologies/Dewey#>
SELECT ?count
WHERE { { SELECT ?count
WHERE { { SELECT ?count
WHERE { { { SELECT ( COUNT( DISTINCT ?source ) AS ?count )
WHERE { GRAPH <http://www.projectdewey.org/branch/master> { { SELECT ?source ?type ?date ?docId ?title ?docText ?docTitlePm ?publishDate ?position ?captionPm ?caption ?textPm ?text ?relTitle ?relPm ?relPubDate
WHERE { { SELECT DISTINCT ?source
WHERE { { ?id dewapp:Destination <http://www.projectdewey.org/Su57> . } UNION { ?id dewapp:Destination <http://www.projectdewey.org/AA10AlamoC> . }
?id a <http://www.projectdewey.org/ontologies/Dewey#Tag> ;
    dewapp:Source ?source . }
 }
?source a ?type .
?source a <http://www.projectdewey.org/ontologies/Dewey#DeweyParagraph> .
?source <http://www.projectdewey.org/createdDate> ?date .
OPTIONAL { ?source dewapp:Text ?text . }
OPTIONAL { ?source dewapp:DocumentText ?docText . }
OPTIONAL { ?source dewapp:Position ?position . }
OPTIONAL { ?source dewapp:PortionMark ?textPm . }
OPTIONAL { ?source dewapp:Caption ?caption . }
OPTIONAL { ?source dewapp:CaptionPortionMark ?captionPm . }
OPTIONAL { ?source <http://purl.org/dc/elements/1.1/title> ?title . }
OPTIONAL { ?source dewapp:DocumentPublishedOn ?publishDate . }
OPTIONAL { ?source dewapp:DocumentTitleClassification ?docTitlePm . }
OPTIONAL { ?source dewapp:DocumentId ?docId .
OPTIONAL { ?docId <http://purl.org/dc/elements/1.1/title> ?relTitle . }
OPTIONAL { ?docId dewapp:DocumentTitleClassification ?relPm . }
OPTIONAL { ?docId dewapp:DocumentPublishedOn ?relPubDate . } } }
 } } }
 } } UNION { { SELECT ( COUNT( DISTINCT ?source ) AS ?count )
WHERE { GRAPH <http://www.projectdewey.org/branch/master> { { SELECT ?source ?type ?date ?docId ?title ?docText ?docTitlePm ?publishDate ?position ?captionPm ?caption ?textPm ?text ?relTitle ?relPm ?relPubDate
WHERE { { SELECT DISTINCT ?source
WHERE { { ?id dewapp:Destination <http://www.projectdewey.org/Su57> . } UNION { ?id dewapp:Destination <http://www.projectdewey.org/AA10AlamoC> . }
?id a <http://www.projectdewey.org/ontologies/Dewey#Tag> ;
    dewapp:Source ?source . }
 }
?source a ?type .
?source a <http://www.projectdewey.org/ontologies/Dewey#DeweyTable> .
?source <http://www.projectdewey.org/createdDate> ?date .
OPTIONAL { ?source dewapp:Text ?text . }
OPTIONAL { ?source dewapp:DocumentText ?docText . }
OPTIONAL { ?source dewapp:Position ?position . }
OPTIONAL { ?source dewapp:PortionMark ?textPm . }
OPTIONAL { ?source dewapp:Caption ?caption . }
OPTIONAL { ?source dewapp:CaptionPortionMark ?captionPm . }
OPTIONAL { ?source <http://purl.org/dc/elements/1.1/title> ?title . }
OPTIONAL { ?source dewapp:DocumentPublishedOn ?publishDate . }
OPTIONAL { ?source dewapp:DocumentTitleClassification ?docTitlePm . }
OPTIONAL { ?source dewapp:DocumentId ?docId .
OPTIONAL { ?docId <http://purl.org/dc/elements/1.1/title> ?relTitle . }
OPTIONAL { ?docId dewapp:DocumentTitleClassification ?relPm . }
OPTIONAL { ?docId dewapp:DocumentPublishedOn ?relPubDate . } } }
 } } }
 } } UNION { { SELECT ( COUNT( DISTINCT ?source ) AS ?count )
WHERE { GRAPH <http://www.projectdewey.org/branch/master> { { SELECT ?source ?type ?date ?docId ?title ?docText ?docTitlePm ?publishDate ?position ?captionPm ?caption ?textPm ?text ?relTitle ?relPm ?relPubDate
WHERE { { SELECT DISTINCT ?source
WHERE { { ?id dewapp:Destination <http://www.projectdewey.org/Su57> . } UNION { ?id dewapp:Destination <http://www.projectdewey.org/AA10AlamoC> . }
?id a <http://www.projectdewey.org/ontologies/Dewey#Tag> ;
    dewapp:Source ?source . }
 }
?source a ?type .
?source a <http://www.projectdewey.org/ontologies/Dewey#DeweyImage> .
?source <http://www.projectdewey.org/createdDate> ?date .
OPTIONAL { ?source dewapp:Text ?text . }
OPTIONAL { ?source dewapp:DocumentText ?docText . }
OPTIONAL { ?source dewapp:Position ?position . }
OPTIONAL { ?source dewapp:PortionMark ?textPm . }
OPTIONAL { ?source dewapp:Caption ?caption . }
OPTIONAL { ?source dewapp:CaptionPortionMark ?captionPm . }
OPTIONAL { ?source <http://purl.org/dc/elements/1.1/title> ?title . }
OPTIONAL { ?source dewapp:DocumentPublishedOn ?publishDate . }
OPTIONAL { ?source dewapp:DocumentTitleClassification ?docTitlePm . }
OPTIONAL { ?source dewapp:DocumentId ?docId .
OPTIONAL { ?docId <http://purl.org/dc/elements/1.1/title> ?relTitle . }
OPTIONAL { ?docId dewapp:DocumentTitleClassification ?relPm . }
OPTIONAL { ?docId dewapp:DocumentPublishedOn ?relPubDate . } } }
 } } }
 } } UNION { { SELECT ( COUNT( DISTINCT ?source ) AS ?count )
WHERE { GRAPH <http://www.projectdewey.org/branch/master> { { SELECT ?source ?type ?date ?docId ?title ?docText ?docTitlePm ?publishDate ?position ?captionPm ?caption ?textPm ?text ?relTitle ?relPm ?relPubDate
WHERE { { SELECT DISTINCT ?source
WHERE { { ?id dewapp:Destination <http://www.projectdewey.org/Su57> . } UNION { ?id dewapp:Destination <http://www.projectdewey.org/AA10AlamoC> . }
?id a <http://www.projectdewey.org/ontologies/Dewey#Tag> ;
    dewapp:Source ?source . }
 }
?source a ?type .
{ ?source a ?innerType .
FILTER ( ?innerType = <http://www.projectdewey.org/ontologies/Dewey#AtomizedDocument> || ?innerType = <http://www.projectdewey.org/ontologies/Dewey#Document> ) }
?source <http://www.projectdewey.org/createdDate> ?date .
OPTIONAL { ?source dewapp:Text ?text . }
OPTIONAL { ?source dewapp:DocumentText ?docText . }
OPTIONAL { ?source dewapp:Position ?position . }
OPTIONAL { ?source dewapp:PortionMark ?textPm . }
OPTIONAL { ?source dewapp:Caption ?caption . }
OPTIONAL { ?source dewapp:CaptionPortionMark ?captionPm . }
OPTIONAL { ?source <http://purl.org/dc/elements/1.1/title> ?title . }
OPTIONAL { ?source dewapp:DocumentPublishedOn ?publishDate . }
OPTIONAL { ?source dewapp:DocumentTitleClassification ?docTitlePm . }
OPTIONAL { ?source dewapp:DocumentId ?docId .
OPTIONAL { ?docId <http://purl.org/dc/elements/1.1/title> ?relTitle . }
OPTIONAL { ?docId dewapp:DocumentTitleClassification ?relPm . }
OPTIONAL { ?docId dewapp:DocumentPublishedOn ?relPubDate . } } }
 } } }
 } } }
 } }
 } }'''


example2 = '''PREFIX<https://www.w3.org/2001/XMLSchema#dateTime>( SUBSTR( REPLX dewapp: <http://www.projectdewey.org/ontologies/Dewey#>
SELECT DISTINCT ( STR( ?source ) AS ?o_Source ) ( STR( ?type ) AS ?o_type ) ( STR( ?date ) AS ?o_date ) ( STR( ?docId ) AS ?o_docId ) ( STR( ?title ) AS ?o_titl_relPubDate )e ) ( STR( ?docTitlePm ) AS ?o_docTitlePm ) ( STR( <http://www.w3.org/2001/XMLSchema#dateTime>( SUBSTR( REPLACE( STR( ?publishDate ), '', ' ' ), 1, 25 ) )
) AS ?o_publishDate ) ( STR( ?position ) AS ?o_position ) ( STR( ?captionPm ) AS ?o_captionPm ) ( STR( ?caption ) AS ?o_caption ) ( STR( ?textPm ) AS ?o_textPm aption ?textPm ?text ?relTitle ?relPm ?relPubDate
) ( STR( ?text ) AS ?o_text ) ( STR( ?relTitle ) AS ?o_relTitle ) ( STR( ?relPm ) AS ?o_relPm ) ( STR( <http://www.w3.org/2001/XMLSchema#dateTime>( SUBSTR( REPLACE( STR( ?relPubDate ), '', ' ' ), 1, 25 ) ) ) AS ?o_relPubDate )
WHERE { { SELECT ?source ?type ?date ?docId ?title ?docText ?docTitlePm ?publishDate ?position ?captionPm ?caption ?textPm ?text ?relTitle ?relPm ?relPubDate
WHERE { GRAPH <http://www.projectdewey.org/branch/master> { { SELECT ?source ?type ?date ?docId ?title ?docText ?docTitlePm ?publishDate ?position ?captionPm ?caption ?textPm ?text ?relTitle ?relPm ?relPubDate
WHERE { { SELECT DISTINCT ?source
WHERE { ?id dewapp:Destination <http://www.projectdewey.org/Aircraft> .
?id a <http://www.projectdewey.org/ontologies/Dewey#Tag> ;
    dewapp:Source ?source . }
 }
?source a ?type .
?source <http://www.projectdewey.org/createdDate> ?date .
OPTIONAL { ?source dewapp:Text ?text . }
OPTIONAL { ?source dewapp:DocumentText ?docText . }
OPTIONAL { ?source dewapp:Position ?position . }
OPTIONAL { ?source dewapp:PortionMark ?textPm . }
OPTIONAL { ?source dewapp:Caption ?caption . }
OPTIONAL { ?source dewapp:CaptionPortionMark ?captionPm . }
OPTIONAL { ?source <http://purl.org/dc/elements/1.1/title> ?title . }
OPTIONAL { ?source dewapp:DocumentPublishedOn ?publishDate . }
OPTIONAL { ?source dewapp:DocumentTitleClassification ?docTitlePm . }
OPTIONAL { ?source dewapp:DocumentId ?docId .
OPTIONAL { ?docId <http://purl.org/dc/elements/1.1/title> ?relTitle . }
OPTIONAL { ?docId dewapp:DocumentTitleClassification ?relPm . }
OPTIONAL { ?docId dewapp:DocumentPublishedOn ?relPubDate . } } }
ORDER BY DESC( COALESCE( ?relPubDate, ?publishDate, ?date ) )
 } } }
LIMIT 10
OFFSET}}'''


def addTabs(tabsC):
    tabs = ''
    for tab in range(tabsC):
        tabs += '    '
    return tabs


def countBackTrack(text, start, end, target):
    count = ''
    # if start == -1 or start == 0:
    #     return ''
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
    replacedTxt = parsedText

    # indent first SELECT
    select_pos = replacedTxt.find('SELECT')
    replacedTxt = replacedTxt[:select_pos] + '\n' + replacedTxt[select_pos:]

    goodText = indentSpecialWords(replacedTxt)
    # w = create file or override file if file exists
    # x = create file
    f = open('sparqlQuery.txt', 'w')
    f.write(goodText)


goodText = ''
parse(example2)
