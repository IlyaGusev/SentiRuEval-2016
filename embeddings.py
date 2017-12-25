from vocabulary import Vocabulary
import numpy as np

FAT_FILE = "/media/yallen/My Passport/Models/senti-2016-w2v.txt"


def shrink_w2v(input_filename, output_filename, vocab_filename):
    vocabulary = Vocabulary(vocab_filename)

    with open(input_filename, "r", encoding='utf-8') as r:
        line = next(r)
        dimension = int(line.strip().split()[1])
        vocabulary_embeddings = dict()
        all_count = 0
        found_count = 0
        words = set(vocabulary.word_to_index.keys())
        while True:
            try:
                print(all_count, found_count, len(words))
                line = next(r)
                try:
                    current_word = line.split()[0]
                    if current_word in words:
                        new_embedding = [float(i) for i in line.strip().split()[1:]]
                        vocabulary_embeddings[vocabulary.word_to_index[current_word]] = new_embedding
                        words.remove(current_word)
                        found_count += 1
                except ValueError:
                    pass
                all_count += 1
            except UnicodeDecodeError:
                pass
            except StopIteration:
                break
    with open(output_filename, "w", encoding='utf-8') as w:
        w.write(str(len(vocabulary_embeddings.items())) + " " + str(dimension) + "\n")
        for i, word in enumerate(vocabulary.index_to_word):
            if i in vocabulary_embeddings:
                w.write(word + " " + " ".join([str(i) for i in list(vocabulary_embeddings[i])]) + "\n")

shrink_w2v(FAT_FILE, "pickles/banks_w2v.txt", "pickles/banks_vocab.pickle")
