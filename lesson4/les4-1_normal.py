# lesson4-1, normal

import re

# 1------------------------------------------------

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

pattern1 = '[a-z][A-Z]+[a-z]'
pattern2 = '[a-z]+'

found = re.findall(pattern1, line)
result1 = [' '.join(re.findall(pattern2, letters)) for letters in found]
result1 = ' '.join(result1)

# 2------------------------------------------------

i = 0
last_append_index = 0
alt_found = []
ispattern = False

for letter in line:
    prev_letter = line[line.index(letter, i)-1]
    if (letter.isupper() and
        prev_letter.islower() and
        last_append_index != i and
        not ispattern):
        ispattern = True
        alt_found.append(prev_letter)
           
    if (letter.islower() and
          prev_letter.isupper() and
          ispattern):
        ispattern = False
        last_append_index = i+1
        alt_found.append(letter)
    i += 1

result2 = ' '.join(alt_found)

print('well done!' if result1 == result2 else 'error')











