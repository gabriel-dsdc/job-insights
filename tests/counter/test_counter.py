from src.pre_built.counter import count_ocurrences


def test_counter():
    words_count = {"PyThOn": 1639, "JaVascRiPt": 122}
    for word in words_count.keys():
        counter = count_ocurrences("data/jobs.csv", word)
        assert counter == words_count[word]
