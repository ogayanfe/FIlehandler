import argparse

parser = argparse.ArgumentParser(description='This scripts helps you to perform basic operations with files')
parser.add_argument('file', type=str, help='Name of the file {')
parser.add_argument('--count', '-c', default=False, help='count the number of words in file')
parser.add_argument('--show', '-sh', default=False, help='switch this to true to show the results')
parser.add_argument('--search', '-s', type=str, help='type word to search for word')
args = parser.parse_args()

try:
    file_hand = open(args.file, 'r')
except FileNotFoundError:
    print(F'{args.file} does not exist')
    print('Note: specify a file that occurs in this directory or their exact path')
    quit()


class FileHandler:
    def __init__(self):
        self.dictionary = dict()
        self.no_of_words = 0

    def count_words(self):
        for line in file_hand:
            words = line.lower().split()
            self.no_of_words += len(words)
            for word in words:
                self.dictionary[word] = self.dictionary.get(word, 0) + 1
        print(f'There are {self.no_of_words} number of words in {args.file}.')
        if args.show:
            self.show_words()
        file_hand.close()

    def show_words(self):
        sort = [(v, k) for k, v in self.dictionary.items()]
        print(f'\nThere are {len(self.dictionary.keys())} unique words in the file.')
        print(f'\n"{(sorted(sort, reverse=True))[0][1]}" is the most occurring word with '
              f'"{(sorted(sort, reverse=True))[0][0]}" appearances.\n')
        print(sorted(sort))

    def search(self, word):
        row = 0
        occurrences = 0
        file = open(args.file, 'r')
        for line in file:
            row += 1
            for x in line.lower().split():
                if x == word.lower():
                    occurrences += 1
                    if args.show:
                        print(f'Line {row}: {line}')
        if occurrences > 0:
            print(F'"{word}" occurs in file {occurrences} times')
        else:
            print(f'"{word}" does not occur in file.\nTry checking spellings or typo and try again')
        file.close()

    def main(self):
        if args.count:
            self.count_words()
        if args.search is not None:
            self.search(args.search)


if __name__ == '__main__':
    summoned = FileHandler()
    summoned.main()
