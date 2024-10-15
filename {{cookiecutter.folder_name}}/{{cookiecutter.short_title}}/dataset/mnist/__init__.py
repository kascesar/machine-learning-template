"""
# MNIST

The *datasetA* are an code for making this dataset

This dataset are the code that generate *MNIST* dataset for clasification task.

this is an ER diagram generated with *mermaid*. and its only
for add some information.

```mermaid
erDiagram
    IMAGE ||--o{ LABEL : "has"
    IMAGE {
        int id PK
        int pixel_0
        int pixel_1
        int pixel_2
        int pixel_3
        int pixel_4
        int pixel_5
        int pixel_6
        int pixel_7
        int pixel_8
        int pixel_9
        int pixel_10
        int pixel_11
        int pixel_12
        int pixel_13
        int pixel_14
        int pixel_15
        int pixel_783
    }
    LABEL {
        int id PK
        string description
    }

```
"""
