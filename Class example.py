class Vowel_class:
    vowels = "aeiouAEIOU"

    def vowel_check(self, input_string):
        if any((c in self.vowels) for c in input_string):
            return True
        else:
            return False

vowel_checker = Vowel_class()

test_string = "ggfdgfd"

print(str(vowel_checker.vowel_check(test_string)))