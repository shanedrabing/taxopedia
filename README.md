# Taxopedia

Build taxonomic trees (cladograms) from Wikipedia-scraped data.

## Example Usage

```python
import taxopedia

# scrape the data
TAXA = "Hominidae"
links_dict = taxopedia.search(TAXA, comprehensive=False)

# link the pages
csv_name = f"{TAXA}.csv"
data = taxopedia.linker(links_dict, filename=csv_name)

# explore the tree
tree = taxopedia.WikiTree.from_csv(csv_name)  # load from a slim CSV
tree.view(with_color=True)  # view in color console (UNIX, VS Code)

# export to file
tree.to_csv(f"{TAXA}_full.csv")  # saves a filled-in CSV
tree.to_txt(f"{TAXA}.txt")  # saves a dendrogram
```

## Example Output (Tree.to_txt)

```txt
Kingdom : Animalia
└── Phylum : Chordata
    └── Class : Mammalia
        └── Magnorder : Boreoeutheria
            └── Grandorder : Euarchonta
                └── Mirorder : Primatomorpha
                    └── Superorder : Euarchontoglires
                        └── Order : Primates
                            └── Parvorder : Catarrhini
                                └── Suborder : Haplorhini
                                    └── Infraorder : Simiiformes
                                        └── Superfamily : Hominoidea (Hominoids or apes)
                                            ├── Family : Hominidae
                                            │   ├── Subfamily : Homininae
                                            │   │   ├── Tribe : Hominini
                                            │   │   │   ├── Genus : Homo
                                            │   │   │   │   ├── Species : †H. erectus
                                            │   │   │   │   │   ├── Subspecies : †H. e. erectus
                                            │   │   │   │   │   └── Subspecies : †H. e. pekinensis (Peking man)
                                            │   │   │   │   ├── Species : H. erectus
                                            │   │   │   │   │   └── Subspecies : H. e. soloensis (Solo Man)
                                            │   │   │   │   ├── Species : H. sapiens
                                            │   │   │   │   │   └── Subspecies : H. s. idaltu
                                            │   │   │   │   ├── Species : Homo erectus
                                            │   │   │   │   ├── Species : Homo sapiens (Human)
                                            │   │   │   │   ├── Species : †Homo antecessor
                                            │   │   │   │   ├── Species : †Homo ergaster
                                            │   │   │   │   ├── Species : †Homo floresiensis
                                            │   │   │   │   ├── Species : †Homo habilis
                                            │   │   │   │   ├── Species : †Homo heidelbergensis
                                            │   │   │   │   ├── Species : †Homo luzonensis
                                            │   │   │   │   ├── Species : †Homo naledi
                                            │   │   │   │   ├── Species : †Homo neanderthalensis (Neanderthal)
                                            │   │   │   │   ├── Species : †Homo rhodesiensis
                                            │   │   │   │   └── Species : †Homo rudolfensis
                                            │   │   │   ├── Subtribe : Australopithecina (Australopiths)
                                            │   │   │   │   ├── Genus : Australopithecus
                                            │   │   │   │   │   ├── Species : Australopithecus afarensis
                                            │   │   │   │   │   ├── Species : Australopithecus africanus
                                            │   │   │   │   │   ├── Species : Australopithecus deyiremeda
                                            │   │   │   │   │   ├── Species : Australopithecus garhi
                                            │   │   │   │   │   ├── Species : Australopithecus sediba
                                            │   │   │   │   │   ├── Species : †Australopithecus anamensis
                                            │   │   │   │   │   └── Species : †Australopithecus bahrelghazali
                                            │   │   │   │   └── Genus : †Paranthropus
                                            │   │   │   │       ├── Species : †P. aethiopicus
                                            │   │   │   │       ├── Species : †P. boisei
                                            │   │   │   │       └── Species : †P. robustus
                                            │   │   │   ├── Subtribe : Panina
                                            │   │   │   │   └── Genus : Pan (Chimpanzees and bonobos)
                                            │   │   │   │       ├── Species : P. troglodytes
                                            │   │   │   │       │   ├── Subspecies : P. t. ellioti (Nigeria-Cameroon chimpanzee)
                                            │   │   │   │       │   ├── Subspecies : P. t. schweinfurthii (Eastern chimpanzee)
                                            │   │   │   │       │   ├── Subspecies : P. t. troglodytes (Central chimpanzee)
                                            │   │   │   │       │   └── Subspecies : P. t. verus (Western chimpanzee)
                                            │   │   │   │       ├── Species : Pan paniscus (Bonobo)
                                            │   │   │   │       └── Species : Pan troglodytes (Chimpanzee)
                                            │   │   │   ├── Subtribe : Hominina
                                            │   │   │   │   └── Genus : †Ardipithecus
                                            │   │   │   │       ├── Species : †A. kadabba
                                            │   │   │   │       └── Species : †A. ramidus
                                            │   │   │   ├── Genus : †Orrorin
                                            │   │   │   │   └── Species : †O. tugenensis (Orrorin)
                                            │   │   │   └── Genus : †Kenyanthropus
                                            │   │   ├── Tribe : Gorillini
                                            │   │   │   ├── Genus : Gorilla
                                            │   │   │   │   ├── Species : G. beringei
                                            │   │   │   │   │   ├── Subspecies : G. b. beringei (Mountain gorilla)
                                            │   │   │   │   │   └── Subspecies : G. b. graueri (Eastern lowland gorilla)
                                            │   │   │   │   ├── Species : G. gorilla
                                            │   │   │   │   │   ├── Subspecies : G. g. diehli (Cross River gorilla)
                                            │   │   │   │   │   └── Subspecies : G. g. gorilla
                                            │   │   │   │   ├── Species : Gorilla beringei (Eastern gorilla)
                                            │   │   │   │   └── Species : Gorilla gorilla
                                            │   │   │   └── Genus : †Chororapithecus
                                            │   │   │       └── Species : †C. abyssinicus (Chororapithecus)
                                            │   │   └── Tribe : †Graecopithecini
                                            │   │       ├── Genus : †Ouranopithecus
                                            │   │       │   ├── Species : †O. macedoniensis
                                            │   │       │   └── Species : †O. turkae
                                            │   │       └── Genus : †Graecopithecus
                                            │   ├── Subfamily : Ponginae
                                            │   │   ├── Tribe : †Sivapithecini
                                            │   │   │   ├── Genus : †Ankarapithecus
                                            │   │   │   │   └── Species : †A. meteai (Ankarapithecus)
                                            │   │   │   ├── Genus : †Gigantopithecus
                                            │   │   │   │   └── Species : †G. blacki (Gigantopithecus)
                                            │   │   │   └── Genus : †Sivapithecus
                                            │   │   ├── Genus : Pongo (Orangutans)
                                            │   │   │   ├── Species : Pongo abelii (Sumatran orangutan)
                                            │   │   │   ├── Species : Pongo pygmaeus (Bornean orangutan)
                                            │   │   │   ├── Species : Pongo tapanuliensis (Tapanuli orangutan)
                                            │   │   │   └── Species : †Pongo hooijeri
                                            │   │   └── Tribe : Pongini
                                            │   │       └── Genus : †Khoratpithecus
                                            │   ├── Subfamily : †Dryopithecinae
                                            │   │   ├── Tribe : †Kenyapithecini
                                            │   │   │   ├── Genus : †Griphopithecus
                                            │   │   │   │   ├── Species : †G. alpani
                                            │   │   │   │   └── Species : †G. suessi
                                            │   │   │   └── Genus : †Kenyapithecus
                                            │   │   │       └── Species : †K. wickeri
                                            │   │   └── Tribe : †Afropithecini
                                            │   │       └── Genus : †Otavipithecus
                                            │   │           └── Species : †O. namibiensis (Otavipithecus)
                                            │   ├── Tribe : †Dryopithecini
                                            │   │   ├── Genus : †Anoiapithecus
                                            │   │   │   └── Species : †A. brevirostris (Anoiapithecus)
                                            │   │   ├── Genus : †Danuvius
                                            │   │   │   └── Species : †D. guggenmosi
                                            │   │   ├── Genus : †Rudapithecus
                                            │   │   │   └── Species : †R. hungaricus (Rudapithecus)
                                            │   │   └── Genus : †Dryopithecus
                                            │   ├── Subfamily : incertae sedis
                                            │   │   └── Genus : †Sahelanthropus
                                            │   │       └── Species : †S. tchadensis
                                            │   ├── Genus : †Nakalipithecus
                                            │   │   └── Species : †N. nakayamai (Nakalipithecus)
                                            │   └── Tribe : †Lufengpithecini
                                            │       └── Genus : †Lufengpithecus
                                            └── Family : Hylobatidae (Gibbons)
```
