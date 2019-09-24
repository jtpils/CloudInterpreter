import CloudInterpreter
import OctreeFormatTools as oft

# pensa tre volte, programma una

if __name__ == '__main__':
    # classes = {
    #     1: "albero",
    #     2: "casa",
    #     3: "stalla",
    #     4: "auto",
    #     5: "computer",
    #     6: "mouse",
    #     7: "strada",
    #     8: "ristorante",
    #     9: "pavimento",
    #     10: "cascata",
    #     11: "ripostiglio",
    #     12: "sedia",
    # }
    #
    # gen = oft.Generator("/home/nicholas/Projects/NuvoleDiPunti/EsempiNuvole/marketplacefeldkirch.txt", "xyzirgb", classes)
    # octreeDir = gen.parse()

    #octreeDir = "/home/nicholas/Projects/NuvoleDiPunti/EsempiNuvole/castleblatten+cOctree/"
    octreeDir = "/home/nicholas/Projects/NuvoleDiPunti/EsempiNuvole/marketplacefeldkirchOctree/"
    octreeDir = "/home/nicholas/Projects/NuvoleDiPunti/EsempiNuvole/whole+cOctree/"
    CloudInterpreter.start(octreeDir, 80)