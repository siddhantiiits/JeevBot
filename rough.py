# importing the module
from englisttohindi.englisttohindi import EngtoHindi



def e2h(message):
    res = EngtoHindi(message)
    r = res.convert
    return r

# displaying the translation
print(e2h('hello'))

