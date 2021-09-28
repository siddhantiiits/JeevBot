# importing the module
from englisttohindi.englisttohindi import EngtoHindi



def e2h(message):
    res = EngtoHindi(message)
    p = res.convert
    return p

r = 'hello'

# displaying the translation
print(e2h(r))

