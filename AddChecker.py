import variables as v


class HayvanCheck:
    def trueFalse(text):
        if(text == "evet"):
            return True
        else:
            return False

    def isThere(text):
        for i in v.hayvanObjList:
            if(i.kimlikNum == text):
                return True
        return False
