# lesson4-1, normal

import re

line = 'mtMmEZUOmcqWiryMQhhTxqKdSTKCYEJlEZCsGAMkg' \
       'AYEOmHBSQsSUHKvSfbmxULaysmNOGIPHpEMujalp' \
       'PLNzRWXfwHQqwksrFeipEUlTLeclMwAoktKlfUBJHPs' \
       'nawvjPhfgewVzKTUfSYtBydXaVIpxWjNKgXANv' \
       'IoumesCSSvjEGRJosUfuhRRDUuTQwLlJJJDdkVjfS' \
       'AHqnLxooisBDWuxIhyjJaXDYwdoVPnsllMngNlmkp' \
       'YOlqXEFIxPqqqgAWdJsOvqppOfyIVjXapzGOrfinz' \
       'zsNMtBIOclwbfRzytmDgEFUzxvZGkdOaQYLVBfsGSA' \
       'fJMchgBWAsGnBnWetekUTVuPluKRMQsdelzBgLzuwii' \
       'mqkFKpyQRzOUyHkXRkdyIEBvTjdByCfkVIAQaAb' \
       'fCvzQWrMMsYpLtdqRltXPqcSMXJIvlBzKoQnSwPFka' \
       'pxGqnZCVFfKRLUIGBLOwhchWCdJbRuXbJrwTRNyA' \
       'xDctszKjSnndaFkcBZmJZWjUeYMdevHhBJMBSShDqb' \
       'jAuDGTTrSXZywYkmjCCEUZShGofaFpuespaZWLFN' \
       'IsOqsIRLexWqTXsOaScgnsUKsJxiihwsCdBViEQBHQa' \
       'OnLfBtQQShTYHFqrvpVFiiEFMcIFTrTkIBpGUf' \
       'lwTvAzMUtmSQQZGHlmQKJndiAXbIzVkGSeuTSkyjIGsiW' \
       'LALHUCsnQtiOtrbQOQunurZgHFiZjWtZCEXZC' \
       'nZjLeMiFlxnPkqfJFbCfKCuUJmGYJZPpRBFNLkqigxF' \
       'krRAppYRXeSCBxbGvqHmlsSZMWSVQyzenWoGxy' \
       'GPvbnhWHuXBqHFjvihuNGEEFsfnMXTfptvIOlhKhyYwx' \
       'LnqOsBdGvnuyEZIheApQGOXWeXoLWiDQNJFaXi' \
       'UWgsKQrDOeZoNlZNRvHnLgCmysUeKnVJXPFIzvdDyleXyln' \
       'KBfLCjLHntltignbQoiQzTYwZAiRwycdlHfyHNGmkNqSwXUrxGc'

# 1------------------------------------------------

pattern = '([a-z])[A-Z]+([a-z])'

found = [' '.join(letters) for letters in re.findall(pattern, line)]
result1 = ' '.join(found)

# 2------------------------------------------------

alt_found = []
ispattern = False
last_index_found = 0
i = 0

for letter in line:
    prev_letter = line[line.index(letter, i)-1]
    if (letter.isupper() and
       prev_letter.islower() and
       last_index_found != i and
       not ispattern):
        ispattern = True
        alt_found.append(prev_letter)

    if (letter.islower() and
       prev_letter.isupper() and
       ispattern):
        ispattern = False
        last_index_found = i+1
        alt_found.append(letter)

    if i == len(line)-1 and ispattern:
        alt_found.pop()

    i += 1

result2 = ' '.join(alt_found)

print('well done!' if result1 == result2 else 'we have a problem...')
