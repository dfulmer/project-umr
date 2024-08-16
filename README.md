# Project UMR

## Getting started

Clone the repository  
```git clone [code from above]``` 

cd into python-cli  
```cd project-umr```

## dmf test 2024-08-12.txt
This was an early draft of the normalization rule.

## dmf test 2024-08-14.txt
This rule adds a 099 $a based on a list of MMS IDs and correspoding UMR numbers.  

This line will need to be replaced with a list of addSubField commands that have the contents of the 099 $a (replace 'UMR1') and the corresponding MMS ID (replace '99188039715706381'):

addSubField "TMZ.a.UMR1" if ( exists "TMZ.b.99188039715706381" )

## dmf test 2024-08-14-2.txt
This rule adds a 490. This line will need to be replaced with a list of addSubField commands with 'UMR1' and '99188039715706381' replaced with corresponding UMR numbers and MMS IDs.

addSubField "TMY.v.UMR1" if ( exists "TMY.b.99188039715706381" )

## dmf test 2024-08-14-3.txt
This rule adds barcode numbers. Replace 123 with barcodes and 99188039715706381 with MMS IDs.

addSubField "TMU.p.123" if ( exists "TMU.b.99188039715706381" )

## createlist.py
This script will create the customized lines. Run like this:  
```python3 createlist.py > out.txt```

## To set up a rule
Take dmf test 2024-08-14-3-4.txt and replace the three addSubField lines with blocks from the createlist.py script.

## Normalization rule size is 150k
Normalization rules can be around 2,237 lines long, depending on content.

## change-852-normalization-rule.txt
This rule changes the 852 first indicator to 4 and removes the $h subfield.