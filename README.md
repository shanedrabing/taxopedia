# Taxopedia

Build taxonomic trees (cladograms) from Wikipedia-scraped data.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install taxopedia.

```bash
pip install taxopedia
```

## Test Script

```python
import taxopedia

# scrape the data, generate a tree
TAXA = "Hominidae"

# (taxa: str,
#  comprehensive: bool) -> WikiTree
tree = taxopedia.centrum(taxa=TAXA,
                         comprehensive=False)

# export the tree
tree.to_csv(f"{TAXA}_full.csv")  # saves a filled-out csv
tree.to_txt(f"{TAXA}_tree.txt")  # saves a dendrogram
```

## Example Output

<details>
  <summary>WikiTree.to_txt</summary>

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

</details>

<details>
  <summary>WikiTree.to_csv</summary>

```txt
Rank       Common.Name                  Kingdom  Phylum   Class    Mirorder      Order    Parvorder  Suborder   Infraorder  Superfamily Family     Subfamily       Tribe            Subtribe          Genus            Species                         Subspecies
Kingdom                                 Animalia                                                                                                                                                                                                                           
Phylum                                  Animalia Chordata                                                                                                                                                                                                                  
Class                                   Animalia Chordata Mammalia                                                                                                                                                                                                         
Mirorder                                Animalia Chordata Mammalia Primatomorpha                                                                                                                                                                                           
Order                                   Animalia Chordata Mammalia Primatomorpha Primates                                                                                                                                                                                  
Parvorder                               Animalia Chordata Mammalia Primatomorpha Primates Catarrhini                                                                                                                                                                       
Suborder                                Animalia Chordata Mammalia Primatomorpha Primates Catarrhini Haplorhini                                                                                                                                                            
Infraorder                              Animalia Chordata Mammalia Primatomorpha Primates Catarrhini Haplorhini Simiiformes                                                                                                                                                
Superfamily Hominoids or apes           Animalia Chordata Mammalia Primatomorpha Primates Catarrhini Haplorhini Simiiformes Hominoidea                                                                                                                                     
Family                                  Animalia Chordata Mammalia Primatomorpha Primates Catarrhini Haplorhini Simiiformes Hominoidea Hominidae                                                                                                                           
Subfamily                               Animalia Chordata Mammalia Primatomorpha Primates Catarrhini Haplorhini Simiiformes Hominoidea Hominidae   Homininae                                                                                                               
Tribe                                   Animalia Chordata Mammalia Primatomorpha Primates Catarrhini Haplorhini Simiiformes Hominoidea Hominidae   Homininae       Hominini                                                                                                
Genus                                   Animalia Chordata Mammalia Primatomorpha Primates Catarrhini Haplorhini Simiiformes Hominoidea Hominidae   Homininae       Hominini                           Homo                                                                 
Species                                 Animalia Chordata Mammalia Primatomorpha Primates Catarrhini Haplorhini Simiiformes Hominoidea Hominidae   Homininae       Hominini                           Homo             †H. erectus                                         
Subspecies                              Animalia Chordata Mammalia Primatomorpha Primates Catarrhini Haplorhini Simiiformes Hominoidea Hominidae   Homininae       Hominini                           Homo             †H. erectus                     †H. e. erectus      
Subspecies  Peking man                  Animalia Chordata Mammalia Primatomorpha Primates Catarrhini Haplorhini Simiiformes Hominoidea Hominidae   Homininae       Hominini                           Homo             †H. erectus                     †H. e. pekinensis   
Species                                 Animalia Chordata Mammalia Primatomorpha Primates Catarrhini Haplorhini Simiiformes Hominoidea Hominidae   Homininae       Hominini                           Homo             H. erectus                                          
Subspecies  Solo Man                    Animalia Chordata Mammalia Primatomorpha Primates Catarrhini Haplorhini Simiiformes Hominoidea Hominidae   Homininae       Hominini                           Homo             H. erectus                      H. e. soloensis     
Species                                 Animalia Chordata Mammalia Primatomorpha Primates Catarrhini Haplorhini Simiiformes Hominoidea Hominidae   Homininae       Hominini                           Homo             H. sapiens                                          
Subspecies                              Animalia Chordata Mammalia Primatomorpha Primates Catarrhini Haplorhini Simiiformes Hominoidea Hominidae   Homininae       Hominini                           Homo             H. sapiens                      †H. s. idaltu       
Species                                 Animalia Chordata Mammalia Primatomorpha Primates Catarrhini Haplorhini Simiiformes Hominoidea Hominidae   Homininae       Hominini                           Homo             Homo erectus                                        
Species     Human                       Animalia Chordata Mammalia Primatomorpha Primates Catarrhini Haplorhini Simiiformes Hominoidea Hominidae   Homininae       Hominini                           Homo             Homo sapiens                                        
Species                                 Animalia Chordata Mammalia Primatomorpha Primates Catarrhini Haplorhini Simiiformes Hominoidea Hominidae   Homininae       Hominini                           Homo             †Homo antecessor                                    
Species                                 Animalia Chordata Mammalia Primatomorpha Primates Catarrhini Haplorhini Simiiformes Hominoidea Hominidae   Homininae       Hominini                           Homo             †Homo ergaster                                      
Species                                 Animalia Chordata Mammalia Primatomorpha Primates Catarrhini Haplorhini Simiiformes Hominoidea Hominidae   Homininae       Hominini                           Homo             †Homo floresiensis                                  
Species                                 Animalia Chordata Mammalia Primatomorpha Primates Catarrhini Haplorhini Simiiformes Hominoidea Hominidae   Homininae       Hominini                           Homo             †Homo habilis                                       
Species                                 Animalia Chordata Mammalia Primatomorpha Primates Catarrhini Haplorhini Simiiformes Hominoidea Hominidae   Homininae       Hominini                           Homo             †Homo heidelbergensis                               
Species                                 Animalia Chordata Mammalia Primatomorpha Primates Catarrhini Haplorhini Simiiformes Hominoidea Hominidae   Homininae       Hominini                           Homo             †Homo luzonensis                                    
Species                                 Animalia Chordata Mammalia Primatomorpha Primates Catarrhini Haplorhini Simiiformes Hominoidea Hominidae   Homininae       Hominini                           Homo             †Homo naledi                                        
Species     Neanderthal                 Animalia Chordata Mammalia Primatomorpha Primates Catarrhini Haplorhini Simiiformes Hominoidea Hominidae   Homininae       Hominini                           Homo             †Homo neanderthalensis                              
Species                                 Animalia Chordata Mammalia Primatomorpha Primates Catarrhini Haplorhini Simiiformes Hominoidea Hominidae   Homininae       Hominini                           Homo             †Homo rhodesiensis                                  
Species                                 Animalia Chordata Mammalia Primatomorpha Primates Catarrhini Haplorhini Simiiformes Hominoidea Hominidae   Homininae       Hominini                           Homo             †Homo rudolfensis                                   
Subtribe    Australopiths               Animalia Chordata Mammalia Primatomorpha Primates Catarrhini Haplorhini Simiiformes Hominoidea Hominidae   Homininae       Hominini         Australopithecina                                                                      
Genus                                   Animalia Chordata Mammalia Primatomorpha Primates Catarrhini Haplorhini Simiiformes Hominoidea Hominidae   Homininae       Hominini         Australopithecina Australopithecus                                                     
Species                                 Animalia Chordata Mammalia Primatomorpha Primates Catarrhini Haplorhini Simiiformes Hominoidea Hominidae   Homininae       Hominini         Australopithecina Australopithecus Australopithecus afarensis                          
Species                                 Animalia Chordata Mammalia Primatomorpha Primates Catarrhini Haplorhini Simiiformes Hominoidea Hominidae   Homininae       Hominini         Australopithecina Australopithecus Australopithecus africanus                          
Species                                 Animalia Chordata Mammalia Primatomorpha Primates Catarrhini Haplorhini Simiiformes Hominoidea Hominidae   Homininae       Hominini         Australopithecina Australopithecus Australopithecus deyiremeda                         
Species                                 Animalia Chordata Mammalia Primatomorpha Primates Catarrhini Haplorhini Simiiformes Hominoidea Hominidae   Homininae       Hominini         Australopithecina Australopithecus Australopithecus garhi                              
Species                                 Animalia Chordata Mammalia Primatomorpha Primates Catarrhini Haplorhini Simiiformes Hominoidea Hominidae   Homininae       Hominini         Australopithecina Australopithecus Australopithecus sediba                             
Species                                 Animalia Chordata Mammalia Primatomorpha Primates Catarrhini Haplorhini Simiiformes Hominoidea Hominidae   Homininae       Hominini         Australopithecina Australopithecus †Australopithecus anamensis                         
Species                                 Animalia Chordata Mammalia Primatomorpha Primates Catarrhini Haplorhini Simiiformes Hominoidea Hominidae   Homininae       Hominini         Australopithecina Australopithecus †Australopithecus bahrelghazali                     
Genus                                   Animalia Chordata Mammalia Primatomorpha Primates Catarrhini Haplorhini Simiiformes Hominoidea Hominidae   Homininae       Hominini         Australopithecina †Paranthropus                                                        
Species                                 Animalia Chordata Mammalia Primatomorpha Primates Catarrhini Haplorhini Simiiformes Hominoidea Hominidae   Homininae       Hominini         Australopithecina †Paranthropus    †P. aethiopicus                                     
Species                                 Animalia Chordata Mammalia Primatomorpha Primates Catarrhini Haplorhini Simiiformes Hominoidea Hominidae   Homininae       Hominini         Australopithecina †Paranthropus    †P. boisei                                          
Species                                 Animalia Chordata Mammalia Primatomorpha Primates Catarrhini Haplorhini Simiiformes Hominoidea Hominidae   Homininae       Hominini         Australopithecina †Paranthropus    †P. robustus                                        
Subtribe                                Animalia Chordata Mammalia Primatomorpha Primates Catarrhini Haplorhini Simiiformes Hominoidea Hominidae   Homininae       Hominini         Panina                                                                                 
Genus       Chimpanzees and bonobos     Animalia Chordata Mammalia Primatomorpha Primates Catarrhini Haplorhini Simiiformes Hominoidea Hominidae   Homininae       Hominini         Panina            Pan                                                                  
Species                                 Animalia Chordata Mammalia Primatomorpha Primates Catarrhini Haplorhini Simiiformes Hominoidea Hominidae   Homininae       Hominini         Panina            Pan              P. troglodytes                                      
Subspecies  Nigeria-Cameroon chimpanzee Animalia Chordata Mammalia Primatomorpha Primates Catarrhini Haplorhini Simiiformes Hominoidea Hominidae   Homininae       Hominini         Panina            Pan              P. troglodytes                  P. t. ellioti       
Subspecies  Eastern chimpanzee          Animalia Chordata Mammalia Primatomorpha Primates Catarrhini Haplorhini Simiiformes Hominoidea Hominidae   Homininae       Hominini         Panina            Pan              P. troglodytes                  P. t. schweinfurthii
Subspecies  Central chimpanzee          Animalia Chordata Mammalia Primatomorpha Primates Catarrhini Haplorhini Simiiformes Hominoidea Hominidae   Homininae       Hominini         Panina            Pan              P. troglodytes                  P. t. troglodytes   
Subspecies  Western chimpanzee          Animalia Chordata Mammalia Primatomorpha Primates Catarrhini Haplorhini Simiiformes Hominoidea Hominidae   Homininae       Hominini         Panina            Pan              P. troglodytes                  P. t. verus         
Species     Bonobo                      Animalia Chordata Mammalia Primatomorpha Primates Catarrhini Haplorhini Simiiformes Hominoidea Hominidae   Homininae       Hominini         Panina            Pan              Pan paniscus                                        
Species     Chimpanzee                  Animalia Chordata Mammalia Primatomorpha Primates Catarrhini Haplorhini Simiiformes Hominoidea Hominidae   Homininae       Hominini         Panina            Pan              Pan troglodytes                                     
Subtribe                                Animalia Chordata Mammalia Primatomorpha Primates Catarrhini Haplorhini Simiiformes Hominoidea Hominidae   Homininae       Hominini         Hominina                                                                               
Genus                                   Animalia Chordata Mammalia Primatomorpha Primates Catarrhini Haplorhini Simiiformes Hominoidea Hominidae   Homininae       Hominini         Hominina          †Ardipithecus                                                        
Species                                 Animalia Chordata Mammalia Primatomorpha Primates Catarrhini Haplorhini Simiiformes Hominoidea Hominidae   Homininae       Hominini         Hominina          †Ardipithecus    †A. kadabba                                         
Species                                 Animalia Chordata Mammalia Primatomorpha Primates Catarrhini Haplorhini Simiiformes Hominoidea Hominidae   Homininae       Hominini         Hominina          †Ardipithecus    †A. ramidus                                         
Genus                                   Animalia Chordata Mammalia Primatomorpha Primates Catarrhini Haplorhini Simiiformes Hominoidea Hominidae   Homininae       Hominini                           †Orrorin                                                             
Species     Orrorin                     Animalia Chordata Mammalia Primatomorpha Primates Catarrhini Haplorhini Simiiformes Hominoidea Hominidae   Homininae       Hominini                           †Orrorin         †O. tugenensis                                      
Genus                                   Animalia Chordata Mammalia Primatomorpha Primates Catarrhini Haplorhini Simiiformes Hominoidea Hominidae   Homininae       Hominini                           †Kenyanthropus                                                       
Tribe                                   Animalia Chordata Mammalia Primatomorpha Primates Catarrhini Haplorhini Simiiformes Hominoidea Hominidae   Homininae       Gorillini                                                                                               
Genus                                   Animalia Chordata Mammalia Primatomorpha Primates Catarrhini Haplorhini Simiiformes Hominoidea Hominidae   Homininae       Gorillini                          Gorilla                                                              
Species                                 Animalia Chordata Mammalia Primatomorpha Primates Catarrhini Haplorhini Simiiformes Hominoidea Hominidae   Homininae       Gorillini                          Gorilla          G. beringei                                         
Subspecies  Mountain gorilla            Animalia Chordata Mammalia Primatomorpha Primates Catarrhini Haplorhini Simiiformes Hominoidea Hominidae   Homininae       Gorillini                          Gorilla          G. beringei                     G. b. beringei      
Subspecies  Eastern lowland gorilla     Animalia Chordata Mammalia Primatomorpha Primates Catarrhini Haplorhini Simiiformes Hominoidea Hominidae   Homininae       Gorillini                          Gorilla          G. beringei                     G. b. graueri       
Species                                 Animalia Chordata Mammalia Primatomorpha Primates Catarrhini Haplorhini Simiiformes Hominoidea Hominidae   Homininae       Gorillini                          Gorilla          G. gorilla                                          
Subspecies  Cross River gorilla         Animalia Chordata Mammalia Primatomorpha Primates Catarrhini Haplorhini Simiiformes Hominoidea Hominidae   Homininae       Gorillini                          Gorilla          G. gorilla                      G. g. diehli        
Subspecies                              Animalia Chordata Mammalia Primatomorpha Primates Catarrhini Haplorhini Simiiformes Hominoidea Hominidae   Homininae       Gorillini                          Gorilla          G. gorilla                      G. g. gorilla       
Species     Eastern gorilla             Animalia Chordata Mammalia Primatomorpha Primates Catarrhini Haplorhini Simiiformes Hominoidea Hominidae   Homininae       Gorillini                          Gorilla          Gorilla beringei                                    
Species                                 Animalia Chordata Mammalia Primatomorpha Primates Catarrhini Haplorhini Simiiformes Hominoidea Hominidae   Homininae       Gorillini                          Gorilla          Gorilla gorilla                                     
Genus                                   Animalia Chordata Mammalia Primatomorpha Primates Catarrhini Haplorhini Simiiformes Hominoidea Hominidae   Homininae       Gorillini                          †Chororapithecus                                                     
Species     Chororapithecus             Animalia Chordata Mammalia Primatomorpha Primates Catarrhini Haplorhini Simiiformes Hominoidea Hominidae   Homininae       Gorillini                          †Chororapithecus †C. abyssinicus                                     
Tribe                                   Animalia Chordata Mammalia Primatomorpha Primates Catarrhini Haplorhini Simiiformes Hominoidea Hominidae   Homininae       †Graecopithecini                                                                                        
Genus                                   Animalia Chordata Mammalia Primatomorpha Primates Catarrhini Haplorhini Simiiformes Hominoidea Hominidae   Homininae       †Graecopithecini                   †Ouranopithecus                                                      
Species                                 Animalia Chordata Mammalia Primatomorpha Primates Catarrhini Haplorhini Simiiformes Hominoidea Hominidae   Homininae       †Graecopithecini                   †Ouranopithecus  †O. macedoniensis                                   
Species                                 Animalia Chordata Mammalia Primatomorpha Primates Catarrhini Haplorhini Simiiformes Hominoidea Hominidae   Homininae       †Graecopithecini                   †Ouranopithecus  †O. turkae                                          
Genus                                   Animalia Chordata Mammalia Primatomorpha Primates Catarrhini Haplorhini Simiiformes Hominoidea Hominidae   Homininae       †Graecopithecini                   †Graecopithecus                                                      
Genus                                   Animalia Chordata Mammalia Primatomorpha Primates Catarrhini Haplorhini Simiiformes Hominoidea Hominidae   Homininae                                          †Sahelanthropus                                                      
Species                                 Animalia Chordata Mammalia Primatomorpha Primates Catarrhini Haplorhini Simiiformes Hominoidea Hominidae   Homininae                                          †Sahelanthropus  †S. tchadensis                                      
Subfamily                               Animalia Chordata Mammalia Primatomorpha Primates Catarrhini Haplorhini Simiiformes Hominoidea Hominidae   Ponginae                                                                                                                
Tribe                                   Animalia Chordata Mammalia Primatomorpha Primates Catarrhini Haplorhini Simiiformes Hominoidea Hominidae   Ponginae        †Sivapithecini                                                                                          
Genus                                   Animalia Chordata Mammalia Primatomorpha Primates Catarrhini Haplorhini Simiiformes Hominoidea Hominidae   Ponginae        †Sivapithecini                     †Ankarapithecus                                                      
Species     Ankarapithecus              Animalia Chordata Mammalia Primatomorpha Primates Catarrhini Haplorhini Simiiformes Hominoidea Hominidae   Ponginae        †Sivapithecini                     †Ankarapithecus  †A. meteai                                          
Genus                                   Animalia Chordata Mammalia Primatomorpha Primates Catarrhini Haplorhini Simiiformes Hominoidea Hominidae   Ponginae        †Sivapithecini                     †Gigantopithecus                                                     
Species     Gigantopithecus             Animalia Chordata Mammalia Primatomorpha Primates Catarrhini Haplorhini Simiiformes Hominoidea Hominidae   Ponginae        †Sivapithecini                     †Gigantopithecus †G. blacki                                          
Genus                                   Animalia Chordata Mammalia Primatomorpha Primates Catarrhini Haplorhini Simiiformes Hominoidea Hominidae   Ponginae        †Sivapithecini                     †Sivapithecus                                                        
Genus       Orangutans                  Animalia Chordata Mammalia Primatomorpha Primates Catarrhini Haplorhini Simiiformes Hominoidea Hominidae   Ponginae                                           Pongo                                                                
Species     Sumatran orangutan          Animalia Chordata Mammalia Primatomorpha Primates Catarrhini Haplorhini Simiiformes Hominoidea Hominidae   Ponginae                                           Pongo            Pongo abelii                                        
Species     Bornean orangutan           Animalia Chordata Mammalia Primatomorpha Primates Catarrhini Haplorhini Simiiformes Hominoidea Hominidae   Ponginae                                           Pongo            Pongo pygmaeus                                      
Species     Tapanuli orangutan          Animalia Chordata Mammalia Primatomorpha Primates Catarrhini Haplorhini Simiiformes Hominoidea Hominidae   Ponginae                                           Pongo            Pongo tapanuliensis                                 
Species                                 Animalia Chordata Mammalia Primatomorpha Primates Catarrhini Haplorhini Simiiformes Hominoidea Hominidae   Ponginae                                           Pongo            †Pongo hooijeri                                     
Tribe                                   Animalia Chordata Mammalia Primatomorpha Primates Catarrhini Haplorhini Simiiformes Hominoidea Hominidae   Ponginae        Pongini                                                                                                 
Genus                                   Animalia Chordata Mammalia Primatomorpha Primates Catarrhini Haplorhini Simiiformes Hominoidea Hominidae   Ponginae        Pongini                            †Khoratpithecus                                                      
Subfamily                               Animalia Chordata Mammalia Primatomorpha Primates Catarrhini Haplorhini Simiiformes Hominoidea Hominidae   †Dryopithecinae                                                                                                         
Tribe                                   Animalia Chordata Mammalia Primatomorpha Primates Catarrhini Haplorhini Simiiformes Hominoidea Hominidae   †Dryopithecinae †Kenyapithecini                                                                                         
Genus                                   Animalia Chordata Mammalia Primatomorpha Primates Catarrhini Haplorhini Simiiformes Hominoidea Hominidae   †Dryopithecinae †Kenyapithecini                    †Griphopithecus                                                      
Species                                 Animalia Chordata Mammalia Primatomorpha Primates Catarrhini Haplorhini Simiiformes Hominoidea Hominidae   †Dryopithecinae †Kenyapithecini                    †Griphopithecus  †G. alpani                                          
Species                                 Animalia Chordata Mammalia Primatomorpha Primates Catarrhini Haplorhini Simiiformes Hominoidea Hominidae   †Dryopithecinae †Kenyapithecini                    †Griphopithecus  †G. suessi                                          
Genus                                   Animalia Chordata Mammalia Primatomorpha Primates Catarrhini Haplorhini Simiiformes Hominoidea Hominidae   †Dryopithecinae †Kenyapithecini                    †Kenyapithecus                                                       
Species                                 Animalia Chordata Mammalia Primatomorpha Primates Catarrhini Haplorhini Simiiformes Hominoidea Hominidae   †Dryopithecinae †Kenyapithecini                    †Kenyapithecus   †K. wickeri                                         
Tribe                                   Animalia Chordata Mammalia Primatomorpha Primates Catarrhini Haplorhini Simiiformes Hominoidea Hominidae   †Dryopithecinae †Afropithecini                                                                                          
Genus                                   Animalia Chordata Mammalia Primatomorpha Primates Catarrhini Haplorhini Simiiformes Hominoidea Hominidae   †Dryopithecinae †Afropithecini                     †Otavipithecus                                                       
Species     Otavipithecus               Animalia Chordata Mammalia Primatomorpha Primates Catarrhini Haplorhini Simiiformes Hominoidea Hominidae   †Dryopithecinae †Afropithecini                     †Otavipithecus   †O. namibiensis                                     
Tribe                                   Animalia Chordata Mammalia Primatomorpha Primates Catarrhini Haplorhini Simiiformes Hominoidea Hominidae                   †Dryopithecini                                                                                          
Genus                                   Animalia Chordata Mammalia Primatomorpha Primates Catarrhini Haplorhini Simiiformes Hominoidea Hominidae                   †Dryopithecini                     †Anoiapithecus                                                       
Species     Anoiapithecus               Animalia Chordata Mammalia Primatomorpha Primates Catarrhini Haplorhini Simiiformes Hominoidea Hominidae                   †Dryopithecini                     †Anoiapithecus   †A. brevirostris                                    
Genus                                   Animalia Chordata Mammalia Primatomorpha Primates Catarrhini Haplorhini Simiiformes Hominoidea Hominidae                   †Dryopithecini                     †Danuvius                                                            
Species                                 Animalia Chordata Mammalia Primatomorpha Primates Catarrhini Haplorhini Simiiformes Hominoidea Hominidae                   †Dryopithecini                     †Danuvius        †D. guggenmosi                                      
Genus                                   Animalia Chordata Mammalia Primatomorpha Primates Catarrhini Haplorhini Simiiformes Hominoidea Hominidae                   †Dryopithecini                     †Rudapithecus                                                        
Species     Rudapithecus                Animalia Chordata Mammalia Primatomorpha Primates Catarrhini Haplorhini Simiiformes Hominoidea Hominidae                   †Dryopithecini                     †Rudapithecus    †R. hungaricus                                      
Genus                                   Animalia Chordata Mammalia Primatomorpha Primates Catarrhini Haplorhini Simiiformes Hominoidea Hominidae                   †Dryopithecini                     †Dryopithecus                                                        
Genus                                   Animalia Chordata Mammalia Primatomorpha Primates Catarrhini Haplorhini Simiiformes Hominoidea Hominidae                                                      †Nakalipithecus                                                      
Species     Nakalipithecus              Animalia Chordata Mammalia Primatomorpha Primates Catarrhini Haplorhini Simiiformes Hominoidea Hominidae                                                      †Nakalipithecus  †N. nakayamai                                       
Tribe                                   Animalia Chordata Mammalia Primatomorpha Primates Catarrhini Haplorhini Simiiformes Hominoidea Hominidae                   †Lufengpithecini                                                                                        
Genus                                   Animalia Chordata Mammalia Primatomorpha Primates Catarrhini Haplorhini Simiiformes Hominoidea Hominidae                   †Lufengpithecini                   †Lufengpithecus                                                      
Family      Gibbons                     Animalia Chordata Mammalia Primatomorpha Primates Catarrhini Haplorhini Simiiformes Hominoidea Hylobatidae                                                                                                                         
```

</details>

## License

[MIT](https://choosealicense.com/licenses/mit/)
