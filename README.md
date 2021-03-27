# Taxopedia

Build taxonomic trees (cladograms) from Wikipedia-scraped data.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install
taxopedia.

```bash
pip install taxopedia
```

## Getting Started

```python
import taxopedia

# create a tree... and get a bag of parsed biota boxes!
tree, bag = taxopedia.search("Bears")

# pretty print the tree
print(tree.pretty())

# export multiple formats
tree.to_txt("Ursidae.txt")    # plain-text dendrogram
tree.to_html("Ursidae.html")  # diagram with images
tree.to_csv("Ursidae.csv")    # filled-out tabular data
```

## Saving and Loading Progress

```py
# save the biota bag (so you don't have to scrape it again!)
taxopedia.dump_bag("bag.json", bag)

# loading the biota bag
bag = taxopedia.load_bag("bag.json")

# how to get a tree from a bag
tree = taxopedia.make_tree(bag)
```

## Example Output

The plain-text dedrogram is as follows. See `docs` folder for an example CSV
and HTML file as well.

```txt
Kingdom: Animalia
└── Phylum: Chordata
    └── Class: Mammalia
        └── Order: Carnivora
            └── Suborder: Caniformia (Caniforms)
                └── Infraorder: Arctoidea
                    └── Family: Ursidae (Bears)
                        ├── Subfamily: Ailuropodinae
                        │   ├── Genus: Ailuropoda (Panda)
                        │   │   ├── Species: A. melanoleuca (Giant panda)
                        │   │   │   └── Subspecies: A. m. qinlingensis (Qinling panda/Brown panda)
                        │   │   ├── Species: A. baconi
                        │   │   └── Species: A. microta
                        │   ├── Tribe: † Indarctini
                        │   │   └── Genus: † Indarctos
                        │   └── Genus: † Miomaci
                        ├── Subfamily: Tremarctinae
                        │   ├── Genus: Tremarctos
                        │   │   ├── Species: T. ornatus (Spectacled bear)
                        │   │   └── Species: † T. floridanus
                        │   ├── Genus: Plionarctos
                        │   ├── Genus: † Arctodus (Short-faced bear)
                        │   └── Genus: † Arctotherium
                        ├── Subfamily: † Hemicyoninae
                        │   ├── Genus: † Cephalogale
                        │   ├── Genus: † Dinocyon
                        │   ├── Genus: † Hemicyon
                        │   ├── Genus: † Phoberocyon
                        │   ├── Genus: † Phoberogale
                        │   └── Genus: † Plithocyon
                        ├── Genus: Ursus
                        │   ├── Species: U. arctos (Brown bear)
                        │   │   ├── Subspecies: U. a. arctos (Eurasian brown bear)
                        │   │   └── Subspecies: U. a. middendorffi / horribilis (Kodiak bear)
                        │   ├── Species: U. americanus (American black bear)
                        │   ├── Species: U. maritimus (Polar bear)
                        │   └── Species: U. thibetanus (Asian black bear)
                        ├── Subfamily: Ursinae
                        │   ├── Genus: Helarctos
                        │   │   └── Species: H. malayanus (Sun bear)
                        │   └── Genus: Melursus
                        │       └── Species: M. ursinus (Sloth bear)
                        ├── Subfamily: † Ursavinae
                        │   └── Tribe: † Ursavini
                        │       └── Genus: † Ursavus
                        ├── Subfamily: † Agriotheriinae
                        │   └── Genus: † Agriotherium
                        ├── Tribe: Ailuropodini
                        │   └── Genus: † Ailurarctos
                        ├── Genus: † Kretzoiarctos
                        │   └── Species: † K. beatrix
                        └── Genus: † Zaragocyon
                            └── Species: † Z. daamsi (Zaragocyon)
```

## License

[MIT](https://choosealicense.com/licenses/mit/)
