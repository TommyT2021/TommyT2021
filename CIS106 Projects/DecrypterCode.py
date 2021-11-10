#the Shift Dictionary and Apply Shift
class Message(object):
    def __init__(self, text):
        self.message_text = text
        self.valid_words = load_words(WORDLIST_FILENAME)

    def get_message_text(self):
        return self.message_text

    def get_valid_words(self):
        return self.valid_words[:]
        
    def build_shift_dict(self, shift):
        shifted =  {}
        abc = string.ascii_letters
        for letter in abc:
            index = abc.find(letter.lower())
            shifted_index = (shift + index) % 26
            nletter = abc[shifted_index]
            if letter == letter.upper():
                nletter = nletter.upper()
            shifted[letter] = nletter
        return shifted

    def apply_shift(self, shift):
        nmessage = ""
        shifted = self.build_shift_dict(shift)
        getText = Message.get_message_text(self)
        for character in getText:
            if character in getText:
                if character in shifted:
                    nmessage += shifted[character]
                else:
                    nmessage += character
        return nmessage

#PlaintextMessage
class PlaintextMessage(Message):
    def __init__(self, text, shift):
        self.message_text = text
        self.shift = shift
        self.encrypting_dict = self.build_shift_dict(shift)
        self.message_text_encrypted = self.apply_shift(shift)

    def get_shift(self):
        return self.shift  
        
    def get_encrypting_dict(self):
        return self.encrypting_dict.copy()
      
    def get_message_text_encrypted(self):
        return self.message_text_encrypted

    def change_shift(self, shift):
        self.shift = shift
        self.encrypting_dict = self.build_shift_dict(shift)
        self.message_text_encrypted = self.apply_shift(shift)
        
#CiphertextMessage
        class CiphertextMessage(Message):
    def __init__(self, text):
        self.message_text = text
        self.valid_words = load_words(WORDLIST_FILENAME)


    def decrypt_message(self):
        bestS = 0
        mDW = 0
        for i in range (26):
            decryptedM = self.apply_shift(i)
            decryptedW = decryptedM.split()
            validW = 0
            for w in decryptedW:
                if is_word(self.valid_words, w):
                    validW +=1
            if validW > mDW:
                mDW = validW
                bestS = i
        return (bestS, self.apply_shift(bestS))

#Decrypt a Story
def decrypt_story():
    story = CiphertextMessage(get_story_string())
    return story.decrypt_message()
