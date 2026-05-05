# Cross-Paradigm Models of Restricted Syndrome Decoding

This repository contains supporting code for the [PQCRYPTO 2026](https://pqcrypto2026.irisa.fr) paper [10.1007/978-3-032-22695-2_7](https://doi.org/10.1007/978-3-032-22695-2_7) ([eprint](https://eprint.iacr.org/2026/705)).

> **Cross-Paradigm Models of Restricted Syndrome Decoding with Application to CROSS**

by Étienne Burle and Aleksei Udovenko.

This work was funded by the Luxembourg National Research Fund (FNR) via project PQseal C24/IS/18978392.

```
@InProceedings{PQCRYPTO:BurUdo26,
  author="Burle, {\'E}tienne
  and Udovenko, Aleksei",
  editor="Bardet, Magali
  and Niederhagen, Ruben",
  title="Cross-Paradigm Models of Restricted Syndrome Decoding with Application to CROSS",
  booktitle="Post-Quantum Cryptography",
  year="2026",
  publisher="Springer Nature Switzerland",
  address="Cham",
  pages="188--221",
  isbn="978-3-032-22695-2",
  doi = "10.1007/978-3-032-22695-2_7",
}
```

A copy of this repository is available at [zenodo.org/records/18230686](https://zenodo.org/records/18230686).

Running the notebooks requires SageMath with `tqdm` package installed. The cells contain precomputed data, so notebooks can be read without running a kernel.

- [Hybrid-ListCVP-Costs.ipynb](./Hybrid-ListCVP-Costs.ipynb) contains theoretic estimates for Hybrid-BatchCVP, Hybrid-ListCVP, and Hybrid-ListSVP instances.
- [Solve-ListCVP.ipynb](./Solve-ListCVP.ipynb) contains experiment implementation of Hybrid-ListCVP and some statistics.
- [AffineDiameter.ipynb](./AffineDiameter.ipynb) contains experiments with the affine diameter of small subsets of Z/127Z.
