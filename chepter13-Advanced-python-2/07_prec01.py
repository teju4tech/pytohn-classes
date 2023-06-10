'''creat two virtual Enviroments,install few packages
   in the first one .How do you create a similar Env
   in the second one?
'''
# Cammand: python -m venv En1
# at prompt
'''See in  file bar there is a Virtual Enviroment is created
   Name:En1
   cammand: .\En1\Scripts\Activate.ps1
   We got Error:
'''

'''File C:\Users\csp\Documents\DATA-STRUCTURE & ALGO\Python-Expo\Python-classes\En1\Scripts\Activate.ps1 cannot be lo
aded because the execution of scripts is disabled on this system. Please see "get-help about_signing" for more det
ails.
At line:1 char:27
+ .\En1\Scripts\Activate.ps1 <<<< 
    + CategoryInfo          : NotSpecified: (:) [], PSSecurityException
    + FullyQualifiedErrorId : RuntimeException
'''

''' Cammand: pip freeze > requirement.txt
    this cmd make txt.flie 4 reqiurments
'''