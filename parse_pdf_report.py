import sys, json, re

def success_warning_failure(key, source):
    """ For CHECKPOINT PASSED WARNED FAILED lines in the source, extract as dictionaries, adding a Total """
    regexp = re.compile(rf'^{key}\s+(-|[0-9]+)\s+(-|[0-9]+)\s+(-|[0-9]+)$', re.MULTILINE)
    matches = regexp.search(source)
    keys = ['Success', 'Warning', 'Failure']
    if matches:
        total = 0
        out = {}
        for index, name in enumerate(keys):
            value = 0 if matches.group(index + 1) == '-' else int(matches.group(index + 1))
            out[name] = value
            total += value
        out['Total'] = total
        return out
    else:
        return None

def text_between(start, end, source):
    """ Given a regex for patterns before and after a string in the source, return the content between the regexs """
    regexp = re.compile(rf'{start}(.*?){end}', re.MULTILINE | re.DOTALL)
    matches = regexp.search(source)
    if matches:
        return ''.join(matches.group(1).splitlines())
    return None

def main():
    """ Given the pdftext output of a PAC 2026 PDF, find interesting metrics and reformat them as JSON """
    """ The JSON will have two sections: metadata as key-value pairs, and checks as success/wanring/failure/total counts """
    report = sys.stdin.read()
    checks = [ "PDF Syntax", "Fonts", "Content", "Embedded Files", "Natural language", "Structure elements", "Structure tree", "Role mapping", "Alternative Descriptions", "Metadata", "Document settings" ]

    output = {'checks': {} }
    for check in checks:
        result = success_warning_failure(check, report)
        if result:
            output['checks'][check] = result
    output['metadata'] = {
        'Title': text_between('^Title$', '^Filename$', report),
        'Filename': text_between('^Filename$', '^Language Tags Pages Size$', report),
        'Language': text_between('^Language Tags Pages Size$', ' [0-9(-]+', report),
        'PDF/UA': 'Yes' if report.find("This PDF file is PDF/UA compliant.") != -1 else 'No'
    }
    print(json.dumps(output))

if __name__ == '__main__':
    main()
