def intro():
    import random
    jobs_perBiom = {"forest": ["Branch of the Elren tree", "The beast of Screams","Missing Dorothey", "Help the Outpost"],
            "city": ["Metersen lost treasure", "Grocher the wicked", "The captive beauty", "The breached crypt"],
            "mountains": ["Heart of the mountain", "Dragon of Ingsuth", "Missing miners", "Help the Skytemple"]}
    aquest = random.choice(jobs_perBiom["forest"])
    bquest = random.choice(jobs_perBiom["city"])
    cquest = random.choice(jobs_perBiom["mountains"])
    start_text = """
    ======================================================
     GGG   RRRR     A    Y   Y    A    RRRR    CCC   H   H
    G   G  R   R   A A    Y Y    A A   R   R  C   C  H   H
    G      R   R  A   A    Y    A   A  R   R  C      H   H
    GGGGG  RRRR   AAAAA    Y    AAAAA  RRRR   C      HHHHH
    G   G  R R    A   A    Y    A   A  R R    C      H   H
    G   G  R  R   A   A    Y    A   A  R  R   C   C  H   H
     GGG   R   R  A   A    Y    A   A  R   R   CCC   H   H
    ======================================================
    
    Welcome to the land of Grayarch. As a young adventurer
    you are looking for new work in every tavern you'r
    travels take you.
    
    You come to the notice bord and see three suitable
    and interesting jobs.
    1) {a}
    2) {b}
    3) {c}
    """.format(a=aquest, b=bquest, c=cquest)
    return start_text, aquest, bquest, cquest