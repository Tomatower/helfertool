(TeX-add-style-hook
 "gift_list_by_day"
 (lambda ()
   (TeX-add-to-alist 'LaTeX-provided-class-options
                     '(("scrartcl" "a4paper" "10pt")))
   (TeX-add-to-alist 'LaTeX-provided-package-options
                     '(("inputenc" "utf8x") ("fontenc" "T1") ("babel" "ngerman") ("geometry" "top=1.5cm" "bottom=1.5cm" "left=2.0cm" "right=1.5cm")))
   (TeX-run-style-hooks
    "latex2e"
    "scrartcl"
    "scrartcl10"
    "inputenc"
    "fontenc"
    "babel"
    "longtable"
    "fancyhdr"
    "multirow"
    "pbox"
    "titlesec"
    "float"
    "caption"
    "geometry")
   (TeX-add-symbols
    '("fakesection" 1)
    '("nop" 1)))
 :latex)

