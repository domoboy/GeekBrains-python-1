# lesson 4-2, normal

import re

line = 'mtMmEZUOmcqWiryMQhhTxqKdSTKCYEJlEZCsGAMkgA' \
       'YEOmHBSQsSUHKvSfbmxULaysmNOGIPHpEMujalp' \
       'PLNzRWXfwHQqwksrFeipEUlTLeclMwAoktKlfUBJHPsnawv' \
       'jPhfgewVzKTUfSYtBydXaVIpxWjNKgXANv' \
       'IoumesCSSvjEGRJosUfuhRRDUuTQwLlJJJDdkVjfSAHqnLxooisBD'\
       'WuxIhyjJaXDYwdoVPnsllMngNlmkp' \
       'YOlqXEFIxPqqqgAWdJsOvqppOfyIVjXapzGOrf'\
       'inzzsNMtBIOclwbfRzytmDgEFUzxvZGkdOaQYLVBfsGSA' \
       'fJMchgBWAsGnBnWetekUTVuPluKRMQsdelzBgLzuwi'\
       'imqkFKpyQRzOUyHkXRkdyIEBvTjdByCfkVIAQaAb' \
       'fCvzQWrMMsYpLtdqRltXPqcSMXJIvlBzKoQnSwPF'\
       'kapxGqnZCVFfKRLUIGBLOwhchWCdJbRuXbJrwTRNyA' \
       'xDctszKjSnndaFkcBZmJZWjUeYMdevHhBJMBSShDqbjA'\
       'uDGTTrSXZywYkmjCCEUZShGofaFpuespaZWLFN' \
       'IsOqsIRLexWqTXsOaScgnsUKsJxiihwsCdBViEQBHQaOnL'\
       'fBtQQShTYHFqrvpVFiiEFMcIFTrTkIBpGUf' \
       'lwTvAzMUtmSQQZGHlmQKJndiAXbIzVkGSeuTSkyjIGs'\
       'iWLALHUCsnQtiOtrbQOQunurZgHFiZjWtZCEXZC' \
       'nZjLeMiFlxnPkqfJFbCfKCuUJmGYJZPpRBFNLkqigxF'\
       'krRAppYRXeSCBxbGvqHmlsSZMWSVQyzenWoGxy' \
       'GPvbnhWHuXBqHFjvihuNGEEFsfnMXTfptvIOlhKh'\
       'yYwxLnqOsBdGvnuyEZIheApQGOXWeXoLWiDQNJFaXi' \
       'UWgsKQrDOeZoNlZNRvHnLgCmysUeKnVJXPFIzvdDyle'\
       'XylnKBfLCjLHntltignbQoiQzTYwZAiRwycdlHfyHNGmkNqSwXUrxGC'

# 1----------------------------------------

pattern = '([A-Z])[a-z]{2}.*?[A-Z]{2}([A-Z])'

found = [' '.join(letters) for letters in re.findall(pattern, line)]
result1 = ' '.join(found)

# 2----------------------------------------

alt_found = []
ispattern = False
last_index_found = 0
i = 0

for letter in line:
    next_two_letters = (line[line.index(line[i+1], i+1)] +
                        line[line.index(line[i+2], i+2)] if
                        line.index(letter, i) < len(line)-2 else
                        'Nothing')
    right_letter = (line[line.index(line[i+3], i+3)] if
                    line.index(letter, i) < len(line)-3 else
                    'Nothing')

    if (not ispattern and
       i != last_index_found and
       letter.isupper() and
       next_two_letters.islower()):
        ispattern = True
        alt_found.append(letter)

    if (ispattern and
       next_two_letters.isupper() and
       right_letter.isupper()):
        ispattern = False
        last_index_found = i + 3
        alt_found.append(right_letter)

    if i == len(line)-1 and ispattern:
        alt_found.pop()

    i += 1

result2 = ' '.join(alt_found)

print('well done!' if result1 == result2 else 'we have a problem...')
