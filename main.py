from artifact import Artifact, Painting, Sculpture, give_name_artifact
from renaissance import paint, sculpture, building


def give_name_main():
    return f"main name: {__name__}"


if __name__ == "__main__":
    a1 = Artifact("a1", 1598)
    a2 = Artifact("a2", 1958)
    a3 = Artifact("a3", 1002)

    p1 = Painting("p1", 1587, "art1", "oil")
    p2 = Painting("p2", 902, "art2", "pastel")
    p3 = Painting("p3", 1877, "art3", "crayon")

    s1 = Sculpture("s1", 1950, "marble", 15)
    s2 = Sculpture("s2", 1801, "bronze", 100)

    r1 = paint
    r2 = sculpture
    r3 = building
    print(f"{s1.is_old(10)=}")
    print(give_name_artifact())
    print(f'{give_name_main()}\n')
    print("Let's see my renaissance Collection")
    print("---------- \n")
    print(f"{r1}\n")
    print(f"{r2}\n")
    print(f"{r3}\n")
    print("-----------")
    print(__name__)
